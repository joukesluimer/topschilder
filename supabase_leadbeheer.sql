-- ===========================================================================
-- TOPSCHILDER.NL — leadbeheer en facturatie (aanvulling op supabase_schema.sql)
--
-- Uitvoeren in Supabase -> SQL Editor. Kan veilig vaker worden gedraaid.
-- Alles hieronder is alleen zichtbaar in het dashboard (service_role);
-- bezoekers van de site kunnen er niets mee.
-- ===========================================================================

-- ------------------------------------------------ schilders: beheervelden ---
alter table public.schilders
  add column if not exists actief                boolean not null default false,
  add column if not exists plaatsen              text[]  not null default '{}',
  add column if not exists max_leads_per_maand   int,
  add column if not exists gratis_leads_over     int     not null default 3,
  add column if not exists exclusief_mogelijk    boolean not null default false,
  add column if not exists factuur_email         text,
  add column if not exists gestart_op            date;

-- ------------------------------------------------------- toewijzingen ---
-- Eén regel per lead per schilder: wie kreeg welke aanvraag, tegen welke prijs.
create table if not exists public.lead_toewijzingen (
  id            uuid primary key default gen_random_uuid(),
  created_at    timestamptz not null default now(),
  lead_id       uuid not null references public.leads(id) on delete cascade,
  schilder_id   uuid not null references public.schilders(id) on delete restrict,
  soort         text not null default 'gedeeld' check (soort in ('gedeeld','exclusief')),
  prijs         numeric(8,2) not null default 0,     -- excl. btw; 0 bij gratis lead
  gratis        boolean not null default false,       -- telt als een van de 3 gratis leads
  gecrediteerd  boolean not null default false,       -- ongeldige lead, niet factureren
  reden_credit  text,
  gefactureerd  date,                                 -- datum van de factuur
  unique (lead_id, schilder_id)
);
create index if not exists toew_schilder_idx on public.lead_toewijzingen (schilder_id, created_at desc);

alter table public.lead_toewijzingen enable row level security;
revoke all on public.lead_toewijzingen from anon, authenticated;

-- Standaardprijzen per dienst (gelijk aan de tabel op /voor-schilders/).
create or replace function public.lead_standaardprijs(p_dienst text, p_soort text)
returns numeric language sql immutable as $$
  select (case
    when p_dienst ilike '%zakelijk%' or p_dienst ilike '%vve%'      then 55
    when p_dienst ilike '%buiten%'                                   then 38
    when p_dienst ilike '%houtrot%'                                  then 28
    when p_dienst ilike '%spuit%'                                    then 26
    else 22 end) * (case when p_soort = 'exclusief' then 2 else 1 end);
$$;

-- Prijs en gratis-tegoed automatisch invullen bij een nieuwe toewijzing.
create or replace function public.toewijzing_vul_in()
returns trigger language plpgsql as $$
declare v_dienst text; v_over int;
begin
  select dienst into v_dienst from public.leads where id = new.lead_id;
  select gratis_leads_over into v_over from public.schilders where id = new.schilder_id for update;
  if v_over > 0 then
    new.gratis := true; new.prijs := 0;
    update public.schilders set gratis_leads_over = gratis_leads_over - 1 where id = new.schilder_id;
  elsif new.prijs = 0 and not new.gratis then
    new.prijs := public.lead_standaardprijs(v_dienst, new.soort);
  end if;
  return new;
end $$;

drop trigger if exists toewijzing_vul_in on public.lead_toewijzingen;
create trigger toewijzing_vul_in before insert on public.lead_toewijzingen
  for each row execute function public.toewijzing_vul_in();

-- Lead-status bijwerken zodra hij is doorgestuurd.
create or replace function public.toewijzing_markeer_lead()
returns trigger language plpgsql as $$
begin
  update public.leads set status = 'doorgestuurd'
   where id = new.lead_id and status = 'nieuw';
  return new;
end $$;

drop trigger if exists toewijzing_markeer_lead on public.lead_toewijzingen;
create trigger toewijzing_markeer_lead after insert on public.lead_toewijzingen
  for each row execute function public.toewijzing_markeer_lead();

-- ================================================================== VIEWS

-- Nieuwe leads met de actieve schilders die in die plaats werken.
create or replace view public.leads_te_verdelen as
select
  l.id, to_char(l.created_at at time zone 'Europe/Amsterdam', 'DD-MM HH24:MI') as binnen,
  l.dienst, l.plaats, l.postcode, l.omvang, l.planning, l.naam, l.telefoon, l.email,
  l.omschrijving,
  (select string_agg(s.bedrijfsnaam, ', ' order by s.bedrijfsnaam)
     from public.schilders s
    where s.actief and exists (select 1 from unnest(s.plaatsen) p where lower(p) = lower(trim(l.plaats)))
  ) as passende_schilders,
  (select count(*) from public.lead_toewijzingen t where t.lead_id = l.id) as al_naar
from public.leads l
where l.status in ('nieuw','doorgestuurd')
  and coalesce(l.omschrijving,'') not ilike '%TESTLEAD%'
order by l.created_at desc;

-- Wat moet er per schilder per maand gefactureerd worden?
create or replace view public.facturatie_per_maand as
select
  to_char(date_trunc('month', t.created_at at time zone 'Europe/Amsterdam'), 'YYYY-MM') as maand,
  s.bedrijfsnaam, coalesce(s.factuur_email, s.email) as factuur_email,
  count(*)                                                  as leads,
  count(*) filter (where t.gratis)                          as gratis,
  count(*) filter (where t.gecrediteerd)                    as gecrediteerd,
  sum(t.prijs) filter (where not t.gecrediteerd)            as bedrag_excl_btw,
  round(sum(t.prijs) filter (where not t.gecrediteerd) * 1.21, 2) as bedrag_incl_btw,
  bool_and(t.gefactureerd is not null)                      as alles_gefactureerd
from public.lead_toewijzingen t
join public.schilders s on s.id = t.schilder_id
group by 1, 2, 3
order by 1 desc, 2;

-- Omzet per week, nu op basis van de toewijzingen (kolommen wijken af, dus eerst weg).
drop view if exists public.omzet_per_week;
create or replace view public.omzet_per_week as
select
  date_trunc('week', l.created_at)::date                                  as week,
  count(distinct l.id)                                                     as leads_binnen,
  count(distinct t.lead_id)                                                as leads_doorgestuurd,
  coalesce(sum(t.prijs) filter (where not t.gecrediteerd), 0)              as omzet_eur,
  round(coalesce(sum(t.prijs) filter (where not t.gecrediteerd), 0)
        / nullif(count(distinct l.id), 0), 2)                              as omzet_per_lead
from public.leads l
left join public.lead_toewijzingen t on t.lead_id = l.id
where coalesce(l.omschrijving,'') not ilike '%TESTLEAD%'
group by 1
order by 1 desc;

revoke all on public.leads_te_verdelen, public.facturatie_per_maand, public.omzet_per_week
  from anon, authenticated;

-- ===========================================================================
-- GEBRUIK
--   Schilder activeren:
--     update schilders set actief = true, plaatsen = '{Zeewolde,Harderwijk}',
--            max_leads_per_maand = 10, gestart_op = current_date
--      where bedrijfsnaam = 'Schildersbedrijf X';
--   Lead doorgestuurd? Leg het vast (prijs en gratis-tegoed gaan vanzelf):
--     insert into lead_toewijzingen (lead_id, schilder_id)
--     values ('<lead-id>', (select id from schilders where bedrijfsnaam = 'Schildersbedrijf X'));
--   Ongeldige lead crediteren:
--     update lead_toewijzingen set gecrediteerd = true, reden_credit = 'verkeerd nummer'
--      where id = '<toewijzing-id>';
-- ===========================================================================

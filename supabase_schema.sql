-- ===========================================================================
-- TOPSCHILDER.NL — Supabase schema
--
-- Plak dit hele bestand in de SQL Editor van je Supabase-project en klik Run.
-- Daarna: Project Settings -> API -> kopieer "Project URL" en de anon key
-- naar assets/js/config.js en zet DEMO_MODE op false.
--
-- Beveiliging: RLS staat aan met ALLEEN insert-rechten voor anonieme
-- bezoekers. Niemand kan leads uitlezen zonder de service_role key. De anon
-- key in je JavaScript is daarmee veilig om publiek te maken.
-- ===========================================================================

-- ---------------------------------------------------------------- LEADS ---
create table if not exists public.leads (
  id            uuid primary key default gen_random_uuid(),
  created_at    timestamptz not null default now(),

  -- klusgegevens
  dienst        text,
  postcode      text,
  plaats        text,
  pandtype      text,
  omvang        text,
  planning      text,
  omschrijving  text,

  -- contactgegevens
  naam          text,
  email         text,
  telefoon      text,

  -- attributie
  bron_url      text,
  utm_source    text,
  utm_medium    text,
  utm_campaign  text,
  gclid         text,
  referrer      text,

  -- verkoop / opvolging (vul jij later in)
  status        text not null default 'nieuw',
  verkocht_aan  text[],
  lead_prijs    numeric(8,2),
  notitie       text,

  -- eenvoudige misbruikbescherming
  constraint leads_email_ok  check (email is null or email ~* '^[^@\s]+@[^@\s]+\.[a-z]{2,}$'),
  constraint leads_lengtes   check (
    coalesce(length(omschrijving),0) <= 4000 and
    coalesce(length(naam),0)         <= 120  and
    coalesce(length(plaats),0)       <= 120  and
    coalesce(length(telefoon),0)     <= 40
  )
);

create index if not exists leads_created_idx  on public.leads (created_at desc);
create index if not exists leads_plaats_idx   on public.leads (lower(plaats));
create index if not exists leads_status_idx   on public.leads (status);

-- ------------------------------------------------------------ SCHILDERS ---
create table if not exists public.schilders (
  id               uuid primary key default gen_random_uuid(),
  created_at       timestamptz not null default now(),
  bedrijfsnaam     text,
  contactpersoon   text,
  kvk              text,
  email            text,
  telefoon         text,
  werkgebied       text,
  diensten         text,
  leads_per_maand  text,
  bron_url         text,
  utm_source       text,
  utm_medium       text,
  utm_campaign     text,
  gclid            text,
  referrer         text,
  status           text not null default 'nieuw',
  notitie          text,
  constraint schilders_email_ok check (email is null or email ~* '^[^@\s]+@[^@\s]+\.[a-z]{2,}$')
);

-- ------------------------------------------------------ OFFERTE-CHECKS ---
create table if not exists public.offerte_checks (
  id             uuid primary key default gen_random_uuid(),
  created_at     timestamptz not null default now(),
  offerte_tekst  text,
  bedrag         text,
  plaats         text,
  naam           text,
  email          text,
  ook_offertes   text,
  bron_url       text,
  utm_source     text,
  utm_medium     text,
  utm_campaign   text,
  gclid          text,
  referrer       text,
  status         text not null default 'nieuw',
  constraint checks_lengte check (coalesce(length(offerte_tekst),0) <= 20000)
);

-- ------------------------------------------------------------ BERICHTEN ---
create table if not exists public.berichten (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  naam        text,
  email       text,
  bericht     text,
  bron_url    text,
  utm_source  text,
  utm_medium  text,
  utm_campaign text,
  gclid       text,
  referrer    text,
  status      text not null default 'nieuw',
  constraint berichten_lengte check (coalesce(length(bericht),0) <= 8000)
);

-- =========================================================== ROW LEVEL SECURITY
alter table public.leads          enable row level security;
alter table public.schilders      enable row level security;
alter table public.offerte_checks enable row level security;
alter table public.berichten      enable row level security;

-- Bezoekers mogen ALLEEN toevoegen. Niet lezen, niet wijzigen, niet verwijderen.
do $$
declare t text;
begin
  foreach t in array array['leads','schilders','offerte_checks','berichten'] loop
    execute format('drop policy if exists %I on public.%I', 'anon_insert_' || t, t);
    execute format(
      'create policy %I on public.%I for insert to anon, authenticated with check (true)',
      'anon_insert_' || t, t
    );
  end loop;
end $$;

-- Expliciete rechten: insert mag, select/update/delete niet.
revoke all on public.leads, public.schilders, public.offerte_checks, public.berichten from anon, authenticated;
grant insert on public.leads, public.schilders, public.offerte_checks, public.berichten to anon, authenticated;

-- =========================================================== HANDIGE VIEWS
-- Deze bekijk je in de Supabase Table Editor (die draait als service_role,
-- dus die mag wel alles zien).

create or replace view public.leads_dashboard as
select
  to_char(created_at at time zone 'Europe/Amsterdam', 'DD-MM-YYYY HH24:MI') as binnengekomen,
  dienst, plaats, postcode, pandtype, omvang, planning,
  naam, telefoon, email,
  case when gclid <> '' then 'Google Ads' when utm_source <> '' then utm_source
       when referrer like '%google%' then 'Google organisch'
       when referrer = '' or referrer is null then 'Direct'
       else 'Overig' end as kanaal,
  utm_campaign, bron_url, status, verkocht_aan, lead_prijs, omschrijving
from public.leads
order by created_at desc;

-- Omzet per week: hoeveel leads binnen, hoeveel verkocht, wat leverde het op.
create or replace view public.omzet_per_week as
select
  date_trunc('week', created_at)::date            as week,
  count(*)                                        as leads_binnen,
  count(*) filter (where lead_prijs is not null)  as leads_verkocht,
  coalesce(sum(lead_prijs), 0)                    as omzet_eur,
  round(coalesce(sum(lead_prijs),0) / nullif(count(*),0), 2) as omzet_per_lead
from public.leads
group by 1
order by 1 desc;

-- Welke plaatsen leveren aanvragen op? Gebruik dit om te bepalen waar je
-- nieuwe schilders moet werven en waar je advertentiebudget heen moet.
create or replace view public.vraag_per_plaats as
select
  initcap(lower(plaats))                          as plaats,
  count(*)                                        as aanvragen,
  count(*) filter (where lead_prijs is not null)  as verkocht,
  coalesce(sum(lead_prijs), 0)                    as omzet_eur,
  max(created_at)                                 as laatste_aanvraag
from public.leads
where plaats is not null and plaats <> ''
group by 1
order by aanvragen desc;

revoke all on public.leads_dashboard, public.omzet_per_week, public.vraag_per_plaats from anon, authenticated;

-- ===========================================================================
-- KLAAR.
--
-- Test daarna even of het werkt. Vul config.js in, zet DEMO_MODE op false,
-- open de site en verstuur een testaanvraag. Daarna in Supabase:
--     select * from leads_dashboard;
-- ===========================================================================

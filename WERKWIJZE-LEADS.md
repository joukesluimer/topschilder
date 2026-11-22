# Werkwijze: van aanvraag tot factuur

Je hebt gekozen voor **handmatig doorsturen**: elke aanvraag komt eerst bij jou binnen,
jij controleert hem en stuurt hem door. Dit is de vaste routine. Nieuwe velden en
overzichten komen uit `supabase_leadbeheer.sql` (één keer uitvoeren in de SQL Editor).

## 1. Nieuwe aanvraag (dagelijks, liefst binnen een paar uur)

1. Je krijgt de mail van Make. De aanvrager krijgt automatisch een bevestiging
   (zie `MAKE-BEVESTIGINGSMAIL.md`).
2. Supabase → Table Editor → view **`leads_te_verdelen`**. In de kolom
   `passende_schilders` staat welke actieve schilders in die plaats werken.
3. Snelle echtheidscheck: klopt het telefoonnummer (06 of vast, 10 cijfers)? Past de
   postcode bij de plaats? Geen dubbele aanvraag van dezelfde persoon? Twijfel je, bel
   dan de aanvrager kort: "Ik wil je aanvraag even checken voor ik hem doorzet."
4. Stuur de lead door naar maximaal drie schilders, met de mail hieronder.
5. Leg het vast in SQL (of via Table Editor → `lead_toewijzingen` → Insert row):

   ```sql
   insert into lead_toewijzingen (lead_id, schilder_id)
   values ('<lead-id>', (select id from schilders where bedrijfsnaam = 'Schildersbedrijf X'));
   ```

   Prijs en gratis tegoed vullen zich vanzelf in. De lead krijgt status `doorgestuurd`.
6. Geen passende schilder? Zet de status op `geen_schilder` en bel of mail de aanvrager
   eerlijk dat je in die plaats (nog) niemand hebt. Zo'n plaats is meteen een
   wervingsdoel (view `vraag_per_plaats`).

### Mail: lead doorsturen aan een schilder

**Onderwerp:** `Nieuwe aanvraag: [dienst] in [plaats]`

```
Hoi [voornaam],

Er is een nieuwe aanvraag binnen in jouw werkgebied:

  Klus:        [dienst] — [omvang]
  Plaats:      [plaats] ([postcode])
  Pand:        [pandtype]
  Planning:    [planning]
  Omschrijving:
  [omschrijving]

  Naam:        [naam]
  Telefoon:    [telefoon]
  E-mail:      [email]

Deze aanvraag gaat naar maximaal [1/2/3] schilders. Bel liefst vandaag nog: wie als
eerste belt, heeft een flinke voorsprong.

Klopt er iets niet (verkeerd nummer, dubbel, buiten je gebied)? Laat het binnen vijf
werkdagen weten, dan crediteren we hem.

[Dit is gratis lead [1/2/3] van 3. | Prijs: € [bedrag] excl. btw, op de maandfactuur.]

Groet,
[je naam]
Topschilder.nl
```

## 2. Nieuwe schilder aangemeld

1. Make stuurt jou de aanmelding.
2. Bel binnen één werkdag (dat belooft de site). Neem door:
   - plaatsen waar ze werken (de exacte plaatsnamen zoals klanten ze invullen);
   - welk werk wel en niet;
   - maximum aantal leads per maand; gedeeld of ook exclusief;
   - de prijzen en de drie gratis leads;
   - het creditbeleid (melden binnen vijf werkdagen);
   - KvK en aansprakelijkheidsverzekering (laat een polis of bewijs mailen);
   - factuuradres.
3. Activeer in Supabase:

   ```sql
   update schilders set actief = true, plaatsen = '{Zeewolde,Harderwijk}',
          max_leads_per_maand = 10, factuur_email = 'administratie@...',
          gestart_op = current_date
    where bedrijfsnaam = 'Schildersbedrijf X';
   ```

4. Stuur de welkomstmail.

### Mail: welkom

**Onderwerp:** `Welkom bij Topschilder.nl`

```
Hoi [voornaam],

Leuk dat je meedoet. Zoals besproken:

  Werkgebied:     [plaatsen]
  Soort werk:     [diensten]
  Maximum:        [aantal] aanvragen per maand
  Prijs per lead: binnen € 22 | spuitwerk € 26 | houtrot € 28 | buiten € 38 |
                  zakelijk/VvE € 55 (excl. btw; exclusief = dubbel)
  Gratis:         je eerste 3 aanvragen

Hoe het werkt:
- Aanvragen komen per mail van dit adres. Bel de klant liefst dezelfde dag.
- Klopt een aanvraag niet? Meld het binnen vijf werkdagen, dan crediteren we hem.
- Agenda vol? Laat het weten, dan pauzeren we tot je weer ruimte hebt.
- Je krijgt aan het begin van de maand één factuur over de vorige maand.

Vragen? Beantwoord gewoon deze mail of bel [je nummer].

Groet,
[je naam]
Topschilder.nl
```

## 3. Maandelijks factureren (eerste werkdag van de maand)

1. Supabase → view **`facturatie_per_maand`**: per schilder het aantal leads, de gratis
   en gecrediteerde leads en het bedrag excl./incl. btw.
2. Maak de facturen in je boekhoudpakket. Zet op de factuur de leads (datum, plaats,
   dienst); die haal je met:

   ```sql
   select t.created_at::date, l.dienst, l.plaats, t.soort, t.prijs
     from lead_toewijzingen t join leads l on l.id = t.lead_id
     join schilders s on s.id = t.schilder_id
    where s.bedrijfsnaam = 'Schildersbedrijf X' and not t.gecrediteerd and not t.gratis
      and t.created_at >= date_trunc('month', now() - interval '1 month')
      and t.created_at <  date_trunc('month', now());
   ```

3. Markeer als gefactureerd:

   ```sql
   update lead_toewijzingen set gefactureerd = current_date
    where gefactureerd is null and not gratis and not gecrediteerd
      and created_at < date_trunc('month', now());
   ```

## Statussen van een lead

| Status | Betekenis |
|---|---|
| `nieuw` | Binnen, nog niet bekeken |
| `doorgestuurd` | Naar een of meer schilders (gaat vanzelf) |
| `geen_schilder` | Geen schilder in die plaats; aanvrager geïnformeerd |
| `ongeldig` | Nep, spam of dubbel; niet doorgestuurd |

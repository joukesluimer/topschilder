# Bevestigingsmail aan de aanvrager (Make.com)

Het scenario "Topschilder - nieuwe lead" stuurt nu alleen jou een mail. Hier komt een
tweede route bij: de aanvrager krijgt direct een bevestiging.

## Inrichting in Make

1. Na de webhook-module een **Router** plaatsen.
   - Route 1: de bestaande mail aan jou (ongewijzigd).
   - Route 2: de bevestiging aan de aanvrager.
2. Filter op route 2 ("Alleen offerteaanvragen met e-mailadres"):
   - `tabel` *Equal to* `leads`
   - `email` *Matches pattern* `^[^@\s]+@[^@\s]+\.[a-z]{2,}$` (hoofdletterongevoelig)
3. Module: dezelfde mailmodule als route 1 (zelfde verbinding en afzender).
   - **Aan:** `{{email}}`
   - **Antwoorden aan:** het adres waarop jij de leads ontvangt
   - **Onderwerp:** zie hieronder
   - **Inhoud:** zie hieronder (als platte tekst, of als HTML met `<br>` per regel)

De tekst staat vast in Make. Uit de aanvraag komen alleen naam, klus en plaats. Zo kan
niemand via het formulier eigen tekst naar willekeurige adressen laten mailen.

## Onderwerp

```
Je aanvraag voor {{dienst}} in {{plaats}} is ontvangen
```

## Inhoud

```
Hoi {{naam}},

Bedankt voor je aanvraag via Topschilder.nl. We hebben hem goed ontvangen:

  Klus:      {{dienst}}
  Plaats:    {{plaats}}
  Planning:  {{planning}}

Wat gebeurt er nu?
We bekijken je aanvraag en zoeken schilders in jouw regio die dit werk doen en ruimte
hebben. Je aanvraag gaat naar maximaal drie bedrijven. Zij nemen zelf contact met je op,
doorgaans binnen één werkdag.

Vergelijk de offertes rustig. Let op wat er precies in staat: voorbereiding, aantal
lagen, verfmerk en garantie. Op https://topschilder.nl/offerte-vergelijken/ kun je een
offerte gratis laten nalopen.

Klopt er iets niet, of wil je je aanvraag intrekken? Beantwoord dan deze mail.

Groet,
Topschilder.nl
https://topschilder.nl
```

## Testen

Stuur na het opslaan één testaanvraag met je eigen e-mailadres, met in de omschrijving
`TESTLEAD`. Controleer of beide mails aankomen (ook in de spambox) en verwijder de
testregel daarna in Supabase.

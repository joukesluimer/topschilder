# Offertecheck aanzetten

De automatische offertecheck op /offerte-vergelijken/ staat uit tot je deze stappen doet.
Zolang `OFFERTECHECK_URL` leeg is, ziet een bezoeker het gewone formulier.

## Wat het doet

1. De bezoeker uploadt een offerte (pdf of foto) of plakt de tekst.
2. Deze functie stuurt hem naar Claude (model `claude-opus-5-5`). Claude haalt de posten, aantallen en bedragen eruit.
3. De browser vergelijkt elke post met de richtprijzen uit `kosten_data.py` (PRIJSBANDEN), gecorrigeerd voor de regio.

Er wordt niets opgeslagen: geen offerte, geen uitkomst.

## Stappen

1. **API-sleutel.** Maak op console.anthropic.com een API-sleutel aan.
   Stel onder *Limits* een maandlimiet in, bijvoorbeeld €25. Wat een check kost hangt af van de lengte van de offerte; kijk de eerste weken in de console naar het verbruik.
2. **Functie aanmaken.** Ga in Supabase naar *Edge Functions* en kies *Deploy a new function* → *Via editor*.
   Noem hem `offertecheck` en plak de inhoud van `index.ts`.
3. **JWT-controle uit.** Zet bij de functie *Verify JWT* uit. De site gebruikt een publishable key, en die is geen JWT.
   De functie accepteert alleen verzoeken vanaf topschilder.nl.
4. **Secret.** Ga naar *Edge Functions* → *Secrets* en voeg `ANTHROPIC_API_KEY` toe met de sleutel uit stap 1.
   Optioneel: `OFFERTECHECK_MODEL` om een ander model te gebruiken (bijvoorbeeld een goedkoper model als de kosten oplopen).
5. **Aanzetten.** Zet in `assets.py` bij CONFIG_JS:
   `OFFERTECHECK_URL: "https://dijcpmqlzetxmnzonytw.supabase.co/functions/v1/offertecheck"`
   en zet de site live.

## Testen

Lokaal testen kan door `OFFERTECHECK_EXTRA_ORIGIN` als secret op bijvoorbeeld `http://localhost:8000` te zetten.
Haal die secret weg als je klaar bent.

## Let op

- De prijsbanden in `kosten_data.py` en de categorieën in `index.ts` moeten gelijk blijven.
- De privacyverklaring noemt Anthropic al als partij die de offerte uitleest.
- Er zit geen limiet per bezoeker in. De maandlimiet bij Anthropic is je vangnet. Wordt de check misbruikt, zet `OFFERTECHECK_URL` dan weer op `""`.

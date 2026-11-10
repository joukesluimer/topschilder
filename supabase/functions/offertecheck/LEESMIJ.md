# Offertecheck met Claude (reserve, staat niet aan)

De offertecheck op /offerte-vergelijken/ werkt nu gratis in de browser (pdf.js en patroonherkenning, zie het blok
"offertecheck in de browser" in `assets.py`). Deze functie is een betaalde uitbreiding voor later, bijvoorbeeld om
foto's en scans te lezen. Hij staat al in Supabase, maar zonder `ANTHROPIC_API_KEY` doet hij niets.
De koppeling aan de site moet dan opnieuw worden gemaakt; een eerdere versie staat in commit 041bedf.

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
5. **Koppelen.** Laat de browsercheck bij een foto of scan deze functie aanroepen op
   `https://dijcpmqlzetxmnzonytw.supabase.co/functions/v1/offertecheck` en vul met het antwoord de posten in.

## Testen

Lokaal testen kan door `OFFERTECHECK_EXTRA_ORIGIN` als secret op bijvoorbeeld `http://localhost:8000` te zetten.
Haal die secret weg als je klaar bent.

## Let op

- De prijsbanden in `kosten_data.py` en de categorieën in `index.ts` moeten gelijk blijven.
- Pas de privacyverklaring aan: noem Anthropic als partij die de offerte uitleest.
- Er zit geen limiet per bezoeker in. De maandlimiet bij Anthropic is je vangnet. Wordt de check misbruikt, haal dan de secret weg.

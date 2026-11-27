# Lokale ronde 2: 15 extra plaatsen (27 november 2026)

Branch `claude/ts-plaatsen2-da5ec6`. `python3 build.py && python3 verify.py` geeft **ALLES OK**. Niets gepusht, `site/` niet gecommit.

## Welke plaatsen

De lokale gids (`/schilder/<plaats>/#lokale-gids`) en het blok "lokale feiten" op de plaats-dienstpagina's staan nu ook op:
Nijkerk, Huizen, Bussum, Dronten, Emmeloord, Weesp, Putten, Bunschoten-Spakenburg, Naarden, Urk, Elburg, Blaricum,
Genemuiden, Biddinghuizen en Swifterbant (`RONDE2` in `lokaal_top.py`).

Selectie: alle overige plaatsen waarvoor het CBS cijfers per buurt publiceert. De 10 kleine dorpen in de Noordoostpolder
(Marknesse, Nagele, Ens, enz.) hebben geen CBS-buurten; per buurt valt daar niets te onderbouwen. Daarom hebben ze geen gids.

## Bronnen per onderdeel

- **Woningvoorraad, bouwjaren, wijken/buurten:** BAG en CBS, al in `plaats_cijfers.py`.
- **Kozijnen per bouwperiode:** de bestaande typering (`TIJDVAKKEN`, met bronnen).
- **Klimaat:** KNMI-normalen 1991–2020 van het dichtstbijzijnde hoofdstation. Nieuw: Schiphol (240) voor Weesp. Afstanden zijn
  hemelsbrede schattingen vanaf een benaderd centrum, en dat staat er ook bij.
- **Monumenten en beschermd gezicht:** RCE-telling in de repo.
- **Kleurregels:** per gemeente uit de welstandsnota of de nota omgevingskwaliteit, met link (`KLEUR` in `lokaal_bronnen.py`).
  De onderzoeksnotities staan in de gedeelde notitiemap (`lokaal-kleurregels-ronde2.md`).
  - Niet gevonden: concrete kleurregels voor Dronten, Biddinghuizen, Swifterbant en Weesp. De pagina zegt dat eerlijk en verwijst naar de gemeente.
  - Oude nota's (van vóór de Omgevingswet): bij deze gemeenten staat dat je moet nagaan wat nu geldt.
- **Prijs:** de landelijke richtprijs maal de regiofactor, met het label "afgeleide". Deze ronde komen er drie formuleringen bij: onder, op of boven het gemiddelde.

## Duplicatie: vóór en na

Gemeten met `python3 duplicatie.py` (8-woordreeksen, plaatsnamen weggefilterd). De nulmeting is commit 623d98f.

| Groep | Duplicatie voor → na | Max-overlap voor → na | Met cijfers: duplicatie voor → na | Met cijfers: max-overlap voor → na | Woorden voor → na |
|---|---|---|---|---|---|
| Plaatspagina's, alle 35 | 91,6% → 90,0% | 72,0% → 65,5% | 83,1% → 81,6% | 57,5% → 51,7% | 2.166 → 2.674 |
| Plaatspagina's, de 15 nieuwe | 91,1% → 87,5% | 67,6% → 57,7% | 82,2% → 79,5% | 53,2% → 45,8% | 1.928 → 3.013 |
| Plaatspagina's, top 10 | 86,8% → 87,0% | 64,8% → 59,9% | 78,3% → 78,2% | 51,8% → 47,6% | 2.990 → 3.064 |
| Plaatspagina's, 10 dorpen zonder gids | 96,9% → 96,7% | 85,9% → 82,7% | 89,2% → 88,0% | 69,5% → 64,8% | 1.698 → 1.778 |
| Plaats-dienstpagina's, de 15 nieuwe (90) | 90,4% → 89,4% | 74,6% → 73,8% | 84,4% → 83,0% | 62,7% → 61,5% | 1.520 → 1.651 |

**Eerlijk gezegd.** De max-overlap (hoeveel een pagina lijkt op de pagina die er het meest op lijkt) daalt duidelijk. Het
duplicatiepercentage daalt minder, en dat heeft twee oorzaken:

- Het meet elke reeks van 8 woorden die op minstens één andere pagina staat. Een zin die op drie plaatsen gelijk is, telt dus net zo zwaar als een zin die op alle 35 plaatsen staat.
- Het formulier en de dienstkaarten (zo'n 400 woorden aan knoppen en labels) staan op elke pagina en zijn bewust niet aangeraakt.

Voor de top 10 blijft het percentage gelijk. De gids staat nu op 25 pagina's in plaats van 10, en zijn vaste zinnen worden dus
vaker gedeeld. De extra variatie vangt dat precies op.

## Wat er veranderd is

1. **`lokaal_top.py`**
   - `RONDE2`, en per plaats de ligging en het type water (meer, rivier, landinwaarts, open polder). Elk type heeft zijn eigen zin over zout en vocht.
   - De intro en de alinea's over gevel, monumenten en prijs hangen nu af van de cijfers:
     - intro: aandeel vóór 1945, nieuwbouw of groeikern;
     - gevel: wind, vorstdagen, aandeel appartementen;
     - monumenten: beschermd gezicht, veel of weinig monumenten.
   - De wijktabel is gegroepeerd per bouwperiode. De typering staat één keer per periode, met de wijknamen erbij.
   - Bouwgolven noemen de buurt waarvan het mediane bouwjaar het dichtst bij de jongste golf ligt.
2. **`plaats_vast.py`** (nieuw, voor alle 35 plaatsen)
   - Deze blokken komen nu uit BAG en CBS: de dienstkaarten, "Zo werkt het", de alinea over het uurtarief, de noot onder de prijstabel, de zin over de woningmix, de buurplaatsen en beide CTA's.
   - De belofte is overal gelijk gebleven: maximaal drie offertes, gratis, nergens aan vast.
3. **`plaats_variatie.py`:** de btw-vraag noemt het aantal woningen uit 2025 of later (BAG). De vraag "hoeveel schilders" noemt het aandeel koopwoningen (CBS).
4. **`build.py`:** twee regels (import plus `body = varieer_plaats(p, body)`). **`assets.py`:** één regel extra in het blok `# --- LOKAAL ---`, voor de tabelkop per rij op mobiel.

## Na het samenvoegen

- Er kan een botsing ontstaan met branches die `build_plaats_pages` wijzigen. `varieer_plaats` zoekt exacte zinnen. Verandert iemand die zin, dan valt die vervanging stil weg, maar er gaat niets kapot.
- Bouw na het samenvoegen één keer en commit dan `lastmod.txt` mee.

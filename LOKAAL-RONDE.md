# Lokale ronde (27 november 2026)

Branch `claude/ts-lokaal-745e59`. `python3 build.py && python3 verify.py` geeft **ALLES OK**. Niets gepusht.

## Meting

Met `python3 duplicatie.py` (en `--met-cijfers`). Het script vergelijkt pagina's van hetzelfde type
met elkaar, met reeksen van 8 woorden. Plaatsnamen worden weggefilterd. "Duplicatie" is het aandeel
reeksen dat ook op een andere pagina van dat type staat. "Max-overlap" is de grootste overlap
(Jaccard) met één andere pagina.

| Groep | Duplicatie voor → na | Max-overlap voor → na | Met cijfers: duplicatie voor → na | Woorden voor → na |
|---|---|---|---|---|
| Plaatspagina's, top 10 | 89,1% → 86,8% | 73,4% → 64,8% | 82,7% → 78,3% | 1.919 → 2.990 |
| Plaatspagina's, overige 25 | 94,5% → 93,4% | 80,6% → 74,9% | 88,8% → 85,0% | 1.737 → 1.836 |
| Plaats-dienstpagina's, alle 210 | 92,5% → 91,6% | 80,5% → 78,0% | 88,1% → 86,3% | 1.479 → 1.483 |
| Plaats-dienstpagina's, top 10 | 90,7% → 88,9% | 76,6% → 72,0% | 85,1% → 81,8% | 1.555 → 1.651 |
| Dienstpagina's (6) | 41,9% → 32,0% | 24,9% → 18,1% | 41,8% → 31,6% | 1.096 → 1.751 |

**Eerlijke kanttekening.** Het grootste deel van de overlap komt nog uit blokken die op elke pagina
staan: het formulier, de dienstkaarten, "Zo werkt het", de buurplaatsen en de CTA. Samen zijn dat
zo'n 500 woorden. Die blokken horen bij design en conversie en zijn niet aangeraakt. Zonder
cijfers telt een zin als "Kampen telt 17.408 woningen" als sjabloon. Mét cijfers is hij uniek.
Daarom staan beide metingen erbij.

## Semrush (database nl, 27-11-2026)

Top 10 op "schilder <plaats>": Amersfoort 1.300, Almere 720, Zwolle 590, Lelystad 320,
Hilversum 320, Harderwijk 210, en Zeewolde, Ermelo, Nunspeet en Kampen elk 170.

In de top 3 staan overal lokale schildersbedrijven met hun homepage, plus Werkspot of Trustoo.
Gelezen zijn twee pagina's van de top 3 voor Amersfoort; Werkspot gaf een 403. Die twee noemen geen
prijzen, wijken, bouwjaren of monumenten. Daar zit het gat dat deze ronde vult.

## Wat er veranderd is

1. **Top 10: lokale gids** op `/schilder/<plaats>/#lokale-gids` (`lokaal_top.py`, `lokaal_bronnen.py`):
   - bouwgolven: de drie jaren met de meeste nieuwbouw (BAG), en wat dat nu betekent;
   - per wijk of buurt (CBS/BAG): mediaan bouwjaar, wat in die periode gebruikelijk was, en waar je op let;
   - klimaat: KNMI-normalen 1991–2020 van het dichtstbijzijnde hoofdstation, de windrichting (KNMI), zoet water (Rijkswaterstaat) en de weerkant (ADLER ARL 504);
   - monumenten en kleur: RCE-telling, plus de kleurregels uit de welstandsnota van elke gemeente, met link;
   - prijs: de landelijke richtprijs maal de regiofactor, uitdrukkelijk benoemd als afgeleide.
   
   Op de plaats-dienstpagina's van de top 10 staat een blok "lokale feiten" per dienst.
2. **Dienstpagina's** (`dienst_uitleg.py`):
   - "In het kort" bovenaan;
   - het werk laag voor laag, met wachttijden;
   - "Wanneer kies je wat?";
   - "Hoe vaak is het nodig?";
   - 4 tot 6 extra FAQ's per dienst;
   - een blok met links naar alle kostenpagina's en kennisbankartikelen van die dienst.
3. **Alle plaatsen** (`plaats_variatie.py`):
   - Vijf FAQ's op elke plaatspagina komen nu uit BAG, CBS en RCE: leeftijd, welke buurt het eerst aan de beurt is, vergunning voor kleur, kosten buitenwerk, en of je het zelf regelt.
   - Plaats-dienstpagina's krijgen een lokale vraag per dienst. Die vervangt "Werken jullie schilders ook in …?".
   - Bouwgolven vervangen een rouleerblok.
   - Algemene alinea's die 35 of 210 keer letterlijk hetzelfde stonden, zijn ingekort.
4. **Kampen** heeft nu 13 CBS-buurten (`plaatsdata_ophalen.py --buurten`). Het CBS kent daar maar één wijk.
5. **Correcties:**
   - Urk en Huizen noemden zoutlucht, maar IJsselmeer en Gooimeer zijn zoet.
   - Lood: er stond "vóór ongeveer 1960". Volgens OnderhoudNL is loodwit voor buitenwerk pas sinds 2009 verboden.
6. **CSS:** een klein gemarkeerd blok onderaan `assets.py` (`# --- LOKAAL ---`). Daarmee worden tabellen op mobiel als gestapelde rijen getoond.

## Bewust niet gedaan of niet gevonden

- **Houtsoort per bouwperiode:** geen betrouwbare bron die per periode één houtsoort noemt. Daarom staan er voorzichtige typeringen, met bronnen voor wat wel vaststaat: lood, Dudok-staal, aluminium in de jaren 50 en 60, en fabrieksmatig afgewerkt hout.
- **Hilversum en Lelystad:** de kleurregels voor kozijnen staan in PDF's die niet te openen waren (groter dan 10 MB). De pagina noemt alleen wat vaststaat, en linkt naar de nota.
- **Welstandsnota's:** die van Zeewolde (2016) en Nunspeet (2015) zijn oud. De pagina van Zeewolde zegt dat je bij de gemeente moet nagaan of de nota nog geldt.
- **Afstanden:** de afstanden tot het KNMI-station en de kust zijn hemelsbrede schattingen, en dat staat er ook bij.
- **Bronnen:** de onderzoeksnotities met alle URL's staan in de gedeelde notitiemap van deze sessies (`lokaal-*.md`).

## Na het samenvoegen

- **`build.py`:** de wijzigingen staan in de gemarkeerde PLAATSDATA-blokken, in `dienst_body` (twee regels) en in de FAQ-regels van de plaats- en plaats-dienstpagina's.
- **`lastmod.txt`:** bouw na het samenvoegen één keer lokaal en commit `lastmod.txt` mee.

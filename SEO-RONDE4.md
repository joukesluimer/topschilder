# SEO-ronde 4 (22 november 2026)

Branch `claude/seo-ronde4-397768`. `python3 build.py && python3 verify.py` geeft **ALLES OK**.
Er staan nu 257 indexeerbare URL's in de sitemap; dat waren er 242.

## 1. Onderzoek (Semrush, database nl)

**Waar staan we nu?** Bijna alles staat op positie 60 tot 97. De uitzonderingen:
- "schilderen huis" op 9 en "huis schilderen kosten" op 16 (/kosten/huis-schilderen/)
- "latex spuiten" op 15
- "behang inclusief behangen" op 39

**Kannibalisatie gevonden:**
- /prijzen/ rankt op uurtarief-zoekwoorden: "wat kost een schilder per uur" (1.600), "schilder uurtarief". Daar is /kosten/schilder-uurtarief/ voor bedoeld.
- Op "per m²"-zoekwoorden ranken /prijzen/ en /kosten/ allebei, terwijl /kosten/schilderen-per-m2/ ervoor bestaat.
- "kozijnen schilderen buiten kosten" rankt met /schilderwerk/buitenschilderwerk/ in plaats van met /kosten/kozijnen-schilderen/.

**Concurrenten:**
- Homedeal staat op 1 voor bijna alle kostenvragen, met één pagina per klus.
- Werkspot wint op plaatsnamen en heeft een btw-artikel (880 + 720 zoekopdrachten).
- Ze hebben onderwerpen die wij niet hadden: winterschilder (880), muren spuiten (1.000), onderhoudscontract en schilderabonnement (380).
- Over offerteadviseur.nl/schilderwerk had Semrush geen gegevens.

**Ontbrekende onderwerpen met volume:**

| Onderwerp | Zoekwoorden (maandvolume) |
|---|---|
| Radiator | radiator verven 1.600, radiator schilderen 480 |
| Kunststof kozijnen | schilderen 1.300, verven 880 |
| Buitenmuur en gevel | buitenmuur verven 1.300, muurverf buiten 1.600 |
| Schutting | schutting beitsen 1.300 |
| Gevel reinigen en impregneren | gevel impregneren 2.400, gevelreiniging kosten 720 |
| Merken | sikkens verf 4.400, sigma verf 4.400, sikkens rubbol 1.900, histor 1.000 |
| Trap | trap verven 2.400 |
| Tegels | tegels verven 1.900 |
| Schimmel | schimmelwerende verf 1.300, schimmel op muur 880 |
| Stucwerk | voorstrijk 4.400, stucwerk schilderen 590 |
| Betonvloer | betonverf 3.600, epoxy vloer 1.900 |
| Winter | winterschilder 880 |
| Hoe vaak | hoe vaak kozijnen schilderen 140 |
| Bladderende verf | verf bladdert af 140 |

## 2. Vijftien nieuwe pagina's

**Kosten** (`kosten_ronde4.py`, gekoppeld onderaan `kosten_data.py`):

| Pagina | Richtprijs |
|---|---|
| /kosten/radiatoren-schilderen/ | €90 – €225 per radiator |
| /kosten/kunststof-kozijnen-schilderen/ | €60 – €140 per kozijn |
| /kosten/gevel-schilderen/ | €20 – €40 per m² |
| /kosten/boeidelen-schilderen/ | €25 – €55 per meter, plus prijzen voor vervangen |
| /kosten/schutting-beitsen/ | €8 – €20 per m², tuinhuis €350 – €1.200 |
| /kosten/gevel-reinigen-impregneren/ | €12 – €32 per m² |

**Kennisbank** (`kennis_ronde4a.py` en `kennis_ronde4b.py`, gekoppeld onderaan `kennis_artikelen.py`):
- nieuw-stucwerk-schilderen
- trap-verven
- tegels-verven
- schimmel-op-muur
- verf-bladdert-af
- sikkens-sigma-of-histor
- hoe-vaak-buitenschilderwerk
- binnen-schilderen-in-de-winter
- betonvloer-verven

**Wat elke pagina heeft:**
- 1.100 tot 1.600 woorden
- een rekenvoorbeeld
- FAQ-schema
- interne links
- bronnen die echt geopend zijn: technische bladen van Sikkens, Sigma, Flexa, Alabastine en Sika, en verder RIVM, Rijksoverheid, Belastingdienst, NBvT/SGT, OnderhoudNL/COT, Homedeal en Slimster

De nieuwe pagina's komen automatisch op /kosten/, /kennisbank/, de dienstpagina's ("Meer weten?") en de plaats-dienstpagina's (kostenlinks). Bestaande artikelen linken nu ook naar de nieuwe kostenpagina's.

**Let op bij de inhoud:**
- **Btw:** reinigen en impregneren van een gevel valt volgens de Belastingdienst onder **21%**, tenzij het voorbereiding is op schilderwerk. Zo staat het ook op de pagina.
- **Eigen inschattingen:** de prijzen voor radiatoren, boeidelen en schutting zijn eigen inschattingen. Er is geen bruikbare Nederlandse bron voor het schilderwerk zelf, en dat staat ook zo op de pagina. Werkspot noemt €100–€250 per radiator, maar die pagina gaf een 403 en staat daarom niet bij de bronnen.
- **Winterschilder:** de oude winterschilderregeling bestaat niet meer, en het artikel zegt dat ook. De 10% korting in het rekenvoorbeeld is uitdrukkelijk een "stel dat".
- Het artikel over Sikkens, Sigma en Histor maakt geen ranglijst. Het noemt de eigenaren (AkzoNobel, PPG; de fusie van AkzoNobel met Axalta is nog niet afgerond) en wat de fabrikant zelf zegt.

## 3. Techniek

**Kannibalisatie:**
- /prijzen/ heet nu "Wat kost een schilder in 2026? Prijslijst schilderwerk". Uurtarief en m² staan niet meer vooraan in de description; daarvoor zijn de eigen kostenpagina's.
- /kosten/ heet nu "Kosten schilderwerk per klus: overzicht 2026".
- /schilderwerk/buitenschilderwerk/ heeft `seo_titel` "Buitenschilderwerk laten doen: kosten en werkwijze", zonder "per kozijn".

**Schema:**
- Kennisbankartikelen krijgen nu ook **HowTo** (uit "Stap voor stap", met het anker `#stappen`).
- Organization, WebSite, BreadcrumbList, FAQPage, Article en Service waren er al en zijn gecontroleerd.

**Sitemap en lastmod:**
- Voorheen kreeg elke URL bij elke build de datum van vandaag.
- Nu bepaalt `lastmod.py` per pagina een hash van de inhoud. Header, footer, scripts en datums tellen daarbij niet mee. De hashes staan in `lastmod.txt`, dat in git hoort.
- `.gitattributes` zet `lastmod.txt` op `merge=union`. Botsen twee branches, dan blijven beide regels staan, en bij de volgende build wint de nieuwste datum. Daarna schrijft de build het bestand weer schoon weg.
- In GitHub Actions krijgt een gewijzigde pagina zonder bijgewerkte `lastmod.txt` gewoon de datum van vandaag.
- **Na het samenvoegen: één keer lokaal bouwen en `lastmod.txt` mee committen.**

**verify.py, nieuwe controles:**
- dubbele H1's
- een canonical die niet naar de pagina zelf wijst
- `#ankers` die niet bestaan
- wezen (indexeerbare pagina zonder interne links)
- `<img>` zonder alt
- FAQPage-schema zonder zichtbare vragen
- noindex-pagina's in de sitemap
- ongeldige lastmod-datums

Kapotte links, dubbele titels en descriptions werden al gecontroleerd.

**Klein herstel:**
- dakkapel: houtrot €85 → €50 per plek
- deuren: deurkozijn binnen €45–€95 → €35–€75 (zoals in PRIJSBANDEN)

## 4. Plaats-dienstpagina's (5.000–50.000 inwoners)

**Meting:** `uniek.py` meet het aandeel 8-woordreeksen dat op geen enkele andere plaatsversie van dezelfde dienst staat. Plaatsnamen worden daarbij weggefilterd. Standaard tellen getallen ook niet mee; met `--met-cijfers` wel.

| | Zonder cijfers | Met cijfers |
|---|---|---|
| Voor deze ronde | 3,7% | 6,4% |
| Na deze ronde | 8,8% | 14,1% |

**Wat ik deed:**
1. **CBS-buurten opgehaald** voor de 16 plaatsen van 5.000 tot 40.000 inwoners. Het commando is `python3 plaatsdata_ophalen.py --buurten`. Bronnen zijn PDOK-buurtgrenzen en CBS 85984NED, beide open data. Per buurt staan er nu woningen, mediaan bouwjaar, aandeel van vóór 1945, vóór 1975 en vanaf 2005, koop en corporatie. De overige cijfers zijn gecontroleerd ongewijzigd.
2. **Nieuw `plaats_buurten.py`:** op elke plaats-dienstpagina met buurt- of wijkcijfers komt een tabel per buurt. Selectie, kolom en uitleg verschillen per dienst:
   - buiten: welke buurten toe zijn aan de eerste beurt
   - houtrot: aandeel van vóór 1975
   - binnen: spachtelputz of kale wanden
   - spuitwerk: originele deuren
   - behang: oud behang
   - zakelijk: huur, koop en VvE

   Er staat ook een kernzin met een echt BAG-aantal bij, bijvoorbeeld "392 woningen gebouwd tussen 2018 en 2020".
3. **FAQ:** de twee algemene vragen, die op alle plaatsen hetzelfde waren, zijn vervangen door twee lokale vragen met antwoorden uit de cijfers.
4. **Rouleerblok aangepast:** het blok met "Hoeveel schilders zitten er in X?" noemde zonder bron dat het aantal schilders "overzichtelijk" is. Het is weg, net als het algemene blok "Vraag hier expliciet naar". Waar buurtcijfers zijn, staat nu het buurtblok.
5. **Checklist ingekort:** de lange checklist "Wat valt er onder ..." op plaatsversies is nu één zin met een link naar de dienstpagina.
6. **Plaatspagina's:** /schilder/{plaats}/ toont nu bij middelgrote plaatsen ook de bouwjaren per buurt.

## Wat nog openstaat

- **Search Console:** over 4 tot 6 weken nakijken of /prijzen/ uurtariefverkeer afstaat aan /kosten/schilder-uurtarief/. Gebeurt dat niet, dan kan de uurtariefsectie op /prijzen/ korter, met een duidelijkere link.
- **Muren spuiten (1.000/mnd):** dat zoekwoord valt nu onder latex-spuiten. Zet "muren spuiten" in de h1 of FAQ van die pagina, of maak een aparte pagina als het niet gaat ranken.
- **Onderhoudscontract en schilderabonnement (380/mnd):** nog geen pagina. Dat kan pas als duidelijk is of schilders in het netwerk dit aanbieden.
- **Plafond spuiten (880) en plafond laten spuiten (320):** die vallen onder plafond-schilderen. Overweeg een eigen kostenpagina of een sterkere sectie.
- **Unieke tekst op plaatspagina's:** 8,8% is beter, maar nog laag. Het grootste deel van de tekst is nog sjabloon: formulier, voor-na-slider, teasers, de "beste moment"-alinea en de kaarten "Ander schilderwerk". Volgende stappen:
  1. de algemene alinea's in de lokale sectie vervangen door cijfers. Denk aan bouwjaargolven uit `per_jaar_vanaf_1940` of het aandeel appartementen met VvE per buurt.
  2. per plaats de gemeentelijke regels voor kleur in een beschermd gezicht linken, met de echte URL van de gemeente.
  3. overwegen om de plaats-dienstpagina's van plaatsen onder ~15.000 inwoners ook op noindex te zetten, als ze na een paar maanden geen vertoningen krijgen.
- **Plaatsen van 40.000 tot 50.000 inwoners:** Nijkerk heeft maar 2 CBS-wijken en Kampen 1. Daar komt geen buurtblok. `--buurten` kan daarvoor uitgebreid worden; `BUURT_MAX_INWONERS` staat nu op 40.000.
- **Foto's:** de nieuwe pagina's hergebruiken bestaande foto's. Eigen foto's van een radiator, kunststof kozijn, schutting en gereinigde gevel zouden helpen.
- **Backlinks:** er zijn er nog geen. Het "deel dit prijsoverzicht"-blok staat ook op de nieuwe kostenpagina's.

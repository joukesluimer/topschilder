# SEO-ronde 5: technische audit (27 november 2026)

Branch `claude/ts-seo2-fb0f93`, gestart vanaf `ronde4` (270 pagina's). Niet gepusht.
`python3 build.py && python3 verify.py` geeft **ALLES OK**.

Gemeten met `meten/seo_audit.py` (alle 270 indexeerbare pagina's) en `meten/perf.mjs`
(headless Chrome). Lighthouse kon niet: `npx --no-install lighthouse` vraagt om een installatie.
Hoe je meet, staat in `meten/README.md`.

## Samenvatting vóór en na

| Onderdeel | Vóór | Na |
|---|---|---|
| Descriptions buiten 120–160 tekens | 11 | 0 |
| Titels langer dan 60 tekens | 0 | 0 |
| Dubbele titels, dubbele H1's, foute canonicals | 0 | 0 |
| Klikdiepte vanaf de home (max) | 3 | 3 |
| Minste inkomende links vanuit de content | 2 (tegels-verven) | 3 |
| Artikelen met 3 of 4 inkomende links | 6 | 1 |
| Fouten in JSON-LD (eigen controle) | 24 | 0 |
| Review- of ratingschema | 0 | 0 (verify.py controleert het nu) |
| CLS /schilderweer/ (412–1350 px breed) | 0,18–0,33 | 0 |
| Desktop-LCP /schilder/{plaats}/ | 272 ms | 192 ms |
| Desktop-LCP /onderhoudscheck/ | 332 ms | 232 ms |

## 1. Titels, descriptions, H1, canonical, hreflang

- **Al in orde:** alle titels zijn 30–60 tekens en uniek, elke pagina heeft één unieke H1, elke
  canonical wijst naar de pagina zelf en elke pagina heeft `lang="nl"`. **Hreflang is niet nodig**:
  de site heeft één taal.
- **Opgelost:** 10 descriptions waren 161–170 tekens. Google kapt ze dan af. Ze zijn nu korter
  (kosten, kennisbank, prijzen en 6 artikelen).
- **/schilderwerk/buitenschilderwerk/:** de description begon met "Richtprijzen per kozijn". Dat
  zoekwoord hoort bij /kosten/kozijnen-schilderen/ (zie de kannibalisatie in ronde 4). De pagina
  heeft nu een eigen `seo_desc` in `data.py`. `build.py` gebruikt `seo_desc` als die er is.

## 2. Interne links

- **Al in orde:** klikdiepte is maximaal 3 (1 home, 57 op niveau 1, 170 op niveau 2, 42 op
  niveau 3). Er zijn geen wezen en geen links zonder slash aan het eind.
- **"Ook handig" (`seo_extra.gerelateerd`)** koos bij gelijke score altijd de pagina die
  alfabetisch eerst komt. Daardoor werden sommige artikelen nooit gekozen. Nu gaat bij gelijke
  score de pagina voor die het minst vaak gekozen is. Onderwerp en score blijven voorgaan.
  Gevolg: tegels-verven van 2 naar 5 inkomende links; oude-verf-verwijderen, schilderwerk-vve,
  binnendeuren-verven en muur-plamuren naar 6–7.
- **Ankerteksten:** op /kennisbank/ en /kosten/ had elke kaart twee links naar hetzelfde doel: de
  titel en "Lees meer →" of "Bekijk de prijzen →". De tweede link heeft nu `aria-hidden` en
  `tabindex="-1"`. De titel is het echte anker; een schermlezer hoort geen 30 keer "Lees meer".
- **Gezien, niet veranderd:** op plaatspagina's linken korte ankers als "Binnenschilderwerk" en
  "Zeewolde" naar plaats-dienstpagina's. Door de context (tabel op de Almere-pagina, zin "Ook in
  de buurt") is duidelijk waar ze heen gaan. Langere ankers maken de tekst stroever.

## 3. Schema (JSON-LD)

Gecontroleerd per paginatype: Organization, WebSite, BreadcrumbList, FAQPage, Article, HowTo,
Service, ItemList, CollectionPage en WebApplication. Alle blokken zijn geldige JSON, de breadcrumb-
posities kloppen, FAQ-antwoorden zijn niet leeg en alle schema-URL's bestaan.
Alles staat in `seo_extra._nazorg()`, zodat de modules zelf niet hoefden te veranderen.

- **Article** (gidsen en inspiratie): datePublished, image en author ontbraken. Nu hebben alle
  Articles een volledige auteur en uitgever (Organization met logo), een datePublished uit git
  (gids 10 november, inspiratie en kennisbank 22 november) en een image (og:image als er geen was).
- **Service:** had `provider: Topschilder`. Topschilder voert het schilderwerk niet zelf uit, dus
  dat klopte niet. Het is nu `broker`: de schema.org-eigenschap voor wie koper en verkoper bij
  elkaar brengt.
- **Organization:** heeft nu een logo (`/assets/merk/icon-512.png`).
- **Datums:** "Bijgewerkt op" (27 artikelen), "Laatst bijgewerkt" (3 gidsen) en `dateModified`
  waren altijd de builddatum. Elke pagina zei dus bij elke build dat hij vandaag was bijgewerkt,
  terwijl de sitemap (ronde 4) de echte datum gaf. Nu volgen ze `lastmod.txt`
  (`lastmod.zet_datums()`, aangeroepen in `write()`).
- **verify.py** meldt nu review- of ratingschema als fout, en een Article zonder headline, author,
  publisher, dateModified of image.

## 4. Snelheid

**Nulmeting (mediaan per pagina):** HTML 39 kB, CSS 71 kB (16,5 kB gzip), JS 50 kB, afbeeldingen
die direct laden 35 kB. Alle `<img>` hebben width en height, alle foto's hebben srcset en sizes, en
de eerste foto boven de vouw heeft een preload met fetchpriority. Alleen `style.css` blokkeert de
weergave. Externe scripts zijn er niet; de Facebook-pixel laadt pas na toestemming.

**Opgelost:**
- **CLS op /schilderweer/:** de widget begint met één regel "wordt geladen…" en groeit daarna
  naar 900–1.260 px. Alles eronder schoof weg (CLS 0,18–0,33; de grens is 0,1). Nu houdt
  `.sw-doel` tijdens het laden die ruimte vrij (`schilderweer.py`, CSS met `:has(.sw-laden)`).
  CLS is 0 bij 360, 412, 768, 1024 en 1350 px.
- **LCP op desktop:** de foto op /schilder/{plaats}/ (35 pagina's) en op /onderhoudscheck/ is op
  desktop het grootste element, maar stond op `loading="lazy"`. Op mobiel staat hij op
  display:none. Nieuwe helper `foto_alleen_desktop()` in `components.py`: een `<picture>` met een
  lege bron onder 980 px en `loading="eager"`. Op desktop laadt hij meteen; een telefoon downloadt
  hem niet (zelfde aantal bytes als ervoor). De sizes van de onderhoudscheckfoto is gelijkgetrokken
  met de echte breedte (560 px).

**Onderzocht, niet gedaan:**
- **Foto's opnieuw comprimeren:** er zijn geen beeldtools (geen cwebp, ImageMagick of PIL). Via
  Chrome-canvas leverde WebP op kwaliteit 0,72 maar 10–15% op voor de 15 zwaarste 800px-foto's.
  De foto's zijn dus al efficiënt; het kwaliteitsverlies is het niet waard.
- **CSS:** `style.css` is al verkleind (een extra minifier haalt 0,1%). Per pagina wordt 23–47%
  gebruikt. Opsplitsen per paginatype kan 8–10 kB gzip schelen, maar raakt het hele `assets.py`,
  waar veel sessies tegelijk in werken. Dat is iets voor een rustig moment.
- **app.js** (46 kB, 70–75% ongebruikt per pagina) wordt niet verkleind, omdat er template-
  literals in staan. Echte minificatie vraagt een tool als terser.

## 5. Meting met headless Chrome

Mediaan van 3 runs per pagina, lokale server met gzip (`meten/serve_gzip.py`). Verschillen tot
±50 ms zijn ruis. Bij /schilderweer/ hangt de CLS af van wanneer de weer-API antwoordt; in deze
mobiele reeks antwoordde hij snel genoeg. Per breedte gemeten was het vóór 0,18–0,33.

### Mobiel (412 px, 150 ms latentie, 1,6 Mbit/s, CPU 4x trager)

| Pagina | LCP vóór | LCP na | CLS vóór | CLS na | kB vóór | kB na |
|---|---|---|---|---|---|---|
| / | 800 | 840 | 0 | 0 | 64 | 64 |
| /kosten/huis-schilderen/ | 668 | 672 | 0 | 0 | 44 | 44 |
| /schilderwerk/buitenschilderwerk/ | 744 | 780 | 0 | 0 | 85 | 85 |
| /schilder/zwolle/ | 620 | 672 | 0 | 0 | 67 | 68 |
| /schilder/zwolle/binnenschilderwerk/ | 688 | 692 | 0 | 0 | 63 | 63 |
| /kennisbank/houtrot-herkennen-en-herstellen/ | 1080 | 1072 | 0 | 0 | 143 | 143 |
| /inspiratie/monument/ | 1440 | 1436 | 0 | 0 | 221 | 221 |
| /onderhoudscheck/ | 528 | 548 | 0 | 0 | 172 | 172 |
| /schilderweer/ | 628 | 608 | 0* | 0 | 56 | 56 |
| /prijzen/ | 580 | 588 | 0 | 0 | 44 | 44 |

### Desktop (1350 px, 10 Mbit/s)

| Pagina | LCP vóór | LCP na | CLS vóór | CLS na | kB vóór | kB na |
|---|---|---|---|---|---|---|
| / | 268 | 348 | 0 | 0 | 142 | 142 |
| /kosten/huis-schilderen/ | 188 | 192 | 0 | 0 | 63 | 63 |
| /schilderwerk/buitenschilderwerk/ | 188 | 192 | 0 | 0 | 85 | 85 |
| /schilder/zwolle/ | 272 | **192** | 0 | 0 | 139 | 139 |
| /schilder/zwolle/binnenschilderwerk/ | 176 | 176 | 0 | 0 | 63 | 63 |
| /kennisbank/houtrot-herkennen-en-herstellen/ | 236 | 232 | 0 | 0 | 143 | 143 |
| /inspiratie/monument/ | 284 | 276 | 0 | 0 | 221 | 221 |
| /onderhoudscheck/ | 332 | **232** | 0 | 0 | 208 | 208 |
| /schilderweer/ | 164 | 164 | **0,205** | **0** | 56 | 56 |
| /prijzen/ | 152 | 156 | 0 | 0 | 44 | 44 |

\* zie de toelichting boven de tabellen. De home is niet veranderd; 268 → 348 ms is ruis van de
koude start.

## Gewijzigde bestanden (voor het samenvoegen)

- `seo_extra.py`: eerlijker "Ook handig", `_nazorg()` voor JSON-LD
- `lastmod.py`: `echte_datum()` en `zet_datums()`
- `build.py` (klein): `zet_datums` in `write()`, `seo_desc`, `foto_alleen_desktop` voor de
  plaatsfoto, `aria-hidden` op "Bekijk de prijzen", description van /kosten/ en /prijzen/
- `components.py`: nieuwe functie `foto_alleen_desktop()` (alleen toegevoegd)
- `verify.py`: controle op review-schema en volledige Article
- `schilderweer.py`, `onderhoudscheck.py`, `kennisbank.py`, `data.py`, `kosten_ronde4.py`,
  `kosten_ronde5.py`, `kennis_artikelen.py`, `kennis_ronde4a.py`, `kennis_ronde4b.py`: een regel
  of een description
- nieuw: `meten/` (audit- en meetscripts) en dit verslag
- **Na het samenvoegen:** één keer `python3 build.py` draaien en `lastmod.txt` committen
  (zoals in ronde 4).

## Wat nog openstaat

- `style.css` opsplitsen in een basis en per paginatype (tools, plaatsen, kennisbank), als er
  minder sessies tegelijk in `assets.py` werken.
- Op /tools/ en /inspiratie/ is op desktop een lazy foto het LCP-element (324–376 ms lokaal).
  /inspiratie/ niet aangeraakt, omdat de inspiratiesessie daar nu aan werkt.
- Echte veldgegevens: na livegang de Core Web Vitals in Search Console bekijken. Het lab zegt
  weinig over trage telefoons.

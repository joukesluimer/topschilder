# Topschilder.nl — startgids & verdienmodel

Alles wat hierin staat is gebaseerd op de site die nu in `site/` klaarstaat, plus echte
Semrush-data voor de Nederlandse markt (opgehaald op 25-08-2026). Geen aannames waar cijfers
beschikbaar waren.

---

## 1. Wat je nu hebt

**263 indexeerbare pagina's**, allemaal uniek qua title, description en content:

| Type | Aantal | URL-patroon |
|---|---|---|
| Homepage | 1 | `/` |
| Dienstpagina's | 6 | `/schilderwerk/binnenschilderwerk/` |
| Plaatspagina's | 35 | `/schilder/lelystad/` |
| Plaats × dienst (longtail) | 210 | `/schilder/lelystad/buitenschilderwerk/` |
| Conversiepagina's | 3 | offerte aanvragen, offerte checken, voor schilders |
| Prijzen + werkgebied | 2 | `/prijzen/`, `/werkgebied/` |
| Juridisch + overig | 6 | over ons, contact, privacy, voorwaarden, cookies, 404 |

Technisch: geen WordPress, geen frameworks, geen database-calls bij het laden. Elke pagina is
platte HTML van ~25 kB met 14 kB CSS. Dat laadt vrijwel instant, wat direct meetelt in je
Core Web Vitals en in je Google Ads-kwaliteitsscore (lagere CPC bij dezelfde positie).

Richtprijzen zijn per regio gecorrigeerd via een prijsindex in `data.py` (Flevoland 0,96 ·
Overijssel 0,95 · Gelderland 1,00 · Utrecht 1,09 · Noord-Holland 1,13). Buitenschilderwerk staat
daardoor op € 86–182 per kozijn in Lelystad en op € 102–215 in Hilversum. Zodra je echte
offertedata uit je eigen leads hebt, stel je die index bij en klopt de hele site in één
`build.py`-run weer.

Ingebouwd: schema.org JSON-LD (Organization, Service, FAQPage, BreadcrumbList), sitemap.xml,
robots.txt, .htaccess met https- en www-redirects, honeypot tegen spambots, gclid/utm-attributie
die 90 dagen bewaard blijft, en Google Ads-conversietracking die je met twee regels aanzet.

---

## 2. Live in ongeveer een uur

### 2.1 Supabase (10 min)
1. Maak in je andere Supabase-account een project aan, bijvoorbeeld `topschilder`, regio **eu-central-1** (Frankfurt).
2. Open **SQL Editor**, plak de volledige inhoud van `supabase_schema.sql`, klik **Run**.
3. Ga naar **Project Settings → API** en kopieer de *Project URL* en de *anon/publishable key*.

### 2.2 Config invullen (2 min)
Open `assets/js/config.js` en vul in:

```js
SUPABASE_URL:      "https://jouwproject.supabase.co",
SUPABASE_ANON_KEY: "sb_publishable_...",
DEMO_MODE:         false,
```

Draai daarna `python3 build.py` opnieuw, zodat de nieuwe config in `site/` terechtkomt.

> De anon key mag publiek. Het SQL-script zet Row Level Security aan met **alleen insert-rechten**:
> bezoekers kunnen een lead insturen, maar niemand kan er één uitlezen zonder de service key.

### 2.3 Hosting + domein (30 min)
Twee routes, beide prima:

**Route A — klassieke hosting** (Cloud86, Vimexx, Antagonist, ~€4/mnd)
Upload de complete inhoud van `site/` naar `public_html`. De meegeleverde `.htaccess` regelt
https, non-www en de 404-pagina. Zet in het hostingpaneel een gratis Let's Encrypt-certificaat aan.

**Route B — Cloudflare Pages of Netlify** (gratis, sneller)
Sleep de map `site/` in het dashboard, koppel `topschilder.nl` en klaar. Wereldwijd CDN,
automatisch https, nul onderhoud. Voor een statische site is dit objectief de betere keuze.

**topschilders.nl** (meervoud) zet je door naar topschilder.nl met een 301-redirect. Niet als
tweede site opzetten — dan concurreer je met jezelf in Google.

### 2.4 Google-spullen (20 min)
- **Search Console**: property toevoegen, `sitemap.xml` indienen, homepage laten indexeren.
- **Google Business Profile**: aanmaken op je bedrijfsadres. Ook een platform mag dit.
- **Analytics 4**: alleen als je het echt gaat gebruiken. Zo niet, sla over — scheelt een cookiebanner.
- **Google Ads**: account aanmaken, conversieactie "Offerteaanvraag" maken, de ID en het label in `config.js` zetten.

---

## 3. De marktdata — waar het geld zit

Echte zoekvolumes en CPC's, Nederlandse database:

### Plaatszoekwoorden (koopintentie, hoge waarde)

| Zoekwoord | Volume/mnd | CPC | Moeilijkheid |
|---|---|---|---|
| schilder amersfoort | 1.000 | € 3,22 | **22** |
| schilder almere | 720 | € 3,61 | 40 |
| schilder zwolle | 590 | € 2,82 | 36 |
| schildersbedrijf zwolle | 480 | € 2,43 | 37 |
| schilder lelystad | 320 | € 3,18 | **8** |
| schilder hilversum | 320 | € 3,18 | **8** |
| schilder harderwijk | 210 | € 2,09 | **13** |
| schilder kampen | 170 | € 1,83 | – |
| schilder zeewolde | 140 | € 3,05 | **11** |
| schilder ermelo | 140 | € 2,04 | – |
| schilder emmeloord | 110 | € 1,66 | **10** |
| schilder bussum / huizen / nunspeet | 110 elk | € 1,33–3,02 | – |
| schilder dronten | 70 | € 2,82 | **12** |

**Dit is het belangrijkste getal in het hele document:** Lelystad, Hilversum, Emmeloord,
Zeewolde, Dronten en Harderwijk hebben een keyword difficulty tussen 8 en 13. Dat is
uitzonderlijk laag. Met de plaatspagina's die nu klaarstaan, wat interne links en een handvol
backlinks kun je daar realistisch binnen twee tot vier maanden op pagina 1 staan — zonder een
euro advertentiebudget.

Amersfoort is de buitenkans: 1.000 zoekopdrachten per maand bij difficulty 22. Dat is een
uitschieter voor een stad van dat formaat.

### Informatieve zoekwoorden (goedkoop verkeer, warmt op naar een aanvraag)

| Zoekwoord | Volume/mnd | CPC |
|---|---|---|
| wat kost een schilder per uur | **1.600** | € 0,39 |
| schilder uurtarief | 480 | € 0,50 |
| keuken spuiten kosten | 480 | € 1,77 |
| trap schilderen kosten | 320 | € 1,83 |
| kozijnen schilderen kosten | 260 | € 1,32 |
| schilder kosten | 260 | € 1,15 |
| houtrot herstellen | 210 | € 0,67 |
| binnendeuren laten spuiten | 170 | € 1,09 |
| kosten buitenschilderwerk | 140 | € 1,26 |
| latex spuiten prijs | 140 | € 1,28 |
| dakkapel schilderen kosten | 110 | € 1,25 |
| deuren spuiten kosten | 110 | € 0,78 |
| vve schilderwerk | 90 | € 3,88 |

"Wat kost een schilder per uur" doet 1.600 zoekopdrachten per maand tegen 39 cent per klik.
Je `/prijzen/`-pagina is precies daarvoor geschreven. Dit is het goedkoopste kwalitatieve
verkeer in deze hele markt.

### Wat je vermijdt in Ads

"offerte schilder" (€ 9,45 CPC) en "schilderwerk offerte" (€ 7,36) zijn de zoekwoorden waar
Trustoo, Slimster en Werkspot elkaar de tent uit vechten. Daar ga jij als nieuwkomer niet
winnen. Blijf van die veiling af.

### Wie er nu staat

Op "schilder lelystad" staan Trustoo, Slimster en Werkspot — allemaal met precies de
URL-structuur die jouw site ook heeft (`/schilder/lelystad/`). Dat is de bevestiging dat je
architectuur klopt. Daartussen staan gewone lokale schildersbedrijven met dunne sites. Dát zijn
de posities die je overneemt.

---

## 4. Het verdienmodel — en de valkuil die iedereen maakt

### De rekensom

Je verkoopt één aanvraag aan maximaal drie schilders. De tarieven staan al op
`/voor-schilders/`: van € 22 (binnenwerk) tot € 55 (zakelijk/VvE) per gedeelde lead.

Neem buitenschilderwerk in Lelystad. CPC € 3,18. Een goede, snelle landingspagina met een
vierstaps-formulier converteert in deze markt rond de 8%. Dus:

```
Kosten per lead via Ads   = € 3,18 / 0,08  = € 40
Opbrengst bij 1 schilder  = € 38           = € 2 VERLIES
Opbrengst bij 2 schilders = € 76           = € 36 winst
Opbrengst bij 3 schilders = € 114          = € 74 winst  (65% marge)
```

**Daar zit de hele business in.** Dezelfde lead, dezelfde kosten. Het verschil tussen verlies
en 65% marge is puur of je genoeg schilders hebt aangesloten in díe plaats.

### De valkuil

Bijna iedereen bouwt eerst de site, zet dan Ads aan, verzamelt leads — en zit vervolgens met
aanvragen die hij aan niemand kwijt kan. Dan gaat hij in paniek schilders bellen met een lead
die inmiddels drie dagen oud en dus waardeloos is.

**Doe het andersom. Schilders eerst.** Zonder afnemers is een lead een kostenpost.

### Wat een schilder een lead waard vindt

Even meerekenen vanuit hun kant, want dat heb je nodig aan de telefoon: een gemiddelde
buitenschilderklus is € 3.500 met pakweg 35% marge, dus € 1.225 aan verdiensten. Bij een
gedeelde lead wint hij er ongeveer één op vier. Vier leads × € 38 = € 152 voor € 1.225 aan
marge. Dat is een factor 8. **Vertel dat rustig hardop tijdens het gesprek** — de meeste
schilders hebben dit nooit uitgerekend.

---

## 5. De eerste 30 dagen

### Dag 1–2 · Live
Supabase, config, upload, Search Console, sitemap indienen. Verstuur zelf een testaanvraag en
check in Supabase of hij binnenkomt (`select * from leads_dashboard;`).

### Dag 3–8 · Schilders werven — dit is het echte werk
Zoek in Google Maps op "schildersbedrijf" in Zeewolde, Almere, Lelystad, Dronten en Harderwijk.
Maak een lijst van 25 bedrijven. Filter eruit: bedrijven met 50+ reviews en een strakke website
zitten meestal vol en hebben je niet nodig. **Je doelgroep is de eenmanszaak of het bedrijfje
met twee man dat een matige website heeft en tussen november en maart een gat in de agenda.**

Doel: **6 aangesloten schilders**, verdeeld over minimaal 2 plaatsen.

#### Belscript

> "Goedemiddag, u spreekt met Jouke van Topschilder. Ik heb een site gebouwd waar mensen uit
> Zeewolde en omgeving offertes voor schilderwerk aanvragen. Ik zoek een paar schilders hier in
> de buurt die die aanvragen kunnen oppakken. Heeft u op dit moment ruimte in de planning?"

*Zo ja:*

> "Mooi. Het werkt zo: als er een aanvraag binnenkomt uit uw werkgebied, stuur ik u naam,
> telefoonnummer en wat ze willen laten doen. U belt zelf, u maakt zelf de offerte, ik zit daar
> verder niet tussen. Een aanvraag gaat naar maximaal drie schilders.
>
> De eerste drie aanvragen krijgt u gratis. Geen abonnement, geen contract, geen opzegtermijn.
> Bevalt het niet, dan stopt het daar en heeft het u niets gekost. Bevalt het wel, dan is het
> achtentwintig euro voor een aanvraag binnenwerk en achtendertig voor buitenwerk.
>
> Even opzij gezet: een buitenklus levert u gauw twaalfhonderd euro marge op. Als u er één op
> vier wint, bent u honderdvijftig euro aan aanvragen kwijt voor twaalfhonderd euro marge. Dat
> is de rekensom.
>
> Zal ik u opnemen voor Zeewolde en Almere?"

**Bezwaren en antwoorden:**

- *"Ik heb werk genoeg."* → "Snap ik, nu wel. Zal ik u erin zetten voor november en december?
  Dan hoort u van me als het rustiger wordt. Kost u nu niets."
- *"Ik heb slechte ervaringen met Werkspot."* → "Terecht vaak. Daar gaat een aanvraag naar
  vijf, zes bedrijven en betaal je een abonnement. Bij mij maximaal drie, betaal je per
  aanvraag, en de eerste drie zijn gratis."
- *"Krijg ik de klus dan wel?"* → "Niet gegarandeerd. Wel dat u binnen een uur na de aanvraag
  bericht krijgt, dus u kunt als eerste bellen. Dat is in dit spel driekwart van het werk. En
  wilt u geen concurrentie, dan kan ik hem exclusief aan u geven voor het dubbele."

Zes van de vijfentwintig zeggen ja. Dat is een normale score en genoeg om te beginnen.

### Dag 9–12 · Ads aan, klein en gericht
Alleen in de plaatsen waar je nu schilders hebt. Budget **€ 15 per dag**.

**Campagne 1 — Lokaal, exact match**
Zoekwoorden: `[schilder zeewolde]`, `[schilder almere]`, `[schilder lelystad]`,
`[schildersbedrijf almere]`, `[schilder harderwijk]`
Landingspagina: de bijbehorende `/schilder/{plaats}/` pagina, niet de homepage.
Locatietargeting: straal van 15 km, **op "aanwezigheid" en niet op "interesse"** — anders
betaal je voor klikken uit heel Nederland.

**Campagne 2 — Klus + plaats**
`[buitenschilderwerk almere]`, `[kozijnen schilderen lelystad]`, `[keuken spuiten almere]`
Landingspagina: `/schilder/{plaats}/{dienst}/`

**Uitsluiten (belangrijk, dit scheelt honderden euro's):**
`vacature`, `baan`, `salaris`, `opleiding`, `cursus`, `zzp gezocht`, `gratis`, `zelf`,
`doe het zelf`, `verf kopen`, `gamma`, `praxis`, `karwei`, `hornbach`, `stukadoor`, `behang kopen`

Zet advertentie-extensies aan: sitelinks naar `/prijzen/` en `/offerte-vergelijken/`, en een
highlight-extensie met "Gratis · Max. 3 schilders · Binnen 24 uur reactie".

### Dag 13–30 · Draaien en meten
Elke lead direct doorzetten. Snelheid is alles: een lead die binnen tien minuten bij de schilder
ligt is drie keer zoveel waard als een van de volgende ochtend.

Kijk wekelijks in Supabase:
```sql
select * from omzet_per_week;
select * from vraag_per_plaats;
```

`vraag_per_plaats` vertelt je precies waar je de volgende schilders moet werven: de plaatsen met
veel aanvragen en weinig verkocht zijn je gaten.

### Realistische verwachting na 30 dagen
€ 450 aan advertentiekosten, 10 tot 18 leads, waarvan je er 6 tot 12 verkoopt aan gemiddeld
1,5 schilder. Omzet € 200 tot € 500. **Je draait waarschijnlijk quitte of licht verlies — en dat
is precies wat je verwacht.** Maand één koop je geen winst maar bewijs: dat het werkt, dat
schilders betalen, en welke plaatsen leveren.

De winst zit in maand 3 tot 6, wanneer de SEO op die difficulty-8-plaatsen begint te draaien.
Dat verkeer is gratis, en dan wordt je marge geen 65% maar bijna 100%.

---

## 6. Het SEO-spoor (parallel, en uiteindelijk het belangrijkste)

De 263 pagina's staan er. Wat ze nodig hebben:

1. **Indexering afdwingen.** Dien de sitemap in en vraag handmatig indexering aan voor je tien
   belangrijkste plaatspagina's. Dat versnelt het aanzienlijk.
2. **Backlinks — de enige echte bottleneck.** Bij difficulty 8 tot 13 heb je er niet veel nodig.
   Vijf tot tien fatsoenlijke links volstaan. Waar je ze haalt:
   - Elke aangesloten schilder een badge "Aangesloten bij Topschilder" met link naar zijn
     plaatspagina. Zes schilders = zes relevante lokale links, gratis.
   - Regionale nieuwssites en ondernemersplatforms in Flevoland.
   - Bedrijvengidsen: KvK-vermelding, Telefoonboek, Openingstijden.nl, Bedrijvenpagina.
   - Sponsoring van een lokale vereniging (€ 100 en je staat met link op hun site).
3. **Content uitbreiden.** De prijzenpagina pakt "wat kost een schilder per uur" (1.600/mnd).
   Voeg later losse pagina's toe voor "trap schilderen kosten" (320), "keuken spuiten kosten"
   (480), "binnendeuren laten spuiten" (170). Vraag me en ik genereer ze in dezelfde stijl.
4. **Meer plaatsen.** Zet extra plaatsen in `data.py` en draai `build.py` opnieuw — elke plaats
   levert automatisch 7 nieuwe pagina's op. Doe dit gefaseerd, en pas als je in de bestaande
   plaatsen schilders hebt. Vierhonderd plaatsen zonder afnemers is spam, geen strategie.

---

## 7. Dingen die je niet moet doen

**Geen verzonnen reviews.** Ik heb bewust geen nep-testimonials of AggregateRating-markup op de
site gezet, ook al is dat de standaardtruc bij dit soort platforms. Twee redenen: de ACM ziet
verzonnen reviews als misleidende handelspraktijk (boetes lopen tot in de tonnen), en Google
haalt rich snippets weg zodra ze verzonnen reviewmarkup detecteren. Verzamel echte reviews via
een mailtje twee weken na oplevering en zet ze er dan pas op. In `components.py` staat
`SHOW_REVIEWS = False` klaar voor dat moment.

**Wees voorzichtig met de review-aggregatietruc van Trustoo.** Google-reviews van een aangesloten
schilder tonen mag, mits je er duidelijk bij zet dat het reviews van dat bedrijf zijn en waar ze
vandaan komen. Ze optellen en presenteren als "1.247 beoordelingen voor Topschilder" mag niet.
Het verschil is klein op de pagina en groot in de wet.

**Vul je echte KvK- en btw-nummer in.** Staat nu op nullen in `data.py`. Een webshop of platform
zonder correcte bedrijfsgegevens is in strijd met de Wet elektronische handel.

**Laat de voorwaarden en privacyverklaring nakijken.** Ik heb bruikbare werkversies geschreven
met de juiste structuur, maar ik ben geen jurist. Voor een paar honderd euro laat je dit
controleren, en dat is goed besteed zodra er echt geld doorheen gaat.

**Let op tekstoverlap tussen plaatspagina's.** Ik heb hierop gemeten: longtail-pagina's lijken
gemiddeld 35% op elkaar, plaatspagina's 66%. Dat is ruim binnen wat normaal is voor lokale
dienstensites — Trustoo en Werkspot zitten aanzienlijk hoger — maar het is wel het punt waarop
Google's helpful content-systeem let. De pagina's variëren nu op prijsindex, bouwperiode,
woningmix, ligging en drie roterende tekstblokken. Wil je verder omlaag, dan is de beste
investering per plaats een paar zinnen die alleen daar kloppen: een wijk, een straat met
bekende houtrotproblemen, een lokaal schildersbedrijf dat je noemt. Vijf regels echte lokale
kennis doen meer dan vijfhonderd woorden gegenereerde tekst.

**Beloof geen reactietijden die je niet waarmaakt.** Op de site staat nu "meestal binnen één
werkdag". Dat kun jij waarmaken zolang je zelf doorzet. Maak er geen "binnen 2 uur" van.

---

## 8. Waar dit heen kan (fase 2)

Je noemde zelf het punt dat het meest oplevert: **schilders zijn enorm veel tijd kwijt aan het
verwerken van offertes.** Dat klopt, en het is de logische tweede laag boven dit platform.

Het model: de lead komt binnen met omschrijving, foto's en afmetingen. Jij genereert daar
automatisch een concept-offerte uit in de huisstijl van de schilder, met zijn eigen tarieven en
teksten. Hij checkt hem, past aan en verstuurt. Van veertig minuten naar vijf.

Waarom dat interessanter is dan leads verkopen:
- Je gaat van een transactie per lead naar een maandbedrag per schilder. Voorspelbare omzet.
- De schilder stapt niet meer over, want zijn hele offerteproces zit bij jou.
- Je kunt de leadprijs verlagen om marktaandeel te pakken en het geld op de software verdienen.

Je zei dat AI-integraties lastig zijn vanwege maatwerk. Dat klopt voor een koppeling met hun
bestaande boekhoudpakket. Maar voor een concept-offerte hoef je niets te koppelen: input is de
aanvraag plus zijn tarievenlijst, output is een PDF. Dat is prima te standaardiseren over
tientallen schilders heen. Begin daarmee zodra je tien betalende schilders hebt — niet eerder,
want dan bouw je voor niemand.

Andere logische uitbreidingen, in volgorde van hoe makkelijk ze zijn:
- **Aangrenzende branches.** Je content-engine is branche-onafhankelijk. "Stukadoor almere" doet
  720 zoekopdrachten per maand met CPC € 4,22 — hoger dan schilder. Dakdekkers, hoveniers,
  installateurs: zelfde `data.py`, andere diensten, één keer `build.py` draaien.
- **Exclusieve leads pushen.** Je opmerking over die aannemer die het dubbele betaalde voor
  exclusiviteit is de meest winstgevende zin uit je hele berichtenreeks. Bied het actief aan
  zodra een schilder twee klussen via jou heeft gescoord.
- **Schildersdashboard.** Nu krijgen ze een mailtje. Later een pagina waar ze leads accepteren
  of weigeren. Scheelt jou werk en verlaagt je creditering.

---

## 9. Onderhoud

Iets aanpassen aan de site:

```bash
python3 build.py     # genereert alles opnieuw in site/
python3 verify.py    # controleert links, dubbele titles, JSON-LD, sitemap
```

- **Nieuwe plaats toevoegen** → regel toevoegen in `PLAATSEN` in `data.py`
- **Nieuwe dienst** → blok toevoegen aan `DIENSTEN` in `data.py`
- **Prijzen bijwerken** → `prijs_van` / `prijs_tot` in `data.py`
- **Bedrijfsgegevens, KvK, e-mail** → `SITE` bovenaan `data.py`
- **Teksten in header/footer/formulieren** → `components.py`
- **Vormgeving** → `assets/css/style.css`

`verify.py` moet altijd eindigen met `✅ ALLES OK` voordat je uploadt.

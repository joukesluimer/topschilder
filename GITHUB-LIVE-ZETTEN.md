# Live zetten via GitHub Pages

Van lege GitHub-account naar `https://topschilder.nl` in ongeveer een uur, waarvan het meeste
wachten op DNS is.

Hoe het straks werkt: jij past `data.py` aan, je pusht, GitHub draait `build.py`, controleert de
uitkomst met `verify.py` en publiceert. Vindt de controle een fout, dan wordt er níéts
gepubliceerd en blijft de oude site staan.

---

## Stap 0 · Eerst je gegevens invullen

Open `data.py` en vul bovenin bij `SITE` in:

```python
"email": "info@topschilder.nl",
"kvk":   "12345678",              # jouw echte KvK-nummer
"btw":   "NL001234567B01",        # jouw echte btw-id
"adres": "Zeewolde",
```

Open `assets/js/config.js` en vul je Supabase-gegevens in, met `DEMO_MODE: false`.

Draai dan:

```bash
python3 build.py
python3 verify.py
```

`verify.py` moet eindigen met `✅ ALLES OK`. Zo niet, laat het me zien.

---

## Stap 1 · Repository aanmaken

Ga naar [github.com/new](https://github.com/new).

- **Naam:** `topschilder`
- **Zichtbaarheid:** **Public**

Die tweede is geen keuze maar een beperking: GitHub Pages werkt op een gratis account alleen bij
publieke repositories. Wil je 'm privé, dan heb je GitHub Pro nodig (ongeveer € 4 per maand).

Wat betekent publiek concreet? Je broncode is voor iedereen te lezen, inclusief `config.js` met
je Supabase anon key. Die key is ontworpen om publiek te zijn en het RLS-beleid in
`supabase_schema.sql` beschermt je data — daar zit het risico niet. Het risico is dat een
concurrent je hele opzet kan kopiëren. Voor een leadplatform waar de waarde in je schilders zit
en niet in je HTML, is dat mijn inschatting geen groot bezwaar. Vind je dat wel, neem dan Pro.

Vink **niets** aan bij "Initialize this repository" — geen README, geen .gitignore. Die heb je al.

---

## Stap 2 · Bestanden uploaden

**Via de terminal** (aanbevolen, dan kun je later makkelijk updaten):

```bash
cd pad/naar/topschilder
git init
git add .
git commit -m "Eerste versie Topschilder"
git branch -M main
git remote add origin https://github.com/JOUWNAAM/topschilder.git
git push -u origin main
```

**Via de browser**, als je liever niet met git werkt: klik op de lege repo op *uploading an
existing file*, en sleep de inhoud van de map `topschilder` erin. Let op twee dingen — de map
`.github` moet mee (die bevat de workflow), en de map `site` juist niet, want die wordt door
GitHub zelf gebouwd.

---

## Stap 3 · Pages aanzetten

In je repo: **Settings → Pages**.

- Bij **Source** kies je **GitHub Actions** (dus niet "Deploy from a branch").

Ga daarna naar de tab **Actions**. Je ziet daar de workflow "Bouw en publiceer Topschilder"
draaien. Na ongeveer een minuut staat je site op `https://JOUWNAAM.github.io/topschilder/`.

> Klik even op die run en kijk of beide stappen groen zijn. De controlestap faalt met opzet als
> `verify.py` iets vindt — dat is je vangnet.

---

## Stap 4 · Custom domein koppelen

Terug naar **Settings → Pages → Custom domain**. Vul in: `topschilder.nl`. Klik **Save**.

> Het `CNAME`-bestand dat `build.py` genereert is bij een Actions-workflow niet nodig — GitHub
> negeert het en gebruikt wat je hier invult. Het bestand kan blijven staan, het doet geen kwaad.

---

## Stap 5 · DNS instellen

Bij de partij waar je topschilder.nl hebt gekocht. Verwijder eerst eventuele bestaande A-records
of parkeer-records voor `@`.

**Vier A-records op `@`:**

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Vier AAAA-records op `@`** (IPv6, aanrader maar niet verplicht):

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

**Eén CNAME-record voor `www`:**

```
www  →  JOUWNAAM.github.io
```

Let op: dat is `JOUWNAAM.github.io` zónder de repo-naam erachter.

Zodra je dit doet, regelt GitHub automatisch de redirect van `www.topschilder.nl` naar
`topschilder.nl`. Daar hoef je verder niets voor te doen.

DNS-wijzigingen kunnen tot 24 uur duren, in de praktijk meestal een half uur.

---

## Stap 6 · HTTPS aanzetten

Ga terug naar **Settings → Pages** en vink **Enforce HTTPS** aan. Die optie verschijnt pas als
GitHub je DNS ziet kloppen — soms binnen tien minuten, soms na een paar uur. Het certificaat
komt van Let's Encrypt en vernieuwt zichzelf.

**Zet Ads en Search Console pas aan als dit vinkje staat.** Zonder https krijg je
browserwaarschuwingen en dan converteert je formulier nul komma nul.

---

## Stap 7 · topschilders.nl doorzetten

Het meervoud kan niet als tweede custom domain op dezelfde repo — GitHub Pages staat er maar één
toe. Twee oplossingen:

**A. URL-forwarding bij je registrar** (makkelijkst). TransIP, Versio, Antagonist en Hostnet
bieden dit gratis onder een naam als "doorsturen" of "URL forwarding". Zet 'm op
`https://topschilder.nl` met een **301** (permanent), niet 302.

**B. Tweede mini-repo.** Maak een repo `topschilders-redirect` met één `index.html` die
doorstuurt, en koppel `topschilders.nl` daaraan. Meer werk en SEO-technisch net iets zwakker dan
een echte 301 op serverniveau. Doe A tenzij je registrar het niet aanbiedt.

---

## Stap 8 · Search Console

1. [search.google.com/search-console](https://search.google.com/search-console) → property
   toevoegen → **Domein** → `topschilder.nl`
2. Verifiëren via een TXT-record in je DNS
3. **Sitemaps** → `sitemap.xml` indienen
4. Bij **URL-inspectie** je tien belangrijkste plaatspagina's stuk voor stuk indienen:
   `/schilder/lelystad/`, `/schilder/zeewolde/`, `/schilder/almere/`, `/schilder/emmeloord/`,
   `/schilder/dronten/`, `/schilder/harderwijk/`, `/schilder/hilversum/`, `/schilder/amersfoort/`,
   `/prijzen/`, `/`

Dat vierde punt is saai handwerk maar het scheelt makkelijk twee weken indexering.

---

## Daarna: iets aanpassen

```bash
# pas data.py aan, bijvoorbeeld een plaats toevoegen
git add .
git commit -m "Nijmegen toegevoegd"
git push
```

Klaar. GitHub bouwt, controleert en publiceert. Binnen twee minuten staat het live.

Wil je eerst lokaal kijken hoe het eruitziet: `python3 build.py` en dan
`python3 -m http.server 8000 --directory site`, en open `http://localhost:8000`.

---

## Wat je op GitHub Pages níét hebt

Eerlijk over de beperkingen, zodat je niet verrast wordt:

- **Geen `.htaccess`.** Die zit wel in `site/` maar wordt genegeerd. Niet erg: https afdwingen
  en de www-redirect regelt GitHub zelf.
- **Geen serverside redirects.** Verander je later een URL, dan kun je geen 301 instellen. Bij
  een SEO-site wil je URL's dus niet zomaar wijzigen. De structuur die er nu staat is bewust
  gekozen om mee te kunnen groeien.
- **Geen logbestanden.** Voor bezoekersdata ben je afhankelijk van Search Console en eventueel
  Analytics.
- **Zachte limieten:** 1 GB repo, 100 GB verkeer per maand, 10 builds per uur. Jouw site is
  7 MB. Daar loop je voorlopig niet tegenaan.

Loop je later tegen die redirect-beperking aan, dan kun je de repo koppelen aan Cloudflare Pages
zonder iets aan je code te wijzigen — zelfde git-workflow, wel redirect-regels. Maar begin
gewoon hier.

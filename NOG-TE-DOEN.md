# Topschilder.nl — stand van zaken

Bijgewerkt 25-08-2026. Alles hieronder is gecontroleerd, niet aangenomen.

## LIVE op https://topschilder.nl

| Onderdeel | Status |
|---|---|
| Site | 263 pagina's live, https actief, certificaat uitgegeven |
| Repository | [github.com/joukesluimer/topschilder](https://github.com/joukesluimer/topschilder) — public |
| Automatische build | GitHub Actions. Push → bouwen → controleren → publiceren |
| DNS | 4 A-records, 4 AAAA-records, CNAME www — geverifieerd bij Mijndomein |
| www | `www.topschilder.nl` stuurt door naar `topschilder.nl` |
| Enforce HTTPS | Aan |
| Supabase | Project TopSchilder, RLS actief |
| Formulieren | Getest vanaf het live domein: lead binnen (201), uitlezen geweigerd (401) |
| KvK 97150975 | In de footer en op contact |
| SPF / DMARC | Ongemoeid gelaten, e-mail werkt gewoon door |

Gecontroleerd met een echte HTTP-check: `/`, `/prijzen/`, `/schilder/lelystad/`,
`/schilder/zeewolde/buitenschilderwerk/`, `/voor-schilders/`, `/offerte-aanvragen/`,
`/contact/`, `/sitemap.xml`, `/robots.txt` en alle assets geven 200.

---

## Twee kleine dingen voor jou

**Testleads weghalen.** Er staan twee testregels in je database (naam "Test Claude" en
"Test live", beide met "TESTLEAD" in de omschrijving). Ik heb ze gebruikt om de keten
te controleren. Weghalen: Supabase → Table Editor → `leads` → rijen selecteren → verwijderen.

**Btw-nummer.** Staat leeg in `data.py` bij `SITE`. Vul je 'm in, dan verschijnt hij
vanzelf op contact en in de voorwaarden. Laat je 'm leeg, dan toont de site die regel niet.

---

## Wat er nu gebeurt zonder dat je iets doet

Google gaat de site vanzelf vinden, maar dat duurt weken. Wil je het versnellen, dan
is Search Console de eerste stap. Zie hieronder.

---

## De volgorde die geld oplevert

**1. Search Console** (20 min, vandaag)

[search.google.com/search-console](https://search.google.com/search-console) → property
toevoegen → **Domein** → `topschilder.nl` → verifiëren met een TXT-record bij Mijndomein.
Dien daarna `sitemap.xml` in en vraag via URL-inspectie handmatig indexering aan voor:
`/`, `/prijzen/`, `/schilder/lelystad/`, `/schilder/zeewolde/`, `/schilder/almere/`,
`/schilder/emmeloord/`, `/schilder/dronten/`, `/schilder/harderwijk/`,
`/schilder/hilversum/`, `/schilder/amersfoort/`.

Saai handwerk, maar het scheelt makkelijk twee weken.

**2. Schilders bellen** (deze week — dit is het echte werk)

25 bedrijven in Zeewolde, Almere, Lelystad, Dronten en Harderwijk. Doel: 6 aangesloten.
Belscript en bezwaarafhandeling staan in `STARTGIDS.md`, hoofdstuk 5.

Je doelgroep is de eenmanszaak of het bedrijfje met twee man en een matige website —
niet de partij met 50+ reviews en een volle agenda.

**3. Pas dán Google Ads** (€15 per dag, alleen in plaatsen waar je schilders hebt)

Stap 2 vóór stap 3. Een lead die je aan niemand kunt verkopen is een kostenpost, en dat
is precies waar bijna iedereen in deze markt op stukloopt. De rekensom staat in de
startgids: dezelfde lead is €2 verlies bij één afnemer en €74 winst bij drie.

**4. topschilders.nl** — staat nog nergens geregistreerd (geen nameservers, geen SOA).
Heb je 'm gekocht, check dan bij je registrar of de registratie is doorgevoerd. Daarna
via Mijndomein → Doorverwijzen een **301** naar `https://topschilder.nl`.

---

## Iets aanpassen aan de site

Geen Python nodig, het kan gewoon in je browser:

1. Open [data.py](https://github.com/joukesluimer/topschilder/blob/main/data.py)
2. Klik het potloodje rechtsboven
3. Wijzig, klik **Commit changes**
4. GitHub bouwt, controleert en publiceert — na twee minuten staat het live

| Wat je wilt aanpassen | Waar |
|---|---|
| Btw-nummer | `data.py` → `SITE` → `"btw": ""` |
| Plaats toevoegen | `data.py` → `PLAATSEN` (levert automatisch 7 pagina's op) |
| Prijzen | `data.py` → `prijs_van` / `prijs_tot`, of `PRIJSINDEX` per provincie |
| E-mailadres | `data.py` → `SITE` |
| Leadtarieven schilders | `build.py` → `build_voor_schilders` |
| Vormgeving | `assets.py` → `STYLE_CSS` |
| Supabase-koppeling | `assets.py` → `CONFIG_JS` |

Maak je een fout, dan faalt de controlestap en blijft de oude site staan. Je kunt de
boel dus niet slopen met een typefout.

---

## Je leads bekijken

Supabase → SQL Editor:

```sql
select * from leads_dashboard;    -- alle aanvragen, met kanaal en campagne
select * from omzet_per_week;     -- leads binnen, verkocht, omzet per week
select * from vraag_per_plaats;   -- waar komt de vraag vandaan
```

`vraag_per_plaats` vertelt je precies waar je de volgende schilders moet werven: veel
aanvragen en weinig verkocht betekent een gat in je aanbod.

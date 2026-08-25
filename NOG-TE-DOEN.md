# Topschilder.nl — stand van zaken

Bijgewerkt 25-08-2026. Alles hieronder is gecontroleerd, niet aangenomen.

---

## Wat er staat

| Onderdeel | Status |
|---|---|
| Repository | [github.com/joukesluimer/topschilder](https://github.com/joukesluimer/topschilder) — public |
| Automatische build | GitHub Actions, groen. Bouwt en controleert bij elke push |
| Site gepubliceerd | 263 pagina's live, sitemap en assets gecontroleerd |
| Supabase | Project **TopSchilder**, schema uitgevoerd, RLS actief |
| Formulieren | Getest: insert lukt (201), uitlezen wordt geweigerd (401) |
| KvK 97150975 | Staat in de footer en op de contactpagina |
| Custom domain | `topschilder.nl` gekoppeld, wacht op DNS |

**Eén ding blijft over: de DNS.** Dat kan ik niet voor je doen, want daarvoor moet
ik inloggen bij je registrar.

---

## Wat jij nog moet doen — DNS bij Mijndomein

Je domein staat bij **Mijndomein** (nameservers `nsn1.mijndomein.nl` en
`nsn2.mijndomein.nl`). Op dit moment wijst topschilder.nl naar `213.249.67.10`,
een parkeerpagina. Die moet eruit.

1. Log in op [mijndomein.nl](https://www.mijndomein.nl) → **Domeinnamen** →
   topschilder.nl → **DNS-instellingen**
2. **Verwijder** het bestaande A-record op `@` dat naar `213.249.67.10` wijst
3. Voeg **vier A-records** toe op `@`:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

4. Voeg **vier AAAA-records** toe op `@` (IPv6, aanrader):

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

5. Voeg **één CNAME** toe:

```
Naam:   www
Waarde: joukesluimer.github.io
```

Let op: `joukesluimer.github.io` **zonder** `/topschilder` erachter.

Sla op. Reken op een half uur tot maximaal 24 uur.

### Daarna, en dit is belangrijk

Ga naar [Settings → Pages](https://github.com/joukesluimer/topschilder/settings/pages)
en vink **Enforce HTTPS** aan. Die optie verschijnt pas zodra GitHub je DNS ziet
kloppen. Zonder dat vinkje krijgen bezoekers een browserwaarschuwing en vult
niemand je formulier in.

**Zet Google Ads en Search Console pas aan als dat vinkje staat.**

### topschilders.nl

Die staat nog nergens geregistreerd — geen nameservers, geen SOA-record. Heb je
'm wel gekocht, dan is de registratie nog niet doorgevoerd. Zodra dat wel zo is:
zet 'm bij je registrar door naar `https://topschilder.nl` met een **301**
(permanent). Niet als tweede site inrichten, dan concurreer je met jezelf.

---

## Twee dingen om te weten

**De github.io-URL ziet er kaal uit.** Op
`joukesluimer.github.io/topschilder/` laadt de opmaak niet, omdat de site met
absolute paden werkt (`/assets/css/style.css`). Dat is correct voor
topschilder.nl, maar niet voor een submap. Zodra je DNS staat, klopt alles. Geen
bug, gewoon hoe het werkt.

**Er staat één testlead in je database.** Die heb ik erin gezet om te
controleren of de keten werkt — naam "Test Claude", omschrijving "TESTLEAD - mag
weg". Weghalen doe je in Supabase → Table Editor → leads → rij selecteren →
verwijderen.

---

## Hoe je hierna iets aanpast

Je hoeft geen Python te kunnen. Alles wat je normaal verandert staat in
`data.py`, en dat bestand kun je gewoon in GitHub in je browser bewerken:

1. Ga naar [data.py](https://github.com/joukesluimer/topschilder/blob/main/data.py)
2. Klik op het potloodje rechtsboven
3. Pas aan, klik **Commit changes**
4. GitHub bouwt de site opnieuw, controleert 'm, en publiceert. Twee minuten later staat het live

Wat waar staat:

| Wat je wilt aanpassen | Waar |
|---|---|
| Btw-nummer toevoegen | `data.py`, bovenin bij `SITE`, regel `"btw": ""` — vul in en het verschijnt vanzelf op contact en in de voorwaarden |
| Plaats toevoegen | `data.py`, lijst `PLAATSEN` (levert automatisch 7 nieuwe pagina's) |
| Prijzen bijstellen | `data.py`, `prijs_van` / `prijs_tot`, of `PRIJSINDEX` per provincie |
| E-mailadres | `data.py`, bij `SITE` |
| Leadtarieven voor schilders | `build.py`, functie `build_voor_schilders` |
| Vormgeving | `assets.py`, `STYLE_CSS` |
| Supabase-koppeling | `assets.py`, `CONFIG_JS` |

Gaat er iets mis in je aanpassing, dan faalt de controlestap en blijft de oude
site gewoon staan. Je kunt de boel dus niet slopen met een typefout.

---

## De volgorde die geld oplevert

Uit `STARTGIDS.md`, maar dit is het stukje dat telt:

1. **DNS zetten** (vandaag)
2. **Enforce HTTPS aanvinken** (zodra het kan)
3. **Search Console** — sitemap indienen, tien belangrijkste plaatspagina's handmatig laten indexeren
4. **Schilders bellen** — 25 bedrijven in Zeewolde, Almere, Lelystad, Dronten, Harderwijk. Doel: 6 aangesloten. Belscript staat in de startgids
5. **Pas dán Google Ads aanzetten**, €15 per dag, alleen in plaatsen waar je schilders hebt

Stap 4 vóór stap 5. Een lead die je aan niemand kunt verkopen is een kostenpost,
en dat is precies waar bijna iedereen in deze markt op stukloopt.

# Content-ronde 5: kosten en kennisbank (27 november 2026)

Branch `claude/ts-content-61fb5b`. Niet gepusht.

## 1. Onderzoek (Semrush, database nl, november 2026)

### Waar topschilder.nl nu staat (geld-zoekwoorden)

| Zoekwoord | Volume | Positie | Pagina die rankt |
|---|---|---|---|
| kosten schilderwerk buiten | 170 | 97 | /prijzen/ |
| buitenschilderwerk kosten | 140 | 82 | /schilderwerk/buitenschilderwerk/ |
| kosten schilder | 390 | 64–74 | /kosten/ |
| wat kost schilderen per m2 | 390 | 87 | /kosten/ (niet /kosten/schilderen-per-m2/) |
| wat kost een schilder per m2 | 390 | 92 | /prijzen/ |
| huis schilderen kosten | 170 | 16 | /kosten/huis-schilderen/ |
| kosten schilderen trap | 210 | 58 | /kosten/ |

Conclusie: voor "kosten buitenschilderwerk" (samen ~450/mnd), "binnenschilderwerk kosten"
en "houtrot herstellen" (260/mnd) had de site geen eigen kostenpagina. Google pakt dan
/prijzen/, /kosten/ of de dienstpagina, en die staan alle drie op 60–97.

### Top 3 in Google (wat we moesten verslaan)

- **kosten buitenschilderwerk:** Homedeal (buitenschilder-kosten), De Schilderscombinatie (blog), Reddit.
- **schilder prijs per m2:** Homedeal (schilder-kosten), Zoofy (kosten-binnenschilderwerk), schilderwerken-expert.
- **binnenschilderwerk kosten:** schilder-concurrent, Werkspot (403), Zoofy.
- **houtrot herstellen kosten:** Semrush heeft geen SERP-data.

Wat zij missen: geen direct antwoord bovenaan (Homedeal), tegenstrijdige prijzen op één pagina
(Homedeal tabel €35–40/m², FAQ €30–50/m²), geen btw-uitleg bij de m²-tabel (De Schilderscombinatie),
geen valkuilen in offertes, geen rekenvoorbeeld per onderdeel.

### Zoekwoorden met volume zonder (goede) pagina

| Onderwerp | Zoekwoorden (maandvolume) | Opgelost met |
|---|---|---|
| Wit voor kozijnen | ral 9010 22.200, ral 9001 12.100, gebroken wit 2.900 | /kennisbank/ral-9010-of-ral-9001/ |
| Glaslatten | glaslatten 2.900 | /kennisbank/glaslatten-vervangen/ |
| Beits | beits 2.900, houtverf 1.600, dekkende beits 1.000 | /kennisbank/beits-of-verf/ |
| Plamuren | plamuren 1.000 | /kennisbank/muur-plamuren/ |
| Deuren | deuren verven 720, hoe verf je een deur 110 | /kennisbank/binnendeuren-verven/ |
| Voordeur | voordeur schilderen 590, voordeur kleur 320, voordeur verven 260 | /kennisbank/voordeur-schilderen/ |
| Oude verf eraf | verf verwijderen hout 480, verf afbijten 90 | /kennisbank/oude-verf-verwijderen/ |
| VvE en MJOP | meerjarenonderhoudsplan 390, vve schilderwerk 90 | /kennisbank/schilderwerk-vve/ |
| Houtrot | houtrot 1.300, houtrot herstellen 260, houtrot repareren epoxy 320 | /kosten/houtrot-herstellen/ + verdiept artikel |

Overige volumes die we bekeken (geen actie, want productzoekwoord of al gedekt):
muurverf 9.900, latex 8.100, grondverf 3.600, muur verven 2.900, boeiboord 2.400,
windveer 2.400, buitenverf 1.900, lijnolie 1.300, plafond verven 1.000,
hoeveel verf per m2 720 (/gids/verf-berekenen/), buiten schilderen temperatuur 260
(/gids/wanneer-buiten-schilderen/), kunststof verven 720 (kostenpagina bestaat).

### Btw

De opdracht noemde "incl. 21% btw". Voor schilderwerk aan een woning ouder dan twee jaar
geldt in 2026 nog steeds 9% (Belastingdienst; ook Trustoo en Jongbloed bevestigen dit voor 2026).
De site rekent daarom, net als alle bestaande pagina's, richtprijzen inclusief btw met de
uitleg 9%/21%. Waar een bron 21% hanteert (Zoofy), staat dat erbij.

## 2. Geldpagina's (kosten_ronde5.py)

Kleine haak in `build_kosten` (build.py): optionele velden `direct`, `prijstabel` en
`valkuilen`, plus `KOSTEN_OVERZICHT` voor /kosten/. Pagina's zonder die velden blijven gelijk.

| URL | Wat | Doelzoekwoorden |
|---|---|---|
| /kosten/buitenschilderwerk/ | **nieuw** | kosten buitenschilderwerk, buitenschilderwerk kosten, kosten schilderwerk buiten (~450/mnd) |
| /kosten/binnenschilderwerk/ | **nieuw** | binnenschilderwerk kosten, woonkamer schilderen kosten, huis binnen schilderen kosten |
| /kosten/houtrot-herstellen/ | **nieuw** | houtrot herstellen (260), houtrot reparatie kosten (50) |
| /kosten/kozijnen-schilderen/ | verdiept | kozijnen schilderen kosten (210), kosten kozijnen schilderen (210) |
| /kosten/schilderen-per-m2/ | verdiept | schilder prijs per m2 (210), kosten schilder per m2 (110), wat kost schilderen per m2 (390) |
| /kosten/huis-schilderen/ | direct antwoord + valkuilen | huis schilderen kosten (170) |
| /kosten/ | verdiept | kosten schilder (390), wat kost een schilder (590), schilderwerk prijzen (110) |

Elke pagina heeft: een direct antwoord, een prijstabel met Topschilder naast Homedeal,
De Schilderscombinatie, Zoofy of Slimster (peildatum november 2026), rekenvoorbeelden,
"wat bepaalt de prijs", valkuilen in offertes met een link naar de offertechecker,
een FAQ van 7–10 vragen met FAQPage-JSON-LD, en interne links.

Eigen inschattingen (staat zo op de pagina): plinten €4–€8/m, glaslatten €8–€20/m,
kitvoegen €6–€15/m, voorstrijken €2–€4/m², behang verwijderen €4–€10/m², onderdorpel €150–€400.

## 3. Nieuwe artikelen (kennis_ronde5.py)

/kennisbank/ral-9010-of-ral-9001/, /kennisbank/voordeur-schilderen/, /kennisbank/binnendeuren-verven/,
/kennisbank/glaslatten-vervangen/, /kennisbank/muur-plamuren/, /kennisbank/oude-verf-verwijderen/,
/kennisbank/beits-of-verf/, /kennisbank/schilderwerk-vve/.
Gekoppeld zoals ronde 4 (onderaan kennis_artikelen.py) en via DIENST_ARTIKELEN in kennisbank.py.
Nieuwe bronnen, allemaal geopend: Wijzonol Dekkend Tuinbeits (PIB), CetaBever Gevel Hout Snel Beits
Dekkend (27-02-2026), Alabastine Sneldrogende Muurvuller en Muurglad Rolbaar, Sikkens Rubbol BL
Endurance, Rijksoverheid (VvE-reservefonds), RAL CLASSIC, Praxis (RAL 9001/9010).

## 4. Verdiepte artikelen

goede-offerte-schilderwerk, behang-verwijderen, kozijnen-schuren-en-voorbereiden, latex-of-muurverf,
verf-op-waterbasis-of-terpentinebasis: elk 2–3 nieuwe secties (rekenvoorbeeld, tabel) en 2–3 FAQ's.

## Controle

`python3 build.py && python3 verify.py`: **ALLES OK**, 268 URL's in de sitemap (was 257): 3 nieuwe kostenpagina's en 8 nieuwe artikelen.
Headless Chrome: /kosten/buitenschilderwerk/ en /kennisbank/ral-9010-of-ral-9001/ op 1280 en 375 px.
Let op: headless Chrome houdt de viewport minimaal 500 px breed. Een echte 375 is getest via een
iframe van 375 px. Geen horizontale scroll op de pagina; brede tabellen scrollen in hun eigen kader.

## Open punten

- **Kannibalisatie:** /kosten/buitenschilderwerk/ en /schilderwerk/buitenschilderwerk/ (seo_titel "…kosten en werkwijze")
  zitten dicht bij elkaar. Over 4–6 weken in Search Console kijken. Rankt de dienstpagina nog op "kosten",
  haal "kosten" dan uit haar seo_titel. Hetzelfde geldt voor binnenschilderwerk en houtrot-reparatie.
- **Btw:** de opdracht noemde 21%; de site houdt 9% aan omdat dat in 2026 nog geldt (zie hierboven).
- **Bronnen die niet lukten:** Werkspot (403), wetten.overheid.nl (botcheck) en de officiële RAL-namen in een document van RAL zelf.

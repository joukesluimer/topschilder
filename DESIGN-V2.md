# Design v2 — audit en aanpak (27-11-2026)

Gekeken naar de homepage, /schilderwerk/buitenschilderwerk/, /schilder/almere/,
/kosten/boeidelen-schilderen/, /kennisbank/houtrot-herkennen-en-herstellen/ en
/offerte-aanvragen/, op 1280 px en op 375 px (een echt viewport van 375 px, via een iframe).

## De 10 zwakste punten (vóór)

1. **Logo onleesbaar in de header.** Het logo staat gestapeld: een poppetje bovenop
   "TOPSCHILDER.NL" en daaronder een slogan. In de header is het ongeveer 36 px hoog.
   Dan is de woordnaam ±7 px hoog en de slogan ±3 px: niet te lezen.
2. **Logo is nagetekend uit een PNG.** De letters hebben rafelige, getraceerde randen
   (33 kB aan paden). De slogan zegt "bij **u**", terwijl de hele site "je" gebruikt.
3. **Favicon zegt niets op 16 px.** Het poppetje met helm wordt een bruine vlek met een
   oranje stip.
4. **og:image is een SVG.** WhatsApp, Facebook en LinkedIn tonen geen SVG. Een gedeelde
   link krijgt dus geen beeld.
5. **Homepage-hero is troebel.** Een donkerbruine laag over een donkere foto: de foto
   verdwijnt en er is geen punt waar het oog naartoe gaat. Er is geen tweede route
   (eerst prijzen bekijken) en de drie "pillen" onder de vinkjes herhalen alleen de diensten.
6. **Koppen zonder karakter.** Alles staat in het systeemlettertype. Koppen, knoppen en
   cijfers lijken op elkaar; de penseelstreep onder "werkt" en "Topschilder" ligt dwars
   over de letters.
7. **Header is vlak.** Geen actieve staat in het menu, geen scheiding als je scrollt, en de
   oranje knop is hoekig terwijl de rest van de site rond is.
8. **Vertrouwensbalk op mobiel is rommelig.** Vier items in een 2×2-raster met kleine,
   ongelijk afbrekende tekst ("Meestal binnen 1 / werkdag reactie").
9. **Bedragen breken middenin.** Op mobiel staan in kostentabellen bedragen als
   "€300 –" op de ene regel en "€660" op de volgende.
10. **Lange artikelen zijn een grijze tekstmuur.** Op de kennisbank en dienstpagina's:
    smalle hiërarchie, bullets en checklists lijken op elkaar, een blok met acht
    onderstreepte links in de prijscallout leest als ruis.

Geen horizontale scroll gevonden op 375 px (scrollWidth = 375 op alle zes pagina's).

## Aanpak

- `stijl_v2.py`: site-brede CSS, één regel onderaan `assets.py`.
- Homepage: nieuwe hero-opmaak (lichter, foto zichtbaar, duidelijke conversie).
- Logo: nieuw, horizontaal, eigen lettering als SVG-paden, beeldmerk "roller-T",
  favicon op een 16-px-raster, og-image als PNG.

## Wat er is gedaan

| Punt | Oplossing |
|---|---|
| 1–3 Logo en favicon | Nieuw horizontaal logo in `merk_data.py`: beeldmerk "roller-T" + eigen ronde lettering, opgebouwd uit SVG-lijnen (geen lettertype, ±1,4 kB). Favicon apart getekend op 16×16. Slogan uit het logo (was "u"). |
| 4 og:image | `merk/og-image.png` (1200×630), plus apple-touch-icon en icon-192/512. Opnieuw maken: `python3 merk_maken.py`. |
| 5 Hero | `.hero-v2`: foto zichtbaar via een verloop van links naar rechts, oranje accent in de kop, twee routes (prijzen / offerte laten checken). Op mobiel staat het formulier sneller in beeld. |
| 6 Koppen | Zwaarder en strakker; penseelstreep zakt onder de letters. |
| 7 Header | Logo groter en leesbaar, hover-streep in het menu, pilknop. |
| 8 Vertrouwensbalk | Op mobiel nette 2×2-tegels. |
| 9 Bedragen | `zachte_spaties()` in `stijl_v2.py`: harde spatie + woordverbinder, "€300 – €660" blijft heel. |
| 10 Lange teksten | Rustiger regelafstand, checklists met een echt vinkje, kostenlinks in de prijscallout als chips. |
| Extra: contrast | Wit op oranje haalde maar 2,4–2,6:1. Primaire knoppen hebben nu donkere tekst (±6,8:1), net als de header-knop al had. |

Gecontroleerd: `build.py && verify.py` → ALLES OK; 375 px zonder horizontale scroll op alle zes
pagina's; automatische contrastcheck (alle tekst met een effen achtergrond) zonder AA-fouten op
8 pagina's × 2 breedtes.

## Nog open (voorstel)

- `/offerte-aanvragen/` op mobiel: het formulier staat pas na ±1100 px (eerst vier vinkjes en een tip).
- Organization-JSON-LD heeft geen `logo`; `https://topschilder.nl/assets/merk/icon-512.png` kan erin.
- Menu heeft geen actieve staat (header() weet niet op welke pagina hij staat).

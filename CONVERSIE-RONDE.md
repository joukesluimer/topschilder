# Conversieronde (ts-conversie, november 2026)

Doel: meer bezoekers die een offerte aanvragen, zonder valse claims.
De Supabase-koppeling en de veldnamen (`dienst`, `postcode`, `plaats`, `pandtype`,
`omvang`, `planning`, `omschrijving`, `naam`, `email`, `telefoon`) zijn niet veranderd.

## 1. Analyse (nulmeting, screenshots 1280 en 375 px)

| Waar | Wat we zagen | Waarom mensen afhaken |
|---|---|---|
| Alle 1.632 links naar `/offerte-aanvragen/` | Kale link, zonder dienst of plaats | Wie op een dienst- of plaatspagina klikt, moet op de offertepagina alles opnieuw kiezen. |
| Formulier op dienst-, plaats- en plaats×dienstpagina's | `app.js` kan dienst en plaats voorvullen via `body data-dienst/data-plaats`, maar geen enkele pagina zette die | De bezoeker leest "Buitenschilderwerk Almere" en moet toch eerst "Buitenschilderwerk" aanklikken en "Almere" typen. |
| Sticky knop op mobiel | Gaat altijd naar `/offerte-aanvragen/`, ook als er een formulier op de pagina staat | Op de offertepagina zelf herlaadt de knop dezelfde pagina. Op plaatspagina's verlaat je de pagina en verlies je de context. |
| `/offerte-aanvragen/` op 375 px | Formulier begint pas na ruim 1,5 scherm tekst | Wie komt om aan te vragen, moet eerst langs vier opsommingen en een tip scrollen. |
| Voortgangsbalk | Vier streepjes, geen tekst | Onduidelijk hoeveel er nog komt en wat elke stap vraagt. |
| Velden | Geen uitleg bij postcode, e-mail en telefoon | Juist bij telefoonnummer twijfelen mensen: wie belt me, krijg ik reclame? |
| Kostenpagina's (19) | Eén kale CTA halverwege: "Wat kost X bij jou?" met een knop naar een leeg formulier | De vraag wordt gesteld maar niet beantwoord. Wie een prijs zoekt, wil eerst een indicatie voor zijn eigen situatie. |
| Na de aanvraag | Alleen een korte tekst in de bedankmelding | Vooraf staat nergens eerlijk wat er gebeurt: wie belt, wanneer, en wat als er geen schilder is. |
| Hero en trustbar | "Meestal binnen 1 werkdag reactie", "Alleen bedrijven met KvK-inschrijving en verzekering" | Niet aantoonbaar (zie punt 3). |

## 2. Verbeteringen

Alles zit in `conversie.py` (één hook in `write()`, net als `seo_extra.verrijk`), plus
`/assets/js/conversie.js` en `/assets/css/conversie.css`. build.py: 3 regels.

| Verbetering | Hoe |
|---|---|
| Slim voorvullen | `body` krijgt `data-dienst`/`data-plaats` op dienst-, plaats-, plaats×dienst- en kostenpagina's. Is de dienst bekend, dan begint het formulier bij stap 2 met "Je klus: Buitenschilderwerk · wijzigen". De plaats van een eerder bezochte plaatspagina wordt dit bezoek onthouden (sessionStorage). |
| Links naar het formulier | Op een pagina mét formulier springen alle offerte-links naar `#offerte`. Zonder formulier krijgen ze `?dienst=…&plaats=…&via=<paginatype>` mee. |
| Voortgang en hulpteksten | "Stap 2 van 4 · Adres en pand" … "Laatste stap · Je gegevens". Hulpteksten bij postcode, omvang, e-mail en telefoon. |
| Sticky mobiele CTA | Tekst per paginatype ("Offertes in Almere", "Offertes voor spuiten", "Wat kost het bij jou?", "Start je aanvraag"). Valt weg als het formulier of de kosten-tussenstap in beeld is, en zolang je in een veld typt (toetsenbord open). |
| Wat gebeurt er na je aanvraag | Uitklapblok onder elk formulier (open op `/offerte-aanvragen/`). Alleen wat in WERKWIJZE-LEADS.md staat: directe bevestigingsmail, wij lezen mee, max. 3 schilders bellen zelf, intrekken via de bevestigingsmail, en eerlijk melden als er geen schilder is. |
| Kosten-tussenstap | Op alle 19 kostenpagina's vervangt "Wil je weten wat X bij jou kost?" de kale CTA: aantal + plaats → indicatie op basis van de eigen richtprijs, knop naar een voorgevuld formulier (dienst, plaats en omschrijving). Op desktop één keer per bezoek een klein kaartje bij exit-intent (muis naar de tabbalk), wegklikbaar. |
| `/offerte-aanvragen/` mobiel | Formulier direct onder kop en intro, de opsommingen eronder. |

Getest in headless Chrome (1280 en 375 px), met verzoeken naar Supabase en Make
geblokkeerd: hele flow kostenpagina → formulier → laatste stap ingevuld, niet verstuurd.
Geen consolefouten. Screenshots voor/na staan in de gedeelde notitiemap (`conversie-shots/`).

## 3. Teksten in de hero: kunnen we ze waarmaken?

| Was | Oordeel | Nu |
|---|---|---|
| "Meestal binnen 1 werkdag reactie" (trustbar) | Niet aantoonbaar. Aanvragen worden met de hand doorgestuurd ("liefst binnen een paar uur", WERKWIJZE-LEADS.md), er is pas één echte lead geweest, en of en wanneer een schilder belt, hebben we niet in de hand. Soms is er geen schilder in die plaats. | "**Direct** een bevestiging per mail" — dat doet Make automatisch (getest 22 nov). |
| "Alleen bedrijven met KvK-inschrijving en verzekering" | Deels. De werkwijze zegt: bij de intake vragen naar KvK en verzekering en "laat een polis of bewijs mailen". Dat is een vraag, geen aantoonbare controle van elk bedrijf. | "We vragen elke schilder om bewijs van KvK-inschrijving en verzekering". |

Zelfde correctie op: FAQ homepage ("Hoe snel…", "Hoe worden schilders geselecteerd?"),
blok "Waarom via Topschilder", checklist op plaatspagina's, bedankmelding, /bedankt/ en
de actiepagina's.

Niet aangepast, wel om naar te kijken:
- `MAKE-BEVESTIGINGSMAIL.md` (de mail in Make) belooft nog "doorgaans binnen één werkdag".
  Dat staat in Make, niet in de site; pas het daar aan als je het niet kunt waarmaken.
- "We reageren doorgaans binnen één werkdag" op /contact/ gaat over jezelf; laten staan
  als je dat haalt.
- /over-ons/ "Welke schilders we toelaten" en de voorwaarden noemen eisen aan schilders
  (KvK, verzekering, reactie binnen één werkdag). Dat zijn afspraken, geen claims naar
  klanten, en zijn daarom blijven staan.

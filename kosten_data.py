"""Kostenpagina's: één pagina per zoekvraag "wat kost ...".

Prijzen zijn richtprijzen inclusief materiaal en btw, tenzij anders vermeld.
Houd ze in lijn met DIENSTEN in data.py: kozijnen buiten = buitenschilderwerk,
keukenfronten en trappen vallen onder spuitwerk en binnenschilderwerk.
"""

KOSTEN = [
    {
        "slug": "keuken-spuiten",
        "klus": "keuken spuiten",
        "h1": "Wat kost een keuken spuiten in 2026?",
        "title": "Keuken spuiten kosten 2026: prijs per front",
        "description": "Een keuken laten spuiten kost €45 tot €95 per front. Een gemiddelde keuken met 15 tot 20 fronten komt uit op €675 tot €1.900. Met rekenvoorbeelden en bespaartips.",
        "dienst": "spuitwerk",
        "eenheid": "per front (deur of la)",
        "van": 45,
        "tot": 95,
        "kort": "€45 – €95 per front",
        "intro": "Je keuken laten spuiten is een stuk goedkoper dan een nieuwe keuken. Je betaalt vooral voor het voorwerk: ontvetten, schuren en gronden. Het spuiten zelf gaat snel. Hieronder zie je wat schilders rekenen, waar het verschil in zit en hoe je een offerte beoordeelt.",
        "voorbeelden": [
            ("Kleine keuken, 10 fronten", 10, "Rechte keuken in een appartement, zonder hoge kasten."),
            ("Gemiddelde keuken, 16 fronten", 16, "Hoekkeuken met boven- en onderkasten, de meest voorkomende situatie."),
            ("Grote keuken met eiland, 24 fronten", 24, "Eiland, hoge kasten en een paar ladeblokken."),
        ],
        "extra": [
            ("Zijpanelen en plinten", "€25 – €60 per stuk"),
            ("Nieuwe grepen monteren", "€5 – €15 per greep, exclusief de grepen"),
            ("Kastombouw aan de binnenkant", "vaak niet nodig; vraag apart om een prijs"),
        ],
        "prijsfactoren": [
            "Het materiaal van de fronten. MDF en hout zijn makkelijk. Kunststof en hoogglans folie hebben een hechtprimer nodig, en losse folie moet er eerst af.",
            "Of de fronten in de werkplaats of bij je thuis worden gespoten. In de werkplaats wordt het strakker en heb je minder overlast, maar er komt transport bij.",
            "Het aantal lagen en de glansgraad. Zijdeglans is het gangbaarst. Hoogglans laat elk foutje zien en kost meer werk.",
            "Profielen en kaders. Vlakke fronten zijn sneller klaar dan fronten met een kader of freeswerk.",
            "Of de kastombouw, zijpanelen en plinten mee moeten.",
        ],
        "uitleg": [
            ("Wat je ervoor krijgt", "Een goede schilder haalt de fronten eraf, ontvet ze, schuurt ze op, zet een hechtprimer en spuit twee lagen lak. Daarna gaan de fronten terug met de oude of nieuwe grepen. Reken op drie tot vijf werkdagen, waarvan je keuken meestal één tot twee dagen niet te gebruiken is."),
            ("Spuiten of rollen?", "Rollen kan goedkoper, maar je ziet de structuur van de roller in het lakwerk. Bij een keuken, waar het licht er schuin op valt, zie je dat snel. Spuiten geeft een gladde, fabrieksachtige laag. Het verschil zit vooral in de afwerking, minder in de duurzaamheid."),
        ],
        "tips": [
            "Laat alleen de fronten spuiten als de ombouw nog goed is. Dat scheelt vaak een derde van de prijs.",
            "Vervang de grepen in dezelfde ronde. Nieuwe grepen met een ander gatenpatroon passen dan meteen.",
            "Vraag welke lak er wordt gebruikt. Een watergedragen 2K-lak of PU-lak is beter bestand tegen vet en stoten dan gewone muurlak.",
            "Kunststof keukens met loslatende folie: vraag eerst of spuiten zin heeft. Soms is nieuwe fronten laten maken voordeliger.",
        ],
        "btw": "Of je 9% of 21% btw betaalt, hangt af van hoe het werk gebeurt en hoe de schilder het factureert. Vraag de schilder om het btw-tarief op de offerte te zetten.",
        "faq": [
            ("Hoeveel kost het om een keuken te laten spuiten?",
             "Reken op €45 tot €95 per front. Een gemiddelde keuken met 16 fronten kost dan €720 tot €1.520, exclusief extra's zoals zijpanelen of nieuwe grepen."),
            ("Is keuken spuiten goedkoper dan een nieuwe keuken?",
             "Ja, meestal flink. Een nieuwe keuken kost al snel enkele duizenden euro's. Spuiten blijft voor een gemiddelde keuken meestal onder de €2.000. Het werkt alleen als de kasten, scharnieren en het werkblad nog goed zijn."),
            ("Hoe lang blijft een gespoten keuken mooi?",
             "Met een goede voorbehandeling en een slijtvaste lak tien jaar of langer. Waar het misgaat, is bijna altijd het voorwerk: slecht ontvet of geen hechtprimer."),
            ("Kan een kunststof of hoogglans keuken gespoten worden?",
             "Vaak wel, met een speciale hechtprimer. Laat folie los, dan moet die er eerst helemaal af. Vraag een schilder om eerst naar de fronten te kijken."),
            ("Hoe lang kan ik mijn keuken niet gebruiken?",
             "Bij spuiten in de werkplaats meestal één tot twee dagen zonder deurtjes. Bij spuiten op locatie moet de keuken langer worden afgeplakt."),
        ],
    },
    {
        "slug": "trap-schilderen",
        "klus": "trap schilderen",
        "h1": "Wat kost een trap schilderen in 2026?",
        "title": "Trap laten schilderen kosten 2026: prijs per trap",
        "description": "Een trap laten schilderen kost €350 tot €950, afhankelijk van het type trap en de staat van de oude lak. Met prijzen per traptype, rekenvoorbeelden en tips.",
        "dienst": "binnenschilderwerk",
        "eenheid": "per trap (één verdieping)",
        "van": 350,
        "tot": 950,
        "kort": "€350 – €950 per trap",
        "intro": "Een trap schilderen is precisiewerk: veel randen, veel hoeken en een trap die je ondertussen zo weinig mogelijk wilt missen. Daardoor is het duurder dan je op basis van het aantal vierkante meters zou verwachten. Dit zijn de richtprijzen per traptype.",
        "voorbeelden": [
            ("Dichte rechte trap, 13 treden", None, "€350 – €600. De meest voorkomende trap in een rijtjeswoning."),
            ("Trap met kwart- of halve draai", None, "€450 – €750. Meer snijwerk bij de draaitreden en de spil."),
            ("Open trap met spijlen", None, "€600 – €950. Elke spijl moet rondom worden geschuurd en gelakt."),
        ],
        "extra": [
            ("Trapgat en wanden langs de trap", "€150 – €400, afhankelijk van de hoogte"),
            ("Oude traploper of tapijt verwijderen", "€75 – €200, inclusief lijmresten"),
            ("Leuning apart schilderen of beitsen", "€75 – €175"),
        ],
        "prijsfactoren": [
            "Het type trap. Een dichte rechte trap is het snelst klaar, een open trap met spijlen kost het meeste tijd.",
            "De staat van de oude laag. Afbladderende lak of oude vloerverf moet eerst worden geschuurd of afgebeten.",
            "Slijtvastheid. Op treden hoort een speciale traplak of vloerlak, en die is duurder dan gewone grondverf en lak.",
            "Of je de trap tussendoor moet kunnen gebruiken. Om en om schilderen (eerst de even treden, dan de oneven) kost een extra werkdag.",
            "Of het trapgat, de leuning en de wanden meegaan.",
        ],
        "uitleg": [
            ("Wat je ervoor krijgt", "Schuren, ontvetten, gaten en naden vullen, een grondlaag en twee lagen slijtvaste traplak op treden en stootborden. De zijkanten (de trapbomen) en de leuning gaan mee. Meestal is een schilder één tot drie dagen bezig, plus droogtijd."),
            ("Kun je de trap tussendoor gebruiken?", "Ja, als de schilder om en om werkt: eerst de oneven treden, dan de even treden. Je stapt dan een trede over. Vraag ernaar bij de offerte, want het kost wat meer tijd."),
        ],
        "tips": [
            "Haal een oude traploper zelf weg als je dat durft. Lijmresten laten zitten is beter dan eraan trekken; de schilder schuurt ze weg.",
            "Combineer de trap met het trapgat of de overloop. De opstartkosten deel je dan.",
            "Kies een lichte, zijdeglans of matte traplak. Hoogglans op treden is glad en laat elke kras zien.",
            "Vraag naar de droogtijd tot je de trap weer normaal mag belasten. Bij veel traplakken is dat een paar dagen.",
        ],
        "btw": "Schilderwerk aan een woning die ouder is dan twee jaar valt onder het lage btw-tarief van 9%, inclusief de gebruikte verf. Staat er 21% op de offerte, vraag dan waarom.",
        "faq": [
            ("Wat kost een trap laten schilderen?",
             "Tussen €350 en €950. Een dichte rechte trap zit aan de onderkant, een open trap met spijlen aan de bovenkant. Het trapgat en de leuning komen er soms apart bij."),
            ("Hoe lang duurt het om een trap te schilderen?",
             "Meestal één tot drie werkdagen, plus droogtijd. Om en om schilderen, zodat je de trap kunt blijven gebruiken, duurt een dag langer."),
            ("Welke verf hoort op een trap?",
             "Op de treden een slijtvaste traplak of vloerlak. Op de trapbomen, stootborden en leuning kan gewone grondverf met lak."),
            ("Kan ik een gelakte trap overschilderen?",
             "Ja. De oude lak wordt opgeschuurd, zodat de nieuwe laag hecht. Bladdert de oude laag, dan moet die eerst helemaal weg."),
        ],
    },
    {
        "slug": "kozijnen-schilderen",
        "klus": "kozijnen schilderen",
        "h1": "Wat kost kozijnen schilderen in 2026?",
        "title": "Kozijnen schilderen kosten 2026: prijs per kozijn",
        "description": "Buitenkozijnen laten schilderen kost €90 tot €190 per kozijn, binnenkozijnen €45 tot €95. Met rekenvoorbeelden per woningtype, steigerkosten en btw-regels.",
        "dienst": "buitenschilderwerk",
        "eenheid": "per buitenkozijn",
        "van": 90,
        "tot": 190,
        "kort": "€90 – €190 per buitenkozijn",
        "intro": "Kozijnen zijn het grootste deel van een gemiddelde buitenschilderbeurt. Schilders rekenen ze meestal per stuk, met de ramen, de draaiende delen en de dorpels erbij. Het verschil tussen een lage en een hoge offerte zit bijna altijd in de staat van het hout en in de steiger.",
        "voorbeelden": [
            ("Tussenwoning, voor- en achtergevel", 8, "Ongeveer acht kozijnen, plus een voordeur en een achterdeur."),
            ("Hoekwoning of twee-onder-een-kap", 12, "Een extra zijgevel met meer kozijnen."),
            ("Vrijstaande woning", 18, "Kozijnen rondom, vaak met dakkapel en boeiboorden."),
        ],
        "extra": [
            ("Binnenkozijnen (deurkozijnen binnen)", "€45 – €95 per kozijn"),
            ("Steiger of hoogwerker voor de bovenverdieping", "€300 – €900 per gevel, afhankelijk van de hoogte"),
            ("Houtrot repareren", "€85 – €275 per reparatieplek"),
        ],
        "prijsfactoren": [
            "De staat van het hout. Licht verweerde verf vraagt alleen schuren en twee lagen. Afbladderende verf en houtrot vragen veel meer voorwerk.",
            "De grootte en vorm van het kozijn. Een groot kozijn met meerdere ramen en roeden kost meer dan een simpel klein raam.",
            "Of er een steiger of hoogwerker nodig is. Bij een bovenverdieping is dat bijna altijd zo.",
            "Het aantal lagen. Een goede beurt is minimaal één grondlaag op kale plekken en twee aflakken.",
            "Kitwerk. Oude kitvoegen rond het glas vervangen is extra werk, maar voorkomt nieuwe houtrot.",
        ],
        "uitleg": [
            ("Wat je ervoor krijgt", "Ontvetten, schuren, losse verf verwijderen, kale plekken gronden, scheuren en naden kitten en twee lagen aflakken. Bij een goede offerte staat erbij hoe houtrot wordt afgerekend: per plek, of op regie met een maximum."),
            ("Hoe vaak moeten kozijnen geschilderd worden?", "Bij dekkende verf ongeveer elke zes tot acht jaar. Kozijnen op het zuiden en westen gaan sneller. Wacht je te lang, dan komt er houtrot bij en wordt de rekening snel twee keer zo hoog."),
        ],
        "tips": [
            "Plan buitenschilderwerk in het voor- of naseizoen. In september en oktober hebben schilders vaker ruimte en zitten ze scherper.",
            "Laat binnen- en buitenkozijnen in één keer doen. Je deelt dan de voorrijkosten en de opstart.",
            "Vraag of de steiger in de prijs zit. Een offerte zonder steiger lijkt goedkoper, maar is het vaak niet.",
            "Vraag per offerte hoe houtrot wordt afgerekend. Dat is de grootste onbekende in de prijs.",
        ],
        "btw": "Schilderwerk aan een woning die ouder is dan twee jaar valt onder het lage btw-tarief van 9%, inclusief de verf. Houten inzetstukken en het vervangen van onderdorpels vallen onder 21%. Een nette offerte splitst die posten.",
        "faq": [
            ("Wat kost het schilderen van een kozijn?",
             "Een buitenkozijn kost gemiddeld €90 tot €190, inclusief ramen en dorpels. Een binnenkozijn kost €45 tot €95. Steiger en houtrotherstel komen er meestal apart bij."),
            ("Wat kost het schilderen van alle kozijnen van een tussenwoning?",
             "Met ongeveer acht kozijnen en twee deuren kom je op €900 tot €1.900, plus €300 tot €900 als er een steiger nodig is voor de bovenverdieping."),
            ("Rekent een schilder per kozijn of per uur?",
             "Meestal per kozijn of als vaste prijs voor de hele woning. Alleen houtrotherstel wordt soms op uurbasis gerekend. Vraag dan om een maximumbedrag."),
            ("Wanneer kun je kozijnen het beste laten schilderen?",
             "Van april tot en met oktober, bij droog weer boven de tien graden. Het nazomerseizoen is vaak het voordeligst."),
        ],
    },
]

KOSTEN_BY_SLUG = {k["slug"]: k for k in KOSTEN}


# Prijsbanden voor de automatische offertecheck. De sleutels moeten gelijk
# blijven aan CATEGORIEEN in supabase/functions/offertecheck/index.ts.
# Bedragen inclusief btw, behalve als excl_btw True is.
PRIJSBANDEN = {
    "muren_plafonds_m2": {"naam": "Muren en plafonds", "van": 10, "tot": 22, "eenheid": "per m²"},
    "buitenkozijn": {"naam": "Buitenkozijnen", "van": 90, "tot": 190, "eenheid": "per kozijn"},
    "binnenkozijn": {"naam": "Binnenkozijnen", "van": 45, "tot": 95, "eenheid": "per kozijn"},
    "deur": {"naam": "Deuren", "van": 65, "tot": 185, "eenheid": "per deur"},
    "keukenfront": {"naam": "Keukenfronten", "van": 45, "tot": 95, "eenheid": "per front"},
    "trap": {"naam": "Trap", "van": 350, "tot": 950, "eenheid": "per trap"},
    "houtrot_plek": {"naam": "Houtrotreparatie", "van": 85, "tot": 275, "eenheid": "per plek"},
    "behang_m2": {"naam": "Behangen", "van": 9, "tot": 24, "eenheid": "per m²"},
    "uurloon": {"naam": "Uurloon", "van": 45, "tot": 68, "eenheid": "per uur", "excl_btw": True},
    "steiger": {"naam": "Steiger of hoogwerker", "van": 300, "tot": 900, "eenheid": "per gevel"},
}

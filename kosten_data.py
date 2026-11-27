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
        "description": "Een keuken laten spuiten kost €45 tot €95 per front. Een gemiddelde keuken met 15 tot 20 fronten komt uit op €675 tot €1.900. Met rekenvoorbeelden en tips.",
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
        "description": "Buitenkozijnen laten schilderen kost €90 tot €190 per kozijn, binnenkozijnen €35 tot €75. Met rekenvoorbeelden per woningtype, steigerkosten en btw-regels.",
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
            ("Binnenkozijnen (deurkozijnen binnen)", "€35 – €75 per kozijn"),
            ("Steiger of hoogwerker voor de bovenverdieping", "€300 – €900 per gevel, afhankelijk van de hoogte"),
            ("Houtrot repareren", "€50 – €275 per reparatieplek"),
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
             "Een buitenkozijn kost gemiddeld €90 tot €190, inclusief ramen en dorpels. Een binnenkozijn kost €35 tot €75. Steiger en houtrotherstel komen er meestal apart bij."),
            ("Wat kost het schilderen van alle kozijnen van een tussenwoning?",
             "Met ongeveer acht kozijnen en twee deuren kom je op €900 tot €1.900, plus €300 tot €900 als er een steiger nodig is voor de bovenverdieping."),
            ("Rekent een schilder per kozijn of per uur?",
             "Meestal per kozijn of als vaste prijs voor de hele woning. Alleen houtrotherstel wordt soms op uurbasis gerekend. Vraag dan om een maximumbedrag."),
            ("Wanneer kun je kozijnen het beste laten schilderen?",
             "Van april tot en met oktober, bij droog weer boven de tien graden. Het nazomerseizoen is vaak het voordeligst."),
        ],
    },
]

LATEX_BRONNEN = ('<p><small>Bronnen voor de spuitprijzen per m²: <a href="https://www.homedeal.nl/schilderwerk/latex-spuiten/" rel="nofollow noopener">Homedeal</a> (gemiddeld €6 tot €12), '
                 '<a href="https://trustoo.nl/kennisbank/schilder/latex-spuiten/" rel="nofollow noopener">Trustoo</a> (gemiddeld €5 tot €15) en '
                 '<a href="https://slimster.nl/schilder/schilderwerk-prijzen/kosten-latex-spuiten/" rel="nofollow noopener">Slimster</a> (€5 tot €20), geraadpleegd in november 2026. '
                 'Dit zijn indicaties van die sites, geen prijzen van Topschilder.</small></p>')

KOSTEN += [
    {
        "slug": "schilder-uurtarief",
        "klus": "een schilder per uur",
        "kruimel": "Uurtarief schilder",
        "h1": "Uurtarief schilder 2026: wat kost een schilder per uur?",
        "title": "Uurtarief schilder 2026: wat kost een schilder per uur?",
        "description": "Een schilder rekent in 2026 gemiddeld €45 tot €65 per uur exclusief btw. Per dag is dat €360 tot €520. Plus wanneer een vaste prijs slimmer is.",
        "dienst": "binnenschilderwerk",
        "regio_link": "plaats",
        "excl_btw": True,
        "eenheid": "per uur",
        "van": 45,
        "tot": 65,
        "kort": "€45 – €65 per uur excl. btw",
        "intro": "Een schilder rekent in 2026 meestal tussen de €45 en €65 per uur, exclusief btw en materiaal. Toch krijg je zelden een offerte op uurbasis: de meeste schilders werken met een vaste prijs per klus. Hier lees je wat een uurtarief inhoudt, wat het per dag kost en wanneer werken op uurbasis wel handig is.",
        "voorbeelden": [
            ("Zelfstandige schilder (zzp)", None, "€45 – €55 per uur. Minder overhead, vaak meer flexibel in planning."),
            ("Schildersbedrijf met personeel", None, "€52 – €65 per uur. Meer mensen, materieel en vaak een langere garantie."),
            ("Dagtarief (8 uur)", None, "€360 – €520 per schilder per dag, exclusief btw en materiaal."),
            ("Inclusief 9% btw", None, "€49 – €71 per uur voor schilderwerk aan een woning ouder dan twee jaar."),
        ],
        "extra": [
            ("Materiaal (verf, kit, plamuur)", "apart gerekend, of verwerkt in een vaste prijs"),
            ("Voorrijkosten bij een kleine klus", "€35 – €75 per keer"),
            ("Steiger of hoogwerker", "€300 – €900 per gevel"),
        ],
        "prijsfactoren": [
            "Zzp of bedrijf. Een zelfstandige heeft minder kosten dan een bedrijf met personeel, bedrijfsbussen en een werkplaats.",
            "De regio. In Noord-Holland en Utrecht ligt het uurtarief hoger dan in Flevoland en Overijssel.",
            "Het seizoen. In het voorjaar en de zomer zitten agenda's vol. In de herfst en winter is er meer ruimte voor een scherpe prijs.",
            "Specialisme. Spuitwerk, monumenten en houtrotherstel vragen ervaring en apparatuur, en dat zie je terug in het tarief.",
            "De grootte van de klus. Bij kleine klussen tellen opstarttijd en reistijd zwaarder mee.",
        ],
        "uitleg": [
            ("Uurtarief of vaste prijs?", "Bij een vaste prijs weet je vooraf waar je aan toe bent, en ligt het risico van uitloop bij de schilder. Werken op uurbasis (regie) is vooral handig als de omvang vooraf niet duidelijk is, zoals bij houtrotherstel. Spreek dan altijd een maximumbedrag af en vraag om een urenoverzicht."),
            ("Wat zit er in een uurtarief?", "Het loon van de schilder, zijn verzekeringen, gereedschap, bus, opleiding en de tijd die niet declarabel is, zoals offertes maken en reizen. Daarom ligt het uurtarief een stuk hoger dan wat een schilder per uur verdient."),
        ],
        "tips": [
            "Vraag om een vaste prijs als de klus goed te omschrijven is. Dan ligt het risico van uitloop niet bij jou.",
            "Werk je op uurbasis, spreek dan een maximum af en laat de uren per dag noteren.",
            "Plan in het najaar of de winter. Dan hebben schilders vaker ruimte en zitten ze scherper.",
            "Doe het voorwerk zelf: kamers leeg, vloeren afdekken. Dat scheelt uren.",
        ],
        "btw": "Voor arbeid aan een woning die ouder is dan twee jaar betaal je 9% btw. Voor bedrijfspanden en nieuwbouw jonger dan twee jaar is het 21%. Een zakelijke klant rekent het uurtarief exclusief btw, omdat hij de btw kan terugvragen.",
        "faq": [
            ("Wat kost een schilder per uur in 2026?",
             "Gemiddeld €45 tot €65 per uur exclusief btw. Met 9% btw is dat €49 tot €71 per uur. Materiaal komt er meestal apart bij."),
            ("Wat kost een schilder per dag?",
             "Reken op €360 tot €520 per schilder per dag van acht uur, exclusief btw en materiaal."),
            ("Is een zzp-schilder goedkoper dan een schildersbedrijf?",
             "Meestal wel, omdat een zelfstandige minder vaste kosten heeft. Een bedrijf kan grotere klussen sneller afronden en biedt vaak een uitgebreidere garantie."),
            ("Waarom krijg ik een vaste prijs en geen uurtarief?",
             "De meeste schilders rekenen per m², per kozijn of per klus. Ze schatten zelf hoeveel uur het werk kost. Voor jou is dat prettig: je weet vooraf wat je betaalt."),
            ("Zit materiaal in het uurtarief?",
             "Nee, bijna nooit. Verf, kit en plamuur worden apart gerekend of zitten in een vaste prijs voor de hele klus."),
        ],
    },
    {
        "slug": "huis-schilderen",
        "klus": "een huis schilderen",
        "h1": "Wat kost een huis schilderen in 2026?",
        "title": "Huis schilderen kosten 2026: buiten en binnen",
        "description": "De buitenkant van een huis laten schilderen kost €1.500 tot €7.000, afhankelijk van het type woning. Met prijzen per woningtype, binnen en buiten.",
        "dienst": "buitenschilderwerk",
        "eenheid": "voor de buitenkant van een woning",
        "van": 1500,
        "tot": 7000,
        "kort": "€1.500 – €7.000 voor de buitenkant",
        "intro": "Wat het schilderen van je huis kost, hangt vooral af van het type woning en hoeveel houtwerk er is. Bij buitenschilderwerk betaal je voor kozijnen, deuren en boeidelen, en vaak een steiger. Hieronder zie je wat je per woningtype kwijt bent, voor buiten en voor binnen.",
        "voorbeelden": [
            ("Tussenwoning, buitenkant", None, "€1.500 – €3.500. Ongeveer acht kozijnen, twee deuren, boeidelen en een steiger achter."),
            ("Hoekwoning of twee-onder-een-kap, buitenkant", None, "€2.000 – €4.800. Een extra zijgevel met meer kozijnen en langere boeidelen."),
            ("Vrijstaande woning, buitenkant", None, "€3.000 – €7.000. Houtwerk rondom, vaak met dakkapel en meer steigerwerk."),
            ("Hele woning binnen, muren en plafonds", None, "€2.500 – €5.500 voor zo'n 250 m² muren en plafonds."),
        ],
        "extra": [
            ("Houtrot repareren", "€50 – €275 per reparatieplek"),
            ("Dakkapel schilderen", "€400 – €950 per dakkapel"),
            ("Binnendeuren laten spuiten", "€95 – €185 per deur"),
        ],
        "prijsfactoren": [
            "Het type woning en de hoeveelheid houtwerk. Een vrijstaande woning heeft vaak twee keer zoveel kozijnen als een tussenwoning.",
            "De staat van het schilderwerk. Afbladderende verf en houtrot betekenen meer voorwerk.",
            "Steigerwerk. Voor de bovenverdieping is bijna altijd een steiger of hoogwerker nodig.",
            "Hoe lang geleden de laatste beurt was. Wie elke zes tot acht jaar laat schilderen, betaalt per keer minder.",
            "De regio. In de Randstad liggen de prijzen hoger dan in Flevoland en Overijssel.",
        ],
        "uitleg": [
            ("Wat valt er onder buitenschilderwerk?", "Kozijnen en ramen, voor- en achterdeur, boeidelen en windveren, en soms de dakkapel, de garagedeur of een houten schuur. Muren van baksteen worden meestal niet geschilderd. Vraag de schilder om alle onderdelen apart op de offerte te zetten."),
            ("Hoe vaak moet een huis geschilderd worden?", "Buiten gemiddeld elke zes tot acht jaar, en kozijnen op het zuiden en westen vaak eerder. Binnen hangt het af van slijtage en smaak; muren gaan meestal acht tot tien jaar mee."),
        ],
        "tips": [
            "Laat binnen en buiten in één ronde doen. Je deelt opstart- en voorrijkosten.",
            "Plan buitenwerk in september of oktober. Dan is de piek voorbij en zijn schilders scherper.",
            "Vraag drie offertes en leg ze per onderdeel naast elkaar, niet alleen op het totaal.",
            "Wacht niet tot het hout rot. Een beurt op tijd is veel goedkoper dan houtrotherstel.",
        ],
        "btw": "Voor schilderwerk aan een woning die ouder is dan twee jaar betaal je 9% btw, ook over de verf. Houten inzetstukken en nieuwe onderdorpels vallen onder 21%.",
        "faq": [
            ("Wat kost het om een huis buiten te laten schilderen?",
             "Een tussenwoning kost €1.500 tot €3.500, een hoekwoning of twee-onder-een-kap €2.000 tot €4.800 en een vrijstaande woning €3.000 tot €7.000. Houtrotherstel komt er meestal apart bij."),
            ("Wat kost een huis binnen schilderen?",
             "Voor de muren en plafonds van een gemiddelde woning, zo'n 250 m², reken je op €2.500 tot €5.500. Deuren en kozijnen binnen komen er apart bij."),
            ("Zijn de kosten voor het schilderen van mijn huis aftrekbaar?",
             "Voor je eigen woning niet: onderhoud aan je eigen huis kun je niet aftrekken van de inkomstenbelasting. Verhuur je de woning of gebruik je hem voor je bedrijf, vraag dan je boekhouder wat er kan. Je betaalt wel het lage btw-tarief van 9% als je woning ouder is dan twee jaar."),
            ("Hoe lang duurt het schilderen van een huis?",
             "De buitenkant van een tussenwoning kost een schilder meestal drie tot vijf werkdagen, een vrijstaande woning een tot twee weken. Regen kan de planning opschuiven."),
            ("Wanneer laat je een huis het beste buiten schilderen?",
             "Van april tot en met oktober, bij droog weer en minimaal tien graden. In het najaar zijn schilders vaak het scherpst geprijsd."),
        ],
    },
    {
        "slug": "schilderen-per-m2",
        "klus": "schilderen per m²",
        "h1": "Wat kost schilderen per m² in 2026?",
        "title": "Schilderen per m² kosten 2026: muren en plafonds",
        "description": "Een schilder rekent €10 tot €22 per m² voor muren en plafonds, inclusief verf en btw. Met prijzen voor muren, plafonds en spuiten per kamer.",
        "dienst": "binnenschilderwerk",
        "eenheid": "per m² muur of plafond",
        "van": 10,
        "tot": 22,
        "kort": "€10 – €22 per m²",
        "intro": "Voor muren en plafonds rekenen schilders bijna altijd per vierkante meter. Dat maakt offertes goed te vergelijken. Hieronder zie je wat een m² kost voor muren, plafonds en spuitwerk, en hoe je zelf uitrekent hoeveel m² je hebt.",
        "voorbeelden": [
            ("Slaapkamer, muren en plafond", 45, "Kamer van 3 bij 4 meter: zo'n 33 m² muur en 12 m² plafond."),
            ("Woonkamer, muren en plafond", 90, "Kamer van 5 bij 7 meter: zo'n 55 m² muur en 35 m² plafond."),
            ("Hele benedenverdieping", 140, "Woonkamer, keuken en hal samen."),
        ],
        "extra": [
            ("Muren sauzen met latex", "€10 – €16 per m²"),
            ("Plafond schilderen", "€12 – €22 per m², door het werken boven je hoofd"),
            ("Latex spuiten (grote, lege ruimtes)", "gemiddeld €6 – €15 per m² volgens andere prijssites"),
            ("Gaten en scheuren vullen, plamuren", "€3 – €8 per m² extra"),
        ],
        "prijsfactoren": [
            "Muur of plafond. Plafonds zijn zwaarder werk en kosten per m² meer.",
            "De ondergrond. Kaal stucwerk heeft een voorstrijklaag nodig, en reparaties kosten extra tijd.",
            "Kleurwissel. Van donker naar licht vraagt vaak een extra laag.",
            "De hoeveelheid oppervlak. Bij grote oppervlakken daalt de prijs per m².",
            "Hoogte. Boven de 2,60 meter is een rolsteiger nodig.",
        ],
        "uitleg": [
            ("Zo reken je het aantal m² uit", "Muren: tel de lengte van alle wanden op en vermenigvuldig met de hoogte. Trek ramen en deuren grofweg af als ze groot zijn. Plafond: lengte maal breedte van de kamer. Een kamer van 4 bij 5 meter en 2,60 meter hoog heeft zo'n 47 m² muur en 20 m² plafond."),
            ("Schilderen of spuiten?", "Rollen is de standaard. Spuiten is per m² vaak goedkoper bij grote, lege ruimtes, zoals nieuwbouw, maar al het afdekken kost tijd. In een bewoonde kamer met veel meubels en kozijnen is rollen meestal voordeliger."),
        ],
        "tips": [
            "Maak de kamer zelf leeg. Afdekken en meubels schuiven kost de schilder uren.",
            "Laat meerdere kamers tegelijk doen. Dan zakt de prijs per m².",
            "Kies een lichte kleur in dezelfde tint als nu. Dan is twee lagen genoeg.",
            "Vraag of de prijs per m² geldt inclusief het vullen van gaten en scheuren.",
        ],
        "btw": "Voor schilderwerk aan een woning die ouder is dan twee jaar betaal je 9% btw, ook over de verf.",
        "bronnen": LATEX_BRONNEN,
        "faq": [
            ("Wat kost schilderen per m²?",
             "Een schilder rekent gemiddeld €10 tot €22 per m² voor muren en plafonds, inclusief verf en btw. Muren zitten aan de onderkant, plafonds aan de bovenkant."),
            ("Wat kost een kamer laten schilderen?",
             "Een slaapkamer met muren en plafond, zo'n 45 m², kost €450 tot €990. Een woonkamer van zo'n 90 m² kost €900 tot €1.980."),
            ("Is spuiten goedkoper dan rollen?",
             "Per m² vaak wel bij grote, lege ruimtes. In een bewoonde kamer kost het afdekken zoveel tijd dat rollen meestal voordeliger is."),
            ("Hoe bereken ik hoeveel m² muur ik heb?",
             "Tel de lengte van alle wanden op en vermenigvuldig met de hoogte van de kamer. Grote ramen en deuren trek je eraf."),
        ],
    },
    {
        "slug": "plafond-schilderen",
        "klus": "een plafond schilderen",
        "h1": "Wat kost een plafond schilderen, witten of spuiten?",
        "title": "Plafond schilderen kosten 2026: witten en spuiten",
        "description": "Een plafond laten schilderen of witten kost €12 tot €22 per m². Voor een woonkamer van 35 m² is dat €420 tot €770. Ook voor witten en spuiten.",
        "dienst": "binnenschilderwerk",
        "eenheid": "per m² plafond",
        "van": 12,
        "tot": 22,
        "kort": "€12 – €22 per m²",
        "intro": "Een plafond schilderen is zwaarder werk dan een muur: alles boven je hoofd, met meer kans op strepen en spetters. Daarom rekenen schilders per m² wat meer. Witten, sauzen en schilderen zijn in de praktijk hetzelfde: een plafond met latex of plafondverf voorzien. Spuiten is een andere techniek.",
        "voorbeelden": [
            ("Slaapkamer van 3 bij 4 meter", 12, "Klein plafond, maar wel volledige opstart en afdekken."),
            ("Woonkamer van 5 bij 7 meter", 35, "De meest gevraagde klus."),
            ("Hele benedenverdieping", 60, "Woonkamer, keuken en hal in één keer."),
        ],
        "extra": [
            ("Scheuren en naden repareren", "€3 – €8 per m² extra"),
            ("Plafond spuiten (grote, lege ruimte)", "gemiddeld €6 – €15 per m² volgens andere prijssites"),
            ("Vlekken isoleren (roet, water)", "€2 – €5 per m² voor een isolerende grondlaag"),
        ],
        "prijsfactoren": [
            "De staat van het plafond. Scheuren, naden en vochtvlekken moeten eerst worden gerepareerd of geïsoleerd.",
            "Het type plafond. Spachtelputz of spuitpleister neemt meer verf op dan een glad plafond.",
            "Hoogte. Boven de 2,60 meter is een rolsteiger nodig.",
            "Of de kamer leeg is. Meubels afdekken en verplaatsen kost tijd.",
            "Rollen of spuiten. Spuiten is per m² goedkoper in een lege ruimte, maar afplakken kost tijd.",
        ],
        "uitleg": [
            ("Witten, sauzen of spuiten?", "Witten en sauzen zijn oude woorden voor het schilderen van een plafond met muurverf. Een schilder rolt meestal twee lagen. Spuiten gaat sneller op grote oppervlakken en geeft een egale laag zonder rolbanen, maar alles moet worden afgedekt. Bij nieuwbouw is spuiten vaak voordelig, in een bewoonde woning rollen."),
            ("Waarom kost een plafond meer per m² dan een muur?", "Werken boven je hoofd is zwaarder en langzamer, er komt een trapje of steiger bij, en een plafond laat in strijklicht elke rolbaan zien. Daar is meer zorg voor nodig."),
        ],
        "tips": [
            "Laat het plafond meenemen als de muren toch worden geschilderd. Dan deel je opstart en afdekken.",
            "Kies een matte plafondverf. Die verbergt oneffenheden beter dan zijdeglans.",
            "Heb je vochtvlekken, los dan eerst de oorzaak op. Anders komen ze terug.",
            "Maak de kamer zo leeg mogelijk. Dat scheelt de schilder uren.",
        ],
        "btw": "Voor schilderwerk aan een woning die ouder is dan twee jaar betaal je 9% btw, ook over de verf.",
        "bronnen": LATEX_BRONNEN,
        "faq": [
            ("Wat kost een plafond laten schilderen?",
             "Gemiddeld €12 tot €22 per m². Een woonkamerplafond van 35 m² kost €420 tot €770, inclusief verf en btw."),
            ("Wat kost een plafond witten?",
             "Hetzelfde als schilderen: witten is een ander woord voor een plafond voorzien van muurverf. Reken op €12 tot €22 per m²."),
            ("Is plafond spuiten goedkoper?",
             "In een grote, lege ruimte vaak wel. Andere prijssites noemen gemiddeld €6 tot €15 per m². In een bewoonde kamer kost het afdekken zoveel tijd dat rollen meestal voordeliger is."),
            ("Hoeveel lagen heeft een plafond nodig?",
             "Meestal twee. Een kaal of gerepareerd plafond krijgt eerst een voorstrijklaag."),
        ],
    },
    {
        "slug": "latex-spuiten",
        "klus": "latex spuiten",
        "h1": "Wat kost latex spuiten in 2026?",
        "title": "Latex spuiten kosten 2026: muren en plafonds per m²",
        "description": "Latex spuiten kost gemiddeld €6 tot €15 per m² volgens Nederlandse prijssites. Wanneer spuiten goedkoper is dan rollen, en wat er bij afdekken en voorwerk komt.",
        "dienst": "spuitwerk",
        "eenheid": "per m² muur of plafond",
        "van": 6,
        "tot": 15,
        "kort": "€6 – €15 per m²",
        "intro": "Bij latex spuiten brengt de schilder muurverf aan met een verfspuit, meestal airless. Op grote oppervlakken gaat dat veel sneller dan rollen en je krijgt een egale laag zonder rolbanen. De richtprijs hieronder komt van andere Nederlandse prijssites; bij Topschilder rekenen we zelf voor rollen met €10 tot €22 per m².",
        "voorbeelden": [
            ("Plafond van een woonkamer", 35, "Lege ruimte, glad plafond."),
            ("Muren en plafonds van een nieuwbouwwoning", 250, "Hele woning in één keer, nog niet bewoond."),
            ("Bedrijfsruimte of kantoor", 400, "Grote, lege oppervlakken: hier is spuiten op zijn voordeligst."),
        ],
        "extra": [
            ("Afdekken en afplakken in een bewoonde ruimte", "vaak een groot deel van de arbeid; vraag het apart"),
            ("Gaten en scheuren vullen", "€3 – €8 per m²"),
            ("Voorstrijklaag op kaal stucwerk", "€2 – €4 per m²"),
        ],
        "prijsfactoren": [
            "Hoeveel oppervlak er is. Hoe groter, hoe lager de prijs per m².",
            "Of de ruimte leeg is. In een bewoonde woning kost afdekken veel tijd.",
            "De ondergrond. Spuiten maskeert niets: gaten en scheuren moeten eerst worden gerepareerd.",
            "Kaal stucwerk of al geschilderd. Kaal stucwerk heeft een voorstrijklaag nodig.",
            "De hoogte. Hoge plafonds vragen een steiger of hoogwerker.",
        ],
        "uitleg": [
            ("Wanneer is spuiten slimmer dan rollen?", "Bij grote, lege oppervlakken: nieuwbouw, een verbouwing, een kantoor of een hoog plafond. Daar weegt de tijdwinst op tegen het afdekken. In een bewoonde kamer met veel kozijnen en meubels is rollen meestal goedkoper."),
            ("Wat je moet weten over verfnevel", "Verfnevel verspreidt zich door de ruimte. Alles wat niet geverfd wordt, gaat onder folie en tape: vloeren, kozijnen, stopcontacten en ramen. Een goede schilder neemt daar de tijd voor. Vraag of het afdekken in de prijs zit."),
        ],
        "tips": [
            "Laat spuiten als de ruimte nog leeg is, bijvoorbeeld vóór je verhuist.",
            "Laat gaten en scheuren eerst repareren. Spuitwerk laat elke oneffenheid zien.",
            "Vraag of de prijs per m² inclusief afdekken is.",
            "Combineer muren en plafonds. Het afdekken doe je dan maar één keer.",
        ],
        "btw": "De Belastingdienst noemt schilderwerk aan woningen ouder dan twee jaar onder het 9%-tarief, maar noemt spuiten niet apart. Kijk op de offerte welk tarief er staat.",
        "bronnen": LATEX_BRONNEN,
        "faq": [
            ("Wat kost latex spuiten per m²?",
             "Andere Nederlandse prijssites noemen gemiddeld €6 tot €15 per m². Het hangt sterk af van hoeveel oppervlak er is en of de ruimte leeg is."),
            ("Is latex spuiten goedkoper dan rollen?",
             "Op grote, lege oppervlakken wel. In een bewoonde kamer kost het afdekken zoveel tijd dat rollen vaak voordeliger is."),
            ("Kan ik in een bewoond huis laten spuiten?",
             "Ja, maar alles moet worden afgedekt. Reken op meer tijd en dus een hogere prijs per m² dan in een lege woning."),
            ("Hoe lang duurt latex spuiten?",
             "Een schilder spuit een paar honderd m² op een dag. Afdekken en voorwerk kosten vaak meer tijd dan het spuiten zelf."),
        ],
    },
    {
        "slug": "deuren-spuiten",
        "klus": "deuren spuiten",
        "h1": "Wat kost deuren laten spuiten of schilderen?",
        "title": "Deuren spuiten kosten 2026: prijs per deur",
        "description": "Een binnendeur laten spuiten kost €95 tot €185, schilderen €65 tot €140. Met prijzen voor binnendeuren, kozijnen en de voordeur.",
        "dienst": "spuitwerk",
        "eenheid": "per deur, gespoten",
        "van": 95,
        "tot": 185,
        "kort": "€95 – €185 per deur",
        "intro": "Binnendeuren laten spuiten geeft een strakke, gladde laag zonder kwaststreken. Je betaalt per deur, en de prijs hangt vooral af van het type deur en of de kozijnen meegaan. Met de kwast schilderen is goedkoper, maar je ziet het verschil.",
        "voorbeelden": [
            ("Binnendeuren van een tussenwoning", 7, "Zo'n zeven deuren, beide kanten, gespoten in de werkplaats."),
            ("Binnendeuren van een vrijstaande woning", 11, "Meer deuren, inclusief trapkast en bijkeuken."),
            ("Eén voordeur, gespoten", 1, "Buitendeur met een slijtvaste laklaag."),
        ],
        "extra": [
            ("Deur met de kwast schilderen", "€65 – €140 per deur"),
            ("Deurkozijn binnen", "€35 – €75 per kozijn"),
            ("Nieuw hang- en sluitwerk monteren", "€15 – €35 per deur, exclusief materiaal"),
        ],
        "prijsfactoren": [
            "Vlakke deur of paneeldeur. Paneeldeuren met profielen kosten meer schuurwerk.",
            "In de werkplaats of op locatie. In de werkplaats wordt het strakker, maar er komt transport bij.",
            "Of de kozijnen mee moeten. Kozijnen worden op locatie geschilderd of gespoten en moeten worden afgeplakt.",
            "De staat van de oude laag. Afbladderende lak moet eerst weg.",
            "Glasdeuren. Glas afplakken of eruit halen kost extra tijd.",
        ],
        "uitleg": [
            ("Spuiten of met de kwast?", "Met de kwast of roller blijven er altijd fijne strepen zichtbaar. Spuiten geeft een gladde, fabrieksachtige laag. Het verschil zit vooral in de afwerking; beide gaan bij goed voorwerk jaren mee."),
            ("Hoe gaat het in zijn werk?", "De schilder haalt de deuren uit de scharnieren en neemt ze mee naar de werkplaats, of spuit ze op locatie in een afgeschermde ruimte. Daar worden ze geschuurd, gegrond en twee keer gelakt. Na een paar dagen hangen ze terug."),
        ],
        "tips": [
            "Laat alle deuren in één keer doen. Per deur wordt het dan goedkoper.",
            "Vervang het hang- en sluitwerk in dezelfde ronde.",
            "Kies een slijtvaste lak voor deuren die veel worden gebruikt.",
            "Zitten er nog oude deuren in met veel profiel, vraag dan of nieuwe vlakke deuren voordeliger zijn.",
        ],
        "btw": "Voor schilderwerk aan een woning die ouder is dan twee jaar betaal je 9% btw. De Belastingdienst noemt spuiten niet apart; kijk op de offerte welk tarief er staat.",
        "faq": [
            ("Wat kost een deur laten spuiten?",
             "Een binnendeur laten spuiten kost €95 tot €185, afhankelijk van het type deur en of de kozijnen meegaan."),
            ("Wat kost het om binnendeuren te laten spuiten?",
             "Voor een tussenwoning met zo'n zeven deuren reken je op €665 tot €1.295. Kozijnen komen er apart bij."),
            ("Wat kost een deur schilderen met de kwast?",
             "€65 tot €140 per deur. Goedkoper dan spuiten, maar je ziet de structuur van de kwast of roller."),
            ("Hoe lang ben ik mijn deuren kwijt?",
             "Bij spuiten in de werkplaats meestal twee tot vijf werkdagen. Sommige schilders zetten tijdelijk een andere deur terug."),
        ],
    },
    {
        "slug": "dakkapel-schilderen",
        "klus": "een dakkapel schilderen",
        "h1": "Wat kost een dakkapel schilderen in 2026?",
        "title": "Dakkapel schilderen kosten 2026: prijs per dakkapel",
        "description": "Een dakkapel laten schilderen kost €400 tot €950, afhankelijk van de breedte, de staat van het hout en de bereikbaarheid. Met rekenvoorbeelden en tips.",
        "dienst": "buitenschilderwerk",
        "eenheid": "per dakkapel",
        "van": 400,
        "tot": 950,
        "kort": "€400 – €950 per dakkapel",
        "intro": "Een dakkapel vangt veel wind, regen en zon, en is lastig bereikbaar. Daardoor kost hij meer dan je op basis van het oppervlak zou verwachten. Je betaalt voor het houtwerk, de kozijnen en vaak een steiger of hoogwerker.",
        "voorbeelden": [
            ("Kleine dakkapel, tot 2,5 meter breed", None, "€400 – €600. Eén kozijn, korte boeidelen."),
            ("Gemiddelde dakkapel, 3 tot 4 meter breed", None, "€550 – €800. Twee of drie ramen en zijwangen."),
            ("Brede dakkapel of slecht bereikbaar", None, "€750 – €950. Meerdere ramen, of een steiger aan de straatkant."),
        ],
        "extra": [
            ("Steiger of hoogwerker", "vaak inbegrepen bij een dakkapel; vraag het na"),
            ("Houtrot repareren", "€50 – €275 per reparatieplek"),
            ("Zijwangen met plaatmateriaal bekleden", "vraag een aparte prijs"),
        ],
        "prijsfactoren": [
            "De breedte van de dakkapel en het aantal ramen.",
            "De bereikbaarheid. Aan de achterkant kan vaak met een ladder of dakstoel; aan de straatkant is een steiger of hoogwerker nodig.",
            "De staat van het hout. Boeidelen en onderdorpels van dakkapellen hebben vaak houtrot.",
            "Houten of kunststof zijwangen. Houten zijwangen moeten mee in de verf.",
            "Of de rest van de woning tegelijk wordt gedaan. Dan deel je de steigerkosten.",
        ],
        "uitleg": [
            ("Wat valt er onder een dakkapel schilderen?", "Het kozijn en de draaiende delen, de boeidelen bovenaan, de zijwangen als die van hout zijn, en de onderdorpel. Een goede schilder controleert ook de kitnaden en de aansluiting op het dak."),
            ("Hoe vaak moet een dakkapel geschilderd worden?", "Ongeveer elke vijf tot zeven jaar, vaak eerder dan de rest van de woning. De dakkapel zit hoog en vangt meer weer."),
        ],
        "tips": [
            "Laat de dakkapel meenemen met de rest van het buitenschilderwerk. De steiger staat er dan toch.",
            "Vraag of de steiger of hoogwerker in de prijs zit.",
            "Laat houtrot in de onderdorpel meteen herstellen. Juist daar komt water binnen.",
            "Overweeg bij veel houtrot kunststof boeidelen of zijwangen. Dat scheelt onderhoud.",
        ],
        "btw": "Voor schilderwerk aan een woning die ouder is dan twee jaar betaal je 9% btw. Houten inzetstukken en nieuwe onderdorpels vallen onder 21%.",
        "faq": [
            ("Wat kost een dakkapel laten schilderen?",
             "Reken op €400 tot €950 per dakkapel, afhankelijk van de breedte, de bereikbaarheid en de staat van het hout."),
            ("Zit de steiger in de prijs?",
             "Bij een dakkapel vaak wel, omdat hij zonder steiger of hoogwerker niet goed bereikbaar is. Vraag het altijd na."),
            ("Hoe vaak moet een dakkapel geschilderd worden?",
             "Elke vijf tot zeven jaar. De dakkapel zit hoog en vangt meer wind en regen dan de rest van de woning."),
            ("Kan ik een dakkapel zelf schilderen?",
             "Het kan, maar werken op hoogte is gevaarlijk zonder goede steiger of valbeveiliging. Laat het bij twijfel over aan een schilder."),
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
    "binnenkozijn": {"naam": "Binnenkozijnen", "van": 35, "tot": 75, "eenheid": "per kozijn"},
    "deur": {"naam": "Deuren", "van": 65, "tot": 185, "eenheid": "per deur"},
    "buitendeur": {"naam": "Buitendeur", "van": 100, "tot": 185, "eenheid": "per deur"},  # bron: Trustoo, nov. 2026 (huiscalculator)
    "keukenfront": {"naam": "Keukenfronten", "van": 45, "tot": 95, "eenheid": "per front"},
    "trap": {"naam": "Trap", "van": 350, "tot": 950, "eenheid": "per trap"},
    "houtrot_plek": {"naam": "Houtrotreparatie", "van": 50, "tot": 275, "eenheid": "per plek"},
    "behang_m2": {"naam": "Behangen", "van": 9, "tot": 24, "eenheid": "per m²"},
    "uurloon": {"naam": "Uurloon", "van": 45, "tot": 68, "eenheid": "per uur", "excl_btw": True},
    "steiger": {"naam": "Steiger of hoogwerker", "van": 300, "tot": 900, "eenheid": "per gevel"},
}


# ---------------------------------------------------------------------------
# Verdieping voor de kostenpagina's met de meeste vertoningen in Search Console
# (november 2026). Zo beantwoordt één pagina de hele zoekvraag rond de klus,
# en hoeven plaats- en dienstpagina's daar niet mee te concurreren.
# ---------------------------------------------------------------------------

UITBREIDING = {
    "keuken-spuiten": {
        "h1": "Keuken laten spuiten: wat kost het en hoe gaat het?",
        "title": "Keuken laten spuiten: kosten per front en werkwijze",
        "description": "Een keuken laten spuiten kost €45 tot €95 per front, voor een gemiddelde keuken €720 tot €1.520. Ook hoogglans, kunststof en spuiten tegenover nieuwe fronten.",
        "verdieping": [
            ("Zo verloopt het spuiten van je keuken",
             "<ol><li><strong>Opname.</strong> De schilder telt de fronten, kijkt naar het materiaal en test of de oude laag goed vastzit.</li>"
             "<li><strong>Demonteren.</strong> Fronten en laden gaan eraf, grepen en scharnieren worden genummerd bewaard.</li>"
             "<li><strong>Voorwerk.</strong> Ontvetten, schuren en waar nodig beschadigingen vullen. Op kunststof en folie komt een hechtprimer.</li>"
             "<li><strong>Spuiten.</strong> Meestal in de werkplaats: een grondlaag en twee lagen lak, met tussendoor licht schuren.</li>"
             "<li><strong>Terugplaatsen.</strong> Na het uitharden gaan de fronten terug en worden de scharnieren afgesteld.</li></ol>"
             "<p>Tussen opname en oplevering zitten meestal drie tot vijf werkdagen. Zonder deurtjes koken kan gewoon, alleen staat alles even open.</p>"),
            ("Hoogglans keuken spuiten",
             "<p>Een hoogglans keuken kan opnieuw in hoogglans worden gespoten, of juist in zijdeglans of mat. Hoogglans is het lastigst: elk stofje en elke oneffenheid blijft zichtbaar. Daarom vraagt het meer schuurwerk, vaak een extra laag en een stofvrije spuitruimte. Reken op een prijs aan de bovenkant van de richtprijs per front.</p>"
             "<p>Veel hoogglans keukens hebben folie of een kunststof toplaag. Zit die nog goed vast, dan kan er met een hechtprimer overheen worden gespoten. Laat de folie bij de randen los, dan moet die er eerst helemaal af, en dat kost extra tijd.</p>"),
            ("Spuiten, wrappen of nieuwe fronten?",
             "<div class=\"tablewrap\"><table><thead><tr><th>Keuze</th><th>Wanneer het past</th><th>Let op</th></tr></thead><tbody>"
             "<tr><td><strong>Spuiten</strong></td><td>De kasten zijn goed, je wilt een andere kleur of glans.</td><td>Elke kleur kan en beschadigingen zijn later bij te werken.</td></tr>"
             "<tr><td><strong>Wrappen (folie)</strong></td><td>Je wilt snel iets anders, bijvoorbeeld een houtlook.</td><td>Bij hitte en op randen kan folie loslaten.</td></tr>"
             "<tr><td><strong>Nieuwe fronten</strong></td><td>De fronten zijn beschadigd of je wilt een ander model.</td><td>Meestal het duurst, en de maten moeten precies passen.</td></tr>"
             "</tbody></table></div>"),
            ("Keukenkastjes zelf verven of laten spuiten?",
             "<p>Zelf verven kan, als je de tijd neemt voor het voorwerk: grondig ontvetten, schuren en een hechtprimer. Met kwast en roller zie je wel de structuur in de lak, vooral als het licht schuin op de fronten valt. Spuiten geeft een gladde laag die meer op een nieuwe keuken lijkt. Wie zelf verft, betaalt vooral in tijd: een keuken met zestien fronten kost al snel meerdere weekenden.</p>"),
        ],
        "faq_extra": [
            ("Wat kost hoogglans keuken spuiten?",
             "Ook hier reken je per front, maar hoogglans zit aan de bovenkant van de richtprijs van €45 tot €95 per front, omdat het meer schuurwerk en vaak een extra laag vraagt."),
            ("Kan ik keukenkastjes zelf verven?",
             "Ja, met goed voorwerk: ontvetten, schuren en een hechtprimer. Het resultaat is minder glad dan spuiten, omdat je de structuur van kwast of roller ziet."),
            ("Moet het werkblad eruit als de keuken gespoten wordt?",
             "Nee. Meestal worden alleen de fronten en laden gespoten. Moet de ombouw ook, dan plakt de schilder het werkblad en de apparaten af."),
        ],
    },
    "latex-spuiten": {
        "h1": "Latex spuiten: kosten per m², verbruik en werkwijze",
        "title": "Latex spuiten: kosten per m², verbruik en werkwijze",
        "description": "Latex spuiten kost gemiddeld €6 tot €15 per m². Hoeveel latex je nodig hebt per m², welke verf geschikt is en wanneer spuiten goedkoper is dan rollen.",
        "verdieping": [
            ("Hoeveel latex heb je nodig per m²?",
             "<p>Met een roller kom je met een liter muurverf grofweg 8 tot 10 m² ver per laag. Het precieze getal staat op het blik. Bij spuiten gaat er meer verloren aan nevel en overspray, dus reken dan op wat extra verf.</p>"
             "<p><strong>Voorbeeld:</strong> 100 m² muur in twee lagen is 200 m² verfwerk. Met de roller is dat zo'n 20 tot 25 liter, met de spuit iets meer. Op kaal stucwerk komt er een voorstrijklaag bij. Reken het voor jouw kamer uit met de <a href=\"/gids/verf-berekenen/\">verfcalculator</a>.</p>"),
            ("Welke latex is geschikt om te spuiten?",
             "<p>Latex is in Nederland de gangbare naam voor watergedragen muurverf. Niet elke muurverf is gemaakt om met een airless spuit te verwerken: kijk op het blik of de fabrikant spuiten noemt, en hoeveel je mag verdunnen. Een schilder werkt meestal met emmers spuitlatex in mat of zijdemat. Mat verbergt kleine oneffenheden beter, zijdemat is beter afwasbaar.</p>"),
            ("Zo gaat een schilder te werk",
             "<ol><li><strong>Leeghalen en afdekken.</strong> Vloeren, kozijnen, ramen en stopcontacten gaan onder folie en tape.</li>"
             "<li><strong>Repareren.</strong> Gaten en scheuren vullen en schuren, want spuitwerk laat elke oneffenheid zien.</li>"
             "<li><strong>Voorstrijken.</strong> Kaal of zuigend stucwerk krijgt eerst een voorstrijklaag.</li>"
             "<li><strong>Spuiten.</strong> Meestal twee lagen, in banen die elkaar overlappen.</li>"
             "<li><strong>Opruimen.</strong> Tape en folie eraf zolang de verf nog niet volledig hard is, zodat de randen strak blijven.</li></ol>"),
            ("Zelf latex spuiten of uitbesteden?",
             "<p>Een airless spuit kun je huren, maar het afdekken en het gelijkmatig spuiten vragen ervaring. Te veel verf geeft druipers, te weinig een vlekkerig resultaat. Voor één kamer is zelf rollen vaak handiger. Gaat het om een hele woning of hoge plafonds, dan verdient een schilder met eigen materiaal zich snel terug.</p>"),
            ("Latex spuiten bij jou in de buurt",
             "<p>Onze schilders werken in Flevoland, het Gooi, de Veluwe, Overijssel en rond Amersfoort. Zoek je iemand voor latex spuiten, kijk dan bij <a href=\"/schilder/almere/spuitwerk/\">Almere</a>, <a href=\"/schilder/zwolle/spuitwerk/\">Zwolle</a>, <a href=\"/schilder/amersfoort/spuitwerk/\">Amersfoort</a>, <a href=\"/schilder/hilversum/spuitwerk/\">Hilversum</a> of <a href=\"/werkgebied/\">alle plaatsen</a>.</p>"),
        ],
        "faq_extra": [
            ("Hoeveel latex heb je nodig per m²?",
             "Met een roller ongeveer een liter per 8 tot 10 m² per laag; het precieze getal staat op het blik. Bij spuiten verbruik je iets meer door nevel en overspray."),
            ("Mag je latex verdunnen om te spuiten?",
             "Alleen zoveel als de fabrikant op het blik aangeeft. Te veel verdunnen geeft een slechtere dekking en druipers."),
            ("Hoe lang moet latex drogen?",
             "Muurverf is meestal binnen een paar uur droog genoeg voor een tweede laag. Kijk voor de precieze tijden op het blik; bij kou en vocht duurt het langer."),
        ],
    },
    "huis-schilderen": {
        "h1": "Wat kost een huis of woning laten schilderen in 2026?",
        "title": "Huis laten schilderen: kosten buiten en binnen 2026",
        "description": "Een huis buiten laten schilderen kost €1.500 tot €7.000, afhankelijk van het woningtype. Met prijzen voor tussenwoning, hoekwoning en vrijstaand, en binnen.",
        "verdieping": [
            ("En binnen?",
             "<p>Binnen reken je per onderdeel. Muren en plafonds kosten €10 tot €22 per m² (<a href=\"/kosten/schilderen-per-m2/\">schilderen per m²</a>), een plafond apart zie je bij <a href=\"/kosten/plafond-schilderen/\">plafond schilderen</a> en binnendeuren bij <a href=\"/kosten/deuren-spuiten/\">deuren spuiten</a>. Voor een hele woning met zo'n 250 m² muren en plafonds kom je op €2.500 tot €5.500. Buiten liever per kozijn rekenen? Kijk bij <a href=\"/kosten/kozijnen-schilderen/\">kozijnen schilderen</a>.</p>"),
            ("Zo laat je je huis schilderen, stap voor stap",
             "<ol><li><strong>Bekijk de staat.</strong> Loop rond je huis en let op afbladderende verf, open naden en zacht hout bij dorpels en hoeken.</li>"
             "<li><strong>Vraag offertes aan.</strong> Liefst drie, met alle onderdelen apart: kozijnen, deuren, boeidelen, steiger en houtrot.</li>"
             "<li><strong>Vergelijk per onderdeel.</strong> Niet alleen het totaal. <a href=\"/offerte-vergelijken/\">Leg je offerte naast de richtprijzen.</a></li>"
             "<li><strong>Plan op tijd.</strong> Buitenwerk kan van maart tot en met oktober; in het voorjaar zitten schilders snel vol. Lees <a href=\"/gids/wanneer-buiten-schilderen/\">wanneer je buiten kunt schilderen</a>.</li>"
             "<li><strong>Oplevering.</strong> Loop samen rond, controleer de hoeken en randen en vraag wat er onder de garantie valt.</li></ol>"),
            ("Moet de gevel ook geschilderd worden?",
             "<p>Een gevel van schoon metselwerk wordt meestal niet geschilderd. Wel kan het voegwerk of een impregneerlaag aan de beurt zijn, maar dat is ander werk. Is je gevel al eerder geschilderd of gepleisterd, dan moet die laag wel onderhouden worden. Vraag daar een aparte prijs voor, want dat wordt per m² gerekend en niet per kozijn.</p>"),
            ("Zelf schilderen of laten doen?",
             "<p>Binnen een kamer verven doen veel mensen zelf. Buiten ligt dat anders: werken op hoogte, het voorwerk aan oude verflagen en houtrot herkennen vragen ervaring. Een schilder werkt ook sneller, zodat je huis korter in de steigers staat. Twijfel je, laat dan alleen het buitenwerk doen en verf binnen zelf.</p>"),
        ],
        "faq_extra": [
            ("Wat kost een rijtjeshuis buiten schilderen?",
             "Voor een tussenwoning reken je op €1.500 tot €3.500 voor de buitenkant, inclusief materiaal en btw. Houtrotherstel en een dakkapel komen er apart bij."),
            ("Wat kost de buitenkant van een vrijstaand huis schilderen?",
             "Reken op €3.000 tot €7.000. Het verschil zit in de hoeveelheid kozijnen, de hoogte en hoeveel steigerwerk er nodig is."),
        ],
    },
    "deuren-spuiten": {
        "title": "Deuren laten spuiten: kosten per deur 2026",
        "verdieping": [
            ("Opdekdeur of stompe deur: maakt het uit?",
             "<p>Een opdekdeur valt met een rand over het kozijn, een stompe deur ligt vlak in het kozijn. Voor het spuiten maakt het weinig uit: beide gaan uit de scharnieren en worden rondom gelakt. Bij een opdekdeur let de schilder extra op de sponning, omdat de rand daar tegen het kozijn slijt. Wil je van opdek naar stomp, dan moet het kozijn worden aangepast. Dat is timmerwerk en geen spuitwerk.</p>"),
            ("Binnendeuren en kozijnen samen laten doen",
             "<p>Nieuwe witte deuren in vergeelde kozijnen vallen op. Laat de kozijnen daarom in dezelfde ronde meenemen. De deuren gaan meestal naar de werkplaats, de kozijnen worden op locatie gelakt of gespoten. Een deurkozijn binnen kost €35 tot €75. Op de offerte horen deuren en kozijnen als aparte posten te staan.</p>"),
            ("En de voordeur?",
             "<p>Een voordeur krijgt zon, regen en veel handen te verduren. Daarom krijgt hij een buitenlak die tegen weer en slijtage kan. Spuiten op locatie is lastig, dus vaak gaat de deur een dag of twee naar de werkplaats en zet de schilder er tijdelijk een noodvoorziening in. Vraag hoe dat geregeld wordt voordat je tekent.</p>"),
        ],
        "faq_extra": [
            ("Kun je een opdekdeur laten spuiten?",
             "Ja. Een opdekdeur wordt net als een stompe deur uit de scharnieren gehaald en rondom gespoten. De schilder let extra op de rand die tegen het kozijn valt."),
        ],
    },
    "dakkapel-schilderen": {
        "verdieping": [
            ("Dakkapel schilderen met een hoogwerker of steiger?",
             "<p>Aan de achterkant kan een schilder vaak via het dak werken, met een dakladder en valbeveiliging. Aan de straatkant, of bij een hoog dak, is een steiger of hoogwerker nodig. Een hoogwerker staat er alleen op de dagen dat er gewerkt wordt en is snel opgebouwd. Een steiger blijft staan en is handiger als er ook houtrot hersteld of meerdere dagen gewerkt moet worden. Los kost een steiger of hoogwerker meestal €300 tot €900 per gevel, afhankelijk van de hoogte en hoe lang hij nodig is.</p>"
             "<p>Vraag of de steiger of hoogwerker in de prijs zit, en zo niet, wat hij apart kost. Laat de dakkapel bij voorkeur meenemen met de rest van het buitenschilderwerk: de steiger staat er dan toch.</p>"),
            ("Waar zit bij een dakkapel vaak houtrot?",
             "<p>In de onderdorpel van het kozijn, in de hoeken van de boeidelen en waar de zijwangen op het dak aansluiten. Daar blijft water het langst staan. Een schilder prikt bij de opname met een priem in het hout om te voelen of het zacht is. Reken houtrot per plek: €50 tot €275 per reparatieplek.</p>"),
        ],
        "faq_extra": [
            ("Wat kost een dakkapel schilderen met een hoogwerker?",
             "De hoogwerker zit bij een dakkapel vaak in de prijs van €400 tot €950. Komt hij er apart bij, vraag dan om een vaste prijs voor het aantal dagen dat hij nodig is."),
        ],
    },
}

for _k in KOSTEN:
    _u = UITBREIDING.get(_k["slug"])
    if _u:
        for _veld in ("h1", "title", "description"):
            if _veld in _u:
                _k[_veld] = _u[_veld]
        _k["verdieping"] = _u["verdieping"]
        _k["faq"] = list(_k["faq"]) + _u["faq_extra"]


# --- seo-ronde 4: zes nieuwe kostenpagina's (inhoud in kosten_ronde4.py) ---
from kosten_ronde4 import KOSTEN_RONDE4  # noqa: E402

KOSTEN += KOSTEN_RONDE4
KOSTEN_BY_SLUG.update({k["slug"]: k for k in KOSTEN_RONDE4})


# --- content-ronde 5: drie nieuwe kostenpagina's en verdieping (inhoud in kosten_ronde5.py) ---
from kosten_ronde5 import KOSTEN_RONDE5, UITBREIDING_R5  # noqa: E402

KOSTEN += KOSTEN_RONDE5
KOSTEN_BY_SLUG.update({k["slug"]: k for k in KOSTEN_RONDE5})
for _slug, _u in UITBREIDING_R5.items():
    _k = KOSTEN_BY_SLUG[_slug]
    for _veld in ("h1", "title", "description", "direct", "prijstabel", "valkuilen"):
        if _veld in _u:
            _k[_veld] = _u[_veld]
    _k["verdieping"] = list(_k.get("verdieping", [])) + _u.get("verdieping", [])
    _k["faq"] = list(_k["faq"]) + _u.get("faq_extra", [])

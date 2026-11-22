"""Kostenpagina's ronde 4: radiatoren, kunststof kozijnen, gevel, boeidelen,
schutting en gevelreiniging.

Zelfde formaat als KOSTEN in kosten_data.py. Prijzen zijn richtprijzen inclusief
materiaal en btw, tenzij anders vermeld. Steiger, houtrot en uurtarief zijn gelijk
gehouden aan de bestaande pagina's. Bronnen zijn geraadpleegd in november 2026.
"""

_BD_SCHILDEREN = "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/werkzaamheden_aan_woningen/schilderen"
_BD_SCHOONMAKEN = "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/werkzaamheden_aan_woningen/schoonmaken_in_woningen"
_BD_OUDER_2 = "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/werkzaamheden_aan_woningen/woningen_ouder_dan_2_jaar"

KOSTEN_RONDE4 = [
    # ------------------------------------------------------------------
    # 1. Radiatoren
    # ------------------------------------------------------------------
    {
        "slug": "radiatoren-schilderen",
        "klus": "radiatoren schilderen",
        "kruimel": "Radiator schilderen of spuiten",
        "h1": "Wat kost een radiator verven of laten spuiten?",
        "title": "Radiator schilderen kosten 2026: prijs per radiator",
        "description": "Een radiator laten verven of spuiten kost €90 tot €225 per radiator, inclusief radiatorlak en btw. Met prijzen per type, ter plekke of in de werkplaats.",
        "dienst": "spuitwerk",
        "eenheid": "per radiator",
        "van": 90,
        "tot": 225,
        "kort": "€90 – €225 per radiator",
        "intro": "Een vergeelde of beschadigde radiator valt meer op dan je denkt, zeker naast een vers geschilderde muur. Een schilder kan hem ter plekke verven of spuiten, of hem laten demonteren en in de werkplaats spuiten. Je betaalt per radiator. Het type radiator, roest en de keuze tussen ter plekke en werkplaats maken het verschil.",
        "voorbeelden": [
            ("Appartement, 4 radiatoren", 4, "Vooral gladde paneelradiatoren, ter plekke geschilderd."),
            ("Tussenwoning, 7 radiatoren", 7, "Paneelradiatoren plus een handdoekradiator in de badkamer."),
            ("Vrijstaande woning, 12 radiatoren", 12, "Bij zoveel radiatoren in één ronde zit je vaak aan de onderkant van de prijs per stuk."),
        ],
        "extra": [
            ("Roest verwijderen en roestwerende grondlaag", "€15 – €40 extra per radiator (eigen inschatting)"),
            ("Radiator los- en vastzetten (cv aftappen en bijvullen)", "op uurbasis, €45 – €65 per uur excl. btw"),
            ("Muur achter de radiator meeschilderen", "€10 – €22 per m², als onderdeel van de muren"),
            ("Nieuwe radiator als alternatief", "€250 – €600 inclusief montage, volgens Homedeal"),
        ],
        "prijsfactoren": [
            "Het type radiator. Een gladde paneelradiator is snel klaar. Een ledenradiator of designradiator heeft veel hoeken en randen.",
            "Roest en afbladderende verf. Die moeten eerst weg, en op kaal metaal komt een roestwerende grondlaag.",
            "Ter plekke of in de werkplaats. In de werkplaats wordt het strakker, maar dan moet de radiator los en komt er transport bij.",
            "Hoeveel radiatoren er in één keer worden gedaan. De opstart en het afdekken deel je dan.",
            "De bereikbaarheid. Een radiator vlak boven de vloer of in een smalle nis is lastiger rondom te verven.",
        ],
        "uitleg": [
            ("Wat je ervoor krijgt", "De schilder zet de verwarming uit en laat de radiator afkoelen. Daarna ontvetten, licht schuren, roestplekken behandelen en de kranen, leidingen en vloer afplakken. Er komt een grondlaag op kale plekken en twee lagen radiatorlak. Bij ter plekke schilderen is een radiator meestal binnen een dag klaar, plus droogtijd."),
            ("Verven of spuiten?", "Met kwast en roller zie je fijne strepen, vooral aan de voorkant. Spuiten geeft een gladde laag die meer op de fabrieksafwerking lijkt. Ter plekke spuiten kan, maar dan moet de hele omgeving onder folie. Wie het echt strak wil, laat de radiator demonteren en in de werkplaats spuiten."),
        ],
        "verdieping": [
            ("Prijs per type radiator",
             "<div class=\"tablewrap\"><table><thead><tr><th>Type</th><th>Richtprijs</th><th>Waarom</th></tr></thead><tbody>"
             "<tr><td><strong>Gladde paneelradiator</strong></td><td class=\"num\">€90 – €150</td><td>Vlakke voorkant, weinig randen. De meest voorkomende radiator.</td></tr>"
             "<tr><td><strong>Paneelradiator met lamellen</strong></td><td class=\"num\">€110 – €175</td><td>De ribbels en lamellen aan de binnenkant zijn lastig te bereiken.</td></tr>"
             "<tr><td><strong>Handdoek- of designradiator</strong></td><td class=\"num\">€120 – €225</td><td>Veel buizen die je rondom moet verven.</td></tr>"
             "<tr><td><strong>Ledenradiator (gietijzer)</strong></td><td class=\"num\">€150 – €225</td><td>Veel leden en tussenruimtes, vaak oude verflagen en roest.</td></tr>"
             "</tbody></table></div>"
             "<p>Dit is een eigen inschatting op basis van het uurtarief van schilders en de tijd die elk type kost. Een convector in een kast of vloerput wordt meestal niet geschilderd; daar gaat het alleen om de omkasting.</p>"),
            ("Ter plekke schilderen of laten demonteren?",
             "<div class=\"tablewrap\"><table><thead><tr><th>Manier</th><th>Wanneer het past</th><th>Let op</th></tr></thead><tbody>"
             "<tr><td><strong>Ter plekke met kwast en roller</strong></td><td>De radiator is nog goed en je wilt hem opfrissen.</td><td>De achterkant is maar deels bereikbaar. Je ziet lichte strepen.</td></tr>"
             "<tr><td><strong>Ter plekke spuiten</strong></td><td>Meerdere radiatoren in een lege kamer, bijvoorbeeld bij een verbouwing.</td><td>Alles in de ruimte moet onder folie.</td></tr>"
             "<tr><td><strong>Demonteren en in de werkplaats spuiten</strong></td><td>Je wilt een strakke, egale laag rondom.</td><td>Een installateur moet de cv aftappen en de radiator los- en vastzetten.</td></tr>"
             "<tr><td><strong>Stralen en opnieuw coaten</strong></td><td>Veel roest of oude, dikke verflagen.</td><td>Vergelijk de prijs met een nieuwe radiator. Dat is vaak niet veel duurder.</td></tr>"
             "</tbody></table></div>"
             "<p>Een radiator los halen is geen schilderswerk. Sommige schilders doen het zelf, anderen werken samen met een installateur. Vraag bij de offerte wie het doet en wat het kost. Laat je ook de muren schilderen, laat de radiator dan in dezelfde ronde meenemen. Wat muren per m² kosten, zie je bij <a href=\"/kosten/schilderen-per-m2/\">schilderen per m²</a>.</p>"),
            ("Welke verf hoort op een radiator?",
             "<p>Op een radiator hoort radiatorlak. Die is gemaakt om tegen de warmte van een cv-radiator te kunnen en vergeelt minder snel dan gewone lak. Gewone muurverf of grondverf kan door de warmte gaan vergelen, scheuren of plakken. Radiatorlak is er op waterbasis en op terpentinebasis; over het verschil lees je meer in <a href=\"/kennisbank/verf-op-waterbasis-of-terpentinebasis/\">verf op waterbasis of terpentinebasis</a>.</p>"
             "<p>Een paar regels die schilders aanhouden:</p>"
             "<ul><li>De verwarming moet uit en de radiator koud zijn tijdens het schilderen.</li>"
             "<li>Op kaal metaal en roestplekken komt eerst een roestwerende grondlaag.</li>"
             "<li>Laat de lak goed doorharden voordat je de verwarming weer hoog zet. Op het blik staat hoe lang.</li>"
             "<li>Kies een kleur die bij de muur past. Wit of de muurkleur valt het minst op.</li></ul>"),
            ("Rekenvoorbeeld: zeven radiatoren in een tussenwoning",
             "<p>Stel: je hebt vijf gladde paneelradiatoren, een handdoekradiator in de badkamer en een oude ledenradiator in de hal. Twee radiatoren hebben roestplekken. Alles wordt ter plekke geschilderd.</p>"
             "<div class=\"tablewrap\"><table><thead><tr><th>Post</th><th>Richtprijs</th></tr></thead><tbody>"
             "<tr><td>5 paneelradiatoren × €90 – €150</td><td class=\"num\">€450 – €750</td></tr>"
             "<tr><td>1 handdoekradiator</td><td class=\"num\">€120 – €225</td></tr>"
             "<tr><td>1 ledenradiator</td><td class=\"num\">€150 – €225</td></tr>"
             "<tr><td>Roest behandelen, 2 × €15 – €40</td><td class=\"num\">€30 – €80</td></tr>"
             "<tr><td><strong>Totaal</strong></td><td class=\"num\"><strong>€750 – €1.280</strong></td></tr>"
             "</tbody></table></div>"
             "<p>Moeten alle radiatoren los voor de werkplaats, dan komen er installatie-uren en transport bij. Laat je ook deuren of kozijnen spuiten, kijk dan bij <a href=\"/kosten/deuren-spuiten/\">deuren spuiten</a>: in één ronde deel je de opstart.</p>"),
        ],
        "tips": [
            "Laat radiatoren meenemen als de muren toch worden geschilderd. Dan deel je opstart en afdekken.",
            "Vraag welke verf er op komt. Radiatorlak vergeelt minder snel dan gewone lak.",
            "Bij veel roest of een oude radiator die slecht warm wordt: vraag ook een prijs voor een nieuwe radiator.",
            "Wil je de radiator los laten halen, spreek dan af wie de cv aftapt en weer vult.",
        ],
        "btw": "Schilderwerk in een woning die ouder is dan twee jaar valt onder het lage btw-tarief van 9%, inclusief de verf. Het stralen van metaal valt volgens de Belastingdienst onder 21%, en een nieuwe radiator plaatsen ook.",
        "bronnen": ("<p><small>Bronnen: <a href=\"https://www.homedeal.nl/cv-ketel/radiator-prijzen\" rel=\"nofollow noopener\">Homedeal</a> (een radiator vervangen kost €250 tot €600 inclusief montage), "
                    "<a href=\"https://slimster.nl/blog/radiator-verven/\" rel=\"nofollow noopener\">Slimster</a> (gewone verf is bestand tot ongeveer 100 °C, hittebestendige verf veel hoger) en "
                    "<a href=\"" + _BD_SCHILDEREN + "\" rel=\"nofollow noopener\">Belastingdienst</a> (btw op schilderen en stralen), geraadpleegd in november 2026. "
                    "De prijs per radiator is een eigen inschatting op basis van het uurtarief van schilders, geen vaste prijs van Topschilder.</small></p>"),
        "faq": [
            ("Wat kost een radiator verven?",
             "Reken op €90 tot €225 per radiator, inclusief radiatorlak en btw. Een gladde paneelradiator zit aan de onderkant, een ledenradiator of designradiator aan de bovenkant."),
            ("Wat kost een radiator laten spuiten?",
             "Ter plekke spuiten kost ongeveer hetzelfde als verven, maar het afdekken kost meer tijd. Laat je de radiator demonteren en in de werkplaats spuiten, dan komen de uren van de installateur en het transport erbij."),
            ("Kun je een radiator schilderen zonder hem eraf te halen?",
             "Ja, dat is de gangbare manier. De voorkant, zijkanten en bovenkant zijn goed te doen. De achterkant is maar deels bereikbaar, met een smalle radiatorroller of kwast."),
            ("Welke verf moet je op een radiator gebruiken?",
             "Radiatorlak. Die kan tegen de warmte van de verwarming en vergeelt minder snel. Op kale of roestige plekken komt eerst een roestwerende grondlaag."),
            ("Kan ik een radiator zelf verven met een spuitbus?",
             "Voor één radiator kan dat. Plak alles in de buurt goed af, want spuitnevel komt verder dan je denkt. Spuit meerdere dunne lagen in plaats van één dikke laag, anders krijg je druipers."),
            ("Is verven goedkoper dan een nieuwe radiator?",
             "Meestal wel. Een nieuwe radiator kost volgens Homedeal €250 tot €600 inclusief montage. Is de radiator erg verroest of lekt hij, dan is vervangen vaak slimmer."),
            ("Hoe lang moet een geverfde radiator drogen?",
             "Radiatorlak is vaak binnen een dag droog, maar heeft langer nodig om helemaal hard te worden. Kijk op het blik hoe lang je moet wachten voordat de verwarming weer hoog mag."),
        ],
    },

    # ------------------------------------------------------------------
    # 2. Kunststof kozijnen
    # ------------------------------------------------------------------
    {
        "slug": "kunststof-kozijnen-schilderen",
        "klus": "kunststof kozijnen schilderen",
        "h1": "Wat kost kunststof kozijnen schilderen of verven?",
        "title": "Kunststof kozijnen schilderen kosten 2026",
        "description": "Kunststof kozijnen laten schilderen kost €60 tot €140 per kozijn, inclusief hechtprimer en btw. Met uitleg over kleurkeuze, garantie en wrappen als alternatief.",
        "dienst": "buitenschilderwerk",
        "eenheid": "per kozijn (buiten)",
        "van": 60,
        "tot": 140,
        "kort": "€60 – €140 per kozijn",
        "intro": "Kunststof kozijnen hoeven niet geschilderd te worden. Toch kan het: als je een andere kleur wilt, of als oude witte kozijnen vergeeld en dof zijn. Het werk lijkt op houten kozijnen schilderen, maar de voorbereiding is anders. Zonder speciale hechtprimer laat de verf los. Hieronder zie je wat het kost en waar je op let.",
        "voorbeelden": [
            ("Appartement, 4 kozijnen", 4, "Kozijnen aan één gevel, goed bereikbaar vanaf het balkon."),
            ("Tussenwoning, 8 kozijnen", 8, "Voor- en achtergevel, zonder deuren. Steiger voor boven komt erbij."),
            ("Vrijstaande woning, 16 kozijnen", 16, "Kozijnen rondom, vaak met een schuifpui of openslaande deuren."),
        ],
        "extra": [
            ("Steiger of hoogwerker voor de bovenverdieping", "€300 – €900 per gevel, afhankelijk van de hoogte"),
            ("Kunststof voordeur schilderen", "€100 – €185 per deur"),
            ("Kozijn laten wrappen als alternatief", "gemiddeld €150 – €300 per kozijn, volgens Homedeal"),
            ("Kitvoegen rond het kozijn vervangen", "vraag een prijs per meter; valt onder 21% btw"),
        ],
        "prijsfactoren": [
            "De grootte van het kozijn en het aantal ramen en draaiende delen.",
            "Het voorwerk. Kunststof moet grondig worden ontvet en licht geschuurd, en krijgt een hechtprimer.",
            "De kleurwissel. Van wit naar een donkere kleur, of andersom, vraagt vaak een extra laag.",
            "Afplakken. Rubbers, beslag en glas mogen niet mee in de verf en moeten netjes worden afgeplakt.",
            "Of er een steiger of hoogwerker nodig is voor de bovenverdieping.",
        ],
        "uitleg": [
            ("Kun je kunststof kozijnen wel schilderen?", "Ja, met de juiste voorbereiding. Gewone grondverf voor hout hecht slecht op hard kunststof (pvc). Daarom gebruikt een schilder een hechtprimer die geschikt is voor kunststof, met daarop een lak die ook voor kunststof bedoeld is. Het resultaat gaat bij goed voorwerk jaren mee, maar niet zo lang als de originele kleur van het profiel."),
            ("Wat je ervoor krijgt", "Reinigen met een kunststofreiniger, ontvetten, licht opschuren, rubbers en beslag afplakken, een hechtprimer en twee lagen aflak. Bij een goede offerte staat erbij welke primer en lak er worden gebruikt, en of de schilder garantie geeft op de hechting."),
        ],
        "verdieping": [
            ("Zo gaat een schilder te werk",
             "<ol><li><strong>Controle.</strong> De schilder kijkt of het kunststof heel is en of er al een verflaag of folie op zit. Loszittende folie moet eerst weg.</li>"
             "<li><strong>Reinigen.</strong> Vuil, vet en aanslag gaan eraf met een reiniger voor kunststof. Daar valt of staat de hechting mee.</li>"
             "<li><strong>Opschuren.</strong> Licht schuren met fijn schuurpapier of een schuurvlies, zodat de primer zich kan vastzetten.</li>"
             "<li><strong>Afplakken.</strong> Glas, rubbers, hang- en sluitwerk en de gevel eromheen.</li>"
             "<li><strong>Hechtprimer.</strong> Een primer die geschikt is voor pvc. Gewone houtgrondverf is niet genoeg.</li>"
             "<li><strong>Aflakken.</strong> Twee lagen lak, bij droog weer en een temperatuur die de verfleverancier aangeeft. Kijk voor een goede dag op het <a href=\"/schilderweer/\">schilderweer</a>.</li></ol>"
             "<p>Meer over geschikte verf lees je in <a href=\"/kennisbank/welke-verf-voor-kozijnen/\">welke verf voor kozijnen</a>.</p>"),
            ("Lichte of donkere kleur?",
             "<p>Kies bij kunststof liever een lichte of middentint. Een donker kozijn wordt in de zon veel warmer dan een wit kozijn. Kunststof zet bij warmte uit, en bij hoge temperaturen kan een profiel kromtrekken of kunnen ramen gaan klemmen. Fabrikanten die donkere kunststof kozijnen maken, gebruiken daar speciale folies, pigmenten of versterkte profielen voor. Een verflaag achteraf heeft die aanpassingen niet.</p>"
             "<p>Wil je toch antraciet of zwart, vraag de schilder dan om een verf die de verfleverancier uitdrukkelijk geschikt noemt voor donkere kleuren op kunststof. Let extra op kozijnen op het zuiden en westen, die de meeste zon krijgen. Twijfel je over de kleur, probeer combinaties dan eerst uit met de <a href=\"/kleuren-kiezen/\">kleurenkiezer</a>.</p>"),
            ("Let op de garantie van de kozijnfabrikant",
             "<p>Op nieuwe kunststof kozijnen zit vaak een lange fabrieksgarantie, ook op de kleur. Als je de kozijnen schildert, kan die garantie (deels) vervallen, bijvoorbeeld op vervorming of op de afwerking. De voorwaarden verschillen per fabrikant en leverancier.</p>"
             "<p>Zijn je kozijnen jonger dan tien jaar, zoek dan eerst je garantiebewijs op of vraag het na bij de leverancier. Vraag ook welke verf of voorbehandeling zij toestaan. Leg het antwoord liefst schriftelijk vast voordat de schilder begint.</p>"),
            ("Schilderen, wrappen of laten zitten?",
             "<div class=\"tablewrap\"><table><thead><tr><th>Keuze</th><th>Wanneer het past</th><th>Let op</th></tr></thead><tbody>"
             "<tr><td><strong>Schilderen</strong></td><td>Je wilt een andere kleur, of vergeelde kozijnen opfrissen.</td><td>Een verflaag op kunststof moet je na een aantal jaar bijwerken. Elke RAL-kleur kan.</td></tr>"
             "<tr><td><strong>Wrappen (folie)</strong></td><td>Je wilt een houtlook of een kleur die lang meegaat.</td><td>Homedeal noemt €150 – €300 per gemiddeld kozijn. Wrapfolie valt onder 21% btw.</td></tr>"
             "<tr><td><strong>Laten zitten en reinigen</strong></td><td>De kozijnen zijn alleen vuil of licht dof.</td><td>Een goede schoonmaakbeurt met kunststofreiniger doet vaak al veel.</td></tr>"
             "</tbody></table></div>"),
            ("Rekenvoorbeeld: acht kozijnen van een tussenwoning",
             "<p>Een tussenwoning met vier kozijnen voor en vier achter. De witte kozijnen zijn vergeeld en worden in gebroken wit geschilderd. Voor de bovenverdieping aan de achterkant is een steiger nodig.</p>"
             "<div class=\"tablewrap\"><table><thead><tr><th>Post</th><th>Richtprijs</th></tr></thead><tbody>"
             "<tr><td>8 kozijnen × €60 – €140</td><td class=\"num\">€480 – €1.120</td></tr>"
             "<tr><td>Steiger achtergevel</td><td class=\"num\">€300 – €900</td></tr>"
             "<tr><td><strong>Totaal</strong></td><td class=\"num\"><strong>€780 – €2.020</strong></td></tr>"
             "</tbody></table></div>"
             "<p>Heb je naast kunststof ook houten kozijnen, bijvoorbeeld een houten voordeur of dakkapel? Die kosten per stuk meer, zie <a href=\"/kosten/kozijnen-schilderen/\">kozijnen schilderen</a>.</p>"),
        ],
        "tips": [
            "Check eerst de garantie van je kozijnfabrikant. Schilderen kan die garantie raken.",
            "Kies een lichte of middentint. Donkere kleuren worden in de zon veel warmer.",
            "Vraag welke hechtprimer de schilder gebruikt en of die geschikt is voor pvc.",
            "Zijn de kozijnen alleen vuil, laat ze dan eerst goed reinigen. Misschien is schilderen dan niet nodig.",
        ],
        "btw": "Schilderwerk aan een woning die ouder is dan twee jaar valt onder het lage btw-tarief van 9%, ook bij kunststof kozijnen en inclusief de verf. Wrapfolie aanbrengen en kitwerk aan de gevel vallen volgens de Belastingdienst onder 21%.",
        "bronnen": ("<p><small>Bronnen: <a href=\"https://www.homedeal.nl/schilderwerk/kozijnen-schilderen-prijs\" rel=\"nofollow noopener\">Homedeal</a> (buitenkozijnen schilderen €50 tot €100 per kozijn; schilderen is bij kunststof niet noodzakelijk), "
                    "<a href=\"https://www.homedeal.nl/inspiratie/kozijn-wrappen\" rel=\"nofollow noopener\">Homedeal</a> (gemiddeld kozijn wrappen €150 tot €300) en "
                    "<a href=\"https://www.bobex.be/nl-be/schilderwerken/ramen/pvc/\" rel=\"nofollow noopener\">Bobex</a> (pvc-ramen met voorbereiding €8 tot €12 per m², Belgische prijzen), geraadpleegd in november 2026. "
                    "Dit zijn indicaties van die sites, geen prijzen van Topschilder.</small></p>"),
        "faq": [
            ("Wat kost het om kunststof kozijnen te laten schilderen?",
             "Reken op €60 tot €140 per kozijn, inclusief hechtprimer, lak en btw. Een steiger voor de bovenverdieping komt er meestal apart bij, €300 tot €900 per gevel."),
            ("Kun je kunststof kozijnen verven?",
             "Ja. Het kunststof moet goed worden gereinigd en licht geschuurd, en krijgt een hechtprimer voor pvc. Gewone houtgrondverf hecht niet goed op kunststof."),
            ("Mag je kunststof kozijnen zwart of antraciet verven?",
             "Het kan, maar donkere kleuren worden in de zon veel warmer. Kunststof zet dan uit en kan vervormen. Gebruik alleen verf die de leverancier geschikt noemt voor donkere kleuren op kunststof, en check de garantie van je kozijnen."),
            ("Vervalt de garantie als ik kunststof kozijnen schilder?",
             "Dat kan. Het hangt af van de voorwaarden van de fabrikant of leverancier. Vraag het na voordat je laat schilderen, en vraag welke verf zij toestaan."),
            ("Hoe lang blijft verf op kunststof kozijnen mooi?",
             "Met goed voorwerk en de juiste primer een flink aantal jaren. Op de zon- en windkant moet je eerder bijwerken. Verf gaat op kunststof minder lang mee dan de originele kleur van het profiel."),
            ("Is wrappen beter dan schilderen?",
             "Wrappen geeft een egale laag en is er ook in houtlook. Homedeal noemt €150 tot €300 per gemiddeld kozijn. Schilderen is flexibeler in kleur en beschadigingen zijn makkelijker bij te werken."),
        ],
    },

    # ------------------------------------------------------------------
    # 3. Gevel / buitenmuur schilderen
    # ------------------------------------------------------------------
    {
        "slug": "gevel-schilderen",
        "klus": "een gevel schilderen",
        "kruimel": "Gevel en buitenmuur schilderen",
        "h1": "Wat kost een buitenmuur of gevel schilderen per m²?",
        "title": "Gevel schilderen kosten 2026: prijs per m²",
        "description": "Een gevel of buitenmuur laten schilderen kost €20 tot €40 per m², inclusief gevelverf en btw. Met rekenvoorbeelden, steigerkosten en wanneer je beter niet schildert.",
        "dienst": "buitenschilderwerk",
        "eenheid": "per m² gevel",
        "van": 20,
        "tot": 40,
        "kort": "€20 – €40 per m²",
        "intro": "Deze pagina gaat over de muur zelf: een stenen, betonnen of gepleisterde gevel die geschilderd wordt. Schilders rekenen dat per m². De prijs hangt vooral af van de staat van de muur, hoeveel voorwerk er nodig is en of er een steiger moet komen. Lang niet elke gevel moet geschilderd worden. Ook dat lees je hieronder.",
        "voorbeelden": [
            ("Tussenwoning, voor- en achtergevel", 50, "Zo'n 50 m² muur na aftrek van ramen en deuren."),
            ("Hoekwoning, inclusief zijgevel", 90, "Een extra zijgevel zonder veel ramen."),
            ("Vrijstaande woning, rondom", 150, "Vier gevels, vaak met een hogere kopgevel."),
        ],
        "extra": [
            ("Steiger of hoogwerker", "€300 – €900 per gevel, afhankelijk van de hoogte"),
            ("Gevel reinigen vooraf", "€5 – €20 per m², afhankelijk van de methode"),
            ("Scheuren en losse plekken repareren", "op uurbasis, €45 – €65 per uur excl. btw"),
            ("Kozijnen in dezelfde ronde schilderen", "€90 – €190 per buitenkozijn"),
        ],
        "prijsfactoren": [
            "De ondergrond. Glad pleisterwerk is sneller klaar dan ruw metselwerk of sierpleister, dat meer verf opneemt.",
            "Het voorwerk. Reinigen, algen en mos verwijderen, scheuren vullen en losse verf wegschuren kosten tijd.",
            "De hoogte en bereikbaarheid. Voor alles boven de begane grond is een steiger of hoogwerker nodig.",
            "De verfsoort. Dampopen gevelverf op silicaat- of siliconenbasis is duurder dan gewone buitenmuurverf.",
            "Het oppervlak. Bij een grote gevel daalt de prijs per m², omdat opstart en steiger over meer meters worden verdeeld.",
        ],
        "uitleg": [
            ("Wat je ervoor krijgt", "De schilder reinigt de gevel, verwijdert algen en losse verf, repareert kleine scheuren en plakt kozijnen en dakgoten af. Op zuigende of kale plekken komt een grondlaag. Daarna volgen meestal twee lagen gevelverf. Vraag of reinigen en repareren in de prijs per m² zitten, want dat verschilt per offerte."),
            ("Muur of houtwerk?", "Bij een buitenschilderbeurt denk je vaak aan kozijnen, deuren en boeidelen. Dat is ander werk, met een prijs per kozijn of per meter. Wil je alles in één keer laten doen, kijk dan ook bij huis schilderen voor de prijs van het houtwerk."),
        ],
        "verdieping": [
            ("Wel of niet schilderen?",
             "<p>Een gevel van schoon metselwerk, dus baksteen die nooit geverfd is, laat je meestal gewoon zo. Metselwerk moet kunnen ademen: vocht uit de muur moet naar buiten kunnen. Een verflaag die dat tegenhoudt, kan leiden tot vochtplekken binnen, vorstschade of verf die na een paar jaar afbladdert. En als de gevel eenmaal geverfd is, moet je hem blijven onderhouden.</p>"
             "<div class=\"tablewrap\"><table><thead><tr><th>Soort gevel</th><th>Schilderen?</th></tr></thead><tbody>"
             "<tr><td><strong>Schoon metselwerk</strong></td><td>Meestal niet. Reinigen en eventueel voegwerk herstellen is vaak beter.</td></tr>"
             "<tr><td><strong>Al eerder geschilderde gevel</strong></td><td>Ja. Die laag moet je onderhouden, ongeveer elke acht tot twaalf jaar.</td></tr>"
             "<tr><td><strong>Gepleisterde gevel of sierpleister</strong></td><td>Ja. Pleisterwerk wordt vaak geschilderd om het te beschermen en op kleur te houden.</td></tr>"
             "<tr><td><strong>Beton of kalkzandsteen</strong></td><td>Kan, met een gevelverf die geschikt is voor die ondergrond.</td></tr>"
             "</tbody></table></div>"
             "<p>Is je gevel alleen vuil of groen, kijk dan eerst bij <a href=\"/kosten/gevel-reinigen-impregneren/\">gevel reinigen en impregneren</a>. Dat is vaak goedkoper en de steen blijft zichtbaar.</p>"),
            ("Welke gevelverf?",
             "<p>Op een gevel hoort een dampopen verf: die laat waterdamp uit de muur door, maar houdt regen tegen. De meest gebruikte soorten:</p>"
             "<ul><li><strong>Acrylaat buitenmuurverf.</strong> Gangbaar en betaalbaar, voor gladde en al geschilderde gevels.</li>"
             "<li><strong>Siliconenharsverf.</strong> Sterk waterafstotend en vuilwerend, goed dampopen. Wat duurder.</li>"
             "<li><strong>Silicaatverf.</strong> Hecht zich chemisch aan minerale ondergronden zoals kalk en steen. Vaak gebruikt bij oudere panden.</li></ul>"
             "<p>Een schilder kiest de verf op basis van de ondergrond en wat er al op zit. Silicaatverf hecht bijvoorbeeld niet op een oude laag kunststofverf. Vraag op de offerte welke verf er gebruikt wordt. Voor de kleur kun je combinaties uitproberen met de <a href=\"/kleuren-kiezen/\">kleurenkiezer</a>.</p>"),
            ("Zo gaat een schilder te werk",
             "<ol><li><strong>Opname.</strong> De schilder kijkt naar scheuren, losse plekken, vochtplekken en wat voor verf er al op zit.</li>"
             "<li><strong>Steiger.</strong> Voor de bovenverdieping komt er een steiger of hoogwerker.</li>"
             "<li><strong>Reinigen.</strong> Vuil, algen en mos gaan eraf. Daarna moet de gevel goed drogen.</li>"
             "<li><strong>Repareren.</strong> Scheuren vullen, losse verf wegschuren, zuigende plekken voorstrijken.</li>"
             "<li><strong>Schilderen.</strong> Twee lagen gevelverf, bij droog weer en niet in de felle zon.</li></ol>"
             "<p>Gevelverf wil droog weer en een minimale temperatuur, net als ander buitenwerk. Lees <a href=\"/gids/wanneer-buiten-schilderen/\">wanneer je buiten kunt schilderen</a>.</p>"),
            ("Rekenvoorbeeld: een hoekwoning",
             "<p>Een hoekwoning met een eerder geschilderde gevel van in totaal 90 m², verdeeld over voor-, achter- en zijgevel. De gevel is groen uitgeslagen en moet eerst gereinigd worden. Aan twee kanten is een steiger nodig.</p>"
             "<div class=\"tablewrap\"><table><thead><tr><th>Post</th><th>Richtprijs</th></tr></thead><tbody>"
             "<tr><td>Gevel schilderen, 90 m² × €20 – €40</td><td class=\"num\">€1.800 – €3.600</td></tr>"
             "<tr><td>Reinigen vooraf, 90 m² × €5 – €15</td><td class=\"num\">€450 – €1.350</td></tr>"
             "<tr><td>Steiger, 2 gevels × €300 – €900</td><td class=\"num\">€600 – €1.800</td></tr>"
             "<tr><td><strong>Totaal</strong></td><td class=\"num\"><strong>€2.850 – €6.750</strong></td></tr>"
             "</tbody></table></div>"
             "<p>Laat je in dezelfde ronde de kozijnen, deuren en boeidelen doen, dan deel je de steiger. Wat dat houtwerk kost, zie je bij <a href=\"/kosten/huis-schilderen/\">huis schilderen</a>.</p>"),
        ],
        "tips": [
            "Laat schoon metselwerk ongeverfd. Reinigen is vaak genoeg en voorkomt jaren van onderhoud.",
            "Combineer gevel en houtwerk in één ronde. Dan betaal je de steiger maar één keer.",
            "Vraag of reinigen en kleine reparaties in de prijs per m² zitten.",
            "Los vochtproblemen eerst op. Verf op een natte muur laat los.",
        ],
        "btw": "Schilderwerk aan een woning die ouder is dan twee jaar valt onder het lage btw-tarief van 9%, inclusief de verf en het voorbereidende werk. Stralen of impregneren van een stenen gevel en alleen voegwerk herstellen vallen volgens de Belastingdienst onder 21%.",
        "bronnen": ("<p><small>Bronnen: <a href=\"https://slimster.nl/schilder/kosten-buitenmuur-verven/\" rel=\"nofollow noopener\">Slimster</a> (gevel schilderen gemiddeld €25 tot €40 per m², reinigen €8 tot €20 per m² extra), "
                    "<a href=\"https://www.homedeal.nl/schilderwerk/buitenschilder-kosten/\" rel=\"nofollow noopener\">Homedeal</a> (gevel €35 tot €40 per m², buitenmuur €15 tot €25 per m²) en "
                    "<a href=\"" + _BD_SCHILDEREN + "\" rel=\"nofollow noopener\">Belastingdienst</a> (btw op schilderen), geraadpleegd in november 2026. "
                    "Dit zijn indicaties van die sites, geen prijzen van Topschilder.</small></p>"),
        "faq": [
            ("Wat kost een gevel schilderen per m²?",
             "Reken op €20 tot €40 per m², inclusief gevelverf en btw. Een steiger en uitgebreid reinigen of repareren komen er vaak apart bij."),
            ("Wat kost het om een buitenmuur te verven?",
             "Voor de voor- en achtergevel van een tussenwoning, zo'n 50 m², kom je op €1.000 tot €2.000. Met een steiger voor de bovenverdieping komt daar €300 tot €900 per gevel bij."),
            ("Welke muurverf gebruik je buiten?",
             "Een dampopen gevelverf, zoals acrylaat buitenmuurverf, siliconenharsverf of silicaatverf. Gewone muurverf voor binnen is niet geschikt voor buiten."),
            ("Kun je een bakstenen gevel schilderen?",
             "Het kan, maar bij schoon metselwerk is het meestal niet verstandig. De muur moet kunnen ademen, en eenmaal geverfd moet je de gevel blijven onderhouden. Reinigen is vaak een beter idee."),
            ("Hoe vaak moet een geschilderde gevel opnieuw?",
             "Ongeveer elke acht tot twaalf jaar, afhankelijk van de verf, de ligging en het weer. De zon- en regenkant gaat sneller."),
            ("Wanneer kun je een gevel het beste laten schilderen?",
             "Van april tot en met oktober, bij droog weer. De muur moet droog zijn en het mag niet vriezen in de nacht na het schilderen."),
        ],
    },

    # ------------------------------------------------------------------
    # 4. Boeidelen
    # ------------------------------------------------------------------
    {
        "slug": "boeidelen-schilderen",
        "klus": "boeidelen schilderen",
        "h1": "Wat kost boeidelen schilderen, of juist vervangen?",
        "title": "Boeidelen schilderen kosten 2026: prijs per meter",
        "description": "Boeidelen laten schilderen kost €25 tot €55 per strekkende meter, inclusief verf en btw. Vervangen door kunststof kost vaak €95 tot €135 per meter.",
        "dienst": "buitenschilderwerk",
        "eenheid": "per strekkende meter",
        "van": 25,
        "tot": 55,
        "kort": "€25 – €55 per meter",
        "intro": "Boeidelen en windveren zitten hoog, vangen veel wind en regen en zijn lastig bereikbaar. Daardoor slijt de verf er sneller dan op de rest van je huis. Schilders rekenen ze meestal per strekkende meter. Zijn ze erg aangetast, dan is vervangen door kunststof soms slimmer. Hieronder zie je beide prijzen.",
        "voorbeelden": [
            ("Tussenwoning, voor en achter", 12, "Twee boeidelen van zo'n zes meter, zonder windveren."),
            ("Hoekwoning met windveren", 22, "Boeidelen voor en achter plus twee schuine windveren aan de kopgevel."),
            ("Vrijstaande woning, rondom", 40, "Boeidelen en windveren rondom, soms met een houten dakgoot."),
        ],
        "extra": [
            ("Steiger of hoogwerker", "€300 – €900 per gevel, afhankelijk van de hoogte"),
            ("Houtrot repareren", "€50 – €275 per reparatieplek"),
            ("Houten boeidelen vervangen, onbeschilderd", "€50 – €75 per meter incl. montage, volgens Slimster"),
            ("Kunststof boeidelen of windveren", "€95 – €135 per meter incl. montage, volgens Slimster"),
        ],
        "prijsfactoren": [
            "De hoogte en bereikbaarheid. Boeidelen zitten bijna altijd zo hoog dat er een steiger of hoogwerker nodig is.",
            "De staat van het hout. Afbladderende verf, open naden en houtrot vragen veel voorwerk.",
            "De breedte. Een breed boeiboord met een overstek aan de onderkant heeft meer oppervlak per meter.",
            "Of de dakgoot meegaat. Een houten bakgoot of zinken goot schilderen is extra werk.",
            "Of de rest van het buitenschilderwerk tegelijk wordt gedaan. Dan deel je de steiger.",
        ],
        "uitleg": [
            ("Wat je ervoor krijgt", "Losse verf verwijderen, schuren, ontvetten, kale plekken gronden, naden kitten en twee lagen buitenlak. Bij de opname prikt de schilder in het hout om houtrot te vinden, vooral bij de hoeken en de uiteinden. Op een goede offerte staat hoe houtrot wordt afgerekend."),
            ("Hoe vaak moeten boeidelen geschilderd worden?", "Bij dekkende verf ongeveer elke vijf tot zeven jaar, vaak eerder dan de kozijnen. Boeidelen op het zuiden en westen gaan het snelst. Wacht je te lang, dan trekt er water in het hout en wordt het herstel duurder dan de schilderbeurt."),
        ],
        "verdieping": [
            ("Boeidelen, windveren en dakgoot: wat is wat?",
             "<ul><li><strong>Boeidelen</strong> (boeiboorden) zijn de planken langs de onderrand van het dak, aan de voor- en achtergevel. Vaak zit de dakgoot erachter of erop.</li>"
             "<li><strong>Windveren</strong> zijn de schuine planken langs de dakrand aan de kopgevel. Ze vangen de meeste wind.</li>"
             "<li><strong>De dakgoot</strong> kan van zink, kunststof of hout zijn. Een houten bakgoot wordt meegeschilderd. Een zinken goot kan ook geschilderd worden, maar dan met een primer die op zink hecht.</li></ul>"
             "<p>Schilders zetten deze onderdelen meestal samen op de offerte, als prijs per meter of als vast bedrag. Vraag of de onderkant van het overstek (de onderzijde van het dak) is inbegrepen.</p>"),
            ("Schilderen of vervangen door kunststof?",
             "<div class=\"tablewrap\"><table><thead><tr><th>Keuze</th><th>Richtprijs per meter</th><th>Wanneer het past</th></tr></thead><tbody>"
             "<tr><td><strong>Schilderen</strong></td><td class=\"num\">€25 – €55</td><td>Het hout is nog grotendeels gezond.</td></tr>"
             "<tr><td><strong>Plaatselijk herstel en schilderen</strong></td><td class=\"num\">€25 – €55 plus €50 – €275 per plek</td><td>Een paar rotte plekken, de rest is goed.</td></tr>"
             "<tr><td><strong>Nieuw hout</strong></td><td class=\"num\">€50 – €75, plus schilderen</td><td>Veel houtrot, en je wilt de houten uitstraling houden.</td></tr>"
             "<tr><td><strong>Kunststof (zoals Keralit)</strong></td><td class=\"num\">€95 – €135</td><td>Je wilt er jaren geen onderhoud meer aan.</td></tr>"
             "<tr><td><strong>Plaatmateriaal (zoals Trespa)</strong></td><td>vraag een prijs</td><td>Strakke, moderne uitstraling en weinig onderhoud.</td></tr>"
             "</tbody></table></div>"
             "<p>De prijzen voor vervangen komen van Slimster en zijn inclusief montage en btw. Offerteadviseur rekent voor kunststof boeidelen €75 tot €115 per m². Kunststof hoeft niet geschilderd te worden, maar wordt wel vuil en moet af en toe worden schoongemaakt. Lees hoe je rot hout herkent in <a href=\"/kennisbank/houtrot-herkennen-en-herstellen/\">houtrot herkennen en herstellen</a>.</p>"),
            ("Steiger of hoogwerker?",
             "<p>Bij een tussenwoning kan een schilder soms met een rolsteiger of een dakladder werken. Bij een hoge nok of aan de straatkant is een steiger of hoogwerker nodig. Een hoogwerker staat er alleen op de werkdagen en is snel opgebouwd. Een steiger blijft staan en is handiger als er ook houtrot hersteld moet worden. Reken op €300 tot €900 per gevel. Staat er voor een <a href=\"/kosten/dakkapel-schilderen/\">dakkapel</a> of de kozijnen toch al een steiger, laat de boeidelen dan meteen meenemen.</p>"),
            ("Rekenvoorbeeld: hoekwoning met windveren",
             "<p>Een hoekwoning met 12 meter boeidelen voor en achter, en twee windveren van 5 meter aan de kopgevel. Bij de opname vindt de schilder twee rotte plekken in de hoeken.</p>"
             "<div class=\"tablewrap\"><table><thead><tr><th>Post</th><th>Richtprijs</th></tr></thead><tbody>"
             "<tr><td>22 meter schilderen × €25 – €55</td><td class=\"num\">€550 – €1.210</td></tr>"
             "<tr><td>Houtrot, 2 plekken × €50 – €275</td><td class=\"num\">€100 – €550</td></tr>"
             "<tr><td>Steiger of hoogwerker, kopgevel en achter</td><td class=\"num\">€600 – €1.800</td></tr>"
             "<tr><td><strong>Totaal</strong></td><td class=\"num\"><strong>€1.250 – €3.560</strong></td></tr>"
             "</tbody></table></div>"
             "<p>Ter vergelijking: dezelfde 22 meter vervangen door kunststof kost volgens de prijzen van Slimster €2.090 tot €2.970, plus de steiger en het afvoeren van het oude hout. Daarna heb je geen schilderwerk meer aan de boeidelen. Wil je weten hoe je huis er verder voor staat, doe dan de <a href=\"/onderhoudscheck/\">onderhoudscheck</a>.</p>"),
        ],
        "tips": [
            "Laat boeidelen meenemen met de kozijnen of dakkapel. De steiger staat er dan toch.",
            "Laat rotte plekken in de hoeken meteen herstellen. Daar trekt het water in.",
            "Vraag bij veel houtrot twee prijzen: herstellen en schilderen, en vervangen door kunststof.",
            "Vraag of de onderkant van het overstek in de prijs per meter zit.",
        ],
        "btw": "Schilderwerk aan een woning die ouder is dan twee jaar valt onder het lage btw-tarief van 9%, inclusief de verf. Boeidelen vervangen en houten inzetstukken vallen onder 21%. Een nette offerte splitst die posten.",
        "bronnen": ("<p><small>Bronnen: <a href=\"https://slimster.nl/windveren/prijzen/\" rel=\"nofollow noopener\">Slimster</a> (vervangen inclusief montage en btw: hout €50 tot €75, kunststof €95 tot €135 en zink €140 per meter), "
                    "<a href=\"https://www.offerteadviseur.nl/categorie/bouw/dakdekker/boeiboord-vervangen-door-kunststof/\" rel=\"nofollow noopener\">Offerteadviseur</a> (kunststof boeidelen €75 tot €115 per m²) en "
                    "<a href=\"https://www.bobex.be/nl-be/schilderwerken/buiten/dakgoot/\" rel=\"nofollow noopener\">Bobex</a> (dakgoot schilderen €55 tot €65 per strekkende meter, Belgische prijzen), geraadpleegd in november 2026. "
                    "De prijs per meter voor schilderen is een eigen inschatting, geen vaste prijs van Topschilder.</small></p>"),
        "faq": [
            ("Wat kost boeidelen schilderen?",
             "Reken op €25 tot €55 per strekkende meter, inclusief verf en btw. Voor een tussenwoning met zo'n 12 meter boeidelen is dat €300 tot €660, plus een steiger of hoogwerker."),
            ("Wat kost boeidelen vervangen?",
             "Volgens Slimster kost nieuw hout €50 tot €75 per meter, onbeschilderd, en kunststof €95 tot €135 per meter, beide inclusief montage en btw. Een steiger en het afvoeren van het oude hout komen er vaak bij."),
            ("Wat kost een dakgoot schilderen?",
             "Een houten bakgoot gaat vaak mee met de boeidelen, in de prijs per meter. Een zinken goot schilderen kan ook, maar vraagt een speciale primer. Vraag daar een aparte prijs voor."),
            ("Wat kost windveren schilderen?",
             "Hetzelfde als boeidelen: €25 tot €55 per strekkende meter. Windveren zitten aan de kopgevel en vaak hoog, dus reken op een steiger of hoogwerker."),
            ("Is kunststof beter dan houten boeidelen?",
             "Kunststof hoeft niet geschilderd te worden en kan niet rotten. Het is duurder in aanschaf. Is het hout nog grotendeels gezond, dan is schilderen goedkoper."),
            ("Hoe vaak moeten boeidelen geschilderd worden?",
             "Ongeveer elke vijf tot zeven jaar. Boeidelen op het zuiden en westen gaan sneller, omdat ze de meeste zon en regen krijgen."),
        ],
    },

    # ------------------------------------------------------------------
    # 5. Schutting en tuinhuis beitsen
    # ------------------------------------------------------------------
    {
        "slug": "schutting-beitsen",
        "klus": "een schutting beitsen",
        "kruimel": "Schutting en tuinhuis beitsen",
        "h1": "Wat kost een schutting of tuinhuis laten beitsen?",
        "title": "Schutting beitsen kosten 2026: prijs per m²",
        "description": "Een schutting laten beitsen kost €8 tot €20 per m² per zijde, inclusief beits en btw. Een tuinhuis €350 tot €1.200. Plus wanneer zelf doen slimmer is.",
        "dienst": "buitenschilderwerk",
        "eenheid": "per m² schutting (één zijde)",
        "van": 8,
        "tot": 20,
        "kort": "€8 – €20 per m²",
        "intro": "Een schutting of tuinhuis beitsen doen veel mensen zelf, en dat is vaak prima te doen. Toch kan een schilder handig zijn: bij een lange schutting, een groot tuinhuis, een dekkende kleur of als je er gewoon geen tijd voor hebt. Hieronder zie je wat het kost als je het laat doen, en wanneer het de moeite waard is.",
        "voorbeelden": [
            ("Schutting van 10 meter, één zijde", 18, "Schutting van 1,80 meter hoog, alleen aan jouw kant."),
            ("Schutting van 10 meter, beide zijden", 36, "Na overleg met de buren beide kanten tegelijk."),
            ("Schutting van 25 meter, beide zijden", 90, "Een tuin met schutting aan twee kanten."),
        ],
        "extra": [
            ("Tuinhuis beitsen of schilderen", "€350 – €1.200 per tuinhuis (eigen inschatting)"),
            ("Tuinhek schilderen of beitsen", "€75 – €250 per hek (eigen inschatting)"),
            ("Vlonder beitsen of oliën", "€10 – €25 per m² (eigen inschatting)"),
            ("Schoonmaken en groene aanslag verwijderen", "€2 – €5 per m² extra (eigen inschatting)"),
        ],
        "prijsfactoren": [
            "Transparant of dekkend. Dekkende beits of verf vraagt meestal een laag meer dan transparante beits.",
            "De staat van het hout. Groene aanslag, oude loszittende beits of verf moet er eerst af.",
            "Eén of twee zijden. Beide kanten tegelijk is per m² goedkoper dan twee losse keren.",
            "De vorm. Een rechte planken schutting gaat snel. Latten, roosterwerk en een tuinhuis met veel randen kosten meer tijd.",
            "Hoeveel er in één keer gebeurt. Schutting, tuinhuis en hek samen is per onderdeel goedkoper.",
        ],
        "uitleg": [
            ("Wat je ervoor krijgt", "De schilder maakt het hout schoon, laat het drogen en schuurt ruwe en loszittende plekken op. Planten en tegels worden afgedekt. Daarna komen twee lagen beits, op onbehandeld hout soms drie. Bij een tuinhuis gaan de kozijnen, de deur en de boeidelen meestal mee."),
            ("Zelf doen of laten doen?", "Een schutting beitsen is een klus die je prima zelf kunt doen: het is laag, de ondergrond is ruw en een kleine afwijking zie je nauwelijks. Een schilder is vooral zinvol bij lange schuttingen, hoge tuinhuizen, dekkende kleuren die strak moeten, of als de oude laag eerst helemaal weg moet."),
        ],
        "verdieping": [
            ("Beits, verf of olie?",
             "<div class=\"tablewrap\"><table><thead><tr><th>Keuze</th><th>Resultaat</th><th>Onderhoud</th></tr></thead><tbody>"
             "<tr><td><strong>Transparante beits</strong></td><td>De houtnerf blijft zichtbaar, met een lichte kleurtint.</td><td>Vaker opnieuw, ongeveer elke één tot twee jaar.</td></tr>"
             "<tr><td><strong>Dekkende beits</strong></td><td>Egale kleur, zoals zwart, antraciet of grijs. De structuur van het hout blijft voelbaar.</td><td>Gaat langer mee, ongeveer elke twee tot vier jaar.</td></tr>"
             "<tr><td><strong>Verf (grondverf en lak)</strong></td><td>Gladde, egale laag. Past bij geschaafd hout, zoals een tuinhuisdeur of kozijn.</td><td>Gaat lang mee, maar bladdert bij achterstallig onderhoud en moet dan geschuurd worden.</td></tr>"
             "<tr><td><strong>Olie</strong></td><td>Natuurlijke uitstraling, vooral voor hardhout en vlonders.</td><td>Meestal elk jaar opnieuw.</td></tr>"
             "</tbody></table></div>"
             "<p>Beits trekt in het hout en bladdert daardoor minder dan verf. Daarom is beits het meest gekozen voor ruw tuinhout. Hoe vaak je opnieuw moet, staat op het blik en hangt af van de zon en regen op die plek.</p>"),
            ("Nieuw geïmpregneerd hout: eerst even wachten",
             "<p>Groen of bruin geïmpregneerd vurenhout zit bij levering vaak nog vol vocht en impregneermiddel. Beits of verf hecht dan slecht. Vaak wordt aangeraden zo'n schutting eerst een paar maanden tot een jaar te laten drogen en verweren. Hoe lang precies, hangt af van het hout en de beits: kijk op het blik wat de fabrikant zegt.</p>"
             "<p>Geïmpregneerd hout hoeft niet per se gebeitst te worden. Het is al beschermd, alleen verkleurt het na verloop van tijd naar grijs. Beitsen doe je dan vooral voor de kleur. Onbehandeld vurenhout moet je wel snel na het plaatsen beitsen.</p>"),
            ("Wanneer laat je het een schilder doen?",
             "<p>Eerlijk is eerlijk: voor een korte schutting is een schilder vaak niet nodig. Met een kwast of blokkwast, een paar droge dagen en een paar blikken beits kom je een heel eind. Een schilder is het geld waard als:</p>"
             "<ul><li>het om veel meters gaat, of om een groot of hoog tuinhuis;</li>"
             "<li>je een dekkende kleur wilt die strak en egaal moet worden;</li>"
             "<li>oude verf of beits afbladdert en eerst weg moet;</li>"
             "<li>er toch al een schilder komt voor de kozijnen of boeidelen van je huis.</li></ul>"
             "<p>Beitsen kan alleen bij droog weer en als het hout droog is. Kijk vooraf op het <a href=\"/schilderweer/\">schilderweer</a>. Voor het buitenseizoen in het algemeen: <a href=\"/gids/wanneer-buiten-schilderen/\">wanneer kun je buiten schilderen</a>.</p>"),
            ("Rekenvoorbeeld: schutting en tuinhuis samen",
             "<p>Een achtertuin met 15 meter schutting van 1,80 meter hoog, aan beide kanten, en een tuinhuis van 3 bij 3 meter. Alles in een dekkende beits.</p>"
             "<div class=\"tablewrap\"><table><thead><tr><th>Post</th><th>Richtprijs</th></tr></thead><tbody>"
             "<tr><td>Schutting, 54 m² × €8 – €20</td><td class=\"num\">€432 – €1.080</td></tr>"
             "<tr><td>Tuinhuis, inclusief deur en boeidelen</td><td class=\"num\">€350 – €1.200</td></tr>"
             "<tr><td><strong>Totaal</strong></td><td class=\"num\"><strong>€782 – €2.280</strong></td></tr>"
             "</tbody></table></div>"
             "<p>Laat je het tuinwerk meenemen met het <a href=\"/schilderwerk/buitenschilderwerk/\">buitenschilderwerk</a> aan je huis, dan betaal je de voorrijkosten en opstart maar één keer.</p>"),
        ],
        "tips": [
            "Overleg met de buren. Beide zijden tegelijk laten doen is goedkoper en ziet er beter uit.",
            "Laat nieuw geïmpregneerd hout eerst drogen en verweren voordat je beitst.",
            "Kies dekkende beits als je niet elk jaar opnieuw wilt. Die gaat langer mee dan transparant.",
            "Doe het zelf bij een korte schutting, en laat een schilder het tuinhuis of de lange stukken doen.",
        ],
        "btw": "De Belastingdienst rekent een tuin op hetzelfde perceel tot de woning, en noemt beitsen bij het 9%-tarief voor schilderwerk. Voor een schutting of tuinhuis bij een woning ouder dan twee jaar betaal je daardoor meestal 9%. Staat er 21% op de offerte, vraag dan waarom.",
        "bronnen": ("<p><small>Bronnen: <a href=\"https://www.bobex.be/nl-be/schilderwerken/buiten/tuinhuis/\" rel=\"nofollow noopener\">Bobex</a> (tuinhuis laten schilderen gemiddeld €30 tot €45 per m², Belgische prijzen), "
                    "<a href=\"https://slimster.nl/blog/hoe-schutting-beitsen/\" rel=\"nofollow noopener\">Slimster</a> (transparant of dekkend, aantal lagen) en "
                    "<a href=\"" + _BD_OUDER_2 + "\" rel=\"nofollow noopener\">Belastingdienst</a> (tuinen op hetzelfde perceel horen bij de woning), geraadpleegd in november 2026. "
                    "De prijs per m² voor beitsen is een eigen inschatting, geen vaste prijs van Topschilder.</small></p>"),
        "faq": [
            ("Wat kost een schutting laten beitsen?",
             "Reken op €8 tot €20 per m² per zijde, inclusief beits en btw. Een schutting van 10 meter lang en 1,80 meter hoog kost aan één kant dan €144 tot €360."),
            ("Wat kost een tuinhuis laten beitsen?",
             "Reken op €350 tot €1.200 per tuinhuis, afhankelijk van de grootte, de staat van het hout en of de deur, kozijnen en boeidelen meegaan."),
            ("Wat is beter voor een schutting: beits of verf?",
             "Voor ruw tuinhout meestal beits. Beits trekt in het hout en bladdert minder snel. Verf past beter bij geschaafd hout, zoals een tuinhuisdeur of kozijn."),
            ("Moet je een geïmpregneerde schutting beitsen?",
             "Het hoeft niet, het hout is al beschermd. Wil je een andere kleur, laat het hout dan eerst een paar maanden tot een jaar drogen en verweren. Kijk op het blik beits wat de fabrikant adviseert."),
            ("Wat kost een tuinhek schilderen?",
             "Reken op €75 tot €250 per hek, afhankelijk van de grootte en het aantal latten. Het is goedkoper als het meegaat met de schutting of het tuinhuis."),
            ("Hoe vaak moet je een schutting beitsen?",
             "Transparante beits ongeveer elke één tot twee jaar, dekkende beits elke twee tot vier jaar. Op een zonnige plek gaat het sneller."),
            ("Kan ik een vlonder beitsen?",
             "Ja, met een beits of olie die geschikt is om op te lopen. Gewone schuttingbeits slijt op een vlonder snel. Hardhout wordt meestal geolied."),
        ],
    },

    # ------------------------------------------------------------------
    # 6. Gevel reinigen en impregneren
    # ------------------------------------------------------------------
    {
        "slug": "gevel-reinigen-impregneren",
        "klus": "een gevel reinigen en impregneren",
        "kruimel": "Gevel reinigen en impregneren",
        "h1": "Wat kost een gevel reinigen en impregneren per m²?",
        "title": "Gevel reinigen en impregneren kosten 2026",
        "description": "Een gevel laten reinigen en impregneren kost €12 tot €32 per m². Alleen reinigen €5 tot €20, alleen impregneren €5 tot €15 per m². Met methodes en btw-regels.",
        "dienst": "buitenschilderwerk",
        "eenheid": "per m² gevel, reinigen en impregneren",
        "van": 12,
        "tot": 32,
        "kort": "€12 – €32 per m²",
        "intro": "Een vuile of groene gevel maakt een huis grauw. Reinigen haalt vuil, algen en mos weg, zodat de steen weer zijn eigen kleur krijgt. Impregneren is een extra stap die de steen waterafstotend maakt. Niet elke schilder doet dit werk: er zijn ook gespecialiseerde gevelreinigers met eigen apparatuur. Hieronder zie je wat het kost en wanneer impregneren zinvol is.",
        "voorbeelden": [
            ("Tussenwoning, voor- en achtergevel", 50, "Zo'n 50 m² metselwerk na aftrek van ramen en deuren."),
            ("Hoekwoning, inclusief zijgevel", 90, "Drie gevels, waarvan één zonder veel ramen."),
            ("Vrijstaande woning, rondom", 150, "Vier gevels, vaak met een hogere kopgevel."),
        ],
        "extra": [
            ("Alleen reinigen", "€5 – €20 per m², afhankelijk van de methode"),
            ("Alleen impregneren", "€5 – €15 per m²"),
            ("Reinigen, voegwerk herstellen en impregneren", "€20 – €50 per m², volgens Slimster"),
            ("Steiger of hoogwerker", "€300 – €900 per gevel; bij gevelreinigers vaak in de prijs"),
        ],
        "prijsfactoren": [
            "De methode. Stoom en lagedruk zijn het voordeligst. Chemisch reinigen en stralen kosten meer.",
            "Hoe vuil de gevel is. Dikke algen, mos, graffiti of roetaanslag vragen meer middel of meer rondes.",
            "Het soort steen. Zachte, oude baksteen vraagt een voorzichtiger methode dan harde klinkers.",
            "De hoogte en bereikbaarheid. Voor alles boven de begane grond is een hoogwerker of steiger nodig.",
            "Het oppervlak. Bij een grote gevel daalt de prijs per m².",
        ],
        "uitleg": [
            ("Wat je ervoor krijgt", "De vakman beschermt ramen, kozijnen en planten, reinigt de gevel met de gekozen methode en spoelt na. Na het drogen kan er een impregneermiddel op. Dat gaat in de steen en de voegen zitten. Je ziet het nauwelijks, maar regenwater parelt daarna van de muur af."),
            ("Schilder of gevelreiniger?", "Gevelreinigen is een vak apart. Sommige schilders doen het met een stoomreiniger of lagedruk. Voor stralen, zware vervuiling of voegwerk ben je meestal beter af bij een gespecialiseerde gevelreiniger of gevelrenovatiebedrijf. Vraag bij de offerte welke methode wordt gebruikt en of de vakman daar ervaring mee heeft."),
        ],
        "verdieping": [
            ("Welke reinigingsmethode past bij jouw gevel?",
             "<div class=\"tablewrap\"><table><thead><tr><th>Methode</th><th>Richtprijs per m²</th><th>Geschikt voor</th></tr></thead><tbody>"
             "<tr><td><strong>Lagedruk met water en reinigingsmiddel</strong></td><td>vergelijkbaar met stoom</td><td>Lichte vervuiling, algen en groene aanslag. Zacht voor de steen.</td></tr>"
             "<tr><td><strong>Stoomreinigen</strong></td><td class=\"num\">€5 – €18</td><td>De meeste bakstenen gevels. Heet water lost vuil en algen op zonder hoge druk.</td></tr>"
             "<tr><td><strong>Chemisch reinigen</strong></td><td class=\"num\">€5 – €25</td><td>Hardnekkig vuil, roet, kalkuitslag of cementsluier. Het middel moet passen bij de steen.</td></tr>"
             "<tr><td><strong>Stralen (gritstralen, nevelstralen)</strong></td><td class=\"num\">€10 – €25</td><td>Verf of zware vervuiling verwijderen. Kan zachte steen en voegen beschadigen.</td></tr>"
             "</tbody></table></div>"
             "<p>De prijzen per methode komen van Slimster en Homedeal. Een hogedrukreiniger van de bouwmarkt lijkt handig, maar kan zachte stenen en voegen uitspoelen. Een vakman kiest de laagste druk die het werk doet.</p>"),
            ("Impregneren: wel of niet?",
             "<p>Impregneren maakt de gevel waterafstotend. Het middel is dampopen: regen komt er moeilijker in, maar vocht uit de muur kan er nog uit. Dat is belangrijk, want een gevel die niet kan ademen, krijgt juist vochtproblemen.</p>"
             "<p><strong>Impregneren is zinvol</strong> als regen door de muur slaat, bij poreuze steen op de regenkant, of om een net gereinigde gevel langer schoon te houden. Een impregneerlaag gaat volgens Slimster ongeveer tien jaar mee.</p>"
             "<p><strong>Niet impregneren</strong> als de voegen kapot zijn (eerst herstellen), als er optrekkend vocht uit de grond is, of als de gevel geschilderd is met een dampdichte verf. Ook bij een gevel met scheuren lost impregneren het probleem niet op. Twijfel je, laat dan eerst de oorzaak van het vocht onderzoeken.</p>"),
            ("Reinigen, impregneren of schilderen?",
             "<p>Een schone bakstenen gevel hoeft meestal niet geschilderd te worden. Reinigen en eventueel impregneren houdt de steen zichtbaar en vraagt veel minder onderhoud. Is de gevel al eerder geschilderd, dan is reinigen vaak de eerste stap van een nieuwe schilderbeurt. Wat dat kost, zie je bij <a href=\"/kosten/gevel-schilderen/\">gevel schilderen</a>. Laat je ook het houtwerk doen, kijk dan bij <a href=\"/kosten/huis-schilderen/\">huis schilderen</a>.</p>"),
            ("Rekenvoorbeeld: een hoekwoning",
             "<p>Een hoekwoning met 90 m² bakstenen gevel. De noordkant is groen, de rest grauw. De gevel wordt met stoom gereinigd en daarna geïmpregneerd. De gevelreiniger werkt met een eigen hoogwerker.</p>"
             "<div class=\"tablewrap\"><table><thead><tr><th>Post</th><th>Richtprijs</th></tr></thead><tbody>"
             "<tr><td>Stoomreinigen, 90 m² × €5 – €15</td><td class=\"num\">€450 – €1.350</td></tr>"
             "<tr><td>Impregneren, 90 m² × €5 – €15</td><td class=\"num\">€450 – €1.350</td></tr>"
             "<tr><td><strong>Totaal</strong></td><td class=\"num\"><strong>€900 – €2.700</strong></td></tr>"
             "</tbody></table></div>"
             "<p>Moet ook het voegwerk worden hersteld, dan loopt de prijs op naar €20 tot €50 per m². Vraag op de offerte naar de methode, het middel en of de hoogwerker erbij zit. Hoe je offertes naast elkaar legt, lees je in <a href=\"/kennisbank/goede-offerte-schilderwerk/\">een goede offerte voor schilderwerk</a>.</p>"),
        ],
        "tips": [
            "Vraag welke methode wordt gebruikt. Stoom of lagedruk is voor de meeste bakstenen gevels genoeg.",
            "Laat kapotte voegen eerst herstellen. Impregneren over slechte voegen houdt het water niet tegen.",
            "Impregneer niet bij optrekkend vocht. Laat eerst de oorzaak onderzoeken.",
            "Vraag ook een gespecialiseerde gevelreiniger om een offerte. Niet elke schilder heeft de apparatuur.",
        ],
        "btw": "Let op: hier geldt meestal 21% btw. Volgens de Belastingdienst valt schoonmaken aan de buitenkant van een woning onder 21%, net als het stralen en impregneren van stenen gevels. Alleen als het reinigen voorbereiding is voor schilderwerk aan een woning ouder dan twee jaar, valt het mee onder 9%.",
        "bronnen": ("<p><small>Bronnen: <a href=\"https://slimster.nl/gevelreiniging/kosten-gevel-reinigen/\" rel=\"nofollow noopener\">Slimster gevelreiniging</a> (stoom en chemisch €5 tot €15, stralen €10 tot €20 per m²), "
                    "<a href=\"https://slimster.nl/gevelrenovatie/gevel-impregneren-kosten/\" rel=\"nofollow noopener\">Slimster impregneren</a> (impregneren €5 tot €15, met reinigen €10 tot €35 per m²), "
                    "<a href=\"https://www.homedeal.nl/gevelreiniging/gevel-reinigen/\" rel=\"nofollow noopener\">Homedeal</a> (stoomreinigen €6 tot €18, stralen €12 tot €25 per m², impregneren rond €7 per m²) en "
                    "<a href=\"" + _BD_SCHOONMAKEN + "\" rel=\"nofollow noopener\">Belastingdienst</a> (btw op schoonmaken aan de buitenkant), geraadpleegd in november 2026. "
                    "Dit zijn indicaties van die sites, geen prijzen van Topschilder.</small></p>"),
        "faq": [
            ("Wat kost gevelreiniging per m²?",
             "Alleen reinigen kost €5 tot €20 per m², afhankelijk van de methode. Stoom en lagedruk zitten aan de onderkant, stralen en chemisch reinigen aan de bovenkant."),
            ("Wat kost een gevel reinigen en impregneren?",
             "Samen €12 tot €32 per m². Voor de voor- en achtergevel van een tussenwoning, zo'n 50 m², is dat €600 tot €1.600."),
            ("Wat kost gevel impregneren?",
             "Alleen impregneren kost €5 tot €15 per m². Meestal wordt de gevel eerst gereinigd, want een impregneermiddel moet op een schone, droge muur."),
            ("Is gevel impregneren zinvol?",
             "Bij doorslaand regenwater of poreuze steen vaak wel. Bij kapotte voegen, scheuren of optrekkend vocht niet: los dan eerst die oorzaak op. Het middel moet dampopen zijn, zodat de muur kan blijven ademen."),
            ("Welke btw betaal je over gevelreiniging?",
             "Meestal 21%. De Belastingdienst noemt schoonmaken aan de buitenkant van een woning en het impregneren van stenen gevels bij het 21%-tarief. Alleen reinigen als voorbereiding op schilderwerk valt onder 9%."),
            ("Doet een schilder ook gevelreiniging?",
             "Sommige schilders wel, vooral met stoom of lagedruk. Voor stralen, zware vervuiling of voegwerk ga je meestal naar een gespecialiseerde gevelreiniger."),
            ("Hoe vaak moet een gevel gereinigd worden?",
             "Er is geen vaste termijn. Veel gevels gaan tien jaar of langer mee. Een noordgevel of een gevel onder bomen wordt sneller groen."),
        ],
    },
]

# -*- coding: utf-8 -*-
"""Kennisbank ronde 4a: vijf nieuwe artikelen in hetzelfde formaat als ARTIKELEN in kennis_artikelen.py.

Onderwerpen: nieuw stucwerk schilderen, trap verven, tegels verven, schimmel op de muur en
afbladderende verf. Technische cijfers komen uit de genoemde technische bladen en folders;
controleer die bij een update, want fabrikanten geven geregeld een nieuwe versie uit.
"""

from kennis_artikelen import TDS_MUURVERF, GGD_LOOD

# Bronnen voor deze ronde (allemaal geopend en gecontroleerd op 22 november 2026)
TDS_VOORSTRIJK = ("Sikkens, technisch blad Binnenmuurverf Voorstrijk (watergedragen voorstrijk, 27 februari 2025)",
                  "https://msp.images.akzonobel.com/prd/dh/enlkge/documents/1e/32/40/56/sikkens_binnenmuurverf_voorstrijk.pdf")
ALAB_VOORSTRIJK = ("Alabastine, productinformatie Voorstrijk Sneldrogend wit (versie 28-05-2026)",
                   "https://www.alabastine.nl/wp-content/uploads/2017/02/AB-Voorstrijk-Sneldrogend-Wit-28-05-2026.pdf")
SIGMA_FUNGI = ("Sigma, kenmerkenblad Sigmaresist Fungi Matt (schimmelbestendige muurverf, juli 2020)",
               "https://www.verf-plaza.nl/app/themes/verfplaza/assets/uploads/2022/01/Sigmaresist-Fungi-Matt.pdf")
SIGMA_TRAPLAK = ("Sigma, kenmerkenblad S2U Nova Traplak Soft-Satin (watergedragen traplak, augustus 2018)",
                 "https://data.decoprof.nl/productblad/sigma-s2u-nova-traplak-soft-satin.pdf")
SIKKENS_REZISTO = ("Sikkens, technisch blad Rubbol BL Rezisto Mat (slijtvaste binnenlak, 6 oktober 2025)",
                   "https://msp.images.akzonobel.com/prd/dh/enlexp/documents/19/05/bd/08/rubbol_bl_rezisto_mat.pdf")
ALAB_TEGELLAK = ("Alabastine, productinformatie Tegellak",
                 "https://www.alabastine.nl/wp-content/uploads/2011/01/tegellak-1-k-1.pdf")
ALAB_TEGELGROND = ("Alabastine, productinformatie Tegelgrondverf",
                   "https://www.alabastine.nl/wp-content/uploads/2011/01/Tegelgrondverf-1k1.pdf")
ALAB_TEGELGROND_2K = ("Alabastine, productinformatie Warmwaterbestendige Tegelgrondverf (2 componenten)",
                      "https://media.hornbach.nl/hb/technicaldatasheet/as.146780871.pdf")
RUSTOLEUM_TEGEL = ("Rust-Oleum Badkamer Tegelverf Matt, productinformatie bij Praxis",
                   "https://praxis.nl/verf-behang-wandbekleding/verf/binnenverf/vloer-trapverf/tegelverf/rust-oleum-badkamer-tegelverf-matt-urbangrijs-750ml/10178716")
RIVM_FOLDER = ("RIVM, folder Schimmel- en vochtproblemen in woningen (april 2015)",
               "https://www.rivm.nl/sites/default/files/2018-11/84305-008013_Schimmel%20en%20vocht%20TG2.pdf")
RIVM_BESTRIJDEN = ("RIVM, Informatie over het bestrijden van schimmels en vochtproblemen (2015)",
                   "https://www.rivm.nl/sites/default/files/2018-11/Informatie%20over%20het%20bestrijden%20van%20schimmels%20en%20vochtproblemen.pdf")
RIJKSOVERHEID_VENTILEREN = ("Rijksoverheid, Hoe kan ik mijn huis ventileren?",
                            "https://www.rijksoverheid.nl/themas/klimaat-milieu-en-natuur/duurzame-energie/vraag-en-antwoord/energie-thuis/hoe-kan-ik-mijn-huis-ventileren")
SIKKENS_1131 = ("Sikkens, Infoblad 1131 Waterdampdoorlaatbaarheid van verven voor hout (januari 2023)",
                "https://sikkens.nl/content/dam/akzonobel-painters/sikkens/nl/nl/services/informatiebladen/1131-waterdampdoorlaatbaarheid-van-verven-voor-hout.pdf")


ARTIKELEN_RONDE4A = [
# ---------------------------------------------------------------------------
{
"slug": "nieuw-stucwerk-schilderen",
"groep": "Voorbereiden en uitvoeren",
"titel": "Nieuw stucwerk schilderen: drogen, voorstrijken en sauzen",
"seo_titel": "Nieuw stucwerk schilderen: zo doe je het",
"description": "Hoe lang moet nieuw stucwerk drogen, moet je voorstrijken en hoe saus je het zonder vlekken? Met droogtest, stappenplan en een rekenvoorbeeld in liters en euro.",
"kort": "Hoe lang nieuw stucwerk moet drogen, wanneer voorstrijken nodig is en hoe je het egaal saust.",
"foto": "kwast-tegen-lichte-muur",
"intro": "Een vers gestucte muur is mooi glad, maar je kunt er niet meteen verf op zetten. Het stucwerk zit nog vol water en het zuigt verf op als een spons. Wie te vroeg begint of de voorstrijk overslaat, krijgt vlekken, aanzetten of verf die later loslaat. Hier lees je hoe lang je moet wachten, wanneer voorstrijken nodig is en hoe je de muur in één keer goed krijgt.",
"kort_antwoord": "Nieuw stucwerk moet helemaal droog zijn voordat je gaat schilderen: overal even licht van kleur, zonder donkere plekken. Daarna breng je een voorstrijk aan, zodat de muur overal even sterk zuigt. Pas als die droog is, saus je de muur met twee lagen muurverf. Met de watertest zie je of voorstrijken echt nodig is.",
"secties": [
("Waarom nieuw stucwerk anders is",
"""<p>Stucwerk wordt nat aangebracht. Na het stucen moet al dat water er weer uit. Zolang dat niet gebeurd is, kan de verf niet goed hechten. Het vocht wil naar buiten en duwt tegen de verflaag. Dat zie je later terug als blaasjes, vlekken of verf die loslaat.</p>
<p>Daarnaast zuigt droog, kaal stucwerk sterk. De eerste laag muurverf trekt dan meteen de muur in. Op de ene plek meer dan op de andere. Het gevolg: matte en glanzende plekken, en randen waar je met de roller hebt aangezet. Een voorstrijk lost dat op. Die dringt in de ondergrond, vermindert de zuiging en zorgt dat de muurverf er gelijkmatig op komt te liggen.</p>
<p>Schilder je liever niet zelf? Op de pagina over <a href="/schilderwerk/binnenschilderwerk/">binnenschilderwerk</a> lees je wat een schilder voor je doet en wat het kost.</p>"""),
("Hoe lang moet nieuw stucwerk drogen?",
"""<p>Daar is geen vast getal voor. De droogtijd hangt af van hoe dik het stucwerk is, hoe warm het is, hoeveel er wordt geventileerd en of de muur eronder ook nat was. Een dunne laag op gipsplaat is veel sneller droog dan een dikke laag op een nieuwe stenen muur. Reken bij nieuwbouw en grote verbouwingen daarom eerder in weken dan in dagen.</p>
<p>Hoe weet je dan wanneer het kan? Kijk naar de kleur. Nat stucwerk is donkergrijs of roze. Droog stucwerk is overal even licht. Zie je nog donkere vlekken of randen, vaak in hoeken en achter radiatoren, dan is de muur nog niet klaar. Wil je het zeker weten, gebruik dan een vochtmeter. Het kenmerkenblad van een schimmelbestendige muurverf noemt als eis voor gipsgebonden ondergronden een vochtpercentage van maximaal 1%.</p>
<p>Help het drogen door goed te ventileren en de ruimte normaal te verwarmen. Zet geen bouwdroger of heater vlak voor de muur. Te snel drogen geeft een grotere kans op scheurtjes.</p>"""),
("Voorstrijken: ja of nee?",
"""<p>Op nieuw stucwerk is een voorstrijk bijna altijd nodig. Je kunt het testen met de watertest uit de productinformatie van een voorstrijkmiddel: maak de muur op een paar plekken vochtig met een spons of plantenspuit. Wordt het water vrijwel meteen opgenomen, dan zuigt de muur sterk en moet je voorstrijken. Blijft het water even staan, dan is de zuiging laag.</p>
<p>Wat zeggen de technische bladen?</p>
<ul>
<li>Een watergedragen voorstrijk van een grote fabrikant is geschikt voor zuigende muren en plafonds, waaronder (glad) pleisterwerk en gipskarton. Op een onbehandelde zuigende ondergrond verdun je hem volgens het blad met 10% water. Hij dekt ongeveer 12 m² per liter.</li>
<li>Een sneldrogende voorstrijk van een ander merk noemt stucwerk, spack, gipsplaten en nieuwbouwmuren als toepassing. Volgens de productinformatie is 2,5 liter genoeg voor ongeveer 25 m², en zeer sterk zuigende muren behandel je twee keer.</li>
</ul>
<p>Het verschil tussen een witte en een transparante voorstrijk: een witte voorstrijk dekt al wat en helpt als je een lichte kleur op een donkere ondergrond zet. Transparant is prima als je de muur toch wit maakt.</p>"""),
("Hoe lang moet de voorstrijk drogen?",
"""<p>Ook dat staat op het blik. Twee voorbeelden uit technische bladen:</p>
<div class="tablewrap"><table>
<thead><tr><th>Product</th><th>Overschilderbaar na</th><th>Verwerken tussen</th></tr></thead>
<tbody>
<tr><td>Watergedragen voorstrijk (merk A)</td><td>4 uur bij 20 °C, 8 uur bij 10 °C</td><td>10 °C en 30 °C</td></tr>
<tr><td>Sneldrogende voorstrijk (merk B)</td><td>3 uur bij 20 °C</td><td>niet onder 10 °C</td></tr>
</tbody></table></div>
<p>Hoe kouder het is en hoe dikker de laag, hoe langer het duurt. Werk dus niet in een onverwarmde ruimte in de winter. Voorkom ook druipers: die blijven volgens de fabrikant zichtbaar door de muurverf heen.</p>"""),
("Sauzen: welke muurverf en hoeveel lagen?",
"""<p>Op nieuw stucwerk gebruik je een gewone watergedragen muurverf, mat of zijdemat. Die laat waterdamp door, en dat is goed op een muur die nog wat restvocht kan hebben. Het technische blad van een matte muurverf noemt een rendement van ongeveer 11 m² per liter en verwerking tussen 10 °C en 30 °C. Bij 20 °C kun je na 5 uur de tweede laag zetten. Reken op twee lagen na de voorstrijk.</p>
<p>Werk nat-in-nat en stop niet midden in een muur. Hoe je strepen voorkomt, lees je in <a href="/kennisbank/plafond-schilderen-zonder-strepen/">plafond schilderen zonder strepen</a>. Twijfel je tussen latex en muurverf: in <a href="/kennisbank/latex-of-muurverf/">latex of muurverf</a> staat het verschil. Is het huis nog leeg, dan is spuiten een optie. Een schilder kan muren en plafonds dan in één keer latex spuiten.</p>"""),
("Rekenvoorbeeld: zelf doen of laten doen",
"""<p>Stel: je hebt een nieuwe woonkamer van 4 bij 5 meter, 2,60 meter hoog. De muren zijn samen ongeveer 47 m². Na aftrek van een raam en een deur blijft er zo'n 40 m² muur over. Met het plafond erbij kom je op ongeveer <strong>60 m²</strong>.</p>
<div class="tablewrap"><table>
<thead><tr><th>Zelf doen</th><th>Hoeveel</th><th>Ongeveer</th></tr></thead>
<tbody>
<tr><td>Voorstrijk, 1 laag (ca. 12 m² per liter)</td><td>5 liter: 2 blikken van 2,5 liter</td><td>€40 tot €60</td></tr>
<tr><td>Muurverf, 2 lagen (ca. 11 m² per liter, 120 m² totaal)</td><td>11 liter: 10 liter plus 2,5 liter</td><td>€90 tot €160</td></tr>
<tr><td>Roller, kwast, verfbak, tape, stucloper</td><td></td><td>€30 tot €50</td></tr>
<tr><td><strong>Totaal materiaal</strong></td><td></td><td><strong>€160 tot €270</strong></td></tr>
</tbody></table></div>
<p>Daar komt je eigen tijd bij: afplakken, voorstrijken, twee lagen sauzen en opruimen. Voor de meeste mensen is dat twee tot drie dagen, inclusief droogtijd.</p>
<p><strong>Laten doen:</strong> met onze richtprijs van €10 tot €22 per m², inclusief materiaal en btw, kost 60 m² ongeveer <strong>€600 tot €1.320</strong>. Een leeg huis met veel vierkante meters wordt met spuiten vaak goedkoper per m². Prijzen van materiaal zijn indicaties van bouwmarkten en wisselen. Wil je zelf rekenen, gebruik dan de <a href="/kosten/calculator/">kostencalculator</a>.</p>"""),
],
"stappen": [
("Controleer of het stucwerk droog is", "Kijk of de muur overal even licht van kleur is, zonder donkere plekken in hoeken of achter de radiator. Gebruik bij twijfel een vochtmeter."),
("Schuur en maak stofvrij", "Schuur bramen en spatten weg met fijn schuurpapier of een schuurgaas, en neem het stof af met een droge borstel of stofzuiger."),
("Doe de watertest", "Maak een paar plekken vochtig met een spons. Trekt het water meteen in, dan moet je voorstrijken."),
("Breng de voorstrijk aan", "Rol of kwast de voorstrijk gelijkmatig op de muur, verdund als het blik dat voorschrijft. Voorkom druipers en laat hem drogen volgens het blik."),
("Plak af en zet de randen", "Plak plinten, kozijnen en het plafond af. Zet de hoeken en randen met een kwast, per muur vlak voordat je gaat rollen."),
("Saus twee lagen muurverf", "Rol nat-in-nat in banen. Laat de eerste laag drogen volgens het blik en zet dan de tweede laag op dezelfde manier."),
],
"kosten": ["schilderen-per-m2", "latex-spuiten"],
"dienst": "binnenschilderwerk",
"faq": [
("Hoe lang moet nieuw stucwerk drogen voor je kunt schilderen?", "Er is geen vaste termijn. Het hangt af van de dikte, de temperatuur en de ventilatie. Begin pas als de muur overal even licht van kleur is. Een vochtmeter geeft zekerheid; een fabrikant van muurverf noemt maximaal 1% vocht voor gipsgebonden ondergronden."),
("Is voorstrijken echt nodig op nieuw stucwerk?", "Bijna altijd. Kaal stucwerk zuigt sterk en ongelijk. Doe de watertest: trekt water meteen in de muur, dan heb je een voorstrijk nodig."),
("Kan ik muurverf verdunnen in plaats van voorstrijken?", "Dat wordt vaak gedaan, maar de technische bladen schrijven een voorstrijk voor. Die is gemaakt om in de ondergrond te dringen en de zuiging te verminderen. Verdunde muurverf doet dat minder goed."),
("Hoeveel lagen muurverf heeft nieuw stucwerk nodig?", "Na de voorstrijk meestal twee lagen. Bij een donkere kleur soms een derde."),
("Wat gebeurt er als ik te vroeg schilder?", "Het vocht in het stucwerk kan niet goed weg. Je kunt vlekken, blaasjes of loslatende verf krijgen. Wacht daarom tot de muur echt droog is."),
("Wat is het verschil tussen witte en transparante voorstrijk?", "Een witte voorstrijk dekt al een beetje en helpt bij een lichte kleur op een donkere ondergrond. Een transparante voorstrijk vermindert alleen de zuiging."),
],
"bronnen": [TDS_VOORSTRIJK, ALAB_VOORSTRIJK, TDS_MUURVERF, SIGMA_FUNGI],
"gerelateerd": ["latex-of-muurverf", "plafond-schilderen-zonder-strepen", "behang-verwijderen"],
},
# ---------------------------------------------------------------------------
{
"slug": "trap-verven",
"groep": "Verf kiezen",
"titel": "Trap verven of lakken: welke verf en hoe pak je het aan?",
"seo_titel": "Trap verven: welke verf en hoe doe je het?",
"description": "Welke verf gebruik je voor een trap, hoe lak je om-en-om zodat je de trap blijft gebruiken en hoe schilder je het trapgat? Met stappenplan en rekenvoorbeeld.",
"kort": "Traplak kiezen, slijtvastheid, om-en-om werken en het trapgat schilderen.",
"foto": "nederlandse-woonkamer-klassiek-interieur",
"intro": "Een trap krijgt het zwaar. Iedereen loopt er elke dag op, met schoenen, op sokken, met een wasmand. Gewone lakverf slijt daar snel door, en een glanzende trap kan glad worden. Daarom bestaan er speciale traplakken. Hier lees je welke verf je kiest, hoe je de trap schildert terwijl je hem blijft gebruiken en hoe je het trapgat aanpakt.",
"kort_antwoord": "Een houten trap verf je met een slijtvaste, watergedragen traplak, bij voorkeur met antislip. Op kaal hout gaat er eerst een grondverf onder. Werk om-en-om: eerst de oneven treden, dan de even treden, zodat je de trap kunt blijven gebruiken. Het trapgat schilder je met een goed afneembare muurverf, vaak vanaf een speciale trapsteiger.",
"secties": [
("Welke verf voor een trap?",
"""<p>Voor de treden heb je een lak nodig die tegen slijtage kan en niet glad wordt. Een traplak is daarvoor gemaakt. Het kenmerkenblad van een watergedragen traplak beschrijft het product als lakverf voor trappen binnen op basis van polyurethaan-acrylaat. Het noemt onder meer antislip, kras- en slijtvast, bestand tegen vetten, vuil en huishoudelijke schoonmaakmiddelen, en niet vergelend.</p>
<p>Je kunt ook kiezen voor een extreem slijtvaste binnenlak die niet speciaal voor trappen is gemaakt. Het technische blad van zo'n matte lak adviseert om op plekken met veel mechanische belasting of huidcontact twee lagen aan te brengen. Let op: zo'n lak heeft geen antislip. Op treden waar je op sokken loopt is een traplak met antislip de veiligere keuze.</p>
<p>Kies binnen voor watergedragen lak. Die ruikt weinig, droogt snel en vergeelt niet. Meer daarover in <a href="/kennisbank/verf-op-waterbasis-of-terpentinebasis/">verf op waterbasis of terpentinebasis</a>.</p>"""),
("Glans en kleur",
"""<p>Hoe lager de glans, hoe minder je krasjes en vuil ziet. Een zijdeglans of zijdemat is voor treden vaak het prettigst. Hoogglans ziet er strak uit, maar laat elke kras zien en voelt eerder glad aan.</p>
<p>Donkere kleuren zijn populair, bijvoorbeeld een antraciet trap met witte stootborden. Het kenmerkenblad van een traplak waarschuwt dat bij donkere kleuren door gebruik een lichte aftekening kan ontstaan. Je ziet dan na een tijd lichtere looppaden. Een middentint verbergt dat het best. Twijfel je over de kleur, kijk dan in de <a href="/kleuren-kiezen/">kleurenkiezer</a>.</p>"""),
("Voorbereiden: reinigen, schuren, gronden",
"""<p>Lak hecht alleen goed op een schone, geschuurde ondergrond. Het kenmerkenblad van een traplak geeft per situatie een systeem:</p>
<div class="tablewrap"><table>
<thead><tr><th>Situatie</th><th>Opbouw volgens het blad</th></tr></thead>
<tbody>
<tr><td>Trap al eerder geschilderd</td><td>Grondig reinigen en zorgvuldig schuren, kale delen bijwerken met primer, daarna voorlakken en aflakken met traplak</td></tr>
<tr><td>Kale of kaalgemaakte trap</td><td>Zorgvuldig schuren, alles gronden met primer, voorlakken en aflakken met traplak</td></tr>
<tr><td>Fabrieksmatig behandelde trap</td><td>Reinigen en schuren, voorlakken en aflakken met traplak</td></tr>
</tbody></table></div>
<p>Ontvet de treden goed. Op een trap zit veel huidvet en vuil van schoenen. Schuur daarna en maak alles stofvrij. Kale plekken krijgen grondverf. Wat het verschil is tussen grondverf en voorlak, lees je in <a href="/kennisbank/grondverf-of-voorlak/">grondverf of voorlak</a>.</p>"""),
("Om-en-om lakken: de trap blijft bruikbaar",
"""<p>Het grootste probleem bij een trap: je moet er ook op lopen. De oplossing is om-en-om werken. Je lakt eerst trede 1, 3, 5 en zo verder. Als die droog zijn, doe je trede 2, 4, 6. Zo kun je de trap steeds gebruiken door alleen op de droge treden te stappen. Markeer de natte treden met een stukje tape aan de zijkant.</p>
<p>Hoe lang moet je wachten? Het kenmerkenblad van een traplak noemt bij 23 °C en 50% luchtvochtigheid: stofdroog na ongeveer 1 uur, kleefvrij na 3 uur en overschilderbaar na 5 uur. Op één dag kun je dus meerdere lagen zetten. Volgens hetzelfde blad moet de temperatuur boven 7 °C liggen en de luchtvochtigheid tussen 60% en 85%. De antislipkorrels kunnen na het drogen deels los op het oppervlak liggen; na 24 uur kun je die met een vochtige doek weghalen.</p>
<p>Wees de eerste weken voorzichtig. Het technische blad van een slijtvaste lak zegt dat de verf pas na volledige doorharding, na een maand, eenvoudig te reinigen is. Gebruik in die tijd geen agressieve schoonmaakmiddelen.</p>"""),
("Het trapgat schilderen",
"""<p>Het trapgat is de hoge ruimte boven de trap. De muren daar zijn lastig te bereiken. Je hebt een trapladder of een trapsteiger nodig waarvan één kant korter is, zodat hij stabiel op de treden staat. Ga nooit op een gewone ladder op de trap staan.</p>
<p>Voor de muren gebruik je een muurverf die goed afneembaar is, want in een trapgat komen handen en tassen langs de muur. Een zijdematte muurverf met een goede schrobklasse is praktisch. Werk ook hier nat-in-nat in banen van boven naar beneden. Volgens het technische blad van een matte muurverf mag je niet verwerken onder 10 °C of boven 30 °C, en is de tweede laag bij 20 °C na 5 uur mogelijk.</p>
<p>Schilder eerst het trapgat en pas daarna de trap. Dan vallen spetters niet op je verse lak.</p>"""),
("Rekenvoorbeeld: zelf doen of laten doen",
"""<p>Neem een gewone dichte trap met 13 treden van 80 centimeter breed. Per trede schilder je de bovenkant (ca. 0,20 m²) en het stootbord (ca. 0,15 m²). Met de trapbomen erbij kom je op ongeveer <strong>7 m²</strong> lakwerk.</p>
<div class="tablewrap"><table>
<thead><tr><th>Zelf doen</th><th>Hoeveel</th><th>Ongeveer</th></tr></thead>
<tbody>
<tr><td>Primer voor kale plekken</td><td>1 liter</td><td>€25 tot €40</td></tr>
<tr><td>Traplak, voorlak plus aflak (ca. 10 m² per liter per laag)</td><td>1,4 liter: 1 blik van 2,5 liter</td><td>€60 tot €100</td></tr>
<tr><td>Ontvetter, schuurpapier, tape, lakroller en kwast</td><td></td><td>€30 tot €50</td></tr>
<tr><td><strong>Totaal materiaal</strong></td><td></td><td><strong>€115 tot €190</strong></td></tr>
</tbody></table></div>
<p>De tijd is het echte werk. Schuren en reinigen kost al snel een dag. Daarna lak je om-en-om: elke laag in twee rondes. Met grondverf, voorlak en aflak zijn dat zes rondes. Reken met droogtijden op drie tot vier dagen.</p>
<p><strong>Laten doen:</strong> onze richtprijs voor een trap is €350 tot €950 per verdieping, inclusief materiaal en btw. Het verschil zit in de staat van de trap, open of dichte treden, en of de trap helemaal kaal moet. Het trapgat komt daar los bij: met €10 tot €22 per m² kost 25 m² muur ongeveer €250 tot €550, en door de hoogte vaak aan de bovenkant van die marge.</p>"""),
],
"stappen": [
("Maak de trap leeg en schoon", "Haal traplopers en spijkers weg, zuig de trap af en ontvet alle treden en stootborden grondig."),
("Schuur alles op", "Schuur de oude lak mat met fijn schuurpapier, en kale of beschadigde plekken eerst iets grover. Maak de trap daarna stofvrij."),
("Plak af", "Plak de muren langs de trap en de leuning af, en markeer welke treden je in de eerste ronde doet."),
("Grond kale plekken", "Breng primer aan op kale delen. Werk om-en-om: eerst de oneven treden, na het drogen de even treden."),
("Voorlakken", "Zet een laag traplak op alle treden, weer om-en-om. Schuur licht tussen de lagen als het blik dat voorschrijft."),
("Aflakken en laten uitharden", "Lak af in dezelfde volgorde. Loop de eerste dagen voorzichtig en gebruik de eerste maand alleen een zacht schoonmaakmiddel."),
],
"kosten": ["trap-schilderen"],
"dienst": "binnenschilderwerk",
"faq": [
("Welke verf is het best voor een trap?", "Een watergedragen traplak met antislip. Die is kras- en slijtvast, vergeelt niet en wordt minder glad dan gewone lak."),
("Moet je een trap schuren voor het verven?", "Ja. Reinig en schuur de oude lak, anders hecht de nieuwe laag slecht. Kale plekken krijgen eerst een primer."),
("Hoe kun je een trap verven en toch gebruiken?", "Werk om-en-om. Lak eerst de oneven treden en, als die droog zijn, de even treden. Zo kun je steeds op droge treden lopen."),
("Hoe lang moet traplak drogen?", "Een traplak uit een kenmerkenblad is na ongeveer 5 uur overschilderbaar bij 23 °C. Volledig hard is de lak pas na enkele weken; wees de eerste tijd voorzichtig."),
("Kan ik muurverf op mijn trap gebruiken?", "Niet op de treden: muurverf is daar niet slijtvast genoeg. Voor de muren van het trapgat gebruik je wel muurverf, liefst een goed afneembare."),
("Hoeveel lagen traplak heb je nodig?", "Op een eerder geschilderde trap meestal een voorlak en een aflak. Op kaal hout eerst een grondverf en dan twee lagen traplak."),
],
"bronnen": [SIGMA_TRAPLAK, SIKKENS_REZISTO, TDS_MUURVERF],
"gerelateerd": ["grondverf-of-voorlak", "verf-op-waterbasis-of-terpentinebasis", "latex-of-muurverf"],
},
# ---------------------------------------------------------------------------
{
"slug": "tegels-verven",
"groep": "Voorbereiden en uitvoeren",
"titel": "Tegels verven: wat kan wel en wat niet?",
"seo_titel": "Tegels verven: welke verf en hoelang mee?",
"description": "Kun je tegels verven in badkamer of keuken? Welke tegelverf je nodig hebt, waarom de douche lastig is en wat je met voegen en kit doet. Met rekenvoorbeeld.",
"kort": "Tegelverf en 2K-systemen, de voegen en kit, en eerlijk over de douche en natte zones.",
"foto": "muur-afplakken-en-verven-gele-kleur",
"intro": "Oude tegels in de badkamer of keuken eruit slopen is veel werk en geeft veel rommel. Verven lijkt dan een slimme oplossing. Het kan ook, maar niet overal even goed. Op een tegelwand naast de wastafel houdt verf het veel langer dan in de douche. Hier lees je welke verf je nodig hebt, hoe je het aanpakt en waar je beter niet aan begint.",
"kort_antwoord": "Tegels kun je verven met een speciale tegelgrondverf en tegellak, of met een tegelverf met activator. Gewone muurverf of lak hecht niet goed op glad keramiek. Buiten de douche werkt het goed. In de douche en rond het bad heb je een tweecomponentensysteem nodig dat daarvoor geschikt is, en ook dan gaat het minder lang mee dan nieuwe tegels. Kit moet eraf, want tegelverf hecht er niet op.",
"secties": [
("Kan je tegels gewoon verven?",
"""<p>Tegels zijn glad en hard. Gewone muurverf of lakverf houdt zich daar slecht aan vast. Daarom bestaan er systemen die speciaal voor tegels zijn gemaakt. Er zijn grofweg drie soorten:</p>
<ul>
<li><strong>Tegelgrondverf met tegellak.</strong> Eerst een hechtlaag, daarna een lak. De productinformatie van zo'n grondverf noemt hem bedoeld voor optimale hechting op gladde tegelondergronden.</li>
<li><strong>Tegelverf met activator.</strong> Een verf waarin je vlak voor gebruik een tweede component mengt. De productinformatie van zo'n badkamertegelverf zegt dat de activator zorgt voor een verhoogde duurzaamheid.</li>
<li><strong>Tweecomponenten grondverf en lak voor natte zones.</strong> Een zwaarder systeem dat volgens de fabrikant ook geschikt is voor tegels in de douche, rond het bad en achter het fornuis.</li>
</ul>
<p>Welke je kiest, hangt vooral af van waar de tegels zitten en hoeveel water erop komt.</p>"""),
("Eerlijk over de douche en natte zones",
"""<p>Hier gaat het vaak mis. Niet elke tegelverf kan tegen water dat er dagelijks overheen loopt. Kijk goed op het blik:</p>
<ul>
<li>De productinformatie van een gewone tegellak (één component) zegt letterlijk dat hij niet geschikt is voor het overschilderen van tegels en voegen in de douche en rondom de badkuip.</li>
<li>Een badkamertegelverf met activator wordt omschreven als waterbestendig tegen druppels en spatten. Dat is iets anders dan een douchewand waar je elke dag onder staat.</li>
<li>Alleen de tweecomponenten grondverf voor natte zones noemt de douche en het bad wel als toepassing.</li>
</ul>
<p>Ook met het goede product blijft een geverfde douchewand kwetsbaar. Warm water, zeep, kalk en schoonmaakmiddelen werken er dagelijks op in. Krassen van een douchewisser of schuursponsje maken de laag sneller kapot. Verwacht dus niet dat het net zo lang meegaat als nieuwe tegels. Zie het als een tijdelijke opknapbeurt voor de douche, en als een duurzamere oplossing voor de rest van de badkamer, het toilet of de keukenwand.</p>
<p>Zit er schimmel in de voegen? Dan is er vaak te veel vocht in de ruimte. Verf lost dat niet op. Lees eerst <a href="/kennisbank/schimmel-op-muur/">schimmel op de muur</a>.</p>"""),
("Voegen en kit",
"""<p>De voegen verf je gewoon mee. Je ziet ze daarna nog wel als lijntjes, maar ze hebben dezelfde kleur als de tegels. Wil je de voegen een andere kleur geven, dan kan dat met een voegenpen nadat de tegelverf droog is. Maak de voegen eerst goed schoon: de productinformatie van een tegelgrondverf adviseert een voegenreiniger en schimmels en zwarte aanslag te verwijderen met chloor of soda. Beschadigde voegen en afgebroken randjes repareer je eerst.</p>
<p>Kit is een ander verhaal. Volgens dezelfde productinformatie hechten tegelgrondverf en tegellak niet op kit. Snijd de oude kit er dus uit, verwijder de resten, verf de tegels en zet daarna een nieuwe kitrand.</p>"""),
("Voorbereiden is het halve werk",
"""<p>De hechting van tegelverf staat of valt met een schone, vetvrije ondergrond. Volgens de productinformatie van een tegelgrondverf:</p>
<ul class="checklist">
<li>de ondergrond moet schoon, droog, stof- en vetvrij zijn;</li>
<li>kalkaanslag verwijder je met een krachtige tegelreiniger;</li>
<li>loszittende delen haal je weg, gaten en scheuren vul je eerst;</li>
<li>alles wat je niet wilt verven, plak je zorgvuldig af.</li>
</ul>
<p>Veel schilders schuren de tegels ook licht op met fijn schuurpapier of een schuurspons, zodat de glazuurlaag iets ruwer wordt. Was daarna na en laat alles goed drogen. Verf niet als de badkamer nog nat is van het douchen.</p>"""),
("Verwerken en droogtijden",
"""<p>Breng tegelverf aan met een lakviltroller voor de vlakken en een kwast voor voegen en hoeken. De grondverf moet volgens de productinformatie zo dun mogelijk worden aangebracht, doorschijnend over tegels en voegen. Een dunne hechtlaag geeft een betere hechting van de laag erop.</p>
<div class="tablewrap"><table>
<thead><tr><th>Product (uit productinformatie)</th><th>Rendement</th><th>Droogtijd</th></tr></thead>
<tbody>
<tr><td>Tegelgrondverf, één component</td><td>ca. 18 m² per liter</td><td>overschilderbaar na 15 uur</td></tr>
<tr><td>Tegellak, één component</td><td>ca. 10 m² per liter</td><td>overschilderbaar na 24 uur</td></tr>
<tr><td>Tegelgrondverf, twee componenten</td><td>ca. 24 m² per 750 ml</td><td>overschilderbaar na minimaal 16 en maximaal 72 uur</td></tr>
<tr><td>Badkamertegelverf met activator</td><td>ca. 14 m² per liter</td><td>handdroog binnen 1 uur, overschilderbaar binnen 4 uur</td></tr>
</tbody></table></div>
<p>Bij een tweecomponentenproduct moet je na het mengen snel werken. De productinformatie van de 2K-grondverf noemt een maximale verwerkingstijd van 2 uur bij 20 °C. Ventileer goed tijdens en na het werk. Gebruik de douche pas weer als de fabrikant aangeeft dat de laag volledig is uitgehard.</p>"""),
("Rekenvoorbeeld: zelf doen of laten doen",
"""<p>Stel: je badkamer heeft ongeveer <strong>14 m² wandtegels</strong> buiten de douche. Je kiest een badkamertegelverf met activator en zet twee lagen.</p>
<div class="tablewrap"><table>
<thead><tr><th>Zelf doen</th><th>Hoeveel</th><th>Ongeveer</th></tr></thead>
<tbody>
<tr><td>Tegelverf, 2 lagen (ca. 14 m² per liter, 28 m² totaal)</td><td>2 liter: 3 blikken van 750 ml</td><td>€90 tot €130</td></tr>
<tr><td>Tegelreiniger, voegenreiniger, schuurspons</td><td></td><td>€20 tot €30</td></tr>
<tr><td>Lakroller, kwast, tape, nieuwe sanitairkit</td><td></td><td>€25 tot €40</td></tr>
<tr><td><strong>Totaal materiaal</strong></td><td></td><td><strong>€135 tot €200</strong></td></tr>
</tbody></table></div>
<p>Reken op een dag voorbereiden en twee dagen verven en drogen. De badkamer is in die tijd niet te gebruiken.</p>
<p><strong>Laten doen:</strong> tegels verven is precisiewerk, en veel schilders rekenen het per uur. Met onze richtprijs van €45 tot €65 per uur exclusief btw en zo'n 12 tot 16 uur werk kom je op ongeveer €540 tot €1.040 exclusief btw. Voor schilderwerk aan een woning die ouder is dan twee jaar geldt 9% btw, zie <a href="/gids/btw-schilderwerk/">btw op schilderwerk</a>. Vraag bij een offerte altijd welk systeem de schilder gebruikt en of de douche daarvoor geschikt is. Een schilder die je eerlijk zegt dat de douche beter opnieuw betegeld kan worden, helpt je meer dan een die alles belooft.</p>"""),
],
"stappen": [
("Bepaal waar je verft", "Buiten de douche volstaat vaak een tegelverf of tegelgrondverf met lak. In de douche en rond het bad alleen een systeem dat daar volgens het blik geschikt voor is."),
("Verwijder de kit", "Snijd alle kitranden eruit en verwijder de resten, want tegelverf hecht niet op kit."),
("Reinig en ontvet grondig", "Verwijder kalk, vet, zeepresten en schimmel van tegels en voegen met een tegelreiniger en voegenreiniger. Spoel na en laat alles drogen."),
("Schuur licht en plak af", "Mat de tegels licht op met een schuurspons, neem het stof af en plak kranen, randen en wat niet geverfd wordt af."),
("Breng grondverf of de eerste laag aan", "Zet eerst de voegen en hoeken met een kwast en rol daarna de vlakken met een lakviltroller. Houd een grondverf dun."),
("Zet de tweede laag en kit opnieuw", "Laat drogen volgens het blik, breng de volgende laag aan en zet pas een nieuwe kitrand als alles goed droog is."),
],
"kosten": ["schilderen-per-m2"],
"dienst": "binnenschilderwerk",
"faq": [
("Kun je tegels in de douche verven?", "Alleen met een systeem dat de fabrikant daarvoor geschikt noemt, zoals een tweecomponenten grondverf en lak voor natte zones. Gewone tegellak is volgens de fabrikant niet geschikt voor de douche en rond het bad. Ook met het goede product gaat het minder lang mee dan nieuwe tegels."),
("Welke verf gebruik je voor tegels?", "Een tegelgrondverf met tegellak, of een tegelverf met activator. Gewone muurverf of lakverf hecht slecht op glad keramiek."),
("Moet je de voegen meeverven?", "Ja, die verf je mee in dezelfde kleur. Een andere kleur voor de voegen kan daarna met een voegenpen."),
("Kun je over siliconenkit heen verven?", "Nee. Tegelverf hecht niet op kit. Verwijder de kit voor het verven en zet daarna een nieuwe kitrand."),
("Hoe lang gaat geverfde tegel mee?", "Dat hangt af van de plek en de voorbereiding. Op een droge wand gaat het veel langer mee dan in de douche. Krassen en agressieve schoonmaakmiddelen verkorten de levensduur."),
("Kun je vloertegels verven?", "Er zijn producten die dat noemen, zoals een tweecomponenten tegelgrondverf. Een vloer slijt wel veel sneller dan een wand. Kies dan een systeem dat uitdrukkelijk voor vloeren bedoeld is."),
],
"bronnen": [ALAB_TEGELLAK, ALAB_TEGELGROND, ALAB_TEGELGROND_2K, RUSTOLEUM_TEGEL],
"gerelateerd": ["schimmel-op-muur", "latex-of-muurverf", "goede-offerte-schilderwerk"],
},
# ---------------------------------------------------------------------------
{
"slug": "schimmel-op-muur",
"groep": "Schade en onderhoud",
"titel": "Schimmel op de muur: oorzaak, verwijderen en schilderen",
"seo_titel": "Schimmel op de muur: oorzaak en aanpak",
"description": "Zwarte plekken op muur of plafond? Zo vind je de oorzaak, verwijder je schimmel veilig en kies je de juiste verf. Waarom schimmelwerende verf vocht niet oplost.",
"kort": "Eerst de oorzaak, dan schoonmaken en pas daarna schilderen, en wat schimmelwerende verf wel en niet doet.",
"foto": "nederlandse-kamer-balkenplafond-zwartwit",
"intro": "Zwarte puntjes in de hoek van de slaapkamer, een grijze waas op het badkamerplafond of vlekken achter de kast. Schimmel op de muur is vervelend en kan klachten geven. De eerste reactie is vaak: er een laag schimmelwerende verf overheen. Maar zolang het vocht blijft, komt de schimmel terug. Hier lees je hoe je de oorzaak vindt, hoe je schimmel verwijdert en wanneer schilderen zin heeft.",
"kort_antwoord": "Schimmel groeit waar het te vochtig is. Zoek daarom eerst de oorzaak: te weinig ventilatie, een koude plek in de muur (koudebrug) of een lekkage. Los die op. Verwijder daarna de schimmel van gladde oppervlakken met een doek en soda in heet water. Pas als de muur droog en schoon is, schilder je, eventueel met schimmelbestendige muurverf. Die verf helpt, maar lost een vochtprobleem niet op.",
"secties": [
("Waar komt schimmel vandaan?",
"""<p>Schimmelsporen zitten overal in de lucht. Ze gaan pas groeien als ze op een plek komen waar genoeg vocht is. Volgens een folder van het RIVM zijn er twee hoofdoorzaken:</p>
<ul>
<li><strong>Bouwtechnisch:</strong> bouwvocht, optrekkend vocht, condensatie op niet-geïsoleerde buitenmuren of enkel glas, een vochtige kruipruimte, regendoorslag en lekkages.</li>
<li><strong>Bewonersgedrag:</strong> door douchen, koken, was drogen, schoonmaken en afwassen komt er waterdamp vrij.</li>
</ul>
<p>Dezelfde folder noemt een luchtvochtigheid tussen 30% en 70% als goed. Te veel vocht merk je aan een muffe lucht, vochtplekken, loslatend behang, schimmelplekken, rottend hout en condens op de ramen.</p>"""),
("Ventilatie, koudebrug of lekkage?",
"""<p>Het patroon van de schimmel vertelt vaak wat er aan de hand is:</p>
<div class="tablewrap"><table>
<thead><tr><th>Wat je ziet</th><th>Waarschijnlijke oorzaak</th><th>Wat je doet</th></tr></thead>
<tbody>
<tr><td>Grijze waas op het badkamerplafond, schimmel in kitvoegen</td><td>Te weinig ventilatie na het douchen</td><td>Raam of rooster open, afzuiging aan, douche drogen</td></tr>
<tr><td>Schimmel in hoeken van buitenmuren, achter kasten, rond kozijnen</td><td>Koude plek in de muur (koudebrug) waarop vocht condenseert</td><td>Meubels van de buitenmuur af, beter verwarmen en ventileren, isolatie laten bekijken</td></tr>
<tr><td>Vochtplek die groter wordt, vaak met een rand</td><td>Lekkage, regendoorslag of een kapotte goot</td><td>Eerst de lekkage laten repareren</td></tr>
<tr><td>Vocht en zoutuitbloei onderaan de muur</td><td>Optrekkend vocht</td><td>Een specialist laten kijken</td></tr>
</tbody></table></div>
<p>Het RIVM schrijft in een informatieblad dat je bij vochtproblemen eerst alle vormen van lekkage moet verhelpen. Bij koudebruggen, optrekkend vocht of een vochtige kruipruimte laat je de aanpak over aan een bouwfysicus of specialist. Huur je je woning, meld het dan bij je verhuurder: bouwkundige gebreken zijn meestal niet jouw taak.</p>"""),
("Goed ventileren en verwarmen",
"""<p>Bij de meeste schimmel binnen speelt ventilatie een grote rol. De Rijksoverheid adviseert om dag en nacht voldoende ventilatieroosters en klepraampjes open te zetten, en extra te ventileren na koken, douchen en slapen. Alleen even luchten is niet genoeg: volgens de Rijksoverheid is de frisse lucht na een half uurtje weer verdwenen.</p>
<p>Het RIVM adviseert daarnaast om het huis goed en gelijkmatig te verwarmen en het 's nachts niet kouder te laten worden dan 15 °C. Koude muren trekken condens aan. Een ontvochtiger lost volgens het RIVM de oorzaak niet op; het effect is gering en bij goede ventilatie is hij niet nodig.</p>"""),
("Schimmel verwijderen",
"""<p>Het RIVM geeft deze aanpak:</p>
<ul>
<li>Verwijder schimmel op gladde oppervlakken met soda opgelost in heet water. Gebruik een doek en geen borstel, dan verspreid je de sporen minder.</li>
<li>Middelen met chloor of een ammoniumverbinding raadt het RIVM af, omdat ze de luchtwegen kunnen irriteren. Dat geldt vooral voor mensen met luchtwegklachten.</li>
<li>Bij poreuze materialen zoals hout, kit, gips en pleisterwerk groeien de schimmeldraden in het materiaal. Volgens de folder kun je de schimmel dan alleen weghalen door de aangetaste delen te verwijderen.</li>
<li>Bij verf, behang en kitvoegen is schoonmaken vaak niet genoeg en moeten ze worden vervangen.</li>
</ul>
<p>Draag handschoenen en zorg voor frisse lucht. Gaat het om grote oppervlakken, of heb je astma of andere luchtwegklachten, laat het dan door een ander doen. Bij gezondheidsklachten kun je terecht bij de huisarts of de GGD.</p>"""),
("Schimmelwerende verf: wat doet het wel en niet?",
"""<p>Schimmelwerende of schimmelbestendige muurverf bevat een middel dat schimmelgroei op de verflaag remt. Dat is nuttig in badkamers en keukens. Maar het is geen vochtwerende verf en geen oplossing voor een vochtprobleem. Het kenmerkenblad van een schimmelbestendige muurverf zegt dat zelf ook: de werking hangt af van de omstandigheden in de ruimte. Als temperatuur en vochtigheid constant ideaal zijn voor schimmel, is schimmelvorming na verloop van tijd niet uit te sluiten. Voor een langdurige werking moet je volgens het blad de oorzaken wegnemen, met als belangrijke maatregel goede ventilatie.</p>
<p>Uit hetzelfde blad:</p>
<ul>
<li>De verf is geschikt voor badkamer en keuken, maar niet voor het douchegedeelte.</li>
<li>Optimale schimmelbestendigheid krijg je met twee lagen in een egaal gesloten laag. Het rendement is 7 tot 8 m² per liter.</li>
<li>De ondergrond moet droog zijn: maximaal 4% vocht, en maximaal 1% bij gipsgebonden ondergronden.</li>
<li>Zet hem niet op een gesloten ondergrond zoals alkydverf; bij vocht kan dat tot loslaten leiden.</li>
</ul>
<p>Ook vochtwerende verf of een vochtwerende voorstrijk houdt water van achteren niet voor altijd tegen. Is de muur nat door lekkage of optrekkend vocht, dan zoekt het vocht een andere weg of duwt het de verf eraf. Daarover lees je meer in <a href="/kennisbank/verf-bladdert-af/">verf bladdert af</a>.</p>"""),
("Schilderen na schimmel",
"""<p>Is de oorzaak opgelost, de schimmel verwijderd en de muur droog? Dan kun je schilderen. Laat de muur na het schoonmaken goed drogen. Vochtvlekken en kringen isoleer je eerst. Het technische blad van een voorstrijk schrijft voor om vochtkringen te isoleren en 24 uur bij 20 °C te laten drogen. Daarna zet je twee lagen muurverf, in een badkamer bij voorkeur een schimmelbestendige.</p>
<p>Voor plafonds geldt hetzelfde: werk nat-in-nat, anders zie je strepen. Tips staan in <a href="/kennisbank/plafond-schilderen-zonder-strepen/">plafond schilderen zonder strepen</a>. Welke muurverf bij welke ruimte past, lees je in <a href="/kennisbank/latex-of-muurverf/">latex of muurverf</a>.</p>"""),
("Rekenvoorbeeld: zelf doen of laten doen",
"""<p>Stel: het plafond van je badkamer (6 m²) en de strook muur boven de tegels (8 m²) zijn grijs van de schimmel. De afzuiging is gerepareerd en je ventileert nu goed. Je wilt <strong>14 m²</strong> schoonmaken en opnieuw schilderen met twee lagen schimmelbestendige muurverf.</p>
<div class="tablewrap"><table>
<thead><tr><th>Zelf doen</th><th>Hoeveel</th><th>Ongeveer</th></tr></thead>
<tbody>
<tr><td>Soda, doeken, handschoenen</td><td></td><td>€10 tot €15</td></tr>
<tr><td>Schimmelbestendige muurverf, 2 lagen (7 tot 8 m² per liter, 28 m² totaal)</td><td>ca. 4 liter: 2 blikken van 2,5 liter</td><td>€70 tot €120</td></tr>
<tr><td>Voorstrijk of isolerende voorstrijk voor kringen</td><td>1 blik van 2,5 liter</td><td>€20 tot €35</td></tr>
<tr><td>Roller, kwast, tape, folie</td><td></td><td>€20 tot €30</td></tr>
<tr><td><strong>Totaal materiaal</strong></td><td></td><td><strong>€120 tot €200</strong></td></tr>
</tbody></table></div>
<p><strong>Laten doen:</strong> onze richtprijs voor een plafond is €12 tot €22 per m², voor muren €10 tot €22 per m², inclusief materiaal en btw. Voor 14 m² kom je dan op ongeveer €150 tot €310. Bij zo'n kleine klus rekenen veel schilders liever per uur of met een minimumbedrag; met €45 tot €65 per uur exclusief btw en een halve tot hele dag werk zit je eerder op €200 tot €520 exclusief btw. Het oplossen van de oorzaak, zoals een nieuwe ventilator of isolatie, komt daar los bij en is werk voor een installateur of aannemer.</p>"""),
],
"stappen": [
("Zoek de oorzaak", "Kijk waar de schimmel zit: badkamerplafond, hoeken van buitenmuren of een plek die groter wordt. Controleer ventilatie, koude plekken en lekkages."),
("Los het vochtprobleem op", "Laat lekkages repareren, ventileer dag en nacht, verwarm gelijkmatig en zet meubels een stukje van de buitenmuur af. Schakel bij koudebruggen of optrekkend vocht een specialist in."),
("Verwijder de schimmel", "Neem gladde oppervlakken af met een doek en soda in heet water. Vervang beschimmelde kit en behang. Draag handschoenen en ventileer."),
("Laat de muur drogen", "Geef de muur de tijd om helemaal droog te worden voordat je verder gaat."),
("Isoleer vlekken en voorstrijk", "Behandel vochtkringen en vlekken met een isolerende voorstrijk en laat die drogen volgens het blik."),
("Schilder twee lagen", "Zet twee lagen muurverf, in vochtige ruimtes een schimmelbestendige, in een egaal gesloten laag."),
],
"kosten": ["schilderen-per-m2", "plafond-schilderen"],
"dienst": "binnenschilderwerk",
"faq": [
("Helpt schimmelwerende verf tegen schimmel op de muur?", "Het remt schimmelgroei op de verflaag, maar het lost de oorzaak niet op. Volgens de fabrikant zelf is schimmel niet uit te sluiten als de ruimte vochtig blijft. Zorg eerst voor droge muren en goede ventilatie."),
("Wat is het verschil tussen schimmelwerende en vochtwerende verf?", "Schimmelwerende verf bevat een middel tegen schimmelgroei op het oppervlak. Vochtwerende verf of voorstrijk is bedoeld om vochtplekken af te sluiten. Geen van beide houdt water uit een lekkage of optrekkend vocht blijvend tegen."),
("Waarmee verwijder je schimmel van de muur?", "Het RIVM adviseert soda opgelost in heet water, met een doek en geen borstel. Middelen met chloor raadt het RIVM af vanwege irritatie van de luchtwegen."),
("Waarom komt schimmel steeds terug?", "Omdat de oorzaak er nog is: te weinig ventilatie, een koude plek in de muur of een lekkage. Zolang het vocht blijft, groeit de schimmel terug."),
("Is schimmel in huis gevaarlijk?", "Vocht en schimmel kunnen astma en andere luchtwegklachten erger maken, vooral bij mensen met een allergie. Heb je klachten, neem dan contact op met de huisarts of de GGD."),
("Wie betaalt schimmel in een huurwoning?", "Gaat het om een bouwkundig gebrek, zoals lekkage of slechte isolatie, dan is dat meestal een zaak voor de verhuurder. Meld het schriftelijk. Gewoon ventileren en schoonhouden is wel de taak van de huurder."),
],
"bronnen": [RIVM_FOLDER, RIVM_BESTRIJDEN, RIJKSOVERHEID_VENTILEREN, SIGMA_FUNGI],
"gerelateerd": ["latex-of-muurverf", "plafond-schilderen-zonder-strepen", "verf-bladdert-af"],
},
# ---------------------------------------------------------------------------
{
"slug": "verf-bladdert-af",
"groep": "Schade en onderhoud",
"titel": "Verf bladdert af: oorzaken en wat je eraan doet",
"seo_titel": "Verf bladdert af: oorzaak en oplossing",
"description": "Afbladderende verf op kozijnen, muren of plafond? De vijf bekendste oorzaken, hoe je ze herkent, wat je eraan doet en waar je op let bij oude verf met lood.",
"kort": "Vocht, slechte hechting, te dikke lagen of de verkeerde ondergrond: zo vind en herstel je de oorzaak.",
"foto": "houtrot-raamdorpel-afbladderende-verf",
"intro": "Verf die in schilfers loslaat, ziet er niet alleen slordig uit. Buiten is het vaak een teken dat er water achter de verf zit, en dat kan houtrot worden. Binnen gaat het meestal om hechting of vocht in de muur. Een nieuwe laag erover helpt niet als je de oorzaak niet aanpakt. Hier lees je waarom verf afbladdert, hoe je de oorzaak herkent en hoe je het goed herstelt.",
"kort_antwoord": "Verf bladdert af door vocht achter de verflaag, slechte hechting op een vuile of gladde ondergrond, te veel of te dikke lagen, of verf die niet bij de ondergrond past. Verwijder alle loszittende verf, los de oorzaak op, schuur en reinig, en bouw het verfsysteem opnieuw op. Wees voorzichtig in oude huizen: oude verflagen kunnen lood bevatten.",
"secties": [
("De vijf bekendste oorzaken",
"""<div class="tablewrap"><table>
<thead><tr><th>Oorzaak</th><th>Hoe je het herkent</th><th>Waar het vaak gebeurt</th></tr></thead>
<tbody>
<tr><td>Vocht achter de verf</td><td>Blazen, bladders vanaf onderdorpels en naden, hout eronder is donker of zacht</td><td>Buitenkozijnen, deuren, muren met lekkage of optrekkend vocht</td></tr>
<tr><td>Slechte hechting</td><td>Verf komt in hele stukken los, onderlaag is glad of vuil</td><td>Over vet, stof, saus of glanzende oude lak zonder schuren</td></tr>
<tr><td>Te dikke of te veel lagen</td><td>Scheurtjes als een netwerk, dikke schilfers met meerdere lagen</td><td>Oud houtwerk dat jaren is overgeschilderd</td></tr>
<tr><td>Verkeerde combinatie met de ondergrond</td><td>Verf laat los van een bepaalde onderlaag, vaak na vocht</td><td>Muurverf op oude lakverf, verf op kit of kunststof</td></tr>
<tr><td>Geschilderd onder slechte omstandigheden</td><td>Problemen kort na het schilderen, verf blijft zacht of dof</td><td>Te koud, te vochtig, dauw of volle zon</td></tr>
</tbody></table></div>
<p>Vaak spelen er meerdere oorzaken tegelijk. Een kozijn met tien oude lagen verf en een open naad bij de onderdorpel heeft zowel een laagdikte- als een vochtprobleem.</p>"""),
("Buiten: vocht is de grote boosdoener",
"""<p>Op buitenhoutwerk komt afbladderen meestal door water dat achter de verf komt. Dat gebeurt via open naden, losgekomen kit, beschadigingen of een te dunne verflaag. Het hout neemt water op, wil het weer kwijt, en duwt daarbij de verf van zich af. Zie je bladders vooral onderaan, bij de onderdorpel en de hoeken? Dan is dat bijna zeker de oorzaak. Prik dan ook in het hout: is het zacht, dan is er al houtrot. Lees daarover <a href="/kennisbank/houtrot-herkennen-en-herstellen/">houtrot herkennen en herstellen</a>.</p>
<p>Vocht kan ook van binnenuit komen. Een infoblad van een verffabrikant legt uit dat waterdamp uit de woning bij slecht ventileren condenseert op koude plekken. Op langere termijn geeft dat volgens het blad een groter risico op afbladderen van de verf aan de buitenkant van kozijnen. Een goed intact verfsysteem aan de binnenkant van het kozijn is daarom net zo belangrijk als buiten. Hetzelfde blad noemt extreme verschillen in laagdikte tussen binnen en buiten als mogelijke oorzaak van afbladderen en blaasvorming, en wijst erop dat de meeste problemen in de praktijk ontstaan bij open verbindingen waar water de constructie in dringt.</p>"""),
("Binnen: hechting en vocht in de muur",
"""<p>Bladdert de verf binnen op een muur of plafond, dan zijn dit de bekendste oorzaken:</p>
<ul>
<li><strong>Saus of witkalk eronder.</strong> Het technische blad van een muurverf schrijft voor om veegvaste muurverf (witkalk of saus) en slecht hechtende verflagen eerst te verwijderen. Doe je dat niet, dan laat de nieuwe verf samen met de saus los. Test het met een vochtige doek: geeft de muur wit af, dan zit er saus op.</li>
<li><strong>Muurverf op een gesloten laag.</strong> Het kenmerkenblad van een muurverf waarschuwt: zet geen dampdoorlatende muurverf op een gesloten ondergrond zoals alkydverf, want bij vocht kan dat tot onthechting leiden. Dat zie je vaak in oude keukens en badkamers waar ooit met lakverf is geschilderd.</li>
<li><strong>Vocht in de muur.</strong> Lekkage, optrekkend vocht of condens duwt de verf eraf. Vaak zie je er ook vochtplekken of schimmel bij. Pak eerst het vocht aan, zie <a href="/kennisbank/schimmel-op-muur/">schimmel op de muur</a>.</li>
<li><strong>Te vroeg geschilderd op nieuw stucwerk.</strong> Restvocht wil eruit en drukt tegen de verf. Hoe je dat voorkomt, staat in ons artikel over nieuw stucwerk schilderen.</li>
</ul>"""),
("Let op: oude verf kan lood bevatten",
"""<p>Verf bevat tegenwoordig geen lood meer, maar in oude huizen kunnen onder de bovenste lagen nog loodhoudende verflagen zitten. Vooral in woningen van voor de jaren zestig is dat een reële kans. Het risico zit in het stof en de dampen die vrijkomen als je die lagen droog schuurt of afbrandt. Jonge kinderen zijn er het gevoeligst voor, en ook het ongeboren kind kan via de moeder worden blootgesteld.</p>
<p>De GGD adviseert om ervoor te zorgen dat er geen kinderen in de buurt zijn tijdens het schuren of afbranden van oude loodhoudende verflagen, en om de ruimtes eerst schoon te maken met een natte doek. Twijfel je, laat de verf dan testen of laat het werk doen door een schilder die nat schuurt of met afzuiging werkt.</p>"""),
("Wat doe je eraan?",
"""<p>Een likje verf over de bladders werkt niet. De nieuwe laag zit dan vast op iets dat zelf loslaat. Zo pak je het goed aan:</p>
<ol>
<li><strong>Vind en los de oorzaak op.</strong> Herstel open naden, losse kit, lekkages of houtrot. Ventileer beter als condens de oorzaak is.</li>
<li><strong>Verwijder alle loszittende verf.</strong> Schraap tot je op verf zit die goed hecht. Test dat met een stuk tape dat je er met een ruk aftrekt.</li>
<li><strong>Zijn er te veel lagen?</strong> Bij oud houtwerk met dikke, gescheurde lagen is het soms beter om alles kaal te maken.</li>
<li><strong>Reinig, schuur en laat drogen.</strong> Ontvet, schuur de randen van de oude verf glad en zorg dat hout of muur droog is.</li>
<li><strong>Bouw het systeem opnieuw op.</strong> Buiten: grondverf op kale plekken, voorlak, aflak. Binnen: voorstrijk en muurverf die bij de ondergrond past.</li>
</ol>
<p>Let op de omstandigheden. Het kenmerkenblad van een muurverf noemt bijvoorbeeld een temperatuur tussen 5 en 30 °C, maximaal 85% luchtvochtigheid en een ondergrond die minstens 3 °C warmer is dan het dauwpunt. Voor lakverf gelden vergelijkbare grenzen; kijk altijd op het blik. Buiten kijk je ook naar het weer; let op regen, dauw en de nachttemperatuur. Hoe je kozijnen voorbereidt, lees je in <a href="/kennisbank/kozijnen-schuren-en-voorbereiden/">kozijnen schuren en voorbereiden</a>.</p>"""),
("Is het de schuld van de schilder?",
"""<p>Bladdert verf al een paar maanden of een jaar na het schilderen, dan heeft het vaak te maken met de voorbereiding of met de omstandigheden tijdens het werk. Na veel jaren is het eerder slijtage, uitgesteld onderhoud of vocht dat er later is bijgekomen. Leg schade vast met foto's en meld het snel en schriftelijk. Wat je rechten zijn, lees je in <a href="/kennisbank/verfschade-en-garantie/">verfschade en garantie</a>.</p>"""),
("Rekenvoorbeeld: zelf doen of laten doen",
"""<p>Stel: bij vier buitenkozijnen bladdert de verf aan de onderkant, en bij twee ervan is de onderdorpel plaatselijk zacht.</p>
<div class="tablewrap"><table>
<thead><tr><th>Zelf doen</th><th>Hoeveel</th><th>Ongeveer</th></tr></thead>
<tbody>
<tr><td>Verfkrabber, schuurpapier, ontvetter, tape</td><td></td><td>€30 tot €50</td></tr>
<tr><td>Tweecomponenten houtrotvuller</td><td>1 set</td><td>€25 tot €40</td></tr>
<tr><td>Grondverf en aflak voor buiten</td><td>elk 0,75 liter</td><td>€50 tot €90</td></tr>
<tr><td>Overschilderbare kit</td><td>1 koker</td><td>€8 tot €15</td></tr>
<tr><td><strong>Totaal materiaal</strong></td><td></td><td><strong>€115 tot €195</strong></td></tr>
</tbody></table></div>
<p>Reken op twee tot drie droge dagen, en een ladder of steiger als de kozijnen op de verdieping zitten.</p>
<p><strong>Laten doen:</strong> onze richtprijs is €90 tot €190 per buitenkozijn, dus €360 tot €760 voor vier kozijnen. De twee houtrotplekken komen daar bij, met €50 tot €275 per plek: samen €100 tot €550. In totaal ligt de prijs dan tussen ongeveer <strong>€460 en €1.310</strong>, inclusief btw. Houtrotherstel met vuller en schilderwerk vallen bij een woning ouder dan twee jaar onder 9% btw, nieuw hout onder 21%. Moet het hele huis worden gedaan, vraag dan offertes aan voor het hele buitenschilderwerk; de richtprijs daarvoor staat hieronder.</p>"""),
],
"stappen": [
("Zoek de oorzaak", "Kijk waar de verf bladdert: bij naden en onderdorpels, op een muur met vochtplekken, of over een oude gladde laag. Prik in hout om houtrot uit te sluiten."),
("Herstel de oorzaak", "Repareer lekkages, open naden en losse kit, ventileer beter bij condens en laat houtrot herstellen."),
("Verwijder de losse verf", "Schraap alles weg wat loszit en doe de tapetest. Schuur in oude huizen nat of met afzuiging en houd kinderen uit de buurt."),
("Reinig en schuur", "Ontvet het oppervlak, schuur de randen van de oude verf glad en mat de rest op. Maak alles stofvrij en laat het drogen."),
("Gronden of voorstrijken", "Breng op kaal hout een grondverf aan en op kale of zuigende muren een voorstrijk die bij de ondergrond past."),
("Afwerken in het juiste systeem", "Zet voorlak en aflak op houtwerk, of twee lagen muurverf binnen. Werk alleen bij de temperatuur en luchtvochtigheid die op het blik staan."),
],
"kosten": ["kozijnen-schilderen", "huis-schilderen"],
"dienst": "buitenschilderwerk",
"faq": [
("Waarom bladdert mijn verf af?", "Meestal door vocht achter de verf, slechte hechting op een vuile of gladde ondergrond, te veel oude lagen, of een verf die niet bij de ondergrond past. Soms is er geschilderd bij te koud of te vochtig weer."),
("Kan ik over afbladderende verf heen schilderen?", "Nee. Verwijder eerst alle loszittende verf. Anders zit de nieuwe laag vast op iets dat zelf loslaat, en bladdert het opnieuw."),
("Moet alle oude verf eraf?", "Niet altijd. Verf die goed hecht mag blijven. Bij oud houtwerk met veel dikke, gescheurde lagen is helemaal kaal maken soms wel de beste keuze."),
("Waarom bladdert verf binnen van de muur?", "Vaak door een sauslaag eronder, muurverf op oude lakverf, of vocht in de muur. Test op saus met een vochtige doek en controleer of de muur droog is."),
("Is afbladderende verf in een oud huis gevaarlijk?", "Oude verflagen kunnen lood bevatten. Het risico zit in stof en dampen bij droog schuren of afbranden. Houd kinderen uit de buurt, maak schoon met een natte doek en laat het bij twijfel testen."),
("Valt afbladderende verf onder de garantie?", "Als het kort na het schilderen gebeurt en door het werk komt, kun je de schilder vragen het te herstellen. Leg het vast met foto's en meld het schriftelijk."),
],
"bronnen": [GGD_LOOD, SIKKENS_1131, SIGMA_FUNGI, TDS_MUURVERF],
"gerelateerd": ["kozijnen-schuren-en-voorbereiden", "houtrot-herkennen-en-herstellen", "verfschade-en-garantie"],
},
]

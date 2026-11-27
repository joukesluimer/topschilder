# -*- coding: utf-8 -*-
"""Handmatig nagezochte feiten voor lokaal_top.py, met bron per regel.

KLEUR       -> per gemeente: wat de gemeente zegt over kleur en welstand, met de echte URL
TIJDVAKKEN  -> per bouwperiode: gebruikelijke kozijnen en hout, en waar je op let bij schilderen
Onderzocht op 27 november 2026. Niets hierin is verzonnen; wat niet te vinden was, staat er niet in.
"""

# (bouwjaar tot, label, gebruikelijk in die periode, let op bij schilderen)
# Bewust voorzichtig: een betrouwbare bron die per periode één houtsoort noemt, bestaat niet (onderzocht 27-11-2026).
# Wel onderbouwd: lood in oude verf (OnderhoudNL), stalen ramen bij Dudok (RCE), aluminium populair in de jaren 50-60
# (Duurzaam Bouwloket), hout dat tegenwoordig kant-en-klaar uit de fabriek komt (Centrum Hout).
TIJDVAKKEN = [
    (1945, "vóór 1945", "Houten kozijnen, vaak met roedes en bovenlichten; bij sommige jaren-20- en -30-bouw stalen ramen",
     "Oude verflagen kunnen lood bevatten: laat stofarm of nat schuren"),
    (1965, "1945–1964", "Houten kozijnen; in de jaren vijftig en zestig ook vaak aluminium",
     "Veel oude lagen, soms met lood; houtrot in onderdorpels"),
    (1980, "1965–1979", "Houten kozijnen van naald- of hardhout",
     "Originele kozijnen zijn nu 45 jaar of ouder: houtrot in hoeken en dorpels"),
    (1995, "1980–1994", "Houten of kunststof kozijnen",
     "Kitnaden, glaslatten en onderdorpels nalopen"),
    (2010, "1995–2009", "Houten kozijnen, vaak in de fabriek voorbehandeld, of kunststof",
     "Hout aan een vaste cyclus houden; kunststof niet met gewone lak"),
    (9999, "2010 en later", "Hout dat kant-en-klaar uit de fabriek komt, kunststof of aluminium",
     "Eerste beurt na zes tot acht jaar; volg het onderhoudsadvies van de fabriek"),
]
TIJDVAK_BRONNEN = (
    '<a href="https://onderhoudnl.nl/stream/handleiding-gevaarlijke-stoffen-bij-het-bewerken-van-oude-verflagen" rel="nofollow noopener" target="_blank">OnderhoudNL</a> '
    '(loodwit buiten verboden sinds 2009, loodmenie sinds 1990), '
    '<a href="https://monumentenregister.cultureelerfgoed.nl/monumenten/407238" rel="nofollow noopener" target="_blank">RCE, monument 407238</a> '
    '(stalen vensters bij Dudok), '
    '<a href="https://res.cloudinary.com/duurzaambouwloket/image/upload/v1689935437/Factsheets%202023/Factsheet_Vervangen_kozijnen_2023.pdf" rel="nofollow noopener" target="_blank">Duurzaam Bouwloket</a> '
    '(aluminium in de jaren 50 en 60) en '
    '<a href="https://www.centrumhout.nl/media/cd2l4kx2/onderhoud-is-houden-van-hout.pdf" rel="nofollow noopener" target="_blank">Centrum Hout</a> '
    '(fabrieksmatig afgewerkt hout); de indeling per periode is een typering van Topschilder'
)

KLEUR = {
    "amersfoort": dict(
        regels=("De gemeente vraagt in de binnenstad om terughoudend kleurgebruik. Een andere kleur of een ander materiaal mag daar "
                "alleen als historisch kleuronderzoek dat onderbouwt. Het Bergkwartier is sinds 2007 een apart rijksbeschermd "
                "stadsgezicht. Elders in de stad kunnen schreeuwende of sterk contrasterende kleuren onder de excessenregeling vallen."),
        url="https://lokaleregelgeving.overheid.nl/CVDR674970",
        extra="Een tip: kozijnen en boeidelen van dakkapellen horen volgens de welstandsnota (gebroken) wit te zijn of te passen bij het hoofdgebouw.",
        bron='kleurregels: <a href="https://lokaleregelgeving.overheid.nl/CVDR674970" rel="nofollow noopener" target="_blank">Welstandsnota Amersfoort</a>; Bergkwartier: Staatscourant 2007',
    ),
    "almere": dict(
        regels=("Almere heeft geen rijksbeschermd gezicht. De meeste woonwijken zijn in principe welstandsvrij, maar in de hele "
                "gemeente geldt een excessenregeling: een kleur die sterk afwijkt van de omgeving kan een exces zijn, ook als je "
                "een bestaand huis overschildert. In de Regenboogbuurt moeten de grote gevelvlakken hun kleur houden; kozijnen en "
                "deuren vallen daar niet onder."),
        url="https://www.almere.nl/bouwen/soorten-vergunningen/welstand-en-erfgoed-oa-reclame-uiting/welstandsnota",
        extra="Woon je in een buurt met kleurafspraken in de koopakte (een kettingbeding), kijk die dan ook na voordat je een nieuwe kleur kiest.",
        bron='welstand: <a href="https://www.almere.nl/bouwen/soorten-vergunningen/welstand-en-erfgoed-oa-reclame-uiting/welstandsnota" rel="nofollow noopener" target="_blank">gemeente Almere</a>',
    ),
    "zwolle": dict(
        regels=("De binnenstad en delen buiten de stadsgracht vormen een rijksbeschermd stadsgezicht. Bij verbouwen of renoveren is "
                "daar het oorspronkelijke kleurgebruik het uitgangspunt. Alleen Vrij Werkeren in Stadshagen is welstandsvrij; elders "
                "kunnen felle of contrasterende kleuren onder de excessenregeling vallen."),
        url="https://lokaleregelgeving.overheid.nl/CVDR717030/1",
        extra="",
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR717030/1" rel="nofollow noopener" target="_blank">Welstandsnota Zwolle</a>',
    ),
    "lelystad": dict(
        regels=("Lelystad heeft geen rijksbeschermd gezicht. De gemeente werkt met drie niveaus: gebieden met welstand, gebieden met "
                "een beeldkwaliteitsplan, en welstandsvrije gebieden. Het grootste deel van de stad en het buitengebied is "
                "welstandsvrij; daar kun je vrijwillig om advies vragen."),
        url="https://www.gemeentelelystad.nl/welstand",
        extra="",
        bron='welstand: <a href="https://www.gemeentelelystad.nl/welstand" rel="nofollow noopener" target="_blank">gemeente Lelystad</a>',
    ),
    "hilversum": dict(
        regels=("Hilversum-Zuid en Tuinwijk Oost (Plan Oost) zijn rijksbeschermd stadsgezicht; het Noordwestelijk Villagebied ook. "
                "De welstandsnota van 2022 geldt voor de hele gemeente. Woon je in een van die gebieden, vraag dan vóór een "
                "kleurwijziging aan de gemeente wat mag."),
        url="https://lokaleregelgeving.overheid.nl/CVDR715260",
        extra="",
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR715260" rel="nofollow noopener" target="_blank">Welstandsnota Hilversum</a>; gezichten: Staatscourant 2015',
    ),
    "harderwijk": dict(
        regels=("De binnenstad is sinds 1970 een rijksbeschermd stadsgezicht. Harderwijk heeft geen welstandsvrije gebieden. In de "
                "binnenstad moet kleur passen bij het historische karakter; de richtlijn is het rapport ‘Kleuren voor Harderwijk’, "
                "en bij renovatie zijn de oorspronkelijke kleuren het uitgangspunt."),
        url="https://lokaleregelgeving.overheid.nl/CVDR639912/1",
        extra=("Een voorbeeld uit het beeldkwaliteitplan voor het kleine gebied Binnenstad-Havendijk: kozijnen overwegend wit, "
               "deuren ossenbloedrood, blauw of groen. Dat geldt alleen voor dat gebied, maar het laat zien hoe concreet de regels kunnen zijn."),
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR639912/1" rel="nofollow noopener" target="_blank">Welstandsnota Harderwijk</a>; Havendijk: beeldkwaliteitplan via ruimtelijkeplannen.nl',
    ),
    "zeewolde": dict(
        regels=("Zeewolde heeft geen rijksbeschermd gezicht. Volgens de welstandsnota van 2016 horen aanbouwen dezelfde kleuren te "
                "krijgen als het hoofdgebouw, en mogen houten gevels naturel, transparant gebeitst of donker zijn (groen, bruin, grijs "
                "of zwart). Felle of contrasterende kleuren vallen onder de excessenregeling. Check bij de gemeente of die nota nog geldt."),
        url="https://www.zeewolde.nl/fileadmin/Site_Zeewolde/documenten/producten/welstandsnota_2016.pdf",
        extra="",
        bron='welstand: <a href="https://www.zeewolde.nl/fileadmin/Site_Zeewolde/documenten/producten/welstandsnota_2016.pdf" rel="nofollow noopener" target="_blank">Welstandsnota Zeewolde 2016</a>',
    ),
    "ermelo": dict(
        regels=("Ermelo werkt met een soepel en een streng welstandsregime; alleen recreatieterreinen zijn welstandsvrij. In "
                "meerdere delen van het dorp is het oorspronkelijke kleurgebruik het uitgangspunt en wordt ingetogen kleur gevraagd. "
                "Felle en sterk contrasterende kleuren noemt de nota als exces."),
        url="https://www.ermelo.nl/fileadmin/Site_Ermelo/documenten/welstand/Nota_Omgevingskwaliteit.pdf",
        extra="",
        bron='welstand: <a href="https://www.ermelo.nl/fileadmin/Site_Ermelo/documenten/welstand/Nota_Omgevingskwaliteit.pdf" rel="nofollow noopener" target="_blank">Nota Omgevingskwaliteit Ermelo</a>',
    ),
    "nunspeet": dict(
        regels=("Nunspeet heeft geen rijksbeschermd gezicht. De meeste woonwijken krijgen vooraf geen welstandstoets, maar zijn niet "
                "welstandsvrij: bij felle of contrasterende kleuren kan de gemeente achteraf optreden. Rond het centrum noemt de "
                "welstandsnota het kleurgebruik traditioneel, met aardkleuren, gebroken wit en standgroen."),
        url="https://www.nunspeet.nl/fileadmin/Nunspeet_documenten/Producten/Bouwen_en_wonen/Welstand_Nunspeet_2015.pdf",
        extra="",
        bron='welstand: <a href="https://www.nunspeet.nl/fileadmin/Nunspeet_documenten/Producten/Bouwen_en_wonen/Welstand_Nunspeet_2015.pdf" rel="nofollow noopener" target="_blank">Welstand Nunspeet 2015</a>',
    ),
    "kampen": dict(
        regels=("De binnenstad, inclusief het Plantsoen, is sinds 1975 een rijksbeschermd stadsgezicht. Daar blijft het historische "
                "kleurgebruik behouden: gedekte kleuren zoals groen en crèmewit. Schoon metselwerk mag niet geschilderd of gesausd "
                "worden, en kozijnen niet in felle of contrasterende kleuren. In de dorpen zijn kozijnen wit of wit met groen."),
        url="https://lokaleregelgeving.overheid.nl/CVDR661794",
        extra=("Sinds eind 2024 is er een gevelinspiratieboek voor de binnenstad, gekoppeld aan een gevelsubsidie. Daarin zijn "
               "sprekendere kleuren die bij de historische stijl van het pand passen juist welkom, en wordt kleuronderzoek aangeraden."),
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR661794" rel="nofollow noopener" target="_blank">Welstandsnota Kampen</a>; gevelinspiratieboek: Gemeenteblad 2024, 548840',
    ),
    'nijkerk': dict(
        regels='Nijkerk werkt met vier regimes: welstandsvrij, beperkt, regulier en bijzonder. Bedrijventerreinen als Arkervaart en Watergoor zijn in principe welstandsvrij, maar in de hele gemeente geldt een excessenregeling. Voor de binnenstad geldt het beeldkwaliteitsplan van 2016: rustig, terughoudend kleurgebruik, schoon metselwerk niet schilderen en muurankers zwart.',
        url='https://www.nijkerk.eu/_flysystem/media/bkp-nijkerk-binnenstad-2016.pdf',
        extra='Bij monumenten in de binnenstad raadt het plan kleuronderzoek aan om de oorspronkelijke kleuren te vinden, en in beginsel natuurlijke verfstoffen. De welstandsnota zelf is ouder (rond 2007); vraag de gemeente of die nog geldt.',
        bron='welstand: <a href="https://www.nijkerk.eu/_flysystem/media/welstandsnota_nijkerk.pdf" rel="nofollow noopener" target="_blank">Welstandsnota Nijkerk</a> en <a href="https://www.nijkerk.eu/_flysystem/media/bkp-nijkerk-binnenstad-2016.pdf" rel="nofollow noopener" target="_blank">Beeldkwaliteitsplan Binnenstad 2016</a>',
    ),
    'huizen': dict(
        regels='Huizen kent drie niveaus: welstandsvrij, nagenoeg welstandsvrij en bijzonder. Waar de gemeente vooraf niet toetst, geldt alleen de excessenregeling, en felle of contrasterende kleuren noemt de nota als exces. In het Oude Dorp en de gemeentelijke dorpsgezichten hoort houtwerk in traditionele kleuren die passen bij de huizen eromheen.',
        url='https://cuatro.sim-cdn.nl/huizen/uploads/welstandsnota_huizen.pdf',
        extra='De welstandsnota is van 2012. In 2018 lag er een concept voor een nieuwe nota; vraag bij de gemeente na welke versie nu geldt.',
        bron='welstand: <a href="https://cuatro.sim-cdn.nl/huizen/uploads/welstandsnota_huizen.pdf" rel="nofollow noopener" target="_blank">Welstandsnota Huizen 2012</a>',
    ),
    'bussum': dict(
        regels='Bussum heeft twee rijksbeschermde gezichten: Het Spiegel en het Brediuskwartier. In Het Spiegel vraagt de welstandsnota van Gooise Meren (2019) om kozijnen en ander houtwerk in traditionele kleuren als crèmewit, donkerblauw, donkerrood en donkergroen. In het Brediuskwartier hebben crèmewit en donkergroen de voorkeur.',
        url='https://archiefbestuur.gooisemeren.nl/fileadmin/Beleidsnota_s/Monumenten/Welstandsnota_2019/Welstand_Gooise_meren_2019_zonder_straatnamenregister.pdf',
        extra='Kleine plannen aan de achterkant toetst de gemeente alleen op excessen. In de beschermde gezichten en bij monumenten geldt die uitzondering niet. De nota is van 2019; controleer de actuele regels bij de gemeente.',
        bron='welstand: <a href="https://archiefbestuur.gooisemeren.nl/fileadmin/Beleidsnota_s/Monumenten/Welstandsnota_2019/Welstand_Gooise_meren_2019_zonder_straatnamenregister.pdf" rel="nofollow noopener" target="_blank">Welstandsnota Gooise Meren 2019</a>',
    ),
    'dronten': dict(
        regels='De gemeente Dronten heeft welstandsbeleid waarin ook welstandsvrije gebieden voorkomen. Welk regime voor jouw adres geldt, kun je volgens de gemeente opzoeken op Dronten Maps. Concrete kleurregels hebben we in het beleid niet gevonden. Twijfel je over een opvallende kleur, vraag het dan vooraf na.',
        url='https://lokaleregelgeving.overheid.nl/CVDR613553',
        extra='',
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR613553" rel="nofollow noopener" target="_blank">vergunningenbeleid gemeente Dronten</a>',
    ),
    'emmeloord': dict(
        regels='De gemeente Noordoostpolder heeft sinds 2024 nieuwe regels voor het uiterlijk van gebouwen. Buiten de gebieden die de gemeente toetst, geldt alleen de excessenregeling. Een gebouw in een felle, sterk contrasterende kleur die niet in de omgeving past, noemt de gemeente als voorbeeld van een exces. In het centrum en de oude schil van Emmeloord moeten kleur en materiaal passen bij de omgeving en bij het oorspronkelijke gebouw.',
        url='https://lokaleregelgeving.overheid.nl/CVDR703939/',
        extra='',
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR703939/" rel="nofollow noopener" target="_blank">Beleidsregel uiterlijk bouwwerken Noordoostpolder</a>',
    ),
    'weesp': dict(
        regels='Weesp hoort sinds 2022 bij Amsterdam en valt onder de Amsterdamse welstandsnota ‘De Schoonheid van Amsterdam’, als gebied Binnenstad Weesp. Die nota is in 2026 nog gewijzigd. De precieze kleurregels voor de binnenstad van Weesp hebben we niet kunnen nalezen. Vraag het daarom bij de gemeente na voordat je een andere kleur kiest.',
        url='https://zoek.officielebekendmakingen.nl/gmb-2026-305658.pdf',
        extra='',
        bron='welstand: <a href="https://zoek.officielebekendmakingen.nl/gmb-2026-305658.pdf" rel="nofollow noopener" target="_blank">wijziging welstandsnota Amsterdam, Gemeenteblad 2026</a>',
    ),
    'putten': dict(
        regels='Putten heeft sinds februari 2026 een nieuwe Nota Ruimtelijke Kwaliteit. In de historische kern vraagt die om aardtinten en geen felle of sterk contrasterende kleuren; schoon metselwerk blijft onbeschilderd. In de woonwijken Noord en Zuidoost hoort schilderwerk in terughoudende kleuren: wit, crème of donkergroen. De excessenregeling past de gemeente terughoudend toe.',
        url='https://lokaleregelgeving.overheid.nl/CVDR757816',
        extra='',
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR757816" rel="nofollow noopener" target="_blank">Nota Ruimtelijke Kwaliteit Putten 2026</a>',
    ),
    'bunschoten-spakenburg': dict(
        regels='In het beschermde havengebied van Spakenburg is het kleurgebruik volgens de welstandsnota (2017) traditioneel en niet uitbundig, met vooral donkergroen, wit en crème. De hoofdkleuren moeten traditioneel zijn of aansluiten op de omgeving. Panden stuken of schilderen mag in het beschermde gezicht niet, behalve bij de woningen langs Kerkemaat en Havenstraat.',
        url='https://lokaleregelgeving.overheid.nl/CVDR450639/1',
        extra='Welstandsvrije gebieden noemt de nota niet. Felle of contrasterende kleuren vallen in de hele gemeente onder de excessenregeling. De nota is van vóór de Omgevingswet; vraag na of hij nog zo geldt.',
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR450639/1" rel="nofollow noopener" target="_blank">Welstandsnota Bunschoten 2017</a>',
    ),
    'naarden': dict(
        regels='Voor de vesting Naarden vraagt de welstandsnota van Gooise Meren (2019) om grote vlakken zoals deuren en luiken in Naardens groen, en kleinere delen in lichte tinten zoals wit. Nieuwe gepleisterde of geschilderde gevels horen er niet bij, en de kleuren wijken niet sterk af van die van de buren.',
        url='https://archiefbestuur.gooisemeren.nl/fileadmin/Beleidsnota_s/Monumenten/Welstandsnota_2019/Welstand_Gooise_meren_2019_zonder_straatnamenregister.pdf',
        extra='Werk aan een pand in het beschermde gezicht of aan een monument toetst de gemeente altijd, ook aan de achterkant.',
        bron='welstand: <a href="https://archiefbestuur.gooisemeren.nl/fileadmin/Beleidsnota_s/Monumenten/Welstandsnota_2019/Welstand_Gooise_meren_2019_zonder_straatnamenregister.pdf" rel="nofollow noopener" target="_blank">Welstandsnota Gooise Meren 2019</a>',
    ),
    'urk': dict(
        regels='Het Oude Dorp is een rijksbeschermd dorpsgezicht. Volgens de beleidsregels omgevingskwaliteit van november 2024 moeten materiaal, kleur en detaillering daar passen bij het pand en de omgeving, en zijn houten kozijnen het uitgangspunt. Achtererven zijn vrij van regels, behalve in het beschermde gezicht en bij monumenten. Felle of contrasterende kleuren vallen onder de excessenregeling.',
        url='https://cuatro.sim-cdn.nl/urk/uploads/beleidsregels%20word%20omgevingskwaliteit%20URK%20%207%20november%202024%20hq%20defintief%20small.pdf',
        extra='Het beeldkwaliteitplan van 2004 beschrijft groen en wit als de kleuren van het houtwerk op Urk. Dat is een beschrijving, geen regel.',
        bron='welstand: <a href="https://cuatro.sim-cdn.nl/urk/uploads/beleidsregels%20word%20omgevingskwaliteit%20URK%20%207%20november%202024%20hq%20defintief%20small.pdf" rel="nofollow noopener" target="_blank">Beleidsregels omgevingskwaliteit Urk 2024</a>',
    ),
    'elburg': dict(
        regels='Het beschermde stadsgezicht van Elburg is nooit welstandsvrij. De Nota Omgevingskwaliteit (2025) vraagt daar om kozijnen in lichte kleuren (crème, oker of wit) en draaiende delen in donkergroen of donkerblauw, met historisch onderzoek als uitgangspunt. Lijstwerk krijgt de kleur van de kozijnen, en gestucte plinten worden donkergrijs of blauwgrijs.',
        url='https://zoek.officielebekendmakingen.nl/gmb-2025-453761.pdf',
        extra='Een goede bakstenen gevel mag je daar in principe niet schilderen. Bij renovatie zijn de oorspronkelijke kleuren het uitgangspunt.',
        bron='welstand: <a href="https://zoek.officielebekendmakingen.nl/gmb-2025-453761.pdf" rel="nofollow noopener" target="_blank">Nota Omgevingskwaliteit Elburg 2025</a>',
    ),
    'blaricum': dict(
        regels='Blaricum heeft geen welstandsvrij gebied. In het beschermde dorpsgezicht zijn kozijnen en deuren van hout, geschilderd in de traditionele kleuren van het dorp: heldergroene luiken, licht okerkleurige kozijnen en wit en groen raamhout. Zo staat het in de welstandsnota van 2009, die in 2018 op onderdelen is gewijzigd.',
        url='https://zoek.officielebekendmakingen.nl/gmb-2018-134976.html',
        extra='De nota is van vóór de Omgevingswet (2024). Controleer daarom de actuele regels bij de gemeente.',
        bron='welstand: <a href="https://zoek.officielebekendmakingen.nl/gmb-2018-134976.html" rel="nofollow noopener" target="_blank">Welstandsnota Blaricum (Gemeenteblad 2018)</a>',
    ),
    'genemuiden': dict(
        regels='Zwartewaterland heeft gebieden zonder welstandstoets, maar overal geldt een excessenregeling tegen sterk afwijkend of contrasterend kleurgebruik. In de oude kern van Genemuiden moeten detaillering, materiaal en kleur passen bij het pand en de omgeving. Een vaste kleur voor kozijnen noemt de nota niet.',
        url='https://repository.overheid.nl/frbr/datacollecties/2023/dc-2023-39/1/bijlage/dc-2023-39.pdf',
        extra='De welstandsnota ‘Slimmer Bekeken’ is van 2016, en de gemeente werkt aan een nieuwe versie. Vraag na wat nu geldt.',
        bron='welstand: <a href="https://repository.overheid.nl/frbr/datacollecties/2023/dc-2023-39/1/bijlage/dc-2023-39.pdf" rel="nofollow noopener" target="_blank">Welstandsnota Zwartewaterland 2016</a>',
    ),
    'biddinghuizen': dict(
        regels='Biddinghuizen valt onder het welstandsbeleid van de gemeente Dronten. Daarin staan ook welstandsvrije gebieden, maar welke regels voor jouw straat gelden, zie je op de kaart Dronten Maps van de gemeente. Kleurregels voor kozijnen of gevels hebben we in dat beleid niet gevonden; overleg bij een felle kleur eerst met de gemeente.',
        url='https://lokaleregelgeving.overheid.nl/CVDR613553',
        extra='',
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR613553" rel="nofollow noopener" target="_blank">vergunningenbeleid gemeente Dronten</a>',
    ),
    'swifterbant': dict(
        regels='Voor Swifterbant geldt het beleid van de gemeente Dronten. Het welstandsregime verschilt per adres en staat volgens de gemeente op Dronten Maps; een deel van de gemeente is welstandsvrij. Vaste kleuren voor schilderwerk hebben we in het beleid niet aangetroffen. Bij een kleur die sterk afwijkt van de buren is navragen verstandig.',
        url='https://lokaleregelgeving.overheid.nl/CVDR613553',
        extra='',
        bron='welstand: <a href="https://lokaleregelgeving.overheid.nl/CVDR613553" rel="nofollow noopener" target="_blank">vergunningenbeleid gemeente Dronten</a>',
    ),
}

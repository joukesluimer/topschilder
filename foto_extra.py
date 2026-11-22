# -*- coding: utf-8 -*-
"""Extra foto's (kennisbank-sessie): kostenpagina's, derde foto op dienstpagina's en de kennisbank.

Alle foto's komen van Wikimedia Commons; licenties zijn op 22-11-2026 via de Commons-API gecontroleerd."""

from foto_data import FOTOS, FOTOS_PAGINA

NIEUW = {'schilder-op-ladder-nederlandse-winkelstraat': {'naam': 'schilder-op-ladder-nederlandse-winkelstraat',
                                                 'alt': 'Schilder op een trap werkt aan het witte houtwerk '
                                                        'boven een voordeur in een Nederlandse straat met '
                                                        'bakstenen huizen',
                                                 'w': 1600,
                                                 'h': 1067,
                                                 'titel': 'ZZP Groep Leiden (14490283179).jpg',
                                                 'maker': 'FaceMePLS from The Hague, The Netherlands',
                                                 'licentie': 'CC BY 2.0',
                                                 'licentie_url': 'https://creativecommons.org/licenses/by/2.0/',
                                                 'bron': 'https://commons.wikimedia.org/wiki/File:ZZP_Groep_Leiden_(14490283179).jpg',
                                                 'bewerking': 'Uitsnede van de rechterhelft (uit 4180 × 2832 '
                                                              'px), opdruk op het shirt en een winkelnaam '
                                                              'vervaagd, verkleind naar 1600, 800 en 400 px '
                                                              'breed en omgezet naar WebP.'},
 'hvlp-verfpistool-close-up': {'naam': 'hvlp-verfpistool-close-up',
                               'alt': 'Hand met een HVLP-verfpistool met een metalen verfbeker, van dichtbij',
                               'w': 1600,
                               'h': 1067,
                               'titel': 'USMC-100818-M-4913M-001.jpg',
                               'maker': 'Cpl. Salvador Moreno',
                               'licentie': 'Public domain',
                               'licentie_url': 'https://creativecommons.org/publicdomain/mark/1.0/deed.nl',
                               'bron': 'https://commons.wikimedia.org/wiki/File:USMC-100818-M-4913M-001.jpg',
                               'bewerking': 'Bijgesneden tot 3:2, verkleind naar 1600, 800 en 400 px breed '
                                            'en omgezet naar WebP. Foto van de Amerikaanse overheid; dat '
                                            'betekent niet dat die overheid deze site of onze diensten '
                                            'goedkeurt.'},
 'villa-in-de-steigers-voorgevel-elburg': {'naam': 'villa-in-de-steigers-voorgevel-elburg',
                                           'alt': 'Voorgevel van een grote villa in Elburg helemaal in de '
                                                  'steigers tijdens een restauratie',
                                           'w': 1600,
                                           'h': 1067,
                                           'titel': 'De voorgevel in de steigers tijdens restauratie - '
                                                    'Elburg - 20532568 - RCE.jpg',
                                           'maker': 'Sergé Technau',
                                           'licentie': 'CC BY-SA 4.0',
                                           'licentie_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                                           'bron': 'https://commons.wikimedia.org/wiki/File:De_voorgevel_in_de_steigers_tijdens_restauratie_-_Elburg_-_20532568_-_RCE.jpg',
                                           'bewerking': 'Bijgesneden tot 3:2, verkleind naar 1600, 800 en '
                                                        '400 px breed en omgezet naar WebP.'},
 'villa-in-de-steigers-achtergevel-elburg': {'naam': 'villa-in-de-steigers-achtergevel-elburg',
                                             'alt': 'Achtergevel van een villa in Elburg in de steigers, '
                                                    'gezien over een vijver',
                                             'w': 1600,
                                             'h': 1067,
                                             'titel': 'Achtergevel in de steigers, tijdens restauratie - '
                                                      'Elburg - 20532586 - RCE.jpg',
                                             'maker': 'Sergé Technau',
                                             'licentie': 'CC BY-SA 4.0',
                                             'licentie_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                                             'bron': 'https://commons.wikimedia.org/wiki/File:Achtergevel_in_de_steigers,_tijdens_restauratie_-_Elburg_-_20532586_-_RCE.jpg',
                                             'bewerking': 'Bijgesneden tot 3:2, verkleind naar 1600, 800 en '
                                                          '400 px breed en omgezet naar WebP.'},
 'bakstenen-muur-verven-oranje-roller': {'naam': 'bakstenen-muur-verven-oranje-roller',
                                         'alt': 'Verfroller brengt oranje verf aan op een bakstenen muur, '
                                                'met de verfemmer ernaast',
                                         'w': 1600,
                                         'h': 1067,
                                         'titel': 'Paint roller 4.jpg',
                                         'maker': 'Michael Cory',
                                         'licentie': 'CC BY 2.0',
                                         'licentie_url': 'https://creativecommons.org/licenses/by/2.0/',
                                         'bron': 'https://commons.wikimedia.org/wiki/File:Paint_roller_4.jpg',
                                         'bewerking': 'Bijgesneden tot 3:2 (uit 3867 × 2597 px), verkleind '
                                                      'naar 1600, 800 en 400 px breed en omgezet naar WebP.'},
 'nederlandse-kamer-balkenplafond-zwartwit': {'naam': 'nederlandse-kamer-balkenplafond-zwartwit',
                                              'alt': 'Kamer met een geschilderd balkenplafond en lichte '
                                                     'wanden (zwart-witfoto)',
                                              'w': 1600,
                                              'h': 1067,
                                              'titel': 'INTERIEUR, WOONKAMER - Paterswolde - 20271132 - '
                                                       'RCE.jpg',
                                              'maker': 'A. J. van der Wal',
                                              'licentie': 'CC BY-SA 4.0',
                                              'licentie_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                                              'bron': 'https://commons.wikimedia.org/wiki/File:INTERIEUR,_WOONKAMER_-_Paterswolde_-_20271132_-_RCE.jpg',
                                              'bewerking': 'Bijgesneden tot 3:2 (uit 3252 × 2216 px), '
                                                           'verkleind naar 1600, 800 en 400 px breed en '
                                                           'omgezet naar WebP.'},
 'muur-verven-met-roller-zwartwit': {'naam': 'muur-verven-met-roller-zwartwit',
                                     'alt': 'Verfroller op een half geschilderde muur, alleen de hand in '
                                            'beeld (zwart-witfoto)',
                                     'w': 1600,
                                     'h': 1067,
                                     'titel': '203 365 Painting the basement. (35705667550).jpg',
                                     'maker': 'David Mulder',
                                     'licentie': 'CC BY-SA 2.0',
                                     'licentie_url': 'https://creativecommons.org/licenses/by-sa/2.0/',
                                     'bron': 'https://commons.wikimedia.org/wiki/File:203_365_Painting_the_basement._(35705667550).jpg',
                                     'bewerking': 'Bijgesneden tot 3:2 (uit 4032 × 3024 px), verkleind naar '
                                                  '1600, 800 en 400 px breed en omgezet naar WebP.'},
 'verfbak-kwasten-en-roller-zwartwit': {'naam': 'verfbak-kwasten-en-roller-zwartwit',
                                        'alt': 'Verfbak met kwasten en een roller op afdekfolie '
                                               '(zwart-witfoto)',
                                        'w': 1600,
                                        'h': 1067,
                                        'titel': 'Tray, brush, roller, paint (4116925693).jpg',
                                        'maker': 'whereareyousimon',
                                        'licentie': 'CC BY 2.0',
                                        'licentie_url': 'https://creativecommons.org/licenses/by/2.0/',
                                        'bron': 'https://commons.wikimedia.org/wiki/File:Tray,_brush,_roller,_paint_(4116925693).jpg',
                                        'bewerking': 'Bijgesneden tot 3:2 (uit 4000 × 3000 px), verkleind '
                                                     'naar 1600, 800 en 400 px breed en omgezet naar WebP.'},
 'nederlandse-woonkamer-klassiek-interieur': {'naam': 'nederlandse-woonkamer-klassiek-interieur',
                                              'alt': 'Nederlandse woonkamer met lichte wanden, wit houtwerk '
                                                     'en een schouw',
                                              'w': 1600,
                                              'h': 1067,
                                              'titel': 'Interieur, overzicht woonkamer - Achtmaal - 20002885 '
                                                       '- RCE.jpg',
                                              'maker': 'Ger Barbiers',
                                              'licentie': 'CC BY-SA 4.0',
                                              'licentie_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                                              'bron': 'https://commons.wikimedia.org/wiki/File:Interieur,_overzicht_woonkamer_-_Achtmaal_-_20002885_-_RCE.jpg',
                                              'bewerking': 'Bijgesneden tot 3:2 (uit 2870 × 2322 px), '
                                                           'verkleind naar 1600, 800 en 400 px breed en '
                                                           'omgezet naar WebP.'},
 'dakkapel-verweerd-houten-kozijn': {'naam': 'dakkapel-verweerd-houten-kozijn',
                                     'alt': 'Dakkapel met een verweerd wit houten kozijn op een oud dak',
                                     'w': 1600,
                                     'h': 1067,
                                     'titel': 'Kencot dilapidated cottage dormer window West Oxfordshire '
                                              'England.jpg',
                                     'maker': 'Acabashi',
                                     'licentie': 'CC BY-SA 4.0',
                                     'licentie_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                                     'bron': 'https://commons.wikimedia.org/wiki/File:Kencot_dilapidated_cottage_dormer_window_West_Oxfordshire_England.jpg',
                                     'bewerking': 'Bijgesneden tot 3:2 (uit 4567 × 3653 px), verkleind naar '
                                                  '1600, 800 en 400 px breed en omgezet naar WebP.'},
 'aangetast-houten-balk-met-meetlint': {'naam': 'aangetast-houten-balk-met-meetlint',
                                        'alt': 'Houten balk aangetast door bruinrot, met een meetlint '
                                               'ernaast voor de schaal',
                                        'w': 1600,
                                        'h': 1067,
                                        'titel': 'Braunfaeule Holz FI20070208.jpg',
                                        'maker': 'Mätes II.',
                                        'licentie': 'CC BY-SA 3.0',
                                        'licentie_url': 'https://creativecommons.org/licenses/by-sa/3.0/',
                                        'bron': 'https://commons.wikimedia.org/wiki/File:Braunfaeule_Holz_FI20070208.jpg',
                                        'bewerking': 'Bijgesneden tot 3:2 (uit 2288 × 1447 px), verkleind '
                                                     'naar 1600, 800 en 400 px breed en omgezet naar WebP.'},
 'bruinrot-blokbreuk-hout-close-up': {'naam': 'bruinrot-blokbreuk-hout-close-up',
                                      'alt': 'Hout met blokvormige scheuren door bruinrot, van dichtbij',
                                      'w': 1600,
                                      'h': 1067,
                                      'titel': 'Pourriture brune cubique 04.2025 (1).jpg',
                                      'maker': 'DidierFy',
                                      'licentie': 'CC BY-SA 4.0',
                                      'licentie_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                                      'bron': 'https://commons.wikimedia.org/wiki/File:Pourriture_brune_cubique_04.2025_(1).jpg',
                                      'bewerking': 'Bijgesneden tot 3:2 (uit 8192 × 6144 px), verkleind naar '
                                                   '1600, 800 en 400 px breed en omgezet naar WebP.'},
 'stationsgebouw-leeuwarden-in-de-steigers': {'naam': 'stationsgebouw-leeuwarden-in-de-steigers',
                                              'alt': 'Stationsgebouw van Leeuwarden in de steigers en '
                                                     'ingepakt in doek tijdens een renovatie',
                                              'w': 1600,
                                              'h': 1067,
                                              'titel': 'Renovatie stationsgebouw Leeuwarden (2024).jpg',
                                              'maker': 'Sneeuwvlakte',
                                              'licentie': 'CC BY-SA 4.0',
                                              'licentie_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                                              'bron': 'https://commons.wikimedia.org/wiki/File:Renovatie_stationsgebouw_Leeuwarden_(2024).jpg',
                                              'bewerking': 'Bijgesneden tot 3:2 (uit 4608 × 3456 px), '
                                                           'verkleind naar 1600, 800 en 400 px breed en '
                                                           'omgezet naar WebP.'},
 'structuurbehang-witte-wand': {'naam': 'structuurbehang-witte-wand',
                                'alt': 'Wit geschilderd structuurbehang op een wand, van dichtbij',
                                'w': 1600,
                                'h': 1067,
                                'titel': 'Tapetentextur 20190822.jpg',
                                'maker': 'PantheraLeo1359531',
                                'licentie': 'CC0',
                                'licentie_url': 'https://creativecommons.org/publicdomain/zero/1.0/',
                                'bron': 'https://commons.wikimedia.org/wiki/File:Tapetentextur_20190822.jpg',
                                'bewerking': 'Bijgesneden tot 3:2, verkleind naar 1600, 800 en 400 px breed '
                                             'en omgezet naar WebP.'},
 'kamer-met-goudkleurig-behang-en-schouw': {'naam': 'kamer-met-goudkleurig-behang-en-schouw',
                                            'alt': 'Kamer met goudkleurig behang met motief naast een grijze '
                                                   'schouw',
                                            'w': 1600,
                                            'h': 1067,
                                            'titel': 'Fireplace and wallpaper 20211113 124502.jpg',
                                            'maker': 'CaptJayRuffins',
                                            'licentie': 'CC BY-SA 4.0',
                                            'licentie_url': 'https://creativecommons.org/licenses/by-sa/4.0/',
                                            'bron': 'https://commons.wikimedia.org/wiki/File:Fireplace_and_wallpaper_20211113_124502.jpg',
                                            'bewerking': 'Bijgesneden tot 3:2 (uit 4032 × 3024 px), '
                                                         'verkleind naar 1600, 800 en 400 px breed en '
                                                         'omgezet naar WebP.'},
 'verweerde-blauwe-houten-schutting': {'naam': 'verweerde-blauwe-houten-schutting',
                                       'alt': 'Verweerde blauwe houten schutting waar de verf van afbladdert',
                                       'w': 1600,
                                       'h': 1067,
                                       'titel': 'Alt Blau Holz-Zaun.jpg',
                                       'maker': 'ZeWrestler',
                                       'licentie': 'CC BY-SA 3.0',
                                       'licentie_url': 'https://creativecommons.org/licenses/by-sa/3.0/',
                                       'bron': 'https://commons.wikimedia.org/wiki/File:Alt_Blau_Holz-Zaun.jpg',
                                       'bewerking': 'Bijgesneden tot 3:2 (uit 5184 × 3127 px), verkleind '
                                                    'naar 1600, 800 en 400 px breed en omgezet naar WebP.'},
 'monumentale-voordeur-amsterdam': {'naam': 'monumentale-voordeur-amsterdam',
                                    'alt': 'Stenen gevel met een monumentale zwarte deur en ramen met '
                                           'smeedwerk in Amsterdam',
                                    'w': 1600,
                                    'h': 1067,
                                    'titel': 'Old stone facade with gate and windows, Amsterdam old city - '
                                             'free photo, Fons Heijnsbroek.jpg',
                                    'maker': 'Fons Heijnsbroek',
                                    'licentie': 'CC0',
                                    'licentie_url': 'https://creativecommons.org/publicdomain/zero/1.0/',
                                    'bron': 'https://commons.wikimedia.org/wiki/File:Old_stone_facade_with_gate_and_windows,_Amsterdam_old_city_-_free_photo,_Fons_Heijnsbroek.jpg',
                                    'bewerking': 'Bijgesneden tot 3:2 (uit 5984 × 4488 px), verkleind naar '
                                                 '1600, 800 en 400 px breed en omgezet naar WebP.'},
 'grachtenhuizen-met-woonboten': {'naam': 'grachtenhuizen-met-woonboten',
                                  'alt': 'Rij grachtenhuizen in Amsterdam met woonboten op de gracht',
                                  'w': 1600,
                                  'h': 1067,
                                  'titel': 'Amsterdam Canal Houses (Unsplash).jpg',
                                  'maker': 'Kaci Baum kacibaum',
                                  'licentie': 'CC0',
                                  'licentie_url': 'https://creativecommons.org/publicdomain/zero/1.0/',
                                  'bron': 'https://commons.wikimedia.org/wiki/File:Amsterdam_Canal_Houses_(Unsplash).jpg',
                                  'bewerking': 'Bijgesneden tot 3:2, verkleind naar 1600, 800 en 400 px '
                                               'breed en omgezet naar WebP.'}}

N = NIEUW

# Kopfoto per kostenpagina (bovenaan, in de prijskaart). Zonder eigen foto valt de pagina terug op de dienstfoto.
KOSTEN_FOTOS = {
    "keuken-spuiten": N["hvlp-verfpistool-close-up"],
    "trap-schilderen": N["verfbak-kwasten-en-roller-zwartwit"],
    "kozijnen-schilderen": N["schilder-op-ladder-nederlandse-winkelstraat"],
    "schilder-uurtarief": N["muur-verven-met-roller-zwartwit"],
    "huis-schilderen": N["villa-in-de-steigers-voorgevel-elburg"],
    "schilderen-per-m2": N["bakstenen-muur-verven-oranje-roller"],
    "plafond-schilderen": N["nederlandse-kamer-balkenplafond-zwartwit"],
    "latex-spuiten": FOTOS["spuitwerk"]["sectie"],
    "deuren-spuiten": FOTOS["spuitwerk"]["hero"],
    "dakkapel-schilderen": N["dakkapel-verweerd-houten-kozijn"],
}

# Sectiefoto op een kostenpagina als die anders gelijk zou zijn aan de kopfoto.
KOSTEN_SECTIE = {
    "latex-spuiten": N["hvlp-verfpistool-close-up"],
    "deuren-spuiten": N["hvlp-verfpistool-close-up"],
}

# Derde foto op elke dienstpagina, bij "Waar hangt de prijs vanaf?".
DIENST_EXTRA = {
    "binnenschilderwerk": N["nederlandse-woonkamer-klassiek-interieur"],
    "buitenschilderwerk": N["schilder-op-ladder-nederlandse-winkelstraat"],
    "houtrot-reparatie": N["aangetast-houten-balk-met-meetlint"],
    "spuitwerk": N["hvlp-verfpistool-close-up"],
    "behangen": N["kamer-met-goudkleurig-behang-en-schouw"],
    "zakelijk-schilderwerk": N["stationsgebouw-leeuwarden-in-de-steigers"],
}

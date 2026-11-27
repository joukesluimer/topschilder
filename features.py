# -*- coding: utf-8 -*-
"""Features-sessie: één aanroep vanuit build.py voor de nieuwe tools.

build.py roept alleen build_features(write, OUT) aan. Nieuwe tools komen hier bij,
zodat build.py klein blijft.
"""

from deelbeeld import schrijf_deelbeeld
from gevelkleur import build_gevelkleur
from onderhoudskalender import build_onderhoudskalender
from verfcalculator import build_verfcalculator


def build_features(write, out):
    schrijf_deelbeeld(out)
    build_onderhoudskalender(write, out)
    build_verfcalculator(write, out)
    build_gevelkleur(write, out)

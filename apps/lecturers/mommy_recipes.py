# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from model_mommy.recipe import Recipe

from . import models


lecturer = Recipe(models.Lecturer,
    id=1337,
    title='Prof. Dr.',
    first_name='David',
    last_name='Krakaduku',
    abbreviation='KRA',
    email='krakaduku@hsr.ch',
    office='1.337',
    subjects='Quantenphysik, Mathematik für Mathematiker',
)

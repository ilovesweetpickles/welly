#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines well location.

:copyright: 2016 Agile Geoscience
:license: Apache 2.0
"""
from . import utils
from .crs import CRS


class Location(object):
    def __init__(self, params):
        """
        Generic initializer for now.
        """
        self.crs = CRS(params.pop('crs', dict()))

        for k, v in params.items():
            if k and v:
                setattr(self, k, v)

    def __repr__(self):
        return 'Location({})'.format(self.__dict__)

    @classmethod
    def from_lasio_well(cls, well, remap=None, funcs=None):
        """
        Assumes we're starting with a lasio well object.
        """
        params = {}
        for field, code in fields.items():
            params[field] = utils.lasio_get_from_well(well, code, remap=remap, funcs=funcs)

        return cls(params)


fields = {
    # WELLY <->  LAS
    'country': 'CTRY',
    'latitude': 'LATI',
    'longitude': 'LONG',
    'datum': 'GDAT',
    'section': 'SECT',
    'range': 'RANG',
    'township': 'TOWN',
    }

# -*- coding: utf-8 -*-

from django import VERSION


def get_val_from_obj(self, obj):
    if VERSION < (2, 0):
        return self._get_val_from_obj(obj)
    if obj is not None:
        return getattr(obj, self.attname)
    else:
        return self.get_default()

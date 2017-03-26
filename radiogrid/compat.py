# -*- coding: utf-8 -*-

import re

from django import VERSION
from django.utils import six
from django.utils.safestring import mark_safe


def add_meta_class(field):
    if VERSION < (1, 8):
        from django.db.models import SubfieldBase
        return six.add_metaclass(SubfieldBase)(field)
    return field


def widget_render(rendered):
    if VERSION < (1, 8):
        rendered = rendered.replace('li', 'td')
        rendered = re.compile(r'<ul.+>|</ul>').sub('', rendered)
        return mark_safe(rendered)
    return rendered


def get_val_from_obj(self, obj):
    if VERSION < (2, 0):
        return self._get_val_from_obj(obj)
    if obj is not None:
        return getattr(obj, self.attname)
    else:
        return self.get_default()

# -*- coding: utf-8 -*-

from django.forms import MultiValueField, ChoiceField

from .widgets import RadioGridWidget


class RadioGridFormField(MultiValueField):

    def __init__(self, rows, values, *args, **kwargs):
        fields = []
        for _ in rows:
            fields.append(ChoiceField(choices=values, required=False))
        kwargs['widget'] = RadioGridWidget(rows, values)
        kwargs['fields'] = fields
        super(RadioGridFormField, self).__init__(*args, **kwargs)

    def compress(self, data_list):
        return '' if data_list is None else ','.join(data_list)

# -*- coding: utf-8 -*-

from django.forms import RadioSelect, MultiWidget


class RadioRadioSelect(RadioSelect):
    template_name = 'radiogrid/radiogrid_input.html'


class RadioGridWidget(MultiWidget):
    input_type = 'grid'
    template_name = 'radiogrid/radiogrid_widget.html'

    def __init__(self, rows, values, attrs=None):
        self.rows = rows
        self.values = values
        choices = [(k, '') for k, _ in values]
        widgets = [RadioRadioSelect(choices=choices, attrs=attrs) for _ in rows]
        super(RadioGridWidget, self).__init__(widgets, attrs)

    def get_context(self, name, value, attrs):
        context = super(RadioGridWidget, self).get_context(name, value, attrs)
        widgets = context['widget']['subwidgets']
        return {
            'rows': [(v[1], widgets[i]) for i, v in enumerate(self.rows)],
            'values': self.values,
            'attrs': self.attrs
        }

    def decompress(self, value):
        if value:
            return value.split(',')
        return [None for _ in self.rows]

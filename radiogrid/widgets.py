# -*- coding: utf-8 -*-

from django import VERSION

if VERSION < (1, 11):
    from django.forms.widgets import RadioSelect, MultiWidget, RadioFieldRenderer
    from django.utils.safestring import mark_safe
    from django.template.loader import render_to_string

    from radiogrid.compat import widget_render


    class RadioChoiceFieldRenderer(RadioFieldRenderer):
        outer_html = '{content}'
        inner_html = '<td>{choice_value}{sub_widgets}</td>'

        def __init__(self, name, value, attrs, choices):
            attrs['class'] = ''
            super(RadioChoiceFieldRenderer, self).__init__(name, value, attrs, choices)

        def render(self):
            rendered = super(RadioChoiceFieldRenderer, self).render()
            return widget_render(rendered)


    class RadioRadioSelect(RadioSelect):
        renderer = RadioChoiceFieldRenderer


    class RadioGridWidget(MultiWidget):
        input_type = 'grid'

        def __init__(self, rows, values, attrs=None):
            self.rows = rows
            self.values = values
            choices = [(k, '') for k, _ in values]
            widgets = [RadioRadioSelect(choices=choices, attrs=attrs) for _ in rows]
            super(RadioGridWidget, self).__init__(widgets, attrs)

        def decompress(self, value):
            if value:
                return value.split(',')
            return [None for _ in self.rows]

        def format_output(self, rendered_widgets):
            widgets = {}
            for i, v in enumerate(rendered_widgets):
                widgets[i] = v
            return mark_safe(render_to_string('radiogrid/radiogrid_widget.html', {
                'rows': [(v[1], widgets[i]) for i, v in enumerate(self.rows)],
                'values': self.values,
                'attrs': self.attrs
            }))
else:
    from django.forms import RadioSelect, MultiWidget
    from django.utils.safestring import mark_safe
    from django.template.loader import render_to_string


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

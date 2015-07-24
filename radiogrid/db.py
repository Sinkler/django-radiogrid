# -*- coding: utf-8 -*-

from django.db.models import TextField

from .fields import RadioGridFormField


class RadioGridField(TextField):

    def __init__(self, *args, **kwargs):
        self.rows = kwargs.pop('rows')
        self.values = kwargs.pop('values')
        self.require_all_fields = kwargs.pop('require_all_fields', True)
        self.verbose_name = kwargs.get('verbose_name', '')
        super(RadioGridField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'rows': self.rows,
            'values': self.values,
            'require_all_fields': self.require_all_fields,
            'label': self.verbose_name,
        }
        defaults.update(kwargs)
        return RadioGridFormField(**defaults)

    def deconstruct(self):
        name, path, args, kwargs = super(RadioGridField, self).deconstruct()
        kwargs['rows'] = self.rows
        kwargs['values'] = self.values
        kwargs['require_all_fields'] = self.require_all_fields
        return name, path, args, kwargs

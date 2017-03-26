from django import VERSION
from django.core.exceptions import ValidationError
from django.forms.models import modelform_factory
from django.test import TestCase

from radiogrid import RadioGridWidget

from example.app.models import Octodex, Octoduck, WEEK_ROWS, WEEK_VALUES


if VERSION < (1, 9):
    def get_field(model, name):
        return model._meta.get_field_by_name(name)[0]
else:
    def get_field(model, name):
        return model._meta.get_field(name)


class MultiSelectTestCase(TestCase):
    fixtures = ['data.json']

    def test_filter(self):
        self.assertEqual(Octodex.objects.filter(categories__contains='pyha').count(), 1)
        self.assertEqual(Octodex.objects.filter(categories__contains='crash').count(), 0)

    def test_form(self):
        form_class = modelform_factory(Octodex, fields=['title', 'categories', 'week'])
        self.assertEqual(len(form_class.base_fields), 3)

        form = form_class({
            'title': 'new octodex',
            'categories_0': 'work',
            'categories_1': 'pyha',
            'categories_2': 'food',
            'week_0': '5',
            'week_1': '4',
            'week_2': '3',
            'week_3': '2',
            'week_4': '1',
            'week_5': '2',
            'week_6': '3',
        })
        self.assertTrue(form.is_valid())

        form = form_class({
            'title': 'new octodex',
            'categories_0': 'die',
            'categories_1': 'phpforum',
            'categories_2': 'depression',
            'week_0': '11',
            'week_1': '23',
            'week_2': '34',
            'week_3': '666',
            'week_4': '74',
            'week_5': '123',
            'week_6': '9',
        })
        self.assertFalse(form.is_valid())

        self.assertTrue(form.as_p())

    def test_object(self):
        octodex = Octodex.objects.get(id=1)

        self.assertEqual(octodex.get_categories_display(), 'Pyha, Work, Happy')
        self.assertEqual(octodex.get_categories_list(), ['Pyha', 'Work', 'Happy'])

        self.assertEqual(octodex.get_week_display(),
                         '2-3 hours, 3-4 hours, 5-7 hours, 8 hours, Never, 8 hours, 5-7 hours')
        self.assertEqual(octodex.get_week_list(),
                         ['2-3 hours', '3-4 hours', '5-7 hours', '8 hours', 'Never', '8 hours', '5-7 hours'])

        self.assertEqual(octodex.get_categories_list(), octodex.get_categories_display().split(', '))
        self.assertEqual(octodex.get_categories_list(), octodex.get_categories_display().split(', '))

        self.assertEqual(octodex.get_week_list(), octodex.get_week_display().split(', '))
        self.assertEqual(octodex.get_week_list(), octodex.get_week_display().split(', '))

        octoduck = Octoduck.objects.get(id=1)
        self.assertEqual(octoduck.get_week_display(),
                         '2-3 hours, 3-4 hours, duck, 8 hours, Never, 8 hours, 5-7 hours')

    def test_validate(self):
        octodex = Octodex.objects.get(id=1)
        try:
            get_field(Octodex, 'categories').clean(['phpforum', 'work'], octodex)
            raise AssertionError()
        except ValidationError:
            pass
        try:
            get_field(Octodex, 'week').clean(['13', '666'], octodex)
            raise AssertionError()
        except ValidationError:
            pass

    def test_serializer(self):
        octodex = Octodex.objects.get(id=1)
        self.assertEqual(get_field(Octodex, 'categories').value_to_string(octodex), 'pyha,work,happy')
        self.assertEqual(get_field(Octodex, 'week').value_to_string(octodex), '1,2,3,4,5,4,3')
        self.assertEqual(get_field(Octodex, 'week').value_to_string(None), '')

    def test_widget(self):
        widget = RadioGridWidget(rows=WEEK_ROWS, values=WEEK_VALUES)
        self.assertTrue(widget.render('days', 'work,pyha,food'))
        self.assertTrue(widget.render('days', None))

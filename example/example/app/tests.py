from django.core.exceptions import ValidationError
from django.forms.models import modelform_factory
from django.test import TestCase

from example.app.models import Octodex


class MultiSelectTestCase(TestCase):
    fixtures = ['data.json']

    def test_filter(self):
        self.assertEqual(Octodex.objects.filter(categories__contains='pyha').count(), 1)
        self.assertEqual(Octodex.objects.filter(categories__contains='crash').count(), 0)

    def test_form(self):
        form_class = modelform_factory(Octodex, fields=['title', 'categories'])
        self.assertEqual(len(form_class.base_fields), 2)

        form = form_class({
            'title': 'new octodex',
            'categories_0': 'work',
            'categories_1': 'pyha',
            'categories_2': 'food'
        })
        self.assertTrue(form.is_valid())

        form = form_class({
            'title': 'new octodex',
            'categories_0': 'die',
            'categories_1': 'phpforum',
            'categories_2': 'depression'
        })
        self.assertFalse(form.is_valid())

    def test_object(self):
        octodex = Octodex.objects.get(id=1)

        self.assertEqual(octodex.get_categories_display(), 'Pyha, Work, Happy')
        self.assertEqual(octodex.get_categories_list(), ['Pyha', 'Work', 'Happy'])

        self.assertEqual(octodex.get_categories_list(), octodex.get_categories_display().split(', '))
        self.assertEqual(octodex.get_categories_list(), octodex.get_categories_display().split(', '))

    def test_validate(self):
        octodex = Octodex.objects.get(id=1)
        try:
            Octodex._meta.get_field_by_name('categories')[0].clean(['phpforum', 'work'], octodex)
            raise AssertionError()
        except ValidationError:
            pass

    def test_serializer(self):
        octodex = Octodex.objects.get(id=1)
        self.assertEqual(Octodex._meta.get_field_by_name('categories')[0].value_to_string(octodex), 'pyha,work,happy')

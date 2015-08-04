# -*- coding: utf-8 -*-

from django.db import models

from radiogrid import RadioGridField

CATEGORIES_ROWS = (
    (1, 'First'),
    (2, 'Second'),
    (3, 'Third'),
)

CATEGORIES_VALUES = (
    ('pyha', 'Pyha'),
    ('work', 'Work'),
    ('happy', 'Happy'),
    ('food', 'Food'),
)

WEEK_ROWS = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)

WEEK_VALUES = (
    (1, '2-3 hours'),
    (2, '3-4 hours'),
    (3, '5-7 hours'),
    (4, '8 hours'),
    (5, 'Never'),
)


class Octodex(models.Model):
    title = models.CharField(max_length=50)
    categories = RadioGridField(rows=CATEGORIES_ROWS, values=CATEGORIES_VALUES, require_all_fields=True)
    week = RadioGridField(rows=WEEK_ROWS, values=WEEK_VALUES, require_all_fields=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()

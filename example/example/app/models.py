# -*- coding: utf-8 -*-

from django.db import models

from radiogrid import RadioGridField

ROWS = (
    (1, 'First'),
    (2, 'Second'),
    (3, 'Third'),
)

VALUES = (
    ('pyha', 'Pyha'),
    ('work', 'Work'),
    ('happy', 'Happy'),
    ('food', 'Food'),
)


class Octodex(models.Model):
    title = models.CharField(max_length=50)
    categories = RadioGridField(rows=ROWS, values=VALUES, require_all_fields=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()

django-radiogrid
================

.. image:: https://badge.fury.io/py/django-radiogrid.png
    :target: https://badge.fury.io/py/django-radiogrid

With this you can create a radio grid field:

.. image:: https://api.monosnap.com/rpc/file/download?id=4rJ1neeFuwSMlonpWaQyd65LPR9R62
    :target: https://api.monosnap.com/rpc/file/download?id=4rJ1neeFuwSMlonpWaQyd65LPR9R62

Installation
============

::

    pip install django-radiogrid

In your settings.py
-------------------

::

    INSTALLED_APPS = (
        # ...

        'radiogrid',
    )

In your models.py
-----------------

::

    from radiogrid import RadioGridField

    ...

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

    class MyModel(models.Model):

        .....

        my_grid = RadioGridField(rows=ROWS, values=VALUES, require_all_fields=True)

Example project
===============

You can run it as usual:

::

    virtualenv venv
    . venv/bin/activate
    pip install django
    pip install -e .
    cd example
    ./manage.py migrate
    ./manage.py loaddata data
    ./manage.py runserver

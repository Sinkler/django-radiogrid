django-radiogrid
================

.. image:: https://travis-ci.org/Sinkler/django-radiogrid.svg
    :target: https://travis-ci.org/Sinkler/django-radiogrid

.. image:: https://coveralls.io/repos/Sinkler/django-radiogrid/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/Sinkler/django-radiogrid?branch=master

.. image:: https://codeclimate.com/github/Sinkler/django-radiogrid/badges/gpa.svg
    :target: https://codeclimate.com/github/Sinkler/django-radiogrid

.. image:: https://img.shields.io/pypi/l/django-radiogrid.svg
    :target: https://pypi.python.org/pypi/django-radiogrid

.. image:: https://img.shields.io/pypi/v/django-radiogrid.svg
    :target: https://pypi.python.org/pypi/django-radiogrid

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

    # ...

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

        # ...

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
    ./manage.py test

or

::

    docker-compose up app
    docker-compose run --rm app test

Developing
==========

Testing
-------

::

    docker-compose run --rm app test
    docker-compose run --rm app coverage
    docker-compose run --rm tox tox -e py36-django-master
    docker-compose run --rm tox

Releasing
---------

- add a new version description in ``CHANGES.rst``
- change a version in ``__init__.py``
- ``docker-compose run --rm app release``
- add a github release

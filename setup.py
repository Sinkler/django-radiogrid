#!/usr/bin/env python

import os
import radiogrid
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name="django-radiogrid",
    version=radiogrid.__version__,
    author="Anton Shurashov",
    author_email="sinkler@sinkler.ru",
    description="Django radio grid field",
    long_description=(read('README.rst') + '\n\n' + read('CHANGES.rst')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    license="LGPL 3",
    keywords="django,radio,grid,field,choices",
    url='https://github.com/Sinkler/django-radiogrid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

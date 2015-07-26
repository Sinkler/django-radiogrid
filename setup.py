#!/usr/bin/env python

import os
import re
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name="django-radiogrid",
    version=get_version('radiogrid'),
    author="Anton Shurashov",
    author_email="sinkler@sinkler.ru",
    description="Django radio grid field",
    long_description=(read('README.rst') + '\n\n' + read('CHANGES.rst')),
    install_requires = ['django>=1.7.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
    zip_safe=False
)

#!/usr/bin/env python

import os
import sys

from django.conf import ENVIRONMENT_VARIABLE
from django.core import management
from django.core.wsgi import get_wsgi_application


if len(sys.argv) == 1:
    os.environ[ENVIRONMENT_VARIABLE] = 'example.settings'
else:
    os.environ[ENVIRONMENT_VARIABLE] = sys.argv[1]

application = get_wsgi_application()

management.call_command('test', 'example.app')

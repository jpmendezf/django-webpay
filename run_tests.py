# !/usr/bin/env python
# -*- coding:utf-8 -*-
import django
import os
import sys
from django.conf import settings

DIRNAME = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    URL_CGI_VALIDA_MAC="webpay/tests/test_files/tbk_check_mac.cgi",
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    ROOT_URLCONF='webpay.urls',
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'webpay',
        'webpay.tests'
    ),
    LOGGER_WEBPAY='logger_webpay',
    USE_TZ=True)

try:
    # Django < 1.8
    from django.test.simple import DjangoTestSuiteRunner
except ImportError:
    # Django >= 1.8
    from django.test.runner import DiscoverRunner as DjangoTestSuiteRunner

django.setup()
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['webpay', ])
if failures:
    sys.exit(failures)

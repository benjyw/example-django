# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.settings_base import *

WSGI_APPLICATION = "helloworld.service.user.wsgi.application"

ROOT_URLCONF = "helloworld.service.user.urls"

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "helloworld.person",
]

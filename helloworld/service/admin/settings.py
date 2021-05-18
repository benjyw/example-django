# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.settings_base import *

WSGI_APPLICATION = "helloworld.service.welcome.wsgi.application"

ROOT_URLCONF = "helloworld.service.admin.urls"

MIDDLEWARE += [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.messages",
    "helloworld.greet",
    "helloworld.person",
    "helloworld.translate",
]

set_up_database("users")
set_up_database("greetings")

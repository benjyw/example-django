# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
from typing import List

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "DEV_SECURITY_KEY"

DEBUG = True

ALLOWED_HOSTS: List[str] = []

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Application definition

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    #"django.contrib.sessions.middleware.SessionMiddleware",
    #"django.contrib.auth.middleware.AuthenticationMiddleware",
    #"django.contrib.messages.middleware.MessageMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEV_PORTS = {
    "helloworld.service.frontend": 8000,
    "helloworld.service.admin": 8001,
    "helloworld.service.user": 8010,
    "helloworld.service.welcome": 8020,
}

# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.settings_base import *

WSGI_APPLICATION = "helloworld.service.welcome.wsgi.application"

ROOT_URLCONF = "helloworld.service.ui.urls"

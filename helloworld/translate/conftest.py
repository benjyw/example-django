# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
from tempfile import mkdtemp

from django.conf import settings


def pytest_configure():
    settings.configure(
        TIME_ZONE="UTC",
        USE_TZ=True,
        INSTALLED_APPS=["helloworld.greet", "helloworld.translate"],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(mkdtemp(), "test.sqlite3"),
            }
        },
    )

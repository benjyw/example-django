# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
import sys


class Service:
    def __init__(self, module: str):
        self._module = module

    def run_gunicorn(self):
        # If no args were provided, fill them in for convenience.
        if len(sys.argv) == 1:
            sys.argv.extend(
                ["--config", "python:helloworld.gunicorn_conf", f"{self._module}.wsgi"]
            )
        from gunicorn.app.wsgiapp import run
        sys.exit(run())

    def run_manage(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{self._module}.settings")
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)

    def wsgi_application(self):
        from django.core.wsgi import get_wsgi_application
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{self._module}.settings")
        return get_wsgi_application()


# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
import sys
from pathlib import PurePath


class Service:
    def __init__(self, name_or_file: str):
        if os.path.sep in name_or_file:
            # This is the __file__ of the caller, so compute the service name.
            rparts = list(reversed(PurePath(name_or_file).parts))
            self._name = ".".join(reversed(rparts[1:rparts.index("helloworld")+1]))
        else:
            self._name = name_or_file

    def run_gunicorn(self):
        # If no args were provided, fill them in for convenience.
        if len(sys.argv) == 1:
            sys.argv.extend(
                ["--config", "python:helloworld.gunicorn_conf", f"{self._name}.wsgi"]
            )
        from gunicorn.app.wsgiapp import run
        sys.exit(run())

    def run_manage(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{self._name}.settings")
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)

    def wsgi_application(self):
        from django.core.wsgi import get_wsgi_application
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{self._name}.settings")
        return get_wsgi_application()


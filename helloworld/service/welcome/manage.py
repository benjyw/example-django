#!/usr/bin/env ./python
# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
import sys


def main():
    # Allows us to reference packages (e.g., helloworld.django.settings) from the source root.
    # Without this Django assumes that these references are relative to the directory containing manage.py.
    # sys.path.insert(0, os.getcwd())

    # Standard Django manage.py boilerplate.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloworld.service.welcome.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

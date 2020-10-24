#!/usr/bin/env python
# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
import sys


def main():
    # Allows us to reference packages (e.g., helloworld.settings) from the source root.
    # Without this Django assumes that these references are relative to the directory containing manage.py.
    sys.path.insert(0, os.getcwd())

    # Standard Django manage.py boilerplate.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

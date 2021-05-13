# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import sys

from gunicorn.app.wsgiapp import run

if __name__ == "__main__":
    # If no args were provided, fill them in for convenience.
    if len(sys.argv) == 1:
        sys.argv.extend(
            ["--config", "python:helloworld.gunicorn_conf", "helloworld.wsgi"]
        )
    sys.exit(run())

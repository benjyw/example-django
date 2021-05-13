# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    # We depend on migrations explicitly, since Pants cannot yet infer this dependency.
    "helloworld/greet/migrations",
)

python_tests(name = 'tests',
    dependencies = [
        "helloworld",  # For settings.py.
    ]
)

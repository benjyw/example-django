# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# `name` defaults to the name of this directory, i.e., `greet`.
# `sources` defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
# `dependencies` are inferred.
python_library(
    # We depend on migrations explicitly, since Pants cannot infer this dependency.
    "helloworld/greet/migrations",
)

# `sources` defaults to ['*_test.py', 'test_*.py', 'conftest.py'].
# `dependencies` are inferred.
python_tests(name = 'tests',
    dependencies = [
        "helloworld",  # For settings.py.
        "//:pytest",
        "//:pytest_ini",
    ]
)

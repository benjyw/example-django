# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    dependencies = [
        "helloworld/greet",
        "helloworld/person",
        "helloworld/translate",
    ]
)

pex_binary(
    name = "manage",
    entry_point = 'manage.py',
    dependencies = [
        ":helloworld",
    ],
)

pex_binary(
    name = 'gunicorn',
    entry_point = 'gunicorn.py',
    dependencies = [
        ':helloworld',
    ],
)

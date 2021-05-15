# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    dependencies = [
        "helloworld/greet",
"helloworld/translate"
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

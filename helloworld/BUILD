# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    dependencies = [
        "helloworld/greet"
    ]
)

pex_binary(
    name = "manage",
    entry_point = 'helloworld.manage',
    dependencies = [
        ":helloworld",
    ],
)

pex_binary(
    name = 'gunicorn',
    entry_point = 'helloworld.gunicorn',
    dependencies = [
        ':helloworld',
    ],
)

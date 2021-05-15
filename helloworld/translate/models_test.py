# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pytest

from helloworld.greet.models import Greeting


@pytest.mark.django_db
def test_database_is_seeded():
    hello = Greeting.objects.get(slug="hello")
    translations = set(hello.translations_set())
    assert {} == translations
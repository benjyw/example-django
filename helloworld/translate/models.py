# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.db import models


class Translation(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["lang", "english_word"], name="lang_english_word")
        ]

    lang = models.CharField(max_length=2)
    english_word = models.CharField(max_length=20)
    lang_word = models.CharField(max_length=20)

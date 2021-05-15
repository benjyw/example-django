# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.db import models


class Greeting(models.Model):
    slug = models.CharField(max_length=30, unique=True)
    salutation = models.CharField(max_length=30)

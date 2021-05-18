# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from enum import Enum

from django.conf import settings


class Mode(Enum):
  DEV = "DEV"
  STAGING = "STAGING"
  PROD = "PROD"


def get_mode() -> Mode:
  return Mode[getattr(settings, "MODE", "DEV")]
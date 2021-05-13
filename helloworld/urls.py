# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.urls import include, path

urlpatterns = [
    path("greet/", include("helloworld.greet.urls")),
]

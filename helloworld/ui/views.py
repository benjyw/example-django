# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import requests
from django.http import Http404, HttpResponse

from helloworld.util.backend import get_backend_url


def query_backend(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 404:
        raise Http404(f"Backend error: {url}")
    # All other backend errors should become 500 errors for the frontend.
    response.raise_for_status()
    return response.text


def index(request) -> HttpResponse:
    person_slug = request.GET.get("person", "")
    lang = request.GET.get("lang", "en")

    # Get person's full name.
    name = query_backend(f"{get_backend_url('helloworld.service.user')}/person/{person_slug}")

    # Get greeting.
    greeting = query_backend(f"{get_backend_url('helloworld.service.welcome')}/translate/hello/{lang}")
    return HttpResponse(f"RENDER FOR: {greeting} {name}")

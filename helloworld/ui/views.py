# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import requests
from django.http import Http404, HttpResponse

from helloworld.util.backend import get_backend_url


def index(request) -> HttpResponse:
    person_slug = request.GET.get("name", "")
    lang = request.GET.get("lang", "en")
    person_url_prefix = get_backend_url("helloworld.service.user")
    person_url = f"{person_url_prefix}/person/{person_slug}"
    response = requests.get(person_url)
    if response.status_code == 404:
        raise Http404(f"Backend error: {person_url}")
    # All other backend errors should become 500 errors for the frontend.
    response.raise_for_status()
    name = response.text
    return HttpResponse(f"RENDER FOR: {name} in {lang}")

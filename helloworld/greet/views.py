# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from datetime import time

from django.http import Http404, HttpResponse

from helloworld.greet.models import Greeting


def index(request, slug):
    try:
        greeting = Greeting.objects.get(slug=slug)
        return HttpResponse(greeting.salutation)
    except Greeting.DoesNotExist:
        raise Http404(f"No such greeting: {slug}")


def for_time_of_day(request, time_of_day: str):
    greeting = Greeting.for_time_of_day(time.fromisoformat(time_of_day))
    if not greeting:
        # Fall back to a generic greeting.
        greeting = Greeting.objects.get(slug="hello")
    return HttpResponse(greeting.salutation)

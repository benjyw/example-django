# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.http import Http404, HttpResponse

from helloworld.greet.models import Greeting


def index(request, slug):
    try:
        greeting = Greeting.objects.get(slug=slug)
        return HttpResponse(greeting.salutation)
    except Greeting.DoesNotExist:
        raise Http404(f"No such greeting: {slug}")

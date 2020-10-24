# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.http import HttpResponse, Http404

from helloworld.greet.models import PersonToGreet


def index(request, slug):
    try:
        person_to_greet = PersonToGreet.objects.get(slug=slug)
        return HttpResponse(f"Hello, {person_to_greet.full_name}")
    except PersonToGreet.DoesNotExist:
        raise Http404(f"No such person: {slug}")

# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.http import Http404, HttpResponse

from helloworld.person.models import Person


def index(request, slug):
    try:
        person = Person.objects.get(slug=slug)
        return HttpResponse(f"Hello, {person.full_name}")
    except Person.DoesNotExist:
        raise Http404(f"No such person: {slug}")

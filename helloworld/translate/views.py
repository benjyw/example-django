# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.http import Http404, HttpResponse

from helloworld.translate.models import Translation


def index(request, lang: str, english_word: str) -> HttpResponse:
    try:
        translation = Translation.objects.get(lang=lang, english_word=english_word)
        return HttpResponse(translation.lang_word)
    except Translation.DoesNotExist:
        raise Http404(f"No translation in {lang} for: {english_word}")

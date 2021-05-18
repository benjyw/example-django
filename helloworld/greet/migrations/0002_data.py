# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from django.db import migrations


def create_greetings(apps, schema_editor):
    Greeting = apps.get_model("greet", "Greeting")

    def create(slug: str, salutation: str) -> None:
        Greeting(slug=slug, salutation=salutation).save()

    create("hello", "Hello")
    create("howareyou", "How are you")
    create("goodmorning", "Good morning")
    create("goodevening", "Good evening")
    create("goodnight", "Good night")


class Migration(migrations.Migration):

    dependencies = [
        ("greet", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_greetings),
    ]

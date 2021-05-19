# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.util.service import Service


application = Service("helloworld.service.welcome").wsgi_application()

#!/usr/bin/env bash
# Copyright 2020 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# See https://www.pantsbuild.org/v2.0/docs/python-third-party-dependencies.

set -euo pipefail

PYTHON_BIN=python3
VIRTUALENV=build-support/.venv
PIP="${VIRTUALENV}/bin/pip"
CONSTRAINTS_FILE=constraints.txt

"${PYTHON_BIN}" -m venv "${VIRTUALENV}"
"${PIP}" install pip --upgrade
"${PIP}" install -r <(./pants dependencies --type=3rdparty ::) -r requirements.txt
echo "# Generated by build-support/generate_constraints.sh on $(date)" > "${CONSTRAINTS_FILE}"
"${PIP}" freeze --all >> "${CONSTRAINTS_FILE}"

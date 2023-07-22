#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e
# Print commands and their arguments as they are executed.
set -x

pytest --cov=app --cov-report=term-missing app/tests "${@}"
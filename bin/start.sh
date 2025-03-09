#!/bin/bash
poetry install --no-root
poetry run ./manage.py migrate
poetry run ./manage.py runserver 0.0.0.0:8000

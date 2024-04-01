#!/bin/bash
source "$HOME/development/igor-vanin/homework-7/django_venv/bin/activate"
API_WORK_DIR="$HOME/development/igor-vanin/homework-7/django-rest-api/DjangoRestApi"
FRONT_WORK_DIR="$HOME/development/igor-vanin/homework-7/react-crud-web-api"

cd "$API_WORK_DIR"
python manage.py runserver 8080 &
cd "$FRONT_WORK_DIR"
npm start &

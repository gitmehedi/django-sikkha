#!/bin/bash

python manage.py makemigrations
echo "---------------- Migrations Created --------------"
python manage.py migrate
echo "------------- Database changes done  -------------"

python manage.py runserver 8000

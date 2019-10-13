#!/bin/sh
sudo python manage.py makemigrations
sudo python manage.py migrate
sudo kill -9 $(lsof -i:8000 |awk '{print $2}' | tail -n 2)
nohup python manage.py runserver 0.0.0.0:8000 &


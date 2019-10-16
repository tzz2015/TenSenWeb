#!/bin/sh
cd /home/python-project/wx-mini
sudo setsid ./sunny clientid 462d2b0c471d87f1 &
#sudo /etc/init.d/sunny restart
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
sudo kill -9 $(lsof -i:8000 |awk '{print $2}' | tail -n 2)
nohup sudo python3 manage.py runserver 0.0.0.0:8000 &


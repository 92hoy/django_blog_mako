venv:
	virtualenv -p python3.6 venv

req:
	pip install -r requirements.txt

db:
	docker-compose up -d

mmig:
	python manage.py makemigrations backend

mig:
	python manage.py migrate

fmig:
	python manage.py migrate --fake backend zero

sql:
	mysql -h127.0.0.1 -P3316 -uroot -p0000 -e"use main;"

mysql:
	mysql -h127.0.0.1 -P3316 -uroot -p0000

server:
	python manage.py runserver 0.0.0.0:8888

#mysql -h127.0.0.1 -P3316 -uroot -p0000 -e"use main;source make.sql;"

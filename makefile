setup:
	python3 -m venv virtual
	source virtual/bin/activate
	pip3 install -r requirements.txt --ignore-installed

makemigrations:
	./virtual/bin/python manage.py makemigrations

migrate:
	./virtual/bin/python manage.py migrate

run:
	./virtual/bin/python manage.py runserver
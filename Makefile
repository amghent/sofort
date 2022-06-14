install:
	poetry update
	poetry install

run: migrate
	python src/manage.py runserver

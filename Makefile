SHELL := /bin/bash

SQLCMD := /opt/mssql-tools/bin/sqlcmd

install:
	poetry update
	poetry install

superuser:
	python src/manage.py auto_create_superuser

reset_migrations:
	rm -f src/bookmarks/migrations/0001_initial.py
	rm -f src/core/migrations/0001_initial.py
	rm -f src/forums/migrations/0001_initial.py
	rm -f src/interests/migrations/0001_initial.py
	rm -f src/issues/migrations/0001_initial.py
	rm -f src/links/migrations/0001_initial.py
	rm -f src/members/migrations/0001_initial.py
	rm -f src/newsletters/migrations/0001_initial.py
	rm -f src/pages/migrations/0001_initial.py
	rm -f src/questions/migrations/0001_initial.py
	rm -f src/tags/migrations/0001_initial.py
	rm -f src/tutorials/migrations/0001_initial.py

migrate:
	python src/manage.py makemigrations
	python src/manage.py migrate

sample_data:
	python src/manage.py sample_data

run: migrate
	python src/manage.py runserver

##
#	Database commands
#
ms_sa_secret:
	@ source ./src/bootstrap/management/config/mssql/sa.secret

ms_drop_login: ms_sa_secret
	@ $(SQLCMD) -S localhost -C -U sa -P "$(MSSQL_SA_PASSWORD)" -i ./src/bootstrap/management/sql/mssql/drop_login.sql

ms_create_login:
	@ $(SQLCMD) -S localhost -C -U sa -P "$(MSSQL_SA_PASSWORD)" -i ./src/bootstrap/management/sql/mssql/create_login.sql

ms_drop_db:
	@ $(SQLCMD) -S localhost -C -U sa -P "$(MSSQL_SA_PASSWORD)" -i ./src/bootstrap/management/sql/mssql/drop_db.sql

ms_create_db:
	@ $(SQLCMD) -S localhost -C -U sa -P "$(MSSQL_SA_PASSWORD)" -i ./src/bootstrap/management/sql/mssql/create_db.sql

ms_reset_db: ms_drop_db ms_create_db

pg_create_db:
	sudo -u postgres psql -d postgres -f src/bootstrap/management/sql/postgres/create_db.sql ;

pg_reset_db: pg_create_db reset_migrations migrate superuser sample_data



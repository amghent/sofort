###
#
# Makefile to automate tasks during development
#
# note: On windows, use Cmder to run this.  
#
SHELL := /bin/bash

SQLCMD := /opt/mssql-tools/bin/sqlcmd

install:
	poetry update
	poetry install

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

###
# settings for local development at Arcelor Mittal Ghent
create_db_am:
	rm -f ./db/db.sqlite3

migrate_am:
	python src/manage.py makemigrations --settings=sofort.settings.am
	python src/manage.py migrate --settings=sofort.settings.am

superuser_am:
	python src/manage.py auto_create_superuser --settings=sofort.settings.am

sample_data_am:
	python src/manage.py sample_data --settings=sofort.settings.am

reset_db_am: create_db_am reset_migrations migrate_am superuser_am sample_data_am

run_am: migrate_am
	python src/manage.py runserver --settings=sofort.settings.am
#
###

###
# settings for local development at vindevoy's Linux pc
create_db_local:
	sudo -u postgres psql -d postgres -f src/bootstrap/management/sql/postgres/create_db.sql ;

migrate_local:
	python src/manage.py makemigrations --settings=sofort.settings.local
	python src/manage.py migrate --settings=sofort.settings.local

superuser_local:
	python src/manage.py auto_create_superuser --settings=sofort.settings.local

sample_data_local:
	python src/manage.py sample_data --settings=sofort.settings.local

reset_db_local: create_db_local reset_migrations migrate_local superuser_local sample_data_local

run_local: migrate_local
	python src/manage.py runserver --settings=sofort.settings.local
#
###

##
#	Database commands SQL server - To be tested again
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
#
##

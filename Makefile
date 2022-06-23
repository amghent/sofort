###
#
# Makefile to automate tasks during development
#
# note: On windows, use Cmder to run this.  
#
SHELL := /bin/bash
MS_SQLCMD := /opt/mssql-tools/bin/sqlcmd

###
#
install:
	poetry update
	poetry install
#
###

###
#
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
#
###

###
#
validate:
ifndef SETTINGS
	@echo "Specify SETTINGS to set the environment"
	@exit 1
endif
#
###

###
#
login: validate
ifeq ("$(SETTINGS)", "sofort.settings.mssql")
	source ./src/bootstrap/management/config/mssql/sa.secret && \
	$(MS_SQLCMD) -S localhost -C -U sa -P "$(MSSQL_SA_PASSWORD)" -i ./src/bootstrap/management/sql/mssql/drop_login.sql  && \
	$(MS_SQLCMD) -S localhost -C -U sa -P "$(MSSQL_SA_PASSWORD)" -i ./src/bootstrap/management/sql/mssql/create_login.sql
endif
#
###

###
#
create_db: validate
ifeq ("$(SETTINGS)", "sofort.settings.sqlite3")
	rm -rf ./db/db.sqlite3
endif

ifeq ("$(SETTINGS)", "sofort.settings.postgres")
	sudo -u postgres psql -d postgres -f src/bootstrap/management/sql/postgres/create_db.sql ;
endif

ifeq ("$(SETTINGS)", "sofort.settings.mssql")
	source ./src/bootstrap/management/config/mssql/sa.secret && \
	$(MS_SQLCMD) -S localhost -C -U sa -P "$(MSSQL_SA_PASSWORD)" -i ./src/bootstrap/management/sql/mssql/drop_db.sql && \
	$(MS_SQLCMD) -S localhost -C -U sa -P "$(MSSQL_SA_PASSWORD)" -i ./src/bootstrap/management/sql/mssql/create_db.sql
endif
#
###

###
#
migrate: validate
	python src/manage.py makemigrations --settings=$(SETTINGS)
	python src/manage.py migrate --settings=$(SETTINGS)
#
###

###
#
superuser: validate
	python src/manage.py auto_create_superuser --settings=$(SETTINGS)
#
###

###
#
sample_data: validate
	python src/manage.py sample_data --settings=$(SETTINGS)
#
###

###
#
reset_db: validate create_db reset_migrations migrate superuser sample_data
#
###

###
#
css:
	lessc ./src/_templates/default/static/css/sofort.less ./src/_templates/default/static/css/sofort.css
#
###

###
#
run: validate css migrate
	python src/manage.py runserver --settings=$(SETTINGS)
#
###

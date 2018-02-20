createsuperuser:
	python django_source_code/manage.py createsuperuser
migrate:
	python django_source_code/manage.py migrate
makemigrations:
	python django_source_code/manage.py makemigrations api
destroymigrations:
	rm -fr ./django_source_code/api/migrations
	rm ./django_source_code/db.sqlite3
runserver:
	python django_source_code/manage.py runserver
mock_up_data:
	python django_source_code/manage.py loaddata item_sets
development:
	gunicorn -w 5 \
		-b 0.0.0.0:8000 \
		--chdir ./django_source_code/ \
		--reload \
		--timeout 1000 \
		thatgamecompany_interview_exercise.wsgi
do_migrate: makemigrations \
			migrate
nukeboot: destroymigrations \
			do_migrate \
			runserver
cleanboot: do_migrate \
			runserver
deploy: destroymigrations \
		makemigrations \
		migrate \
		mock_up_data \
		development


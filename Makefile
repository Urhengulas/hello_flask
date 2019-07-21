FLASK_APP:=flaskr
FLASK_ENV:=development


run:
	make run-production

run-development:
	FLASK_APP=$(FLASK_APP) \
	FLASK_ENV=$(FLASK_ENV) \
	env/bin/flask run --host=0.0.0.0

run-production:
	FLASK_APP=$(FLASK_APP) \
	FLASK_ENV="production" \
	env/bin/waitress-serve --call 'flaskr:create_app'

dep:
	if [ ! -d "env" ];then virtualenv env;fi
	env/bin/pip install -r requirements.txt

db:
	FLASK_APP=$(FLASK_APP) \
	FLASK_ENV=$(FLASK_ENV) \
	env/bin/flask init-db

test:
	# TESTS
	env/bin/coverage run -m pytest -vvv

	# COVERAGE
	env/bin/coverage report

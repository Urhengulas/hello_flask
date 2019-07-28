FLASK_APP:=flaskr
FLASK_ENV:=development


run:
	make run-production

run-development:
	FLASK_APP=$(FLASK_APP) \
	FLASK_ENV=$(FLASK_ENV) \
	env/bin/flask run --host=0.0.0.0

run-production:
	env/bin/waitress-serve --call 'flaskr:create_app'


setup:
	make dep
	make key

dep:
	if [ ! -d "env" ];then virtualenv env;fi
	env/bin/pip install -r requirements.txt

key:
	touch env/var/flaskr-instance/config.py
	echo "SECRET_KEY = \\" > env/var/flaskr-instance/config.py
	echo """    $(shell python -c """import os; print(os.urandom(16).replace(b'\n', b'\t'))""")""" >> env/var/flaskr-instance/config.py


test:
	# TESTS
	env/bin/coverage run -m pytest -vvv

	# COVERAGE
	env/bin/coverage report

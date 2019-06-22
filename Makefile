FLASK_APP:=flaskr
FLASK_ENV:=development


run:
	FLASK_APP=$(FLASK_APP) \
	FLASK_ENV=$(FLASK_ENV) \
	env/bin/flask run --host=0.0.0.0

run-local:
	FLASK_APP=$(FLASK_APP) \
	FLASK_ENV=$(FLASK_ENV) \
	env/bin/flask run

dep:
	if [ ! -d "env" ];then virtualenv env;fi
	env/bin/pip install -r requirements.txt

db:
	FLASK_APP=$(FLASK_APP) \
	FLASK_ENV=$(FLASK_ENV) \
	env/bin/flask init-db

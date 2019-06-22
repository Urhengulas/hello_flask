run:
	FLASK_APP=app.py \
	FLASK_ENV=development \
	env/bin/flask run --host=0.0.0.0

run-local:
	FLASK_APP=app.py \
	FLASK_ENV=development \
	env/bin/flask run

dep:
	if [ ! -d "env" ];then python -m venv env;fi
	env/bin/pip install -r requirements.txt

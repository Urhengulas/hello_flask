run:
	export FLASK_APP=hello.py
	flask run

dep:
	if [ ! -d "env" ];then python -m venv env;fi
	env/bin/pip install -r requirements.txt

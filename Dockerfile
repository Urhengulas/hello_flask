FROM python:3.7-slim

WORKDIR /app

COPY docker_requirements.txt .
RUN pip install -r docker_requirements.txt

COPY flaskr ./flaskr

EXPOSE 8080

ENTRYPOINT [ "waitress-serve", "--call", "flaskr:create_app" ]

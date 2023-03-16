FROM python:3.11-alpine

RUN pip install Flask pyyaml prometheus-flask-exporter
WORKDIR /app

COPY service.py service.py

ENV FLASK_APP=service.py
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]


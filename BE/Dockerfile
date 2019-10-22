FROM python:3.6-slim
COPY . /srv/flask_app
WORKDIR /srv/flask_app
RUN apt-get clean \
    && apt-get -y update
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "application"]
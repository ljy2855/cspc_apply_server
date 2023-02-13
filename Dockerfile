FROM python:3.8.13

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME

WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt $APP_HOME/requirements.txt

RUN pip install --no-cache-dir --upgrade -r $APP_HOME/requirements.txt



COPY . $APP_HOME

RUN python manage.py makemigrations

RUN python manage.py migrate --no-input
RUN python manage.py collectstatic --no-input
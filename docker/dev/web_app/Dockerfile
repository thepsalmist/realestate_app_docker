# pull official base image
FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

# Create an app user
RUN useradd --user-group --create-home --no-log-init --shell /bin/bash app

ENV  APP_HOME=/home/app/web_app

# Create the staticfiles directory. This avoids the permission errors
RUN mkdir -p $APP_HOME/staticfiles

#set work directory
WORKDIR $APP_HOME 

COPY ./app/requirements.txt $APP_HOME

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY ./app $APP_HOME
COPY ./docker/dev/web_app/entrypoint.sh $APP_HOME/entrypoint.sh

RUN chown -R app:app $APP_HOME
RUN chmod +x $APP_HOME/entrypoint.sh

#user
USER app:app

# entrypoint
ENTRYPOINT [ "/home/app/web/entrypoint.sh" ]
# /home/thealchemist/Desktop/projects/new_developers/docker/web_app/entrypoint.sh
# docker/web_app/entrypoint.sh
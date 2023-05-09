###########
# BUILDER #
###########
# pull official base image
FROM python:3.10.6-alpine as builder
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# lint
RUN pip install --upgrade pip
COPY . .
# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
#########
# FINAL #
#########

# pull official base image
FROM python:3.10.6-alpine
# create directory for the app user
RUN mkdir -p /home/app
# create the app user
RUN addgroup -S app && adduser -S app -G app
# create dir for upploads file
ARG UPLOAD_FOLDER
ENV UPLOAD_FOLDER $UPLOAD_FOLDER
RUN mkdir -p $UPLOAD_FOLDER
# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/image_service
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . $APP_HOME
# chown all the files to the app user
RUN chown -R app:app $HOME
# change to the app user
USER app
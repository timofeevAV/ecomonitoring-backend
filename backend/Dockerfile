# pull official base image
FROM python:3.12.1-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache --upgrade pip
RUN pip install --no-cache -r requirements.txt
RUN pip install --no-cache gunicorn

# copy django project
COPY . .
COPY .env ./server

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
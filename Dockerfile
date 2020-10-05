FROM ubuntu:16.04
MAINTAINER Luiz Gerhardt <luizogfernandes@gmail.com>

USER root

RUN apt-get update -qqy
RUN apt-key update
RUN apt-get -qqy --no-install-recommends install \
    python3 \
    python3-pip \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install flask
RUN pip3 install flask-request-validator

RUN mkdir /app
COPY ./app /app
COPY ./input_files /input_files

WORKDIR /
CMD ["python3", "app/Controllers/RouteController.py"]
FROM python:3.10.8

RUN mkdir /opt/app
WORKDIR /opt

COPY ./app/ /opt/app
COPY requirements.txt .

RUN pip3 install pip==23.0.1 -r requirements.txt

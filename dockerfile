FROM python:3.11-slim

WORKDIR /app
ADD . /app

RUN pip3 install -r requirements.txt

EXPOSE 8221
CMD python3 main.py

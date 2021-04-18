FROM python:3.8-slim-buster

WORKDIR /client/

RUN pip3 install requests

COPY . .

CMD [ "python3",  "./client.py" ]

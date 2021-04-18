FROM python:3.8-slim-buster

WORKDIR /server/

# set flask env
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# install flask requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

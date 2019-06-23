FROM python:3.6.8

COPY requirements.txt /code/
WORKDIR /code/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y aapt

COPY . /code/

CMD [ "./startup.sh" ]
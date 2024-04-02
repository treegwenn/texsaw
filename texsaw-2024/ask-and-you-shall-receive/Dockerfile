FROM python:latest

ADD . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
EXPOSE 80

CMD ["python3", "webapp.py"]

FROM python:3.8.3-slim-buster

WORKDIR /src

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "simple-mqtt-client.py"]
# mosquitto-example
This repository contains a running example of feeding data from a simple python mqtt client (running in a docker container) through an mqtt broker (Mosquitto, running in a docker container) over Telegraf (running in a docker container) to Inflixdb (running in a docker container) and visualising it in Grafana (running in a docker container)

All config and data files are included as volumes in the repository

To start everything, run

    docker compose up

from the command line at the root of the repository.

Access the services using:

[Grafana](http://localhost:3000)
user: admin
password: adminadmin
port: 3000
Grafana has been pre-condifured with an InflixDB API token (Read-Only)

[Influxdb](http://localhost:8086)
user: admin
password: adminadmin
port: 8086

Telegraf:
has been pre-configred with an inflixdb API Token (Read/Write)

Mosquitto:
has been preconfigured to allow anonymus access
port: 1086

[NodeRed](http://localhost:1880)
An example flow has been added that subscribes to the PING MQTT Topic
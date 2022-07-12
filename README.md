# mosquitto-example
This repository contains a running example of feeding data from a simple python mqtt client (running in a docker container) through an mqtt broker (Mosquitto, running in a docker container) over Telegraf (running in a docker container) to Inflixdb (running in a docker container) and visualising it in Grafana (running in a docker container)

All config and data files are included as volumes in the repository

To start everything, run

    docker compose up

from the command line at the root of the repository.

Access the services using:

[Grafana](localhost:3000)

[Influxdb](localhost:8086)

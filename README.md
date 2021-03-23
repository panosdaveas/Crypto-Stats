# Crypto-Stats
Implementation of bitcoin asset database

# Overview
Run a containerized `mongoDB`.

# Usage

Run it at the foreground (hit ctrl-c to stop):
```
docker-compose up
```

or

Run it at the background:
```
docker-compose up -d
```

Stop it:
```
docker-compose down
```
Use Docker GUI to set up custom ports and volume directories. Defaults
are:
* port: 27017
* database volume: ./database

# Notes
Be sure to have your system's `mongo`'s service stopped, or running at a different port.

# API
Request limit from [coinAPI](https://rest.coinapi.io/v1/assets/BTC) = 100 / day

# Current State

![myplot](https://user-images.githubusercontent.com/63146477/112148330-6cdb9180-8be6-11eb-9b99-3cabbe073fc7.png)

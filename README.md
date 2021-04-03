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
Request limit from [coinAPI](https://docs.coinapi.io/#md-rest-api) = 100 / day

# PIPENV

to enable `pipenv`, run
```
$ pipenv shell
$ python main.py
```

to run without loading the virtual environment:
```
pipenv run python main.py
```
# Crontab

add a cronjob to run ```main.py``` from inside\
the pipenv shell :
```
*/10 * * * * cd path/to/file/ && /usr/local/bin/pipenv run python main.py
```

# Current State

![Screen Recording 2021-03-24 at 10 46 33 AM](https://user-images.githubusercontent.com/63146477/112281434-b8e21100-8c8e-11eb-97e7-7b3577a1dad3.gif)


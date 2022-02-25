# claims

## Requirements

- Python 3.9+
- redis

## Prepare

- Its possible to configure redis to connect to a different port

```config
REDIS_HOST: Default 'redis'
REDIS_PORT: Default '6379'
```

- The backend needs a `redis` instance running to store the claims data.

```sh
redis-server
```

- Create virtual env and run the api

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python api.py
```


## Load db

To load the db run the following command with `redis-server` running 

`file` should be the csv containing the claims data.

```sh
source .venv/bin/activate
python loaddb.py [file]
```
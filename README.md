# circuit-db-backend
## Installation

### Requirements:
1. python >= 3.7
2. docker >= 19.03.8
3. docker-compose >= 1.25.0

```
$ git clone git@github.com:mannenen/circuit-db-backend.git
$ python3 -m venv .venv
$ source .venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Running

Create a `.env` file with values for the following keys:

1. `DEBUG` - whether to run the app in debug mode or not (default=False)
2. `TESTING` - whether the app is under test or not (default=False)
3. `MONGODB_HOSTNAME` - the hostname of the MongoDB server (default=`mongo`)
4. `MONGODB_TABLENAME` - the name of the database table to store data (default=`test_data`)

`$ docker-compose up -d --build`

The backend is available at `http://localhost:5000/api/v1`
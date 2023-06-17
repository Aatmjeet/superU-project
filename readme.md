# SuperU Project

### Description

This is a basic `REST API` application on `Django and Django rest_framework`
which supports basic `CRUD` operations.

Tech Stack:
```
Python
Django Rest-framework
Postgres
Simple-JWT
```

In the current version of this project, I have only added `User` entity i.e.
the project contains APIs to create/update/get User.
Alongside the user APIs, I have also provided `login` and `logout` APIs to get authorization tokens.

As for the `Authorization`, we are using `Bearer` mode `JWT` to validate user request.

---

## Setup
### Prerequisites
To run this project on a machine, we need `Python` and `Postgres` database as basic requirements.
To install both, Just use google :)

### Install Steps
- We start by creating a virtual environment, I have used `virtual` as the
name of environment.
```python
python -m venv virtual
```
- Once that is done, we navigate to bin and activate the environment

```shell
source virtual/bin/activate
```

- Now we install the dependencies through the `requirements.txt` file
```python
pip install -r requirements.txt
```

Now that we've installed the required dependencies, we move on to setting up the project.

### Setup
Once the dependencies are installed, we set out project up.

- This project uses `.env` file to store all our secret keys, so create a `.env` file and store following variables
```.dotenv
DB_NAME={your database name}
DB_USER={your database user's name}
DB_PASSWORD={your database user's password}
DB_HOST=127.0.0.1 or {url of database if using remote databse}
DB_PORT=5432
```

- After this is done, we migrate our model
```shell
python3 manage.py migrate
```

- Now that migration is done, we are ready to run our application

```shell
python3 manage.py runserver
```
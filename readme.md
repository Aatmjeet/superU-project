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
---

## Usage

- The resources provided in this project are as follows
```
- /user/ POST to create user
- /user/ PATCH to update user
- /user/<str:email> GET to get the user information
- /login/ POST with user name and password to get access token
```

- `/user/ POST` does not require any authorization, to create user.
- Once we create a user, we could send a `POST` request to `/login/` to get `access` and `refresh` token
- Now we could use this `access` token as `Bearer ${access}` as `Authorization` header in our request.

---
## Unit Tests

I have written a test case for create user endpoint `/user/` `POST` using `factory-boy`
and `faker`. 

It is stored in the `tests/` directory in of `user_app`.

Following is the command to run create user test case
```shell
python3 manage.py test user_app.tests.test_user_api
```
# Casting Agency Project

This project is the Capstone project for the Full Stack Web Developer Nanodegree program. It aims to create a RESTful API for a casting agency.

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Hosted API
The API is currently hosted on Render and can be accessed at the following URL: 
https://capstone-cyuj.onrender.com/

Localhost URL: http://127.0.0.1:5000

## Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Creaete environment & setup Auth0

Create the environment variables with the DATABASE_URL, AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, AUTH0_DOMAIN, APP_SECRET_KEY, and API_AUDIENCE

```
AUTH0_CLIENT_ID={CLIENT_ID}
AUTH0_CLIENT_SECRET={CLIENT_SECRET}
AUTH0_DOMAIN={DOMAIN}
APP_SECRET_KEY=RandomlyString

API_AUDIENCE={API_AUDIENCE}

DATABASE_URL={DATABASE_URL}
```



## Running the server

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Endpoints

- GET /movies: Retrieve a list of all movies.
- POST /movies: Create a new movie.
- PATCH /movies/{movie_id}: Update an existing movie.
- DELETE /movies/{movie_id}: Delete a movie.

- GET /actors: Retrieve a list of all actors.
- POST /actors: Create a new actor.
- PATCH /actors/{actor_id}: Update an existing actor.
- DELETE /actors/{actor_id}: Delete an actor.

## RBAC Controls

This project implements three roles: 'Assistant', 'Director' and 'Producer'.

- Casting Assistant
    + Can view actors and movies
- Casting Director
    + All permissions a Casting Assistant has and…
    + Add or delete an actor from the database
    + Modify actors or movies
- Executive Producer
    + All permissions a Casting Director has and…
    + Add or delete a movie from the database

## Testing

Before test, must update `.env` file, add 3 variable to `.env` file
```
ASSISTANT_TOKEN={YOUR_TOKEN}
DIRECTOR_TOKEN={YOUR_TOKEN}
PRODUCER_TOKEN={YOUR_TOKEN}
```

To get your token, you can access the following [URL](https://capstone-cyuj.onrender.com/) to login, and receive a JWT token.

To run the test suite, execute the following command:

```bash
dropdb casting_test
createdb casting_test
psql casting_test < casting_test.sql
python test_app.py
```
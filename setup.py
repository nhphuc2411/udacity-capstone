from dotenv import find_dotenv, load_dotenv
from os import environ as env

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


APP_SECRET_KEY = env.get("APP_SECRET_KEY")
AUTH0_CLIENT_ID = env.get("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = env.get("AUTH0_CLIENT_SECRET")
AUTH0_DOMAIN = env.get("AUTH0_DOMAIN")
API_AUDIENCE = env.get("API_AUDIENCE")
ALGORITHMS = ["RS256"]

DATABASE_URL = env.get("DATABASE_URL")

ASSISTANT_TOKEN = env.get('ASSISTANT_TOKEN')
DIRECTOR_TOKEN = env.get('DIRECTOR_TOKEN')
PRODUCER_TOKEN = env.get('PRODUCER_TOKEN')


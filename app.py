from os import environ
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from application.controllers.pokemons import pokemons_resource


try:
    load_dotenv(verbose=False)
except Exception as e:
    print(f"Can't load dotenv. {e}")

BASE_PATH_SERVER = environ["BASE_PATH_SERVER"]

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

app.register_blueprint(pokemons_resource.blueprint, url_prefix=BASE_PATH_SERVER)

if __name__ == "__main__":
    app.run()










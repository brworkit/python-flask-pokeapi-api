import requests
from os import environ
from http import HTTPStatus
from application.utils import log, json, constants

class PokemonService(object):
    def __init__(self):
        pass
        
    def assets(self, id):                
        url = environ["PATH_POKEMON"].format(id)            
        response = requests.get(url)
        result = json.to_json(response.text)["sprites"]
        
        for field in dict(result):
            if result[field] is None:
                del result[field]            
        return result


   
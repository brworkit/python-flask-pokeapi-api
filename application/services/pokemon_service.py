import requests
from os import environ
from http import HTTPStatus
from cachetools import cached, TTLCache
from application.utils import log, json, constants

class PokemonService(object):
    def __init__(self):
        pass
    
    @cached(cache=TTLCache(maxsize=int(environ["CACHE_MAX_SIZE"]), ttl=int(environ["CACHE_TTL_SECONDS"])))
    def assets(self, id):
        url = environ["PATH_POKEMON"].format(id)
        response = requests.get(url)
        result = json.to_json(response.text)["sprites"]

        for field in dict(result):
            if result[field] is None:
                del result[field]
        return result

    @cached(cache=TTLCache(maxsize=int(environ["CACHE_MAX_SIZE"]), ttl=int(environ["CACHE_TTL_SECONDS"])))
    def essentials(self, id):
        url = environ["PATH_POKEMON"].format(id)
        response = requests.get(url,timeout=10)
        result = json.to_json(response.text)
        return self.extract_essentials(result)

    @cached(cache=TTLCache(maxsize=int(environ["CACHE_MAX_SIZE"]), ttl=int(environ["CACHE_TTL_SECONDS"])))
    def essentials_range(self, _from, _to):
        result = []
        start_id = _from
        end_id = _to + 1
        for id in range(start_id, end_id):
            print(f"id: {id}")
            result.append(self.essentials(id))         
        return result

    def default_image(self, id):        
        return self.assets(id)["front_default"]

    def extract_essentials(self, _input):        
        return {
            "id": _input["id"],
            "order": _input["order"],
            "name": _input["name"],
            "weight": _input["weight"],
            "height": _input["height"],
            "base_experience": _input["base_experience"],
            "types": self.extract_types(_input),
            "color": self.find_pokemon_color(_input["id"]),
            "image":self.default_image(_input["id"])
        }

    def extract_types(self, _input):
        print("extract_types")
        types = _input["types"]
        print(f"types: {types}")

        result = []
        for item in types:
            try:
                type_name = item["type"]["name"]
                result.append({"name": type_name, "color": self.define_color_type(type_name)})
            except Exception as e:
                print(f"exception: {e}")            
        return  result

    @cached(cache=TTLCache(maxsize=int(environ["CACHE_MAX_SIZE"]), ttl=int(environ["CACHE_TTL_SECONDS"])))
    def find_pokemon_color(self, id):
        url = environ["PATH_POKEMON_COLORS"].format(id)
        try:
            response = requests.get(url)
            return json.to_json(response.text)["name"]
        except Exception as e:
            return self.define_pokemon_color(id)
        
    @cached(cache=TTLCache(maxsize=int(environ["CACHE_MAX_SIZE"]), ttl=int(environ["CACHE_TTL_SECONDS"])))
    def define_color_type(self, type_name):
        switch = {
            "grass": "green",
            "poison": "purple",
            "bug": "light_green"
        }
        return switch.get(type_name, "black")

    @cached(cache=TTLCache(maxsize=int(environ["CACHE_MAX_SIZE"]), ttl=int(environ["CACHE_TTL_SECONDS"])))
    def define_pokemon_color(self, id):
        switch = {
            11: "light_green"
        }
        return switch.get(id, "black")


    

















    #         {
        #     "abilities": [
        #         {
        #             "ability": {
        #                 "name": "chlorophyll",
        #                 "url": "https://pokeapi.co/api/v2/ability/34/"
        #             },
        #             "is_hidden": true,
        #             "slot": 3
        #         },
        #         {
        #             "ability": {
        #                 "name": "overgrow",
        #                 "url": "https://pokeapi.co/api/v2/ability/65/"
        #             },
        #             "is_hidden": false,
        #             "slot": 1
        #         }
        #     ],
        #     "base_experience": 64,
        #     "height": 7,
        #     "held_items": [],
        #     "id": 1,
        #     "is_default": true,
        #     "location_area_encounters": "https://pokeapi.co/api/v2/pokemon/1/encounters",
        #     "name": "bulbasaur",
        #     "order": 1,
        #     "species": {
        #         "name": "bulbasaur",
        #         "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
        #     },
        #    
        # }
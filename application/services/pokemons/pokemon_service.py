from os import environ
from application.lib import pokeapi


class PokemonService(object):
    def __init__(self):
        pass

    def sprites(self, id):
        result = pokeapi.pokemons(id)["sprites"]
        for field in dict(result):
            if result[field] is None:
                del result[field]
        return result

    def essentials(self, id):
        result = pokeapi.pokemons(id)
        return self.extract_essentials(result)

    def essentials_range(self, _from, _to):
        result = []
        start_id = _from
        end_id = _to + 1
        for id in range(start_id, end_id):            
            result.append(self.essentials(id))
        return result

    def default_image(self, id):
        return self.sprites(id)["front_default"]

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
            "image": self.default_image(_input["id"])
        }

    def extract_types(self, _input):
        types = _input["types"]
        result = []
        for item in types:
            try:
                result.append(self.build_type(item))
            except Exception as e:
                print(f"exception: {e}")
        return result

    def build_type(self, item):
        type_name = item["type"]["name"]
        return {"name": type_name, "color": self.define_color_type(type_name)}

    def find_pokemon_color(self, id):
        try:
            return pokeapi.pokemons_color(id)["name"]
        except Exception as e:
            return self.define_pokemon_color(id)

    def define_color_type(self, type_name):
        switch = {
            "grass": "green",
            "poison": "purple",
            "bug": "light_green"
        }
        return switch.get(type_name, "black")

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

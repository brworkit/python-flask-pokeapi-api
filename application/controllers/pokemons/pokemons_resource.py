from http import HTTPStatus
from flask import Blueprint, jsonify, request
from application.services.pokemons.pokemon_service import PokemonService

blueprint = Blueprint('pokemons_resource', __name__)
pokemon_service = PokemonService()

@blueprint.route("/v1/pokemons/<id>", methods=["GET"])
def find_essentials(id):
    result = pokemon_service.essentials(id)        
    return jsonify({"result": result}), HTTPStatus.OK

@blueprint.route("/v1/pokemons/<id>/sprites", methods=["GET"])
def find_assets(id):
    result = pokemon_service.sprites(id)        
    return jsonify({"result": result}), HTTPStatus.OK
    

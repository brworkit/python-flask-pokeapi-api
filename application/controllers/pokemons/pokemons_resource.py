from http import HTTPStatus
from flask import Blueprint, jsonify, request
from application.services.pokemons.pokemon_service import PokemonService

blueprint = Blueprint('pokemons_resource', __name__)
pokemon_service = PokemonService()

@blueprint.route("/v1/pokemons/<id>/essentials", methods=["GET"])
def find_essentials(id):
    result = pokemon_service.essentials(id)        
    return jsonify({"result": result}), HTTPStatus.OK

@blueprint.route("/v1/pokemons/essentials", methods=["GET"])
def find_essentials_range():
    _from = int(request.args.get("from", 1))
    _to = int(request.args.get("to", 51))
    result = pokemon_service.essentials_range(_from=_from, _to=_to)        
    return jsonify({"result": result}), HTTPStatus.OK

@blueprint.route("/v1/pokemons/<id>/sprites", methods=["GET"])
def find_assets(id):
    result = pokemon_service.sprites(id)        
    return jsonify({"result": result}), HTTPStatus.OK
    

from http import HTTPStatus
from flask import Blueprint, jsonify
from application.services.pokemon_service import PokemonService

blueprint = Blueprint('pokemons_resource', __name__)
pokemon_service = PokemonService()


@blueprint.route("/v1/pokemons/<id>/essentials", methods=["GET"])
def find_essentials(id):
    result = pokemon_service.essentials(id)        
    return jsonify({"result": result}), HTTPStatus.OK

@blueprint.route("/v1/pokemons/<id>/assets", methods=["GET"])
def find_assets(id):
    result = pokemon_service.assets(id)        
    return jsonify({"result": result}), HTTPStatus.OK
    

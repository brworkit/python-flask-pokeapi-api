from os import environ
from http import HTTPStatus
from flask import Blueprint, jsonify, request
from application.utils import time, log
from application.services.pokemon_service import PokemonService

blueprint = Blueprint('assets_resource', __name__)
pokemon_service = PokemonService()

@blueprint.route("/v1/assets/<id>", methods=["GET"])
def find_assets(id):
    print("find_assets")
    print(f"id: {id}") 

    result = pokemon_service.assets(id)
        
    return jsonify({"result": result}), HTTPStatus.OK
    
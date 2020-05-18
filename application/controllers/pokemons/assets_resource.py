from http import HTTPStatus
from flask import Blueprint, jsonify, request
from application.utils import time, log

blueprint = Blueprint('assets_resource', __name__)

@blueprint.route("/assets/<id>", methods=["GET"])
def find_assets(id):
    print("find_assets")
    print(f"id: {id}")    
    return jsonify({"message": "Assets Found", "result": []}), HTTPStatus.OK
    

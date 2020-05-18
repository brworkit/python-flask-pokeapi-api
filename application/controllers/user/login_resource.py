from http import HTTPStatus
from flask import Blueprint, jsonify, request
from application.utils import time, log
from application.controllers.user.login_service import LoginService
from application.utils.custom_exceptions import NotFoundException
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

blueprint = Blueprint('login_resource', __name__)
login_service = LoginService()

@blueprint.route("/registrations", methods=["POST"])
def create_new_login():
    print("create_new_login")

    body = request.get_json()
    print(f"create_new_login body: {body}")

    try:
        if login_service.find_by_email(body['email']):
            return jsonify({"message": "User already exists."}), HTTPStatus.CONFLICT

        _access_token = create_access_token(identity = body['password'])
        print(f"create_new_login access_token: {_access_token}")

        _refresh_token = create_refresh_token(identity = body['password'])
        print(f"create_new_login refresh_token: {_refresh_token}")

        body['password'] = login_service.generate_hash(body['password'])
        login_service.create_new_login(body)
        print("create_new_login CREATED NEW USER")

        return jsonify({"message": "OK", "result": {
            'access_token': _access_token,
            'refresh_token': _refresh_token
        }}), HTTPStatus.OK

    except Exception as e:
        print(f"create_new_login exception: {e}")
        return jsonify({"message": "ERROR", "result": {}}), HTTPStatus.INTERNAL_SERVER_ERROR


@blueprint.route("/logins", methods=["POST"])
@jwt_required
def login_user():
    print("login_user")
    try:

        body = request.get_json()
        print(f"create_new_login body: {body}")

        current_user = login_service.find_by_email(body['email'])

        print(f"create_new_login current_user: {current_user}")

        if not current_user:
            raise NotFoundException("User not found.")

        if login_service.verify_hash(body['password'], current_user['password']):
            _access_token = create_access_token(identity = body['password'])
            print(f"login_user access_token: {_access_token}")

            _refresh_token = create_refresh_token(identity = body['password'])
            print(f"login_user refresh_token: {_refresh_token}")

            return jsonify({"message": "OK", "result": {
            'access_token': _access_token,
            'refresh_token': _refresh_token
        }}), HTTPStatus.OK
        else:
            return jsonify({"message": "Invalid credentials"}), HTTPStatus.CONFLICT

    except NotFoundException as e:
        log.i("NotFoundException: {}".format(e))
        return jsonify({"message": "Error", "error": f"{e}"}), HTTPStatus.NOT_FOUND
    except Exception as e:
        log.i("Exception: {}".format(e))
        return jsonify({"message": "Internal Error", "error": f"{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR


@blueprint.route("/refresh", methods=["POST"])
@jwt_refresh_token_required
def refresh_token():
    print("refresh_token")
    try:
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return jsonify({"message": "OK", "result": {'access_token': access_token} }), HTTPStatus.OK
    except NotFoundException as e:
        log.i("NotFoundException: {}".format(e))
        return jsonify({"message": "Error", "error": f"{e}"}), HTTPStatus.NOT_FOUND
    except Exception as e:
        log.i("Exception: {}".format(e))
        return jsonify({"message": "Internal Error", "error": f"{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR


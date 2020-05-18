from http import HTTPStatus
from flask import Blueprint, jsonify, request
from application.utils import time, log
from application.services.marketing.email_service import EmailService
# from application.services.marketing.phone_service import PhoneService

blueprint = Blueprint('marketing_resource', __name__)
email_service = EmailService()
# phone_service = PhoneService()

@blueprint.route("/subscriptions/emails", methods=["POST"])
def new_email():
    print("new_email")
    try:
        body = request.get_json()                
        email_service.save_new_email(body=body)        
        return jsonify({"message": "Email collected."}), HTTPStatus.OK    
    except Exception as e:
        log.i("Exception: {}".format(e))
        return jsonify({"message": "Failed to find your coupons.", "error": "{}".format(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


@blueprint.route("/subscriptions/emails", methods=["GET"])
def find_emails():
    print("find_emails")
    try:
        active = request.args.get("active") if request.args.get("active") else False
        
        if active and active == "true":
            active = True
        else:
            active = False

        result = email_service.find_emails(active=active)

        return jsonify({"message": "Email collected.", "result": result}), HTTPStatus.OK    
    except Exception as e:
        log.i("Exception: {}".format(e))
        return jsonify({"message": "Failed to find your coupons.", "error": "{}".format(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@blueprint.route("/subscriptions/emails", methods=["DELETE"])
def unsubscribe_email():
    print("unsubscribe_email")
    try:
        email = request.args.get("email")        
        result = email_service.unsubscribe_email(email=email)
        return jsonify({"message": "Email unsubscribed."}), HTTPStatus.OK    
    except Exception as e:
        log.i("Exception: {}".format(e))
        return jsonify({"message": "Failed to find your coupons.", "error": "{}".format(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
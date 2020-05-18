import requests
from os import environ
from http import HTTPStatus
from cachetools import cached, TTLCache
from application.utils import log, json, time
from application.database.db import mongo
from passlib.hash import pbkdf2_sha256 as sha256

class LoginService(object):
    def __init__(self):
        pass

    def create_new_login(self, body):
        return mongo.db.users.insert_one(body)

    def find_by_email(self, email):
        result = mongo.db.users.find_one({"email": email})
        return result

    def generate_hash(self, password):
        return sha256.hash(password)

    def verify_hash(self, password, hash):
        return sha256.verify(password, hash)

    def is_jti_blacklisted(self, jti):
        # query = cls.query.filter_by(jti = jti).first()
        # return bool(query)
        return False
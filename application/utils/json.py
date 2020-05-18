import json
from flask import jsonify


def to_json(obj):
    if type(obj) is dict:
        return obj
    if type(obj) is not str:
        return json.loads(str(obj.__dict__))
    return json.loads(obj)

def dumps(obj):
    return json.dumps(obj)
    
def fy(obj):
    if type(obj) is dict:
        return obj
    return jsonify(obj)


def exclude_fields(obj, fields):
    dictonary = obj
    try:
        if type(dictonary) is not dict:
            dictonary = obj.__dict__
        for key in fields:
            try:
                dictonary.pop(key)
            except Exception as ex:
                print(str(ex))
    except Exception as ex:
        print("Error with fields: {}".format(fields))


# import boto3
# import jwt
# import ast


# class Util():

#     @staticmethod
#     def get_client_id(token):
#         defaults = {
#             'verify_signature': False,
#             'verify_aud': False,
#             'verify_iat': False,
#             'verify_exp': False,
#             'verify_nbf': False,
#             'verify_iss': False,
#             'verify_sub': False,
#             'verify_jti': False,
#             'verify_at_hash': False,
#             'leeway': 0}

#         decodedToken = jwt.decode(
#             token, algorithms=['RS256'], options=defaults)

#         return decodedToken['client_id']

#     @staticmethod
#     def get_pier_header(credentials):
#         return {
#             'Accept': "application/json",
#             'client_id': credentials['client_id'],
#             'access_token': credentials['access_token']
#         }

#     @staticmethod
#     def get_credentials(region, app_client):
#         session = boto3.session.Session()
#         client = session.client(service_name='secretsmanager',
#                                 region_name=region)

#         response = client.get_secret_value(SecretId=app_client)
#         dictResponse = ast.literal_eval(response['SecretString'])

#         pier_access_token = dictResponse['access_token']
#         pier_client_id = dictResponse['client_id']
#         id_emissor = dictResponse['id_emissor']

#         return {"client_id": pier_client_id, "access_token": pier_access_token, "id_emissor": id_emissor}

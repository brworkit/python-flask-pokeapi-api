import requests
from os import environ
from http import HTTPStatus
from application.utils import log, json, constants

class CommonService(object):
    def __init__(self):
        pass
        
    def deeplink(self, request):
        log.i("deeplink")
        url = environ["PATH_LOMADEE_DEEPLINK"].format(environ["APP_TOKEN"])
        log.i("url: {}".format(url))
        PARAMS_DEFAULT_COPY = constants.PARAMS_DEFAULT
        PARAMS_DEFAULT_COPY["url"] = request.args.get('url')
        response = requests.get(url, params=PARAMS_DEFAULT_COPY)
        log.i("response: {}".format(response))
        if response.status_code != HTTPStatus.OK: 
            raise Exception(response.text) 
        return json.to_json(response.text)


   
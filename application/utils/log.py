import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
APP_NAME='DESCONTZ'
def i(obj):
    logging.error(APP_NAME + ' ' + str(obj))

def e(obj):
    logging.error(APP_NAME + ' ' + str(obj))
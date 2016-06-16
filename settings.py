import logging

APP_DIR = 'c:/work/web-log-prov-ws/'
WEB_SUBFOLDER = 'api'  # no starting slash
HOST = '0.0.0.0'
PORT = 9000
LOGFILE = APP_DIR + 'weblogprovws.log'
LOGLEVEL = logging.DEBUG
DEBUG = True

BASE_URI_ENTITY = 'http://pid-test.geoscience.gov.au/dataset/wsoutput/'
SPARQL_ENDPOINT = 'http://52.63.202.107/db3/sparql'
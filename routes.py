import logging
import json
from flask import Blueprint, Response, render_template, request
import functions
import settings
import requests
routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return render_template('index.html')



@routes.route('/activities')
def activities():
    r = requests.get('http://52.63.202.107/data/sparql?query=DESCRIBE+%3Chttp%3A%2F%2Fpid-test.geoscience.gov.au%2Factivity%2Fservice%2Fj6ncqa%3E',
                      headers={'Accept': 'text/turtle'})

    return r.content



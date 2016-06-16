from flask import Blueprint, Response, render_template, request
import functions
import settings
import requests
import urllib
import rdflib
routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return render_template('index.html', web_subfolder=settings.WEB_SUBFOLDER)


@routes.route('/activities')
def activities():
    r = requests.get('http://52.63.202.107/data/sparql?query=DESCRIBE+%3Chttp%3A%2F%2Fpid-test.geoscience.gov.au%2Factivity%2Fservice%2Fj6ncqa%3E',
                      headers={'Accept': 'text/turtle'})

    return r.content


@routes.route('/dataset/wsoutput/')
def datasets():
    if request.args.get('_format') is None or request.args.get('_format') == 'text/html':
        # parse the graph into HTML
        return Response(functions.datasets_html(), status=200, mimetype='text/html')
    else:  # return RDF in all other cases request.args.get('_format') == 'text/turtle':
        r = requests.get(functions.datasets_turtle(),
                         headers={'Accept': 'text/turtle'})
        return Response(r.content, status=200, mimetype='text/turtle')


@routes.route('/dataset/wsoutput/<string:uri_id>')
def entity(uri_id):
    uri = '<' + settings.BASE_URI_ENTITY + uri_id + '>'
    encoded_uri = urllib.quote_plus(uri)
    if request.args.get('_format') is None or request.args.get('_format') == 'text/html':
        # parse the graph into HTML
        return Response(functions.dataset_html(uri), status=200, mimetype='text/html')
    else:  # return RDF in all other cases request.args.get('_format') == 'text/turtle':
        r = requests.get(settings.SPARQL_ENDPOINT + '?query=DESCRIBE+' + encoded_uri,
                         headers={'Accept': 'text/turtle'})
        return Response(r.content, status=200, mimetype='text/turtle')

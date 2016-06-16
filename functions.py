from rdflib import Graph
import requests
import urllib
import json
import settings

'''
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://pid-test.geoscience.gov.au/dataset/wsoutput/p2qrcu> a prov:Entity ;
    rdfs:label "Web Service Request Output" ;
    prov:generatedAtTime "2016-04-25T20:13:51.322000"^^xsd:datetime ;
    prov:wasGeneratedBy <http://pid-test.geoscience.gov.au/activity/service/lbmrx5>
.
'''
def entity_html(uri):
    html = ''
    query = '''
        PREFIX prov: <http://www.w3.org/ns/prov#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT *
        WHERE {
            ''' + uri + '''
                a prov:Entity;
                rdfs:label ?label;
                prov:generatedAtTime ?date;
                prov:wasGeneratedBy/prov:wasAssociatedWith ?webservice;
            .
        }
    '''
    encoded_query = urllib.quote_plus(query)
    r = requests.get(settings.SPARQL_ENDPOINT + '?query=' + encoded_query,
                     headers={'Accept': 'application/sparql-results+json'})
    if r.status_code == 200:
        print r.content
        j = json.loads(r.content)['results']['bindings'][0]
        print j
        html += '<h1>' + j['label']['value'] + '</h1>'
        html += '<table class="data">\n'
        html += '   <tr><th>Generated At:</th><td>' + j['date']['value'] + '</td></tr>\n'
        html += '   <tr><th>Web Service:</th><td>' + j['webservice']['value'] + '</td></tr>\n'
        html += '</table>\n'

        return html
    else:
        raise Exception('ERROR getting data from SPARQL endpoint')

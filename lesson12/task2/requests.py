from http import client
from urllib.parse import quote_plus
import json


"""
https://developers.google.com/maps/documentation/geocoding/intro?hl=es-419
http://maps.google.com/maps/api/geocode/json
https://www.google.com.bo/
maps/search/UMSS/@-17.3935685,-66.1494593,17z/data=!3m1!4b1?hl=es-419
"""
def geocode(address): 
    # formato url
    hostname = 'maps.google.com'
    base = '/maps/api/geocode/json'
    add_plus = quote_plus(address)
    direccion = '{}?address={}'.format(base, add_plus)
    print(hostname+direccion)
    # coneccion y metodo GET
    connection = client.HTTPConnection(hostname)
    connection.request('GET', direccion)
    # respuesta
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    results = reply["results"]
    diccionario_base = results[0]
    address_components = diccionario_base["geometry"]
    location = address_components["location"]
    print(location)
    # print(reply['results'][0]['geometry']['location'])


if __name__ == '__main__':
    address = 'UMSS'
    geocode(address)
    address = 'CEIS UMSS (Centro de Estudiantes de Ingeniería de Sistemas),'
    address += 'Cochabamba'
    geocode(address)

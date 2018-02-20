from pygeocoder import Geocoder
import os

"""
geocoder.py
"""
if __name__ == '__main__':
    autor = os.getenv('CURSO')
    print(autor)
    direccion = 'UMSS'
    print(Geocoder.geocode(direccion)[0].coordinates)

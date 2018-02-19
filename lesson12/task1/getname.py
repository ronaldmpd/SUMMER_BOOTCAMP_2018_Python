import socket

"""
getname.py
"""

if __name__ == '__main__':
    hostname = 'maps.google.com'
    direccion = socket.gethostbyname(hostname)
    mensaje = '{} es {}' .format(hostname, direccion)
    print(mensaje)


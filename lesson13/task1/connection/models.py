import os
import socket

"""
Las variables de entorno del sistema deben
estar establecidas.
"""



class Connection:
    def __init__(self):
        self.token = os.getenv('TOKEN')
        self.token_secret = os.getenv('TOKEN_SECRET')
        self.consumer_key = os.getenv('CONSUMER_KEY')
        self.consumer_secret = os.getenv('CONSUMER_SECRET')

    def getToken(self):
        return self.token

    def getTokenSecret(self):
        return self.token_secret

    def getConsumerKey(self):
        return self.consumer_key

    def getConsumerSecret(self):
        return self.consumer_secret

    def isConneted(self):
        res = True
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect( ('data.pr4e.org', 80))
            s.close()
        except socket.gaierror:
            res = False
        return res


if __name__ == "__main__":
    c = Connection()
    print(c.getToken())

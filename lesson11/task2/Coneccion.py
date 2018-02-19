import os
class Coneccion:

    def __init__(self):
        self.token = os.getenv("CURSO")

    def getToken(self):
        return self.token


c = Coneccion()
print(c.getToken())
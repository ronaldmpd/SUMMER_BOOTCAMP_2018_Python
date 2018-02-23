import unittest
from connection.models import Connection


"""
unittest - Unit testing framework
unittest proporciona un amplio conjunto de herramientas para
construir y ejecutar pruebas.
Los métodos setUp() y tearDown() le permiten definir instrucciones
que se ejecutarán antes y después de cada método de prueba.

AssertionError se genera cuando falla la declaración afirmativa.

python -m unittest test_module.TestClass.test_method

Ejm: Un directorio arriba ejecute
python -m unittest -v connection.test.TestConnection
"""
class TestConnection(unittest.TestCase):

    def setUp(self):
        self.connection = Connection()
        self.assertEqual(self.connection.isConneted(), True)
        
    def test_secret(self):
        res = self.connection.getToken()
        self.assertNotEqual(res, None)
        res = self.connection.getTokenSecret
        self.assertNotEqual(res, None)
        res = self.connection.getConsumerKey
        self.assertNotEqual(res, None)
        res = self.connection.getConsumerSecret
        self.assertNotEqual(res, None)

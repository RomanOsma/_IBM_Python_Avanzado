import unittest

class metodos_unittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Este metodo inicia cuando empieza la clase")

    def setUp(self):
        print("Yo me inicio en cada test case")

    def test_mensaje(self):
        print("Yo soy el test case del mensaje")

    def test_numero(self):
        print("Yo soy el test case del numero")

    def tearDown(self):
        print("Yo finalizo la ejecucion de cada uno de los test case\n")

    @classmethod
    def tearDownClass(cls):
        print("Yo me ejecuto al final de la clase")

if __name__ == '__main__':
    unittest.main()
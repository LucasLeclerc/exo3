import unittest
from exo3 import calcule,operation,OperationSigne,convertListToInt

class TestExo3(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calcule(1,2,'+'), 3)
    def test_soustraction(self):
        self.assertEqual(calcule(1,2,'-'), -1)
    def test_multiplication(self):
        self.assertEqual(calcule(1,2,'*'), 2)
    def test_division(self):
        self.assertEqual(calcule(4,2,'/'), 2)
    def test_division(self):
        self.assertEqual(calcule(4,0,'/'), 'error')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
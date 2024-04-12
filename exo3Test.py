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

    def test_operation(self):
        list=[1,2,3,4]
        result=[1,3,6,10]
        self.assertEqual(operation(list,'+'),result)


if __name__ == '__main__':
    unittest.main()
import unittest
from Calc import Calculator

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        obj1 = Calculator(3, 9)
        obj2 = Calculator(-10, 10)
        obj3 = Calculator(0, -55)

        self.assertEqual(obj1.add(), 12)
        self.assertEqual(obj2.add(), 0)
        self.assertEqual(obj3.add(), -55)
    
    def test_substraction(self):
        obj1 = Calculator(3, 9)
        obj2 = Calculator(-10, 10)
        obj3 = Calculator(0, -55)

        self.assertEqual(obj1.substract(), -6)
        self.assertEqual(obj2.substract(), -20)
        self.assertEqual(obj3.substract(), 55)

    def test_multiply(self):
        obj1 = Calculator(3, 9)
        obj2 = Calculator(-10, 10)
        obj3 = Calculator(0, -55)

        self.assertEqual(obj1.multiply(), 27)
        self.assertEqual(obj2.multiply(), -100)
        self.assertEqual(obj3.multiply(), 0)

    def test_division(self):
        obj1 = Calculator(9, 2)
        obj2 = Calculator(-10, 10)
        obj3 = Calculator(0, -55)

        self.assertEqual(obj1.division(), 4.5)
        self.assertEqual(obj2.division(), -1)
        self.assertEqual(obj3.division(), None)

if __name__ == '__main__':
    unittest.main()
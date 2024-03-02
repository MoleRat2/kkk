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
    

if __name__ == '__main__':
    unittest.main()
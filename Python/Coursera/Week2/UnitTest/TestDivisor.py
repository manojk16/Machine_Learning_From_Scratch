import unittest
import divisor

class TestDivisors(unittest.TestCase):
    "Example UnitTest method for get_divisor"
    def test_divisors_example_1(self):
        actual=divisor.get_divisor(8,[1,2,3])
        expected=[1,2]
        self.assertEqual(expected,actual)
    def test_divisors_example_1(self):
        actual=divisor.get_divisor(4,[-2,0,2])
        expected=[1,2]
        self.assertEqual(expected,actual)
        
     

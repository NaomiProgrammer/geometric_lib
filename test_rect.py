import unittest
from Rectangle1 import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_perimeter_with_positive_numbers(self):
        self.assertEqual(perimeter(5, 10), 30)

if __name__ == '__main__':
    unittest.main()
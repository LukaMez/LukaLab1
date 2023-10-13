import unittest
from app import add_numbers

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-2, 2), 0)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()

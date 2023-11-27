import unittest
from module import square, doubler

class TestModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_doubler(self):
        self.assertEqual(doubler(3), 6)


if __name__ == '__main__':
    unittest.main()
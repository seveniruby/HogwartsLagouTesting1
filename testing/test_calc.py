import sys
import unittest

sys.path.append("..")
from python.calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calc()

    def test_add_1(self):
        self.assertEqual(3, self.calc.add(1, 2))

    def test_add_2(self):
        self.assertEqual(0.003, self.calc.add(0.01, 0.02))


if __name__ == '__main__':
    unittest.main()

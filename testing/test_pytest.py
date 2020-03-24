from python.calc import Calc


class TestCalc:
    def test_add(self):
        calc = Calc()
        assert calc.add(1, 2) == 3

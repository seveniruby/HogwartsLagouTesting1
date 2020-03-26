import sys

import pytest

from python.calc import Calc


def setup_module():
    print("setup_module")


class TestCalc:

    @classmethod
    def setup_class(cls):
        print("setup_class")
        cls.calc = Calc()

    def setup_method(self):
        print("setup_method")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def teardown_method(self):
        print("teardown_method")

    @pytest.mark.demo2
    def test_add(self):
        print("add")
        assert self.calc.add(1, 2) == 3
        assert TestCalc.calc.add(1, 2) == 3

    def test_div(self):
        print("div")
        assert self.calc.div(1, 2) == 0.5

    @pytest.mark.demo
    @pytest.mark.parametrize("a, b", [
        (1, 2), (2, 3), (3, 4)
    ])
    def test_params(self, a, b):
        print("params")
        data = (a, b)
        self.calc.add2(data)
        self.calc.add(*data)


class Demo:
    kind = 0

    def __init__(self):
        self.name = ""


class TestCalc2:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def test_demo1(self):
        demo_1 = Demo()
        demo_2 = Demo()
        print(demo_1.kind)
        print(demo_2.kind)
        print(Demo.kind)

        print("class change var")
        Demo.kind = 1

        print(demo_1.kind)
        print(demo_2.kind)
        print(Demo.kind)

        print("instance change var")
        demo_1.kind += 1
        print(demo_1.kind)
        print(demo_2.kind)
        print(Demo.kind)

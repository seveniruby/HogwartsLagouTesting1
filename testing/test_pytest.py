import sys

import pytest
import yaml

from python.calc import Calc


def setup_module():
    print("setup_module")


# @pytest.fixture(scope="module")
def data():
    with open("test_pytest.data.yaml") as f:
        return yaml.load(f)


def steps():
    with open("test_pytest.steps.yaml") as f:
        return yaml.load(f)


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

    # todo: fixture与参数化合并使用
    @pytest.mark.demo
    @pytest.mark.parametrize("a, b, r", data())
    def test_params(self, a, b, r):
        print("params")
        data = (a, b)
        self.steps(data, r)
        # assert self.calc.add2(data) == r
        # assert self.calc.add(*data) ==r

    def steps(self, data, r):
        test_steps = steps()
        for step in test_steps:
            if step == "add":
                assert self.calc.add(*data) == r
            elif step == "add2":
                assert self.calc.add2(data) == r

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

    def test_demo2(self):
        assert Calc.add_static(1, 2) == 3

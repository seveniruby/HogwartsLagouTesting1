import pytest


@pytest.fixture(scope="module", params=[
    [1, 1, 2],
    [2, 1, 3]
])
def data(request):
    yield request.param


class TestFixture:
    def test_add(self):
        assert 1 + 1 == 2

    def test_add2(self, data):
        assert data[0] + data[1] == data[2]

    @pytest.mark.parametrize("a, b, c", [
        [1, 1, 2],
        [2, 1, 3]
    ])
    def test_add3(self, a, b, c):
        assert a + b == c

    def provider(self):
        for i in range(5):
            print("setup")
            yield i
            print("teardown")

    def test_yield(self):
        for d in self.provider():
            print(d)

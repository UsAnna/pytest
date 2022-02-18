import pytest


@pytest.fixture
def make_dict():
    return 0, {0: 0}

def test_value_in_dict(make_dict):
    value, my_dict = make_dict
    assert value in my_dict.values()

def test_mutability():
    x = {}
    y = x
    x[0] = 0
    assert y[0] == 0

def test_key_error():
    try:
        dict()[0]
    except KeyError:
        pass

if __name__ == '__main__':
    test_value_in_dict()
    test_mutability()
    test_key_error()
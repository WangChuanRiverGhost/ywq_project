import pytest

@pytest.fixture
def aaa():
    a = 1
    b = 2
    yield a + b
    a = 0

def test_aaa(aaa):
    x = aaa
    assert x==aaa

def test_bbb(aaa):
    pass
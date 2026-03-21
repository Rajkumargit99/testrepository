import pytest

def test_addition():
    n1 = 20
    n2 = 30
    assert n1+n2 == 50
    print(n1+n2)

@pytest.mark.xfail
def test_multiplication():
    x = 3
    y = 20
    assert x*y == 60
    print(x*y)

@pytest.mark.xfail
def test_division():
    v1 = 30
    v2 = 4
    assert v1//v2 == 8


def test_subtraction():
    m = 500
    n = 200
    assert m-n == 300

@pytest.mark.xfail
def test_addition_2():
    ram = 20
    beem = 30
    assert ram + beem == 50

def test_subtraction_2():
    ra = 200
    be = 100
    assert ra - be == 100
    print(ra-be)

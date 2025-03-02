import pytest

from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("0/1") == 0

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(101) == None

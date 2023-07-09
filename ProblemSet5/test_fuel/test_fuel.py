from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("4/4") == 100

    with pytest.raises(ValueError):
        convert("three/four")

    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
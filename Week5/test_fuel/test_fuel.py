from fuel import convert, gauge
import pytest

#  int
def test_convert():
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    with pytest.raises(ValueError):
        convert("man/woman")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
#  str
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"


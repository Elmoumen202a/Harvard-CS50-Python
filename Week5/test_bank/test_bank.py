from bank import value

def test_value():
    assert value("Hello me") == 0
    assert value("Hi?") == 20
    assert value("What's up?") == 100
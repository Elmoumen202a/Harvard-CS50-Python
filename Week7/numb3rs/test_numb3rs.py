from numb3rs import validate

def testInput_validate():
    assert validate("cat") == False
    assert validate("1.2.3.1000") == False
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("2.2.2.1") == True
    assert validate("1.200.2000.0") == False
    assert validate("1.200.400.800") == False
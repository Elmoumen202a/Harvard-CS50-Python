import pytest
from seasons import checkBirthDay

def check():
    assert checkBirthDay("525600") == "Invalid Date"
    assert checkBirthDay("1,2,2002") == "Invalid Date"
    assert checkBirthDay("1999-09-09") == "Twelve million, two hundred forty thousand minutes"
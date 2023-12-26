import pytest
from jar import Jar

def test_init():
    jar = Jar(4)
    assert jar.capacity == 4
    jar_ =Jar()
    assert jar_.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(4)
    assert jar.size == 9

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    jar.withdraw(1)
    assert jar.size == 1
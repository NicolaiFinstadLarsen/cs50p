from bank import value

'''
The issue I had here was that the original problem returned strings
and this one wanted int's as return value.
I changed the code and the test code, the it worked right away.
'''

def test_greet():
    assert value("hello") == 0
    assert value("HeLlO") == 0
    assert value("h") == 20
    assert value("hei") == 20
    assert value("yo") == 100
    assert value("1") == 100
    assert value("Hello my name is") == 0

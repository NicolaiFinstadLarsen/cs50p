from numb3rs import validate

def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("275.1.1.1") == False
    assert validate("1.") == False
    assert validate("1.1.1.1.1") == False
    assert validate("1.1.1.256") == False
    assert validate("127.0.0.1") == True
    assert validate("140.247.235.144") == True
from plates import is_valid

def test_is_valid():
    assert is_valid("cs50") == True
    assert is_valid("c50") == False # All vanity plates must start with at least two letters.
    assert is_valid("CS05") == False  # The first number used cannot be a ‘0'
    assert is_valid("CS50P") == False # Numbers cannot be used in the middle of a plate; they must come at the end
    assert is_valid("PI3.14") == False # No periods, spaces, or punctuation marks are allowed
    assert is_valid("OUTATIME") == False # vanity plates may contain a maximum of 6 characters (letters or numbers) \n
    assert is_valid("H") == False # and a minimum of 2 characters.
    assert is_valid("AAA222") == True # For example, AAA222 would be an acceptable
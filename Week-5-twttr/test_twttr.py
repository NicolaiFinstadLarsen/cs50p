from twttr import shorten

def test_shorten():
    assert shorten("ABC") == "BC" # Testing removal of vowel
    assert shorten("1") == "1" # Testing int as tuype string passes
    assert shorten("aA") == "" # Testing upper and lower case vowel
    assert shorten("Bb") == "Bb" # Testing upper and lower case consonants
    assert shorten("Ab.") == "b." # Testing punctuation stays
from um import count

def test_count():
    assert count("Um hi um.") == 2
    assert count("yummy") == 0
    assert count("Um this is my um umbrella") == 2
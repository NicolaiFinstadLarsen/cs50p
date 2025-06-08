from seasons import format_input
from seasons import printing_result
import datetime


def test_format_input():
    result = format_input("1988-09-25")
    expected = (datetime.date(1988, 9, 25), datetime.date.today())
    assert result == expected

def test_printing_result():
    assert printing_result(19301760) == "Nineteen million, three hundred one thousand, seven hundred sixty"
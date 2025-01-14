from sloth1 import censor

def test_right():
    assert censor("The code is fourty") == "The code is ******"
    assert censor("aaaa aaaaa 1234 12345") == "aaaa ***** 1234 *****"
    assert censor("Two plus three is five") == "Two plus ***** is five"

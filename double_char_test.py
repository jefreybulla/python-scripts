from double_char import double_char 

def test_double_char():
    # Test case 1: Empty string
    assert double_char('') == ''

    # Test case 2: Single character
    assert double_char('a') == 'aa'

    # Test case 3: String with multiple characters
    assert double_char('hello') == 'hheelllloo'

    # Test case 4: String with special characters
    assert double_char('@#$%') == '@@##$$%%'

    # Test case 5: String with numbers
    assert double_char('12345') == '1122334455'

    print("All test cases pass")

test_double_char()
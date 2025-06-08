from name_reverse import reversed_string

# Test functions
def test_reverse_string():
    input_name = "Lisa"
    expected_output = "asiL"
    actual_output = reversed_string(input_name)
    assert actual_output == expected_output

def test_reverse_empty_string():
    assert reversed_string("") == ""

def test_reverse_single_character():
    assert reversed_string("A") == "A"
def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

# Передача значений в функцию test_substring
full_string = "some text"
substring = "text"
test_substring(full_string, substring)
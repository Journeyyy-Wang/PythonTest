from name_function import get_formatted_name

def test_first_last_name():
    full_name = get_formatted_name('john', 'doe')
    assert full_name == 'John Doe'

def test_first_middle_last_name():
    full_name = get_formatted_name('john', 'doe', 'mozart')
    assert full_name == 'John Mozart Doe'
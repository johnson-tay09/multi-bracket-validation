
from multi_bracket_validation import validate_string


def test_import():
    assert validate_string


def test_matched_parens():
    testing_string = '()'
    actual = validate_string(testing_string)
    expect = True
    assert actual == expect


def test_matched_bracket():
    testing_string = '[]'
    actual = validate_string(testing_string)
    expect = True
    assert actual == expect


def test_matched_curly():
    testing_string = '{}'
    actual = validate_string(testing_string)
    expect = True
    assert actual == expect


def test_extra_paren():
    testing_string = '())'
    actual = validate_string(testing_string)
    expect = False
    assert actual == expect


def test_inter_nested_mixed():
    testing_string = '[(])'
    actual = validate_string(testing_string)
    expect = False
    assert actual == expect


def test_properly_nested_mixed():
    testing_string = '[()]'
    actual = validate_string(testing_string)
    expect = True
    assert actual == expect


def test_properly_nested_same():
    testing_string = '(())'
    actual = validate_string(testing_string)
    expect = True
    assert actual == expect


def test_properly_nested_all():
    testing_string = '{[()]}'
    actual = validate_string(testing_string)
    expect = True
    assert actual == expect


def test_extra_characters():
    testing_string = 'testing [ 123 ( abc ) 789 ] xyz'
    actual = validate_string(testing_string)
    expect = True
    assert actual == expect

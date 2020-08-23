from larning.strings import concatenate_with_separation
from pydantic import ValidationError
from pytest import raises


def test_a():
    assert concatenate_with_separation(["a", "a"], ".") == "a.a"
    assert concatenate_with_separation(["", "a"], ".") == ".a"
    assert concatenate_with_separation(["", ""], ".") == "."
    assert concatenate_with_separation(["a"], ".") == "a"
    assert concatenate_with_separation([1, 2], 2) == "122"
    assert concatenate_with_separation([1.2], 2) == "1.2"
    with raises(ValidationError):
        concatenate_with_separation("a", ".")

from larning.testing import name
from pydantic import ValidationError, validate_arguments
from pytest import raises
from typing import Union


@name(validate_arguments, 0, globals())
def _():
    @validate_arguments
    def tested(a: int):
        return a

    assert tested(1) == 1
    assert tested(1.1) == 1
    with raises(ValidationError):
        tested("a")


@name(validate_arguments, 1, globals())
def _():
    @validate_arguments
    def tested(a) -> int:
        return a

    assert tested(1) == 1
    assert tested(1.1) == 1.1
    assert tested("a") == "a"


@name(validate_arguments, 2, globals())
def _():
    @validate_arguments
    def tested(a: Union[int, str]):
        return a

    assert tested(1) == 1
    assert tested(1.1) == 1
    assert tested("a") == "a"


@name(validate_arguments, 3, globals())
def _():
    @validate_arguments
    def tested(a: Union[str, int]):
        return a

    assert tested(1) == "1"
    assert tested(1.1) == "1.1"
    assert tested("a") == "a"

from pydantic import validate_arguments
from typing import Union, Callable
from larning.strings import concatenate_with_separation
from contextlib import contextmanager
from io import StringIO
import sys


@validate_arguments
def name(tested: Callable, name: str, globals: dict):
    def decorator(func):
        new_name = concatenate_with_separation(
            ["test", tested.__qualname__, name], separator="_"
        )
        if new_name in globals.keys():
            raise NameError("GIVE UNIQUE NAME FOR THE TEST")
        func.__name__ = new_name
        globals[new_name] = func
        return func

    return decorator


@contextmanager
def input_manager(string: str) -> None:
    original_stdin = sys.stdin
    sys.stdin = StringIO(string + "\n")
    yield
    sys.stdin = original_stdin

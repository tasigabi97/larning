from collections.abc import Callable
from pydantic import validate_arguments
from typing import Iterable
from os import system
from larning.strings_i import concatenate_with_separation


class Bash(Callable):
    @validate_arguments
    def __init__(self, *args: str):
        self._command = concatenate_with_separation(args, " ")

    def __call__(self, *args, **kwargs):
        exit_code = system(self._command)
        return exit_code

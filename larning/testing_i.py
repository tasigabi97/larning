from contextlib import contextmanager
from io import StringIO
import sys


@contextmanager
def input_manager(string: str) -> None:
    original_stdin = sys.stdin
    sys.stdin = StringIO(string + "\n")
    yield
    sys.stdin = original_stdin


@contextmanager
def argv_manager(*strings: str) -> None:
    original_argv = list(sys.argv)
    sys.argv.__init__(strings)
    yield
    sys.argv.__init__(original_argv)

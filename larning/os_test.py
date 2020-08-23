from larning.os import Bash
from larning.testing import name


@name(Bash.__init__, 1, globals())
def _():
    assert Bash("a", 1)._command == "a 1"

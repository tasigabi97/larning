from larning.testing import name
from larning.ci import TaskList, ProcExecuter
from pytest import raises
from pydantic import ValidationError


@name(TaskList.__init__, 0, globals())
def _():
    with raises(ValidationError):
        TaskList(1)
    a = TaskList(lambda: 1, lambda: 2, name="name")
    assert a.name == "name" and a() == [1, 2]


@name(ProcExecuter, 0, globals())
def _():
    print(ProcExecuter.CLASS)
    ProcExecuter.CLASS = None
    print(ProcExecuter.CLASS)
    print(ProcExecuter().OBJECT)
    input()

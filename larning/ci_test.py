from larning.testing import name, input_manager
from larning.ci import TaskList, ProcExecuter, InputVariable, InputVariableFactory
from pytest import raises
from pydantic import ValidationError


@name(InputVariable.__init__, 0, globals())
def _():
    a = InputVariable("a")
    assert a._name == "a" and a._value == None and a in InputVariable


@name(InputVariable.__str__, 0, globals())
def _():
    a = InputVariable("a")
    assert str(a) == "<@a@>"


@name(InputVariable.value.fget, 0, globals())
def _():
    a = InputVariable("a")
    a._value = 1
    assert a.value == 1
    a = InputVariable("a")
    with input_manager("A"):
        assert a.value == "A"


@name(InputVariable.Factory, 0, globals())
def _():
    InputVariable.clear()
    a = InputVariableFactory.a
    b = InputVariableFactory.b
    a2 = InputVariableFactory.a
    assert a is a2
    assert InputVariable._objects == {a, b}


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

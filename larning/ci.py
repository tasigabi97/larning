from collections.abc import Iterable
from larning.property import with_property
from larning.abc import Namable
from collections.abc import Callable as aCallable
from typing import Callable as tCallable
from pydantic import validate_arguments
from abc import ABCMeta
from larning.metaclass import CollectorType
from larning.os import Proc


class InputVariable(
    Namable, metaclass=type("InputVariableType", (CollectorType, ABCMeta), {})
):
    def __init__(self, name: str):
        self._name, self._value = name, None

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        if self._value is None:
            self._value = input(str(self) + ":=")
        return self._value

    def __str__(self):
        return "<@" + self._name + "@>" if self._value is None else self._value

    class Factory:
        def __getattr__(self, name):
            for input_variable in InputVariable:
                if input_variable.name == name:
                    return input_variable
            return InputVariable(name)


InputVariableFactory = InputVariable.Factory()


class Task(
    Namable, aCallable, metaclass=type("TaskType", (CollectorType, ABCMeta), {})
):
    @validate_arguments
    def __init__(self, name: str, callable_: tCallable):
        self._name, self._callable = name, callable_

    def __call__(self):
        return self._callable()

    @property
    def name(self):
        return self._name

    class Factory:
        def __setattr__(self, name, value):
            if isinstance(value,list):
                return
                callable_=Proc(*value[1],wd_path=v)
            Task(name,callable_)

TaskFactory = Task.Factory()

@with_property("name")
class TaskList(aCallable):
    @validate_arguments
    def __init__(self, *tasks: tCallable, name: str = None):
        self.name = name
        self._tasks = list(tasks)

    def __call__(self):
        return [task() for task in self._tasks]


class MyMetaclass(ABCMeta):
    def __getattribute__(self, item):
        print("Mgetattribute", item, type(item))
        return ABCMeta.__getattribute__(self, item)

    def __getattr__(self, item):
        print("Mgetattr", item, type(item))
        return 1


class ProcExecuter(aCallable, metaclass=MyMetaclass):
    def __call__(self):
        ...

    def __getattribute__(self, item):
        print("getattribute", item)
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print("getattr", item, type(item))
        return 2

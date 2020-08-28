from collections.abc import Iterable
from larning.property import with_property
from larning.abc import Namable, Printable, ContextManager
from collections.abc import Sequence
from collections.abc import Callable as aCallable
from typing import Callable as tCallable
from pydantic import validate_arguments
from abc import ABCMeta
from larning.metaclass import CollectorType
from larning.os import Proc
from typing import Union
from larning.strings import func_to_str, concatenate_with_separation

AbstractCollectorMetaclass = type("InputVariableType", (CollectorType, ABCMeta), {})


class InputVariable(
    Namable, Printable, metaclass=AbstractCollectorMetaclass,
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

    @staticmethod
    def collect_input(args, kwargs):
        args = [arg.value if isinstance(arg, InputVariable) else arg for arg in args]
        kwargs = {
            key: value.value if isinstance(value, InputVariable) else value
            for key, value in kwargs.items()
        }
        return args, kwargs

    def __str__(self):
        return "<@" + self._name + "@>" if self._value is None else self._value

    class Factory:
        def __getattr__(self, name):
            try:
                return InputVariable[name]
            except IndexError:
                return InputVariable(name)


class Task(
    Namable, Printable, aCallable, metaclass=AbstractCollectorMetaclass,
):
    @validate_arguments
    def __init__(
        self, func: tCallable, args=None, kwargs=None, name: Union[str, None] = None
    ):
        self._func, self._args, self._kwargs, self._name, = func, args, kwargs, name
        self._args = [] if self._args is None else self._args
        self._kwargs = dict() if self._kwargs is None else self._kwargs

    def __str__(self):
        return self.name + "->" + func_to_str(self._func, *self._args, **self._kwargs)

    def __call__(self):
        args, kwargs = InputVariable.collect_input(self._args, self._kwargs)
        return self._func(*args, **kwargs)

    @property
    def name(self):
        return self._name

    class Factory:
        def __setattr__(self, name, l: list):
            args, kwargs = [], {}
            for i in l:
                if isinstance(i, Sequence):
                    args = i
                if isinstance(i, dict):
                    kwargs = i
            Task(l[0], args, kwargs, name=name)

        def __getattr__(self, name):
            return Task[name]


class ProcTask(Task, metaclass=AbstractCollectorMetaclass):
    ...


class Script(
    Namable, Printable, aCallable, Iterable, metaclass=AbstractCollectorMetaclass,
):
    def __init__(self, *tasks: Task, name: Union[str, None] = None):
        self._tasks, self._name = tasks, name

    def __iter__(self):
        return iter(self._tasks)

    @property
    def name(self):
        return self._name

    def __str__(self):
        sep = "\n\t\t"
        return (
            self.name
            + ":"
            + sep
            + concatenate_with_separation([str(task) for task in self._tasks], sep)
        )

    def __call__(self):
        ret = []
        print(self.name)
        for task in self._tasks:
            print(str(task))
            input("Press Enter to continue...")
            ret.append(task())
        return ret

    class Factory(ContextManager):
        def __setattr__(self, name, l: list):
            Script(*l, name=name)

        def __enter__(self):
            return InputVariable.Factory(), Task.Factory(), Script.Factory()

        def __exit__(self, exc_type, exc_val, exc_tb):
            ...

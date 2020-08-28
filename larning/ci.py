from collections.abc import Iterable
from larning.property import with_property
from larning.abc import Namable,Printable
from collections.abc import Sequence
from collections.abc import Callable as aCallable
from typing import Callable as tCallable
from pydantic import validate_arguments
from abc import ABCMeta
from larning.metaclass import CollectorType
from larning.os import Proc
from typing import Union
from larning.strings import func_to_str
class InputVariable(
    Namable,Printable, metaclass=type("InputVariableType", (CollectorType, ABCMeta), {})
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
    Namable,Printable, aCallable, metaclass=type("TaskType", (CollectorType, ABCMeta), {})
):
    @validate_arguments
    def __init__(self, func: tCallable, args=None, kwargs=None, name: Union[str, None] = None):
        self._func, self._args,self._kwargs, self._name, =func,args,kwargs, name
        self._args=[] if self._args is None else self._args
        self._kwargs=dict() if self._kwargs is None else self._kwargs

    def __str__(self):
        return self.name+"->"+func_to_str(self._func,*self._args,**self._kwargs)


    def __call__(self):
        args=[arg.value if isinstance(arg,InputVariable) else arg for arg in self._args]
        kwargs = {key:value.value if isinstance(value,InputVariable) else value for key,value in self._kwargs.items()}
        return self._func(*args,**kwargs)

    @property
    def name(self):
        return self._name

    class Factory:
        def __setattr__(self, name, l:list):
            args,kwargs=[],{}
            for i in l:
                if isinstance(i,Sequence):
                    args=i
                if isinstance(i,dict):
                    kwargs=i
            Task(l[0],args,kwargs,name=name)

        def __getattr__(self, name):
            for task in Task:
                if task.name == name:
                    return task


TaskFactory = Task.Factory()

@with_property("name")
class TaskList(aCallable,Namable):
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

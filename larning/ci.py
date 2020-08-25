from collections.abc import Iterable
from larning.property import with_property
from collections.abc import Callable as aCallable
from typing import Callable as tCallable
from pydantic import validate_arguments
from abc import ABCMeta


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

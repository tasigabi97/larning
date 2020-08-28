from abc import ABC, abstractmethod

def del_abstractmethod(cls:type,method_name:str):
    if "__abstractmethods__" in cls.__dict__.keys():
        setattr(cls, "__abstractmethods__",
                frozenset([i for i in cls.__dict__["__abstractmethods__"] if i != method_name]))

class Namable(ABC):
    @property
    @abstractmethod
    def name(self):
        ...


class Printable(ABC):
    @abstractmethod
    def __str__(self):
        ...


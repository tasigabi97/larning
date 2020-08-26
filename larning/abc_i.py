from abc import ABC, abstractmethod


class Namable(ABC):
    @property
    @abstractmethod
    def name(self):
        ...

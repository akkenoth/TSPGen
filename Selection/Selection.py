from abc import ABC, abstractmethod


class Selection(ABC):
    """docstring"""

    def __init__(self):
        pass

    @abstractmethod
    def make(self, population, size, elitism):
        pass

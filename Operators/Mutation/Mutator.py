from abc import ABC, abstractmethod

class Mutator(ABC):
    """docstring"""

    def __init__(self):
        pass

    @abstractmethod
    def make(self, problemMap, unit):
        pass

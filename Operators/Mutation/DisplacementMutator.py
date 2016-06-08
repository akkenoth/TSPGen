import random
import itertools

from Operators.Mutation import Mutator
from Map import City

class DisplacementMutator(Mutator):
    """docstring"""

    def __init__(self):
        super().__init__()

    def make(self, problemMap, unit):
        pass

    def findValidMutation(self, problemMap, unit):
        path = unit.path[:]

        begin = random.randrange(len(path))

        if begin > 1:
            end = random.randrange(begin, len(path))
        else:
            end = random.randrange(begin, len(path) - 2 + begin)

        beginLeft = path[begin - 1]
        endRight = path[(end + 1) % len(path)]

        if problemMap.cities[beginLeft].isConnectedTo(problemMap.cities[endRight]):
            # OK
            pass
        else:
            # such a path is not allowed for mutation
            pass

        # sub-path will be inserted after insert element
        # make sure the same insert is not being chosen twice
        leftInterval = list(range(0, beginLeft))
        rightInterval = list(range(endRight, len(path)))
        possibleInserts = leftInterval + rightInterval
        insert = random.choice(possibleInserts)

        insertRight = path[(insert + 1) % len(path)]

        if problemMap.cities[insert].isConnectedTo(problemMap.cities[begin]) \
                and problemMap.cities[insertRight].isConnectedTo(problemMap.cities[end]):
            # OK
            pass
        else:
            # such insertion is not allowed for mutation
            pass




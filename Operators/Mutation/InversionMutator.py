import random

from Operators.Mutation import Mutator
from Map import City

class InversionMutator(Mutator):
    """docstring"""

    def __init__(self):
        super().__init__()

    def make(self, problemMap, unit):
        pass

    def findValidMutation(self, problemMap, unit):
        """

            :param problemMap:
            :return unit:
        """
        path   = unit.path[:]
        cities = problemMap.cities
        found  = False
        tries  = 0

        while not found and tries < len(path)**3:
            tries += 1
            begin  = random.randrange(1    , len(path) - 1)
            end    = random.randrange(begin, len(path) - 1)
            shifts = random.randrange(len(path) - end) / 2 + 1    # number of  subpath right shifts

            # swap first and last city of subpath
            path[end], path[begin] = path[begin], path[end]

            # try shift subpath max to the right
            for i in range(shifts):
                beginLeft = path[begin - 1]
                endRight  = path[(end + 1) % len(path)]

                # check if three conditions needed to shift are true  - if not, further shifting is impossible
                if cities[beginLeft].isConnectedTo(cities[endRight]) \
                    and cities[endRight].isConnectedTo(cities[path[begin]]) \
                    and cities[path[end]].isConnectedTo(cities[(end + 2) % len(path)]):
                    # (jeśli macie pomysł jak to zrobić ładniej to śmiało)
                    found = True
                    tmp = path[begin:end+1]
                    path[begin] = endRight
                    path = path[:begin+1] + tmp

                    begin += 1
                    end   += 1
                else:
                    # swap back first and last city of subpath
                    path[end], path[begin] = path[begin], path[end]
                    break

        # invert rest of subpath
        path[begin+1:end] = path[begin+1:end][::-1]

        return path

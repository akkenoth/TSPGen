import random
import itertools

from Operators.Mutation import Mutator
from Map import City
from Population import Unit

class DisplacementMutator(Mutator):
    """docstring"""

    def __init__(self):
        super().__init__()

    def make(self, problemMap, unit):
        """
        :param problemMap:
        :return unit:
        """

        path = unit.path[:]
        pathLength = len(unit.path)
        found = False
        tries = 0

        #TODO: explain what the 'tries' condition is
        while not found and tries < pathLength**3:
            tries += 1
            # get a random place where to begin the subpath to displace
            begin = random.randrange(pathLength)
            # get a random length (max half the length of path - anything more would be equal to displacing the rest of path)
            length = random.randrange(pathLength/2)
            # get a random shift we're to displace the subpath by
            shift = random.randrange(pathLength) - 1
            shiftTries = 0

            while not found and shiftTries < pathLength:
                shift += 1
                shiftTries += 1

                end = (begin + length - 1) % pathLength

                beginCity = problemMap.cities[unit.path[begin]]
                beginCityPrev = problemMap.cities[unit.path[begin - 1]]
                endCity = problemMap.cities[unit.path[end]]
                endCityNext = problemMap.cities[unit.path[(end + 1) % pathLength]]
                endCityNewNext = problemMap.cities[unit.path[(end + shift) % pathLength]]

                if not beginCityPrev.isConnectedTo(endCityNext):
                    continue
                if not beginCity.isConnectedTo(endCityNext):
                    continue
                if not endCity.isConnectedTo(endCityNewNext):
                    continue
                found = True

            if found:
                end = (begin + length - 1) % pathLength
                if end < begin:
                    tmp = end
                    end = begin
                    begin = tmp
                path = unit.path[: begin] + unit.path[end + 1 : end + 1 + shift] + unit.path[begin : end + 1] + unit.path[end + 1 + shift :]
                return Unit(problemMap, path)

    def findValidMutation(self, problemMap, unit):
        """
        :param problemMap:
        :return unit:
        """
        path = unit.path[:]
        cities = problemMap.cities
        found = False
        tries = 0

        while not found and tries < len(path)**3:
            tries += 1
            begin = random.randrange(1, len(path) - 1)
            end = random.randrange(begin, len(path) - 1)
            # number of  subpath right shifts
            shifts = random.randrange(len(path) - end) / 2 + 1

            # try shift subpath max to the right
            for i in range(shifts):
                beginLeft = path[begin - 1]
                endRight = path[(end + 1) % len(path)]

                # check if three conditions needed to shift are true - if not, further shifting is impossible
                if cities[beginLeft].isConnectedTo(cities[endRight]) \
                    and cities[endRight].isConnectedTo(cities[path[begin]]) \
                    and cities[path[end]].isConnectedTo(cities[(end + 2) % len(path)]):
                    # (jeśli macie pomysł jak to zrobić ładniej to śmiało)
                    found = True
                    tmp = path[begin:end+1]
                    path[begin] = endRight
                    path = path[:begin+1] + tmp

                    begin += 1
                    end += 1
                else:
                    break

        return path

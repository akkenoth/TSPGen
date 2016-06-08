import random

from Selection.Selector import Selector
from Population.Population import Population

class TournamentSelector(Selector):
    """docstring"""

    def __init__(self):
        super().__init__()

    def make(self, population, selectSize, tSize):
        """

        :param population:
        :param selectSize:
        :param tSize:
        :return:
        """
        selection = []

        while len(selection < selectSize):
            # for now it is possible to pick the same unit more than one time
            unit = self.make_single(population, tSize)
            selection.append(unit)

        return selection

    def make_single(self, population, tSize):
        """

        :param population:
        :param tSize:
        :return:
        """
        tournament = Population(tSize)
        units = population.units[:]

        try:
            while len(tournament.units) < tSize:
                unit = random.choice(units)
                units.remove(unit)
                tournament.addUnit(unit)
        except IndexError:
            raise IndexError("Tournament size set greater than population size.")

        return tournament.bestUnit(0)

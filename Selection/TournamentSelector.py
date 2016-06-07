import random

from Selection.Selector import Selector
from Population.Population import Population

class TournamentSelector(Selector):
    """docstring"""

    def __init__(self):
        super().__init__()

    def make(self, population, size):
        tournament = Population(size)
        units = population.units[:]

        while len(tournament.units) < size:
            unit = random.choice(units)
            units.remove(unit)
            tournament.addUnit(unit)

        return tournament.bestUnit(0)

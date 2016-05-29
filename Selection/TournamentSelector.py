from random import randrange

from Selection.Selector import Selector
from Population.Population import Population

class TournamentSelector(Selector):
    """docstring"""

    def __init__(self):
        super().__init__()

    def make(self, population, size, elite):
        tournament = Population(size)

        if elite > 0:
            for i in range(elite):
                tournament.addUnit(population.bestUnit(i))
                # population.removeUnit() ?

        while len(tournament.units) < size:
            position = randrange(size)
            tournament.addUnit(population.units[position])

        return tournament.bestUnit(0)

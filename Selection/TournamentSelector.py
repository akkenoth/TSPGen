from Selection.Selector import Selector
from Population.Population import Population

from random import randrange


class TournamentSelector(Selector):
    """docstring"""

    def __init__(self):
        super().__init__()

    def make(self, population, size, elite):
        tournament = Population(size)

        if elite > 0:
            for i in range(elite):
                tournament.add_unit(population.best_unit(i))

        while len(tournament.units) < size:
            position = randrange(size)
            tournament.add_unit(population.units[position])

        return tournament.best_unit(0)

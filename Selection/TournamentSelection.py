from Selection.Selection import Selection
from Population.Population import Population

from random import randrange


class TournamentSelection(Selection):
    """docstring"""

    def __init__(self):
        super().__init__()

    def make(self, population, size, elite):
        tournament = Population(size)

        if elite > 0:
            for i in range(elite):
                tournament.addUnit(population.bestUnit(i))

        while len(tournament.units) < size:
            position = randrange(size)
            tournament.addUnit(population.units[position])

        return tournament.bestUnit(0)

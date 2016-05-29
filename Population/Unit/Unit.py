from itertools import islice


class Unit(object):
    """docstring"""

    path = []
    size = 0
    length = 0.0
    fitness = 0.0

    def __init__(self, size, path):
        self.path = path
        self.size = size

    def calc_length(self):
        if len(self.path) == self.size:

            edges = zip(islice(self.path, 1, None), self.path)

            for one, two in edges:
                self.length += one.distanceTo(two)

            self.length += self.path[0].distanceTo(self.path[len(self.path) - 1])
        else:
            pass

    def calc_fitness(self):
        if self.length > 0:
            self.fitness = 1/self.length
        else:
            pass

from Population import Unit

class Population(object):
    """docstring"""

    elitism = False
    mutationRate = 0.1

    def __init__(self, size, units = None):
        self.size = size
        if units is None:
            self.units = []
            self.sorted = False
        else:
            self.units = units
            self.units.sort(key=lambda u: u.fitness, reverse=True)
            self.sorted = True;

    def addUnit(self, unit):
        if len(self.units) < self.size:
            if unit not in self.units:
                self.units.append(unit)
                self.sorted = False
            else:
                pass
        else:
            pass

    def bestUnit(self, position):
        if position >= self.size:
            position = self.size - 1
        if self.sorted == False:
            self.units.sort(key = Unit.calcFitness)
            self.sorted = True

        return self.units[position]

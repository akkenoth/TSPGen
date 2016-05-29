from Population.Unit import Unit


class Population(object):
    """docstring"""

    units = []
    size = 0

    def __init__(self, size, units=None):
        if units is None:
            self.units = []
        else:
            self.units = units
            self.units.sort(key=Unit.Unit.calcFitness)

        self.size = size

    def addUnit(self, unit):
        if len(self.units) < self.size:
            if unit not in self.units:
                self.units.append(unit)
            else:
                pass
        else:
            pass

    def bestUnit(self, position):
        if position < self.size:
            return self.units[position]
        else:
            pass

from Population.Unit.Unit import Unit


class Population(object):
    """docstring"""

    units = []
    size = 0

    def __init__(self, size, units=None):
        if units is None:
            self.units = []
        else:
            self.units = units

        self.size = size

    def add_unit(self, unit):
        if len(self.units) < self.size:
            if unit not in self.units:
                self.units.append(unit)
            else:
                pass
        else:
            pass

    def best_unit(self, position):
        if position < self.size:
            self.units.sort(key=Unit.calc_fitness)
            return self.units[position]
        else:
            pass

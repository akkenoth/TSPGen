from Population.Unit import Unit

class Population(object):
    """docstring"""

    def __init__(self, size, units = None):
        if units is None:
            self.units = []
        else:
            self.units = units

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
            # Perhaps move to addUnit()? Or add boolean 'sorted' flag and sort on demand
            self.units.sort(key = Unit.calcFitness)
            return self.units[position]
        else:
            pass

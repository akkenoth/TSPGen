from Population import Unit

class Population(object):
    """docstring"""

    def __init__(self, size, units = None):
        if units is None:
            self.units = []
        else:
            self.units = units

        self.size = size
        self.sorted = False

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
        if position < self.size:
            if self.sorted == False:
                self.units.sort(key=Unit.calcFitness)
                self.sorted = True;

            return self.units[position]
        else:
            pass

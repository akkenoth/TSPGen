class Unit(object):
    """docstring for Population/Unit"""

    def __init__(self, problemMap, path):
        #TODO: add parameter checks

        self.map = problemMap
        self.path = path
        self.length = 0.0
        self.fitness = 0.0

        nextCity = self.map.cities[self.path[0]]
        for i in range(-1, len(self.path)-1):
            currentCity = nextCity
            nextCity = self.map.cities[self.path[i+1]]
            self.length += currentCity.getDistanceTo(nextCity)

        self.fitness = 1.0 / self.length

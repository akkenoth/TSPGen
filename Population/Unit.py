from random import choice

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

    @staticmethod
    def generateUnit(problemMap):
        """
        Generate an unit by starting from city0 and randomly selecting unused neighbour to connect to.
        If there is no such one, begin anew (very inefficient!).
        TODO: when there are no unused neighbours, go back one step - this should vastly improve generation time. Aka do depth-search.

        """
        while True:
            currentIndex = 0
            path = [0]
            while len(path) < problemMap.size:
                currentCity = problemMap.cities[currentIndex]
                neighbours = [i for i in currentCity.connections if not i in path]
                if len(neighbours) == 0:
                    break
                currentIndex = choice(neighbours)
                path.append(currentIndex)
            if len(path) < problemMap.size:
                continue
            firstCity = problemMap.cities[path[0]]
            lastCity = problemMap.cities[path[problemMap.size - 1]]
            if not firstCity.isConnectedTo(lastCity):
                continue
            return Unit(problemMap, path)

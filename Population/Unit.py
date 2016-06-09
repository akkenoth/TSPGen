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
    def generateUnitRand(problemMap):
        """
        Generate an unit by starting from city0 and randomly selecting unused neighbour to connect to.
        If there is no such one, begin anew (random is quite inefficient).

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

    @staticmethod
    def generateUnitDS(problemMap):
        """
        Generate an unit by doing random choice depth search.
        Sloooooow.
        TODO: make it work in finite time by applying some equivalent of alpha-beta for depth-search or something else.
        """

        def _generatePath(problemMap, path, targetLength):
            currentCity = problemMap.cities[path[-1]]

            if len(path) == targetLength:
                firstCity = problemMap.cities[path[0]]
                if firstCity.isConnectedTo(currentCity):
                    return path
                else:
                    return None

            usableNeighbours = [i for i in currentCity.connections if not i in path]

            selectedNeighbour = -1
            newPath = None
            while len(usableNeighbours) > 0:
                neighbour = choice(usableNeighbours)
                newPath = path[:]
                newPath.append(neighbour)
                newPath = _generatePath(problemMap, newPath, targetLength)
                if newPath is None:
                    usableNeighbours.remove(neighbour)
            return newPath

        return Unit(_generatePath(problemMap, [0], problemMap.size))

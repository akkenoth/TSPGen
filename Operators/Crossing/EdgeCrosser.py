import random

from Operators.Crossing import Crosser
from Population import Population, Unit

class EdgeCrosser(Crosser):
    """docstring"""

    def __init__(self, parentsCount):
        super().__init__()
        self.parentsCount = parentsCount

    def applyCrossing(self, problemMap, population, newPopulationSize):
        children = []
        while len(children) < newPopulationSize:
            parents = []
            possibleParents = population.units[:]
            while len(parents) < self.parentsCount:
                parent = random.choice(possibleParents)
                possibleParents.remove(parent)
                parents.append(parent)
            childUnit = self.make(problemMap, parents)
            duplicate = False
            for unit in children:
                if duplicate:
                    break
                if childUnit.path == unit.path:
                    duplicate = True
            for unit in population.units:
                if duplicate:
                    break
                if childUnit.path == unit.path:
                    duplicate = True

            if not duplicate:
                children.append(childUnit)
        return Population(newPopulationSize, children)

    def make(self, problemMap, units):
        """
        :param problemMap:
        :param units:
        :return unit:
        TODO: make static?
        """
        paths = [unit.path for unit in units]

        adjList = self.makeAdjacencyList(problemMap, paths)
        path = self.makePath(adjList)

        ##TODO: verify obtained path

        return Unit(problemMap, path)

    def makePath(self, adjList):
        """
        :param adjList: adjacency list
        :return path: new path
        TODO: make it back up 1 step if no choice is possible instead of starting all over - see note in Population.Unit
        """

        while True:
            src = 0
            path = []

            while len(path) != len(adjList):
                path.append(src)

                srcList = adjList[src][:]
                curr = random.choice(srcList)

                while curr in path:
                    srcList.remove(curr)
                    if len(srcList) == 0:
                        break
                    curr = random.choice(srcList)
                if len(srcList) == 0:
                    break

                src = curr
            if len(path) != len(adjList):
                continue

            return path

    def makeAdjacencyList(self, problemMap, paths):
        """
        :param problemMap:
        :param paths: list of paths from Units chosen for crossing
        :return adjList: adjacency list (object mapping city index -> list of adjacencies)
        """

        adjList = {i.index: [] for i in problemMap.cities}
        #should be equivalent to this matrix:
        #adjList = [[] for i in range(problemMap.size)]

        for path in paths:
            for j in range(len(path)):
                index = path[j]
                prevIndex = path[j-1]
                nextIndex = path[(j+1) % len(path)]
                if prevIndex not in adjList[index]:
                    adjList[index].append(prevIndex)
                if nextIndex not in adjList[index]:
                    adjList[index].append(nextIndex)

        return adjList

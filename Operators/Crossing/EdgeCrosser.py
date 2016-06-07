import random

from Operators.Crossing import Crosser
from Population import Unit

class EdgeCrosser(Crosser):
    """docstring"""

    def __init__(self):
        super().__init__()

    def make(self, problemMap, units):
        """
        :param problemMap:
        :param units:
        :return unit:
        """
        paths = []

        for i in range(len(units)):
            paths.append(units[i].path)

        adjList = self.makeAdjacencyList(problemMap, paths)
        path = self.makePath(adjList)

        unit = Unit(problemMap, path)
        return unit

    def makePath(self, adjList):
        """
        :param adjList: adjacency list
        :return path: new path
        """
        path = []
        src = 0

        while(len(path) != len(adjList)):
            path.append(src)

            srcList = adjList[src][:]
            curr = random.choice(srcList)

            try:
                while curr in path:
                    srcList.remove(curr)
                    curr = random.choice(srcList)
            except IndexError:
                allNodes = set(adjList.keys())
                notInPath = allNodes.difference(path)
                curr = random.choice(notInPath)

            src = curr

        return path

    def makeAdjacencyList(self, problemMap, paths):
        """
        :param problemMap:
        :param paths: list of paths from Units chosen for crossing
        :return adjList: adjacency list
        """

        adjList = {i.index: [] for i in problemMap.cities}

        for i in range(0, len(paths)):
            path = paths[i]
            for j in range(0, len(path)):
                if path[j-1] not in adjList[path[j]]:
                    adjList[path[j]].append(path[j-1])
                if path[(j+1) % len(path)] not in adjList[path[j]]:
                    adjList[path[j]].append(path[(j+1) % len(path)])

        return adjList
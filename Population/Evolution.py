import random

from Population import Population

class Evolution(object):
    """docstring for Evolution"""

    @staticmethod
    def evolve(problemMap, population, selector, crosser, mutator):
        """

                :param problemMap:
                :param population:
                :param selector:
                :param crosser:
                :param mutator:
                :return:
        """

        children = []
        newUnits = []

        # select parents, perform crossing and mutate child
        while len(children) < population.size:
            parents = selector.make(population, 4, 8)
            child = crosser.make(problemMap, parents)
            child = mutator.make(problemMap, child)
            children.append(child)

        # select new units
        sum = population + children
        while len(newUnits) < len(population):
            newUnit = selector.make(sum, 4, 8)
            newUnits.append(newUnit)

        # if elitism is enabled create space and save the best unit
        if population.elitism:
            best = population.bestUnit(0)
            removed = random.choice(sum)
            sum.remove(removed)
            sum.append(best)

        return Population(len(population), newUnits)


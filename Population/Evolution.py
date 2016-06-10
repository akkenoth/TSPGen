import random

from Population import Population

class Evolution(object):
    """docstring for Evolution"""

    def __init__(self, problemMap, population, selector, crosser, mutator):
        self.problemMap = problemMap
        self.population = population
        self.selector = selector
        self.crosser = crosser
        self.mutator = mutator

    def evolve(self):

        children = []
        newUnits = []

        # select parents, perform crossing and mutate child
        while len(children) < self.population.size:
            parents = self.selector.make(self.population, 2, 4)
            child = self.crosser.make(self.problemMap, parents)
            child = self.mutator.make(self.problemMap, child)
            children.append(child)

        # select new units
        sum = Population(2 * self.population.size, self.population.units + children)
        while len(newUnits) < self.population.size:
            newUnits += self.selector.make(sum, 3, 6)

        # if elitism is enabled create space and save the best unit
        if self.mutator.elitism:
            best = self.population.bestUnit(0)
            removed = random.choice(sum)
            newUnits.remove(removed)
            newUnits.append(best)


        return Population(self.population.size, newUnits[:self.population.size])


    def make(self, iters):
        """

                        :param iters:
                        :return:
        """

        for i in range(iters):
            # evolve one generation
            newPopulation = self.evolve()

            # change options
            #self.mutator.changeParams()
            #self.selector.changeParams()

            # print results
            print("Next generation: ")
            for unit in newPopulation.units:
                print(unit.path, " | ", unit.fitness)
            print()

            self.population = newPopulation
            trash = input('Next iteration? (Press enter)')

        return self.population.units.bestUnit(0)



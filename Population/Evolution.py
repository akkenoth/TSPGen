import random

from Population.Population import Population

class Evolution(object):
    """docstring for Evolution"""

    def __init__(self, problemMap, population, selector, crosser, mutator):
        self.problemMap = problemMap
        self.population = population
        self.selector = selector
        self.crosser = crosser
        self.mutator = mutator

    def evolve(self):
        # Crossing and mutation
        children = []
        while len(children) < self.population.size:
            parentA = random.choice(self.population.units)
            parentB = parentA
            while parentB == parentA:
                parentB = random.choice(self.population.units)
            child = self.crosser.make(self.problemMap, [parentA, parentB])
            child = self.mutator.make(self.problemMap, child)
            
            # Check whether child is not a duplicate of already existing unit or a child generated before
            duplicate = False
            for unit in children:
                if duplicate:
                    break
                if child.path == unit.path:
                    duplicate = True
            for unit in self.population.units:
                if duplicate:
                    break
                if child.path == unit.path:
                    duplicate = True

            if not duplicate:
                children.append(child)

        # Selection
        sumPopulation = Population(2 * self.population.size, self.population.units + children)
        newUnits = self.selector.make(sumPopulation, self.population.size)

        return Population(self.population.size, newUnits[:self.population.size])

    def make(self, iterations):
        """
        :param iterations:
        :return:
        """
        for i in range(iterations):
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



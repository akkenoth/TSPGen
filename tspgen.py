#!/usr/bin/env python3

import sys

from Map import Map
from Operators.Crossing import EdgeCrosser
from Operators.Mutation import DisplacementMutator, InversionMutator
from Population import Evolution, Population, Unit
from Selection import TournamentSelector

def main():
	problemMap = Map.generateCNN(50, 15)
	# print("Generated %d cities:" % problemMap.size)
	# for city in problemMap.cities:
	# 	print("City " + str(city) + ", connections to: " + str(city.connections))

	# Unit generation 'benchmark'
	# print("Generated units:")
	# unit1 = Unit.generateUnitRand(problemMap)
	# print("Random: cost {0}, fitness {1}".format(unit1.cost, unit1.fitness))
	# unit2 = Unit.generateUnitDSRandom(problemMap)
	# print("DS Random: cost {0}, fitness {1}".format(unit2.cost, unit2.fitness))
	# unit3 = Unit.generateUnitDSGreedy(problemMap)
	# print("DS Greedy: cost {0}, fitness {1}".format(unit3.cost, unit3.fitness))

	# units = []
	# cost = 0
	# fitness = 0.0
	# for i in range(10):
	# 	unit = Unit.generateUnitRand(problemMap)
	# 	print("Unit {0}: fitness {1}, cost {2}".format(i+1, unit.fitness, unit.cost))
	# 	fitness += unit.fitness
	# 	cost += unit.cost
	# 	units.append(unit)
	# print("Avg fitness: {0}".format(fitness/10))
	# print("Avg cost: {0}".format(cost/10))

	"""
	problemMap2 = Map.readFromFile("samples/sampleMap.json")
	print("Read %d cities from file:" % problemMap2.size)
	"""
	
	units = []
	for i in range(10):
		units.append(Unit.generateUnitRand(problemMap))
	population = Population(10, units)

	# print("Initial population: ")
	# for i in range(len(population.units)):
	# 	unit = population.units[i]
	# 	print("{0}: {1} | {2}".format(i, unit.path, unit.fitness))

	# selector = TournamentSelector(6, 2)
	# crosser = EdgeCrosser()
	# mutator = DisplacementMutator(0.1)
	# evolution = Evolution(problemMap, population, selector, crosser, mutator)
	# evolution.make(10)

	sys.exit(0)

if __name__ == "__main__":
	main()

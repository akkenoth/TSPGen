#!/usr/bin/env python3

import sys

from Map import Map
from Operators.Crossing import EdgeCrosser
from Operators.Mutation import DisplacementMutator, InversionMutator
from Population import Population
from Population import Unit
from Selection import TournamentSelector

def main():
	problemMap = Map.generateCNN(50, 15)
	problemMap2 = Map.readFromFile("samples/sampleMap.json")
	# print("Generated %d cities:" % problemMap.size)
	# for city in problemMap.cities:
	# 	print("City " + str(city) + ", connections to: " + str(city.connections))
	# print("Read %d cities from file:" % problemMap2.size)
	# for city in problemMap2.cities:
	# 	print("City " + str(city) + ", connections to: " + str(city.connections))

	"""
	print("Map1:")
	print("Generated units:")
	unit1 = Unit.generateUnitRand(problemMap)
	print(unit1.path)
	unit2 = Unit.generateUnitRand(problemMap)
	print(unit2.path)

	print("Child of generated units:")
	crosser = EdgeCrosser()
	unit3 = crosser.make(problemMap, [unit1, unit2])
	print(unit3.path)

	print("Displacement mutated child:")
	displacementMutator = DisplacementMutator()
	unit4 = displacementMutator.make(problemMap, unit3)
	print(unit4.path)

	print("Inversion mutated child:")
	inversionMutator = InversionMutator()
	unit5 = inversionMutator.make(problemMap, unit3)
	print(unit5.path)

	print("Map2:")
	print("Generated units:")
	unit6 = Unit.generateUnitRand(problemMap2)
	print(unit6.path)
	unit7 = Unit.generateUnitRand(problemMap2)
	print(unit7.path)

	print("Child of generated units:")
	crosser = EdgeCrosser()
	unit8 = crosser.make(problemMap, [unit6, unit7])
	print(unit8.path)

	print("Displacement mutated child:")
	displacementMutator = DisplacementMutator()
	unit9 = displacementMutator.make(problemMap, unit8)
	print(unit9.path)

	print("Inversion mutated child:")
	inversionMutator = InversionMutator()
	unit10 = inversionMutator.make(problemMap, unit8)
	print(unit10.path)
	"""
	
	for city in problemMap.cities:
		print("City " + str(city) + ", connections to: " + str(city.connections))

	units = []
	populationSize = 10
	while len(units) < populationSize:
		units.append(Unit.generateUnit(problemMap))

	population = Population(populationSize, units)

	print("Initial population: ")
	for unit in population.units:
		print(unit.path, " | ", unit.fitness)
	print()

	selector = TournamentSelector()
	crosser = EdgeCrosser()
	mutator = DisplacementMutator()
	evolution = Evolution(problemMap, population, selector, crosser, mutator)

	evolution.make(10)


	sys.exit(0)

if __name__ == "__main__":
	main()

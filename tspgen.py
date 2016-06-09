#!/usr/bin/env python3

import sys

from Map import Map
from Operators.Crossing import EdgeCrosser
from Operators.Mutation import DisplacementMutator, InversionMutator
from Population import Population
from Population import Unit
from Selection import TournamentSelector

def main():
	problemMap = Map.generateCNN(50, 10)
	print("Generated %d cities:" % problemMap.size)
	for city in problemMap.cities:
		print("City " + str(city) + ", connections to: " + str(city.connections))

	print("Generated units:")
	unit1 = Unit.generateUnit(problemMap)
	print(unit1.path)
	unit2 = Unit.generateUnit(problemMap)
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

	sys.exit(0)

if __name__ == "__main__":
	main()

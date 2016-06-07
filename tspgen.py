import sys

from Map import Map
from Population import Population
from Population import Unit
from Selection import TournamentSelector
from Operators.Crossing import EdgeCrosser

def main():
	problemMap = Map.generateCNN(50, 4)
	print("Generated %d cities:" % problemMap.size)
	for city in problemMap.cities:
		print("City " + str(city) + ", connections to: " + str(city.connections))
	sys.exit(0)

if __name__ == "__main__":
	main()

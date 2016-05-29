import sys

from Map.Map import Map
from Population.Population import Population
from Population.Unit import Unit
from Selection.TournamentSelector import TournamentSelector

def main():
	problemMap = Map.generateCNN(50, 4)
	print("Generated %d cities:" % problemMap.size)
	for city in problemMap.cities:
		print("City " + str(city) + ", connections to: " + str(city.connections))
	sys.exit(0)

if __name__ == "__main__":
	main()

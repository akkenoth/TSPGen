from Map import City

class Map(object):
	"""Docstring for Map"""

	size = 0
	cities = []

	def __init__(self):
		#TODO
		pass

	def addCity(self, newCity):
		if not isinstance(newCity, City):
			raise Exception("argument is not a City!")
			return
		if not newCity in self.cities:
			newCity.setIndex(self.size)
			self.size = self.size + 1
			self.cities.append(newCity)

	#TODO map verification function, reading/saving from/to file, getDistance etc etc

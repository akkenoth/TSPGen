from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush

class MapPainter(object):
	def __init__(self, scene, displayCities, displayConnections, displayBestUnit):
		super().__init__()
		self.scene = scene
		self.displayCities = displayCities
		self.displayConnections = displayConnections
		self.displayBestUnit = displayBestUnit
		self.problemMap = None

	def setSceneSize(self, height, width):
		pass

	def setProblemMap(self, problemMap):
		self.problemMap = problemMap

	def setDisplayCities(self, enabled = False):
		self.displayCities = bool(enabled)

	def setDisplayConnections(self, enabled = False):
		self.displayConnections = bool(enabled)

	def setDisplayBestUnit(self, enabled = False):
		self.displayBestUnit = bool(enabled)

	def repaint(self):
		if self.problemMap is None:
			return
		print("repaint begin")
		self.scene.clear()
		height = self.scene.height()
		width = self.scene.width()

		brush = QBrush(Qt.SolidPattern)
		pen = QPen(brush, 2.0)

		print("repaint cities {0} {1}".format(height, width))
		for city in self.problemMap.cities:
			print("{0}: {1} {2} - {3} {4}".format(city.index, city.positionX, city.positionY, width * city.positionX, height * city.positionY))
			self.scene.addLine(width * city.positionX, height * city.positionY, width * city.positionX, height * city.positionY, pen)
		print("repaint end")

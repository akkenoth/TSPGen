class City(object):
	"""docstring for City"""

	index = -1
	positionX = 0.0
	positionY = 0.0
	connections = []

	def __init__(self, positionX, positionY):
		self.positionX = positionX
		self.positionY = positionY

	def setIndex(self, index):
		self.index = index

	def setPosition(self, positionX, positionY):
		#TODO
		pass

	def addConnection(self, index):
		if not index in self.connections:
			self.connections.append(index)

	def removeConnection(self, index):
		#TODO
		pass

	def hasConnection(self, index):
		return index in self.connections

	#TODO

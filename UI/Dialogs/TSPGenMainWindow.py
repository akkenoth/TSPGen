from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QLabel, QGraphicsScene

from UI import MapPainter
from UI.Dialogs import MapGenerationDialog
from UI.Layouts.TSPGenMainWindow import Ui_TSPGenMainWindow
from UI.Wrappers import MapGenerator

class TSPGenMainWindow(QMainWindow):
    """Docstring for TSPGenMainWindow"""

    def __init__(self):
        QMainWindow.__init__(self)
        self.problemMap = None

        self.statusbarMapMessage = "No problem map"
        self.statusbarPopulationMessage = "No population"
        self.statusbarBestUnitMessage = "No best unit"

        # Setup UI elements
        self.ui = Ui_TSPGenMainWindow()
        self.ui.setupUi(self)
        self.ui.statusbarLabel = QLabel("", self)
        self.ui.statusbarLabel.setObjectName("statusbarLabel")
        self.ui.statusbar.addPermanentWidget(self.ui.statusbarLabel)

        # Setup asynchronous objects
        self.mapGenerator = MapGenerator(self)

        # Map painter
        displayCities = self.ui.checkBoxDisplayCities.isChecked()
        displayConnections = self.ui.checkBoxDisplayConnections.isChecked()
        displayBestUnit = self.ui.checkBoxDisplayBestUnit.isChecked()
        self.mapPainter = MapPainter(self, self.ui.graphicsViewMap, displayCities, displayConnections, displayBestUnit)

        # Refresh display elements
        self.refreshStatusbarMessage()

        # Setup UI actions - signals/slots
        self.setupUIActions()

    def setupUIActions(self):
        # Menu
        self.ui.actionImportMap.triggered.connect(self.importMap)
        self.ui.actionGenerateMap.triggered.connect(self.displayMapGenerationDialog)
        
        # Checkboxes
        self.ui.checkBoxDisplayCities.stateChanged.connect(self.toggleDisplayCities)
        self.ui.checkBoxDisplayConnections.stateChanged.connect(self.toggleDisplayConnections)
        self.ui.checkBoxDisplayBestUnit.stateChanged.connect(self.toggleDisplayBestUnit)

        # Map Generator
        self.mapGenerator.mapGenerated.connect(self.mapGenerated)
        self.mapGenerator.mapGenerationFailed.connect(self.mapGenerationFailed)

        # Map View
        # self.ui.graphicsViewMap.rubberBandChanged.connect(self.mapPainter.repaint)

    def importMap(self):
        filename = QFileDialog.getOpenFileName(self, "TSPGen - load problem map", filter = "JSON File (*.json)")
        if not filename[0]:
            return

        self.mapGenerator.setGenerationMode(True, filename[0])
        self.statusbarMapMessage = "Loading problem map..."
        self.refreshStatusbarMessage()
        self.mapGenerator.start()

    def displayMapGenerationDialog(self):
        citiesCount, connectionsCount, statusOK = MapGenerationDialog.getMapProperties(self)
        if not statusOK:
            return
        self.mapGenerator.setGenerationMode(False, "", citiesCount, connectionsCount)
        self.statusbarMapMessage = "Loading problem map..."
        self.refreshStatusbarMessage()
        self.mapGenerator.start()

    def toggleDisplayCities(self, state):
        self.mapPainter.setDisplayCities(state)
        self.mapPainter.repaint()

    def toggleDisplayConnections(self, state):
        self.mapPainter.setDisplayConnections(state)
        self.mapPainter.repaint()

    def toggleDisplayBestUnit(self, state):
        self.mapPainter.setDisplayBestUnit(state)
        self.mapPainter.repaint()

    def mapGenerated(self, problemMap):
        self.problemMap = problemMap
        self.statusbarMapMessage = "Map: {0} cities".format(problemMap.size)
        self.refreshStatusbarMessage()
        self.mapPainter.setProblemMap(problemMap)
        self.mapPainter.repaint()

    def mapGenerationFailed(self, e):
        QMessageBox.warning(self, "TSPGen - Error", "Error during map generation: {0}".format(e), QMessageBox.Ok, QMessageBox.Ok)
        self.statusbarMapMessage = "Map generation/loading failed"
        self.refreshStatusbarMessage()

    def refreshStatusbarMessage(self):
        self.ui.statusbarLabel.setText("{0} | {1} | {2}".format(self.statusbarMapMessage, self.statusbarPopulationMessage, self.statusbarBestUnitMessage))

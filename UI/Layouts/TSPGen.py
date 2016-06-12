# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TSPGen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TSPGen(object):
	def setupUi(self, TSPGen):
		TSPGen.setObjectName("TSPGen")
		TSPGen.resize(600, 480)
		TSPGen.setStatusTip("")
		self.centralwidget = QtWidgets.QWidget(TSPGen)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
		self.graphicsView.setObjectName("graphicsView")
		self.verticalLayout.addWidget(self.graphicsView)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.checkBoxDisplayCities = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBoxDisplayCities.setObjectName("checkBoxDisplayCities")
		self.horizontalLayout.addWidget(self.checkBoxDisplayCities)
		self.checkBoxDisplayConnections = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBoxDisplayConnections.setObjectName("checkBoxDisplayConnections")
		self.horizontalLayout.addWidget(self.checkBoxDisplayConnections)
		self.checkBoxDisplayBestUnit = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBoxDisplayBestUnit.setObjectName("checkBoxDisplayBestUnit")
		self.horizontalLayout.addWidget(self.checkBoxDisplayBestUnit)
		self.verticalLayout.addLayout(self.horizontalLayout)
		TSPGen.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(TSPGen)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
		self.menubar.setObjectName("menubar")
		self.menuMap = QtWidgets.QMenu(self.menubar)
		self.menuMap.setObjectName("menuMap")
		self.menuPopulation = QtWidgets.QMenu(self.menubar)
		self.menuPopulation.setObjectName("menuPopulation")
		self.menuGeneration = QtWidgets.QMenu(self.menubar)
		self.menuGeneration.setObjectName("menuGeneration")
		TSPGen.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(TSPGen)
		self.statusbar.setSizeGripEnabled(True)
		self.statusbar.setObjectName("statusbar")
		TSPGen.setStatusBar(self.statusbar)
		self.actionImport = QtWidgets.QAction(TSPGen)
		self.actionImport.setObjectName("actionImport")
		self.actionGenerate = QtWidgets.QAction(TSPGen)
		self.actionGenerate.setObjectName("actionGenerate")
		self.actionGenerateNew = QtWidgets.QAction(TSPGen)
		self.actionGenerateNew.setObjectName("actionGenerateNew")
		self.actionDisplay = QtWidgets.QAction(TSPGen)
		self.actionDisplay.setObjectName("actionDisplay")
		self.actionProcess = QtWidgets.QAction(TSPGen)
		self.actionProcess.setObjectName("actionProcess")
		self.menuMap.addAction(self.actionImport)
		self.menuMap.addAction(self.actionGenerate)
		self.menuPopulation.addAction(self.actionGenerateNew)
		self.menuPopulation.addAction(self.actionDisplay)
		self.menuGeneration.addAction(self.actionProcess)
		self.menubar.addAction(self.menuMap.menuAction())
		self.menubar.addAction(self.menuPopulation.menuAction())
		self.menubar.addAction(self.menuGeneration.menuAction())

		self.retranslateUi(TSPGen)
		QtCore.QMetaObject.connectSlotsByName(TSPGen)

	def retranslateUi(self, TSPGen):
		_translate = QtCore.QCoreApplication.translate
		TSPGen.setWindowTitle(_translate("TSPGen", "TSPGen"))
		self.checkBoxDisplayCities.setText(_translate("TSPGen", "Display cities"))
		self.checkBoxDisplayConnections.setText(_translate("TSPGen", "Display connections"))
		self.checkBoxDisplayBestUnit.setText(_translate("TSPGen", "Display best unit"))
		self.menuMap.setTitle(_translate("TSPGen", "Map"))
		self.menuPopulation.setTitle(_translate("TSPGen", "Population"))
		self.menuGeneration.setTitle(_translate("TSPGen", "Generation"))
		self.actionImport.setText(_translate("TSPGen", "Import..."))
		self.actionGenerate.setText(_translate("TSPGen", "Generate"))
		self.actionGenerateNew.setText(_translate("TSPGen", "Generate new..."))
		self.actionDisplay.setText(_translate("TSPGen", "Display"))
		self.actionProcess.setText(_translate("TSPGen", "Process"))
		self.actionProcess.setShortcut(_translate("TSPGen", "F9"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	TSPGen = QtWidgets.QMainWindow()
	ui = Ui_TSPGen()
	ui.setupUi(TSPGen)
	TSPGen.show()
	sys.exit(app.exec_())


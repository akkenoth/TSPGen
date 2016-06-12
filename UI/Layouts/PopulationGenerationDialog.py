# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopulationGenerationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PopulationGenerationDialog(object):
	def setupUi(self, PopulationGenerationDialog):
		PopulationGenerationDialog.setObjectName("PopulationGenerationDialog")
		PopulationGenerationDialog.resize(220, 110)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(PopulationGenerationDialog.sizePolicy().hasHeightForWidth())
		PopulationGenerationDialog.setSizePolicy(sizePolicy)
		PopulationGenerationDialog.setMinimumSize(QtCore.QSize(220, 110))
		PopulationGenerationDialog.setMaximumSize(QtCore.QSize(220, 110))
		self.verticalLayout = QtWidgets.QVBoxLayout(PopulationGenerationDialog)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtWidgets.QLabel(PopulationGenerationDialog)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.spinBox = QtWidgets.QSpinBox(PopulationGenerationDialog)
		self.spinBox.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
		self.spinBox.setMinimum(6)
		self.spinBox.setMaximum(50)
		self.spinBox.setProperty("value", 15)
		self.spinBox.setObjectName("spinBox")
		self.horizontalLayout.addWidget(self.spinBox)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.label_2 = QtWidgets.QLabel(PopulationGenerationDialog)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_2.addWidget(self.label_2)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem1)
		self.comboBox = QtWidgets.QComboBox(PopulationGenerationDialog)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
		self.comboBox.setSizePolicy(sizePolicy)
		self.comboBox.setMinimumSize(QtCore.QSize(140, 20))
		self.comboBox.setMaximumSize(QtCore.QSize(140, 20))
		self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
		self.comboBox.setFrame(True)
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.horizontalLayout_2.addWidget(self.comboBox)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem2)
		self.buttonBox = QtWidgets.QDialogButtonBox(PopulationGenerationDialog)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(PopulationGenerationDialog)
		self.buttonBox.accepted.connect(PopulationGenerationDialog.accept)
		self.buttonBox.rejected.connect(PopulationGenerationDialog.reject)
		QtCore.QMetaObject.connectSlotsByName(PopulationGenerationDialog)

	def retranslateUi(self, PopulationGenerationDialog):
		_translate = QtCore.QCoreApplication.translate
		PopulationGenerationDialog.setWindowTitle(_translate("PopulationGenerationDialog", "Population Generation"))
		self.label.setText(_translate("PopulationGenerationDialog", "Number of units"))
		self.label_2.setText(_translate("PopulationGenerationDialog", "Method"))
		self.comboBox.setItemText(0, _translate("PopulationGenerationDialog", "Random (recommended)"))
		self.comboBox.setItemText(1, _translate("PopulationGenerationDialog", "Depth search"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	PopulationGenerationDialog = QtWidgets.QDialog()
	ui = Ui_PopulationGenerationDialog()
	ui.setupUi(PopulationGenerationDialog)
	PopulationGenerationDialog.show()
	sys.exit(app.exec_())


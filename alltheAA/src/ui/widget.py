# Form implementation generated from reading ui file '/Users/corykornowicz/Documents/ChimeraTools/AllTheAminoAcids/alltheAA/src/ui/widget.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(679, 517)
        self.layoutWidget = QtWidgets.QWidget(Widget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 621, 491))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ligandImageArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.ligandImageArea.setMinimumSize(QtCore.QSize(250, 20))
        self.ligandImageArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ligandImageArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.ligandImageArea.setWidgetResizable(False)
        self.ligandImageArea.setObjectName("ligandImageArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 16, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.ligandImageArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.ligandImageArea, 3, 0, 6, 1)
        self.ligandSearchText = QtWidgets.QLineEdit(self.layoutWidget)
        self.ligandSearchText.setObjectName("ligandSearchText")
        self.gridLayout.addWidget(self.ligandSearchText, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.ligandSearchButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ligandSearchButton.setDefault(False)
        self.ligandSearchButton.setObjectName("ligandSearchButton")
        self.gridLayout.addWidget(self.ligandSearchButton, 0, 1, 1, 1)
        self.resetNormalAAButton = QtWidgets.QPushButton(self.layoutWidget)
        self.resetNormalAAButton.setObjectName("resetNormalAAButton")
        self.gridLayout.addWidget(self.resetNormalAAButton, 8, 1, 1, 1)
        self.ligandTotalLabel = QtWidgets.QLabel(self.layoutWidget)
        self.ligandTotalLabel.setObjectName("ligandTotalLabel")
        self.gridLayout.addWidget(self.ligandTotalLabel, 7, 1, 1, 1)
        self.searchOperationBox = QtWidgets.QComboBox(self.layoutWidget)
        self.searchOperationBox.setObjectName("searchOperationBox")
        self.searchOperationBox.addItem("")
        self.searchOperationBox.addItem("")
        self.searchOperationBox.addItem("")
        self.gridLayout.addWidget(self.searchOperationBox, 0, 2, 1, 1)
        self.pageBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.pageBox.setSuffix("")
        self.pageBox.setMinimum(1)
        self.pageBox.setMaximum(999)
        self.pageBox.setObjectName("pageBox")
        self.gridLayout.addWidget(self.pageBox, 3, 1, 1, 1)
        self.aminoAcidComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.aminoAcidComboBox.setEditable(False)
        self.aminoAcidComboBox.setObjectName("aminoAcidComboBox")
        self.gridLayout.addWidget(self.aminoAcidComboBox, 1, 0, 1, 1)
        self.pageLabel = QtWidgets.QLabel(self.layoutWidget)
        self.pageLabel.setEnabled(True)
        self.pageLabel.setObjectName("pageLabel")
        self.gridLayout.addWidget(self.pageLabel, 6, 1, 1, 1)
        self.browseSimilarButton = QtWidgets.QPushButton(self.layoutWidget)
        self.browseSimilarButton.setObjectName("browseSimilarButton")
        self.gridLayout.addWidget(self.browseSimilarButton, 1, 1, 1, 1)
        self.browseOperationBox = QtWidgets.QComboBox(self.layoutWidget)
        self.browseOperationBox.setObjectName("browseOperationBox")
        self.browseOperationBox.addItem("")
        self.browseOperationBox.addItem("")
        self.gridLayout.addWidget(self.browseOperationBox, 1, 2, 1, 1)
        self.ligExpoProgressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.ligExpoProgressBar.setEnabled(True)
        self.ligExpoProgressBar.setProperty("value", 0)
        self.ligExpoProgressBar.setTextVisible(False)
        self.ligExpoProgressBar.setObjectName("ligExpoProgressBar")
        self.gridLayout.addWidget(self.ligExpoProgressBar, 4, 1, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Form"))
        self.ligandSearchButton.setText(_translate("Widget", "Search"))
        self.resetNormalAAButton.setText(_translate("Widget", "Reset to Standard AA"))
        self.ligandTotalLabel.setText(_translate("Widget", "Total: 20"))
        self.searchOperationBox.setItemText(0, _translate("Widget", "name-exact"))
        self.searchOperationBox.setItemText(1, _translate("Widget", "name-substring"))
        self.searchOperationBox.setItemText(2, _translate("Widget", "name-close"))
        self.pageLabel.setText(_translate("Widget", "Page: 1"))
        self.browseSimilarButton.setText(_translate("Widget", "Browse By Similarity"))
        self.browseOperationBox.setItemText(0, _translate("Widget", "smiles"))
        self.browseOperationBox.setItemText(1, _translate("Widget", "fpsmi"))
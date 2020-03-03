# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finish.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Finish(object):
    def setupUi(self, Finish):
        Finish.setObjectName("Finish")
        Finish.resize(197, 295)
        Finish.setSizeGripEnabled(False)

        self.verticalLayout = QtWidgets.QVBoxLayout(Finish)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.imieLabel = QtWidgets.QLabel(Finish)
        self.imieLabel.setObjectName("imieLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.imieLabel)
        self.labelImie = QtWidgets.QLabel(Finish)
        self.labelImie.setText("")
        self.labelImie.setScaledContents(False)
        self.labelImie.setObjectName("labelImie")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelImie)

        self.nazwiskoLabel = QtWidgets.QLabel(Finish)
        self.nazwiskoLabel.setObjectName("nazwiskoLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nazwiskoLabel)
        self.labelNazwisko = QtWidgets.QLabel(Finish)
        self.labelNazwisko.setText("")
        self.labelNazwisko.setObjectName("labelNazwisko")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelNazwisko)

        self.dataLabel = QtWidgets.QLabel(Finish)
        self.dataLabel.setObjectName("dataLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dataLabel)
        self.labelData = QtWidgets.QLabel(Finish)
        self.labelData.setText("")
        self.labelData.setObjectName("labelData")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelData)

        self.nartyLabel = QtWidgets.QLabel(Finish)
        self.nartyLabel.setObjectName("nartyLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.nartyLabel)
        self.labelNarty = QtWidgets.QLabel(Finish)
        self.labelNarty.setText("")
        self.labelNarty.setObjectName("labelNarty")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelNarty)

        self.snowboardLabel = QtWidgets.QLabel(Finish)
        self.snowboardLabel.setObjectName("snowboardLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.snowboardLabel)
        self.labelSnowboard = QtWidgets.QLabel(Finish)
        self.labelSnowboard.setText("")
        self.labelSnowboard.setObjectName("labelSnowboard")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.labelSnowboard)

        self.butyLabel = QtWidgets.QLabel(Finish)
        self.butyLabel.setObjectName("butyLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.butyLabel)
        self.labelButy = QtWidgets.QLabel(Finish)
        self.labelButy.setText("")
        self.labelButy.setObjectName("labelButy")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.labelButy)

        self.kaskLabel = QtWidgets.QLabel(Finish)
        self.kaskLabel.setObjectName("kaskLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.kaskLabel)
        self.labelKask = QtWidgets.QLabel(Finish)
        self.labelKask.setText("")
        self.labelKask.setObjectName("labelKask")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.labelKask)

        self.kijkiLabel = QtWidgets.QLabel(Finish)
        self.kijkiLabel.setObjectName("kijkiLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.kijkiLabel)
        self.labelKijki = QtWidgets.QLabel(Finish)
        self.labelKijki.setText("")
        self.labelKijki.setObjectName("labelKijki")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.labelKijki)

        self.ileDniLabel = QtWidgets.QLabel(Finish)
        self.ileDniLabel.setObjectName("ileDniLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.ileDniLabel)
        self.labelIleDni = QtWidgets.QLabel(Finish)
        self.labelIleDni.setText("")
        self.labelIleDni.setObjectName("labelIleDni")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.labelIleDni)

        self.priceLabel = QtWidgets.QLabel(Finish)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.priceLabel.setFont(font)
        self.priceLabel.setObjectName("priceLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.priceLabel)
        self.labelPrize = QtWidgets.QLabel(Finish)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPrize.setFont(font)
        self.labelPrize.setText("")
        self.labelPrize.setObjectName("labelPrize")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.labelPrize)

        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Finish)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Finish)
        self.buttonBox.accepted.connect(Finish.accept)
        self.buttonBox.rejected.connect(Finish.reject)
        QtCore.QMetaObject.connectSlotsByName(Finish)

    def retranslateUi(self, Finish):
        _translate = QtCore.QCoreApplication.translate
        Finish.setWindowTitle(_translate("Finish", "Rozlicz"))
        self.imieLabel.setText(_translate("Finish", "Imie:"))
        self.nazwiskoLabel.setText(_translate("Finish", "Nazwisko:"))
        self.dataLabel.setText(_translate("Finish", "Data wypożyczenia:"))
        self.nartyLabel.setText(_translate("Finish", "Narty: "))
        self.snowboardLabel.setText(_translate("Finish", "Snowboard:"))
        self.butyLabel.setText(_translate("Finish", "Buty:"))
        self.kaskLabel.setText(_translate("Finish", "Kask:"))
        self.kijkiLabel.setText(_translate("Finish", "Kijki:"))
        self.ileDniLabel.setText(_translate("Finish", "Ilość dni:"))
        self.priceLabel.setText(_translate("Finish", "Do zapłaty: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Finish = QtWidgets.QDialog()
    ui = Ui_Finish()
    ui.setupUi(Finish)
    Finish.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dane.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(286, 352)
        self.formLayout_2 = QtWidgets.QFormLayout(Dialog)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.imieLabel = QtWidgets.QLabel(Dialog)
        self.imieLabel.setObjectName("imieLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.imieLabel)
        self.imieLineEdit = QtWidgets.QLineEdit(Dialog)
        self.imieLineEdit.setObjectName("imieLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.imieLineEdit)
        self.nazwiskoLabel = QtWidgets.QLabel(Dialog)
        self.nazwiskoLabel.setObjectName("nazwiskoLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nazwiskoLabel)
        self.nazwiskoLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nazwiskoLineEdit.setObjectName("nazwiskoLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nazwiskoLineEdit)
        self.dataWypozyczeniaLabel = QtWidgets.QLabel(Dialog)
        self.dataWypozyczeniaLabel.setObjectName("dataWypozyczeniaLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dataWypozyczeniaLabel)
        self.dataWypozyczeniaDateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dataWypozyczeniaDateTimeEdit.setCalendarPopup(True)
        self.dataWypozyczeniaDateTimeEdit.setObjectName("dataWypozyczeniaDateTimeEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dataWypozyczeniaDateTimeEdit)
        self.nartyLabel = QtWidgets.QLabel(Dialog)
        self.nartyLabel.setObjectName("nartyLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.nartyLabel)
        self.nartySpinBox = QtWidgets.QSpinBox(Dialog)

        self.nartySpinBox.setObjectName("nartySpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.nartySpinBox)
        self.snowboardLabel = QtWidgets.QLabel(Dialog)
        self.snowboardLabel.setObjectName("snowboardLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.snowboardLabel)
        self.snowboardSpinBox = QtWidgets.QSpinBox(Dialog)
        self.snowboardSpinBox.setObjectName("snowboardSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.snowboardSpinBox)
        self.butyLabel = QtWidgets.QLabel(Dialog)
        self.butyLabel.setObjectName("butyLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.butyLabel)
        self.butySpinBox = QtWidgets.QSpinBox(Dialog)
        self.butySpinBox.setObjectName("butySpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.butySpinBox)
        self.kaskLabel = QtWidgets.QLabel(Dialog)
        self.kaskLabel.setObjectName("kaskLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.kaskLabel)
        self.kaskSpinBox = QtWidgets.QSpinBox(Dialog)
        self.kaskSpinBox.setObjectName("kaskSpinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.kaskSpinBox)
        self.kijkiLabel = QtWidgets.QLabel(Dialog)
        self.kijkiLabel.setObjectName("kijkiLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.kijkiLabel)
        self.kijkiSpinBox = QtWidgets.QSpinBox(Dialog)
        self.kijkiSpinBox.setObjectName("kijkiSpinBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.kijkiSpinBox)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dane"))
        self.imieLabel.setText(_translate("Dialog", "Imie: "))
        self.nazwiskoLabel.setText(_translate("Dialog", "Nazwisko:"))
        self.dataWypozyczeniaLabel.setText(_translate("Dialog", "Data wypożyczenia:"))
        self.nartyLabel.setText(_translate("Dialog", "Narty"))
        self.snowboardLabel.setText(_translate("Dialog", "Snowboard"))
        self.butyLabel.setText(_translate("Dialog", "Buty"))
        self.kaskLabel.setText(_translate("Dialog", "Kask"))
        self.kijkiLabel.setText(_translate("Dialog", "Kijki"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

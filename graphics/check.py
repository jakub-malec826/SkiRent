# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(215, 124)
        Dialog.setBaseSize(QtCore.QSize(215, 124))
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(6, -1, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.nazwiskoLineEdit.setText("")
        self.nazwiskoLineEdit.setObjectName("nazwiskoLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nazwiskoLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sprawdź"))
        self.imieLabel.setText(_translate("Dialog", "imie:"))
        self.nazwiskoLabel.setText(_translate("Dialog", "nazwisko:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'archiwum.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Archiwum(object):
    def setupUi(self, Archiwum):
        Archiwum.setObjectName("Archiwum")
        Archiwum.setFixedSize(870, 244)

        self.verticalLayout = QtWidgets.QVBoxLayout(Archiwum)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Archiwum)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setViewportMargins(20,0,20,0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 115)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3, 83)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.setColumnWidth(4, 83)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.setColumnWidth(5, 83)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.setColumnWidth(6, 83)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.setColumnWidth(7, 83)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)

        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Archiwum)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Archiwum)
        self.buttonBox.accepted.connect(Archiwum.accept)
        self.buttonBox.rejected.connect(Archiwum.reject)
        QtCore.QMetaObject.connectSlotsByName(Archiwum)

    def retranslateUi(self, Archiwum):
        _translate = QtCore.QCoreApplication.translate
        Archiwum.setWindowTitle(_translate("Archiwum", "Archiwum Klientów"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Archiwum", "Imię"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Archiwum", "Nazwisko"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Archiwum", "DataWypo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Archiwum", "Narty"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Archiwum", "Snowboard"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Archiwum", "Buty"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Archiwum", "Kask"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Archiwum", "Kijki"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Archiwum", "Rozliczony"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Archiwum = QtWidgets.QDialog()
    ui = Ui_Archiwum()
    ui.setupUi(Archiwum)
    Archiwum.show()
    sys.exit(app.exec_())

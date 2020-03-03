import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from graphics import mainWindow, check, dane, show, error, archiwum, finish
import base.database as base
import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.Ui = mainWindow.Ui_MainWindow()
        self.Ui.setupUi(self)

        self.Ui.closeButton.clicked.connect(self.endProgram)
        self.Ui.addButton.clicked.connect(self.dialog)
        self.Ui.showButton.clicked.connect(self.showCheck)
        self.Ui.changeButton.clicked.connect(self.changeCheck)
        self.Ui.finishButton.clicked.connect(self.finishCheck)

        self.Ui.showArch.triggered.connect(self.showArch)

    def endProgram(self):
        self.close()
        based.close()

    def dialog(self):
        self.dane = Dane()
        self.dane.show()

    def showCheck(self):
        self.check = Check()
        self.check.showCheck()

    def changeCheck(self):
        self.check = Check()
        self.check.changeCheck()

    def finishCheck(self):
        self.check = Check()

    def showArch(self):
        self.arch = Archiwum()
        self.arch.dane()
        self.arch.show()


class Archiwum(QDialog):
    def __init__(self):
        super(Archiwum, self).__init__()
        self.Ui = archiwum.Ui_Archiwum()
        self.Ui.setupUi(self)

    def dane(self):
        self.allRows = based.fetchAll()
        self.Ui.tableWidget.setRowCount(len(self.allRows))
        row = 0
        for name in self.allRows:
            self.Ui.tableWidget.setItem(row, 0, QTableWidgetItem(name[0]))
            self.Ui.tableWidget.setItem(row, 1, QTableWidgetItem(name[1]))
            self.Ui.tableWidget.setItem(row, 2, QTableWidgetItem(name[2]))
            self.Ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(name[3])))
            self.Ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(name[4])))
            self.Ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(name[5])))
            self.Ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(name[6])))
            self.Ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(name[7])))
            self.Ui.tableWidget.setItem(row, 8, QTableWidgetItem(name[8]))
            row += 1


class Dane(QDialog):
    def __init__(self):
        super(Dane, self).__init__()
        self.Ui = dane.Ui_Dialog()
        self.Ui.setupUi(self)
        self.Ui.dataWypozyczeniaDateTimeEdit.setDateTime(datetime.datetime.today())

        self.Ui.buttonBox.accepted.connect(self.values)

    def values(self):
        self.imie = self.Ui.imieLineEdit.text()
        self.nazwisko = self.Ui.nazwiskoLineEdit.text()

        self.d = self.Ui.dataWypozyczeniaDateTimeEdit.dateTime()
        self.data = self.d.toString('dd/MM/yyyy HH:mm')

        self.narty = self.Ui.nartySpinBox.value()
        self.snowboard = self.Ui.snowboardSpinBox.value()
        self.buty = self.Ui.butySpinBox.value()
        self.kask = self.Ui.kaskSpinBox.value()
        self.kijki = self.Ui.kijkiSpinBox.value()

        try:
            if not self.imie or not self.nazwisko:
                raise ValueError('empty string')
            else:
                based.insert(self.imie, self.nazwisko, self.data,
                     self.narty, self.snowboard, self.buty, self.kask, self.kijki)
        except ValueError:
            self.err = Error()
            self.err.Ui.label.setText("Pola nie mogą być puste")
            self.err.show()


class Update(QDialog):
    def __init__(self):
        super(Update, self).__init__()
        self.Ui = dane.Ui_Dialog()
        self.Ui.setupUi(self)

    def values(self, simie, snazwisko):
        self.imie = self.Ui.imieLineEdit.text()
        self.nazwisko = self.Ui.nazwiskoLineEdit.text()

        self.d = self.Ui.dataWypozyczeniaDateTimeEdit.dateTime()
        self.data = self.d.toString('dd/MM/yyyy HH:mm')
        self.narty = self.Ui.nartySpinBox.value()
        self.snowboard = self.Ui.snowboardSpinBox.value()
        self.buty = self.Ui.butySpinBox.value()
        self.kask = self.Ui.kaskSpinBox.value()
        self.kijki = self.Ui.kijkiSpinBox.value()
        try:
            if not self.imie or not self.nazwisko:
                raise ValueError('empty string')
            else:
                based.update(self.imie, self.nazwisko, self.data,
                            self.narty, self.snowboard, self.buty, self.kask, self.kijki, simie, snazwisko)
        except ValueError:
            self.err = Error()
            self.err.Ui.label.setText("Pola nie mogą być puste")
            self.err.show()

    def dane(self, imie, nazwisko, data, narty, snowboard, buty, kask, kijki):
        self.Ui.imieLineEdit.setText(f"{imie}")
        self.Ui.nazwiskoLineEdit.setText(f"{nazwisko}")
        self.date = datetime.datetime.strptime(data, '%d/%m/%Y %H:%M')
        self.Ui.dataWypozyczeniaDateTimeEdit.setDateTime(self.date)
        self.Ui.nartySpinBox.setValue(int(narty))
        self.Ui.snowboardSpinBox.setValue(int(snowboard))
        self.Ui.butySpinBox.setValue(int(buty))
        self.Ui.kaskSpinBox.setValue(int(kask))
        self.Ui.kijkiSpinBox.setValue(int(kijki))


class Check(QDialog):
    def __init__(self):
        super(Check, self).__init__()
        self.Uic = check.Ui_Dialog()
        self.Uic.setupUi(self)
        self.exec()

    def values(self):
        self.imie = self.Uic.imieLineEdit.text()
        self.nazwisko = self.Uic.nazwiskoLineEdit.text()

        client = based.select(self.imie, self.nazwisko)
        return client

    def showCheck(self):

        client = self.values()

        for name in client:
            imie = name['Imie']
            nazwisko = name['Nazwisko']
            data = name['DataWypo']
            narty = name['Narty']
            snowboard = name['Snowboard']
            buty = name['Buty']
            kask = name['Kask']
            kijki = name['Kijki']
            rozliczony = name['Rozliczony']

        try:
            self.showc = Show()
            self.showc.data(imie, nazwisko, data, narty, snowboard, buty, kask, kijki, rozliczony)
            self.showc.show()
        except UnboundLocalError:
            self.err = Error()
            self.err.Ui.label.setText("Nie ma takiego klienta w bazie")
            self.err.show()

    def changeCheck(self):
        client = self.values()
        for name in client:
            imie = name['Imie']
            nazwisko = name['Nazwisko']
            data = name['DataWypo']
            narty = name['Narty']
            snowboard = name['Snowboard']
            buty = name['Buty']
            kask = name['Kask']
            kijki = name['Kijki']
        try:
            self.update = Update()
            self.update.dane(imie, nazwisko, data, narty, snowboard, buty, kask, kijki)
            self.update.show()
        except UnboundLocalError:
            self.err = Error()
            self.err.Ui.label.setText("Nie ma takiego klienta w bazie")
            self.err.show()

        self.update.Ui.buttonBox.accepted.connect(lambda: self.update.values(imie, nazwisko))

    def finishCheck(self):

        client = self.values()

        for name in client:
            imie = name['Imie']
            nazwisko = name['Nazwisko']
            data = name['DataWypo']
            narty = name['Narty']
            snowboard = name['Snowboard']
            buty = name['Buty']
            kask = name['Kask']
            kijki = name['Kijki']

        try:
            pass
        except UnboundLocalError:
            self.err = Error()
            self.err.Ui.label.setText("Nie ma takiego klienta w bazie")
            self.err.show()


class Show(QDialog):
    def __init__(self):
        super(Show, self).__init__()
        self.Ui = show.Ui_Dialog()
        self.Ui.setupUi(self)

    def data(self, imie, nazwisko, data, narty, snowboard, buty, kask, kijki, rozliczony):
        self.Ui.labelImie.setText(f"{imie}")
        self.Ui.labelNazwisko.setText(f"{nazwisko}")
        self.Ui.labelData.setText(f"{data}")
        self.Ui.labelNarty.setText(f"{narty}")
        self.Ui.labelSnowboard.setText(f"{snowboard}")
        self.Ui.labelButy.setText(f"{buty}")
        self.Ui.labelKask.setText(f"{kask}")
        self.Ui.labelKijki.setText(f"{kijki}")
        self.Ui.labelRozliczony.setText(f"{rozliczony}")


class Error(QDialog):
    def __init__(self):
        super(Error, self).__init__()
        self.Ui = error.Ui_Error()
        self.Ui.setupUi(self)


class Finish(QDialog):
    def __init__(self):
        super(Finish, self).__init__()
        self.Ui = finish.Ui_Finish()
        self.Ui.setupUi(self)

    def data(self, imie, nazwisko, data, narty, snowboard, buty, kask, kijki):
        self.Ui.labelImie.setText(f"{imie}")
        self.Ui.labelNazwisko.setText(f"{nazwisko}")
        self.Ui.labelData.setText(f"{data}")
        self.Ui.labelNarty.setText(f"{narty}")
        self.Ui.labelSnowboard.setText(f"{snowboard}")
        self.Ui.labelButy.setText(f"{buty}")
        self.Ui.labelKask.setText(f"{kask}")
        self.Ui.labelKijki.setText(f"{kijki}")

        self.date = datetime.datetime.strptime(data, '%d/%m/%Y %H:%M')
        self.current = datetime.datetime.now()
        self.delta = self.current - self.date
        ileDni = self.delta.days
        self.Ui.labelIleDni.setText(f"{ileDni}")

    def values(self, narty, snowboard, buty, kask, kijki):
        self.prize = 0
        self.cost = []

        if narty >= 1:
            self.cost.append(16)
        if snowboard >= 1:
            self.cost.append(8)
        if buty >= 1:
            self.cost.append(4)
        if kask >= 1:
            self.cost.append(2)
        if kijki >= 1:
            self.cost.append(1)

        l = sum(self.cost)

        if l >= 9 and l <= 31:
            self.prize = 20
        if l == 7 or l == 8 or l == 16:
            self.prize = 15
        if l == 3 or l == 4:
            self.prize = 10
        if l == 1 or l == 2:
            self.prize = 5

        self.komplet = [narty, snowboard, buty, kask, kijki]
        wyn = 0

        for x in range(0, 4):
            if self.komplet[x] != 0:
                wyn = self.komplet[x] * self.prize
        return wyn


if __name__ == "__main__":
    based = base.Base()
    based.connect()
    based.newDatabase()
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

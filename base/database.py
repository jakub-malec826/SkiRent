import sqlite3
import datetime
Error = sqlite3.ProgrammingError


class Base:
    def __init__(self):
        self.sql = None

    def connect(self):
        try:
            self.connect = sqlite3.connect("base/skirent.db")
            self.cur = self.connect.cursor()
            self.cur.row_factory = sqlite3.Row
            print("Connected")
        except Error:
            print(Error)

    def newDatabase(self):
        self.sql = """
            CREATE TABLE IF NOT EXISTS wypozyczalnia(
            Imie VARCHAR NOT NULL,
            Nazwisko VARCHAR NOT NULL,
            DataWypo TEXT NOT NULL,
            Narty INT NOT NUll,
            Snowboard INT NOT NUll,
            Buty INT NOT NUll,
            Kask INT NOT NUll,
            Kijki INT NOT NUll,
            Rozliczony VARCHAR(3) NOT NULL);
        """
        try:
            self.cur.execute(self.sql)
            self.connect.commit()
            print("Create")
        except Error:
            print(Error)

    def insert(self, imie, nazwisko, dataWypo, narty, snowboard, buty, kask, kijki):
        self.sql = f"""
            INSERT INTO wypozyczalnia VALUES ('{imie}', '{nazwisko}', '{dataWypo}', 
            '{narty}', '{snowboard}', '{buty}', '{kask}', '{kijki}', 'NIE'); 
        """

        try:
            self.cur.execute(self.sql)
            self.connect.commit()
            print("Added")
        except Error:
            print(Error)

    def select(self, imie, nazwisko):
        self.sql = f"""SELECT * FROM wypozyczalnia 
        WHERE Imie LIKE '{imie}' AND Nazwisko LIKE '{nazwisko}'"""

        try:
            self.cur.execute(self.sql)
        except Error:
            print(Error)

        select = self.cur.fetchall()
        return select

    def update(self, imie, nazwisko, data,
               narty, snowboard, buty, kask, kijki, simie, snazwisko):
        self.sql = f"""UPDATE wypozyczalnia
        SET Imie = '{imie}',
            Nazwisko = '{nazwisko}',
            DataWypo = '{data}',
            Narty = '{narty}',
            Snowboard = '{snowboard}',
            Buty = '{buty}',
            Kask = '{kask}',
            Kijki = '{kijki}'
        WHERE Imie = '{simie}' AND Nazwisko = '{snazwisko}';
        """
        try:
            self.cur.execute(self.sql)
            self.connect.commit()
        except Error:
            print(Error)

    def fetchAll(self):
        self.sql = """SELECT * FROM wypozyczalnia;"""

        try:
            self.cur.execute(self.sql)
        except Error:
            print(Error)

        self.allRows = self.cur.fetchall()
        return self.allRows

    def close(self):
        self.connect.close()

import sqlite3

import sqlite3
from sqlite3 import Error

# Ruda
class Banco:
    def __init__(self, catetoX, catetoY, hip) -> None:
        self.conn = sqlite3.connect('banco.db')
        self.cur = self.conn.cursor()
        self.catetoX = catetoX
        self.catetoY = catetoY
        self.hip = hip

    def salva(self):
        self.cur.execute("INSERT INTO TRIANGULOS (catetoX, catetoY, hip)VALUES (?, ?, ?)", (self.catetoX, self.catetoY, self.hip))
        self.conn.commit()
        self.conn.close()

# Ruda
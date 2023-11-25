import sys
import math
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from turtle import *
from arch_turtle import *
from bancoDeDados import Banco

# Cruz
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Catetando345")

        layout = QGridLayout()

        label1 = QLabel("Cateto X:")
        self.cateto1 = QLineEdit()
        self.cateto1.setValidator(QIntValidator())
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.cateto1, 0, 1)

        label2 = QLabel("Cateto Y:")
        self.cateto2 = QLineEdit()
        self.cateto2.setValidator(QIntValidator())
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.cateto2, 1, 1)

        button = QPushButton("Enviar")
        button.clicked.connect(self.btnRecebe)
        layout.addWidget(button, 2, 0, 1, 2)

        self.setLayout(layout)

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Exemplo PyQt6")

        self.show()

# Cruz

# Ethan

    def btnRecebe(self):
        cateto_x = int(self.cateto1.text())
        cateto_y = int(self.cateto2.text())
        hip = math.sqrt(math.pow(cateto_x, 2) + math.pow(cateto_y, 2))
        tutela = Tutel(cateto_x, cateto_y, hip)
        salva = Banco(cateto_x, cateto_y, hip)
        salva.salva()
        tutela.desenho()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()

# Ethan
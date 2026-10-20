import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QColor, QPalette
import random

minas = []

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscaminas")
        self.setFixedSize(500, 500)

        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("limegreen"))
        self.setPalette(paleta)

        widget_central = QWidget(self)
        self.setCentralWidget(widget_central)

        tablero = QGridLayout()
        widget_central.setLayout(tablero)

        self.casillas = []

        for i in range(8):
            for j in range(8):
                casilla = Casilla()
                self.casillas.append(casilla)

                if (casilla.mina):
                    minas.append(casilla)

                tablero.addWidget(casilla.boton, i, j)



class Casilla:
    def __init__(self):
        self.mina = random.choice([True, False])
        self.revelada = False
        self.boton = QPushButton(" ")
        self.boton.clicked.connect(self.revelar)

    def revelar(self):
        if self.mina:
            self.boton.setText("💣")
            for casilla in minas:
                casilla.boton.setText("💣")

        else:
            self.boton.setText("0")

        self.revelada = True
        self.boton.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
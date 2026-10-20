import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QRadioButton, QHBoxLayout, \
    QGridLayout, QPushButton
from PyQt6.QtGui import QColor, QPalette
import random


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

        for i in range(8):
            for j in range(8):
                casilla = Casilla()
                tablero.addWidget(casilla.boton, i, j)

        self.setLayout(tablero)

class Casilla:
    def __init__(self):
        self.mina = random.choice([True, False])
        self.revelada = False
        self.boton = QPushButton(f" ")
        self.boton.clicked.connect(self.revelar)

    def revelar(self):
        if self.mina:
            self.boton.setText("💣")
        else:
            self.boton.setText("0")
        self.revelada = True
        self.boton.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
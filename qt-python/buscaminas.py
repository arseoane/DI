import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QRadioButton, QHBoxLayout, \
    QGridLayout, QPushButton
from PyQt6.QtGui import QColor, QPalette


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

        for i in range(10):
            for j in range(10):
                boton = QPushButton(f"{i},{j}")
                tablero.addWidget(boton, i, j)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QColor, QPalette


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de Cuadrícula")

        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)

        diseno_cuadricula = QGridLayout()
        boton1 = QPushButton("A")
        boton2 = QPushButton("B")
        boton3 = QPushButton("C")
        boton4 = QPushButton("D")
        boton5 = QPushButton("E")
        boton6 = QPushButton("F")

        diseno_cuadricula.addWidget(boton1, 0, 0)
        diseno_cuadricula.addWidget(boton2, 1, 0)
        diseno_cuadricula.addWidget(boton3, 2, 0)
        diseno_cuadricula.addWidget(boton4, 3, 0)
        diseno_cuadricula.addWidget(boton5, 4, 0)
        diseno_cuadricula.addWidget(boton6, 0, 1, 2, 2)

        widget_principal = QWidget()
        widget_principal.setLayout(diseno_cuadricula)
        self.setCentralWidget(widget_principal)

        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
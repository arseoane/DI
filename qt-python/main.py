import sys

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class VentanaPrincipal(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Demo de Qt")
    self.setMinimumSize(720, 540)
    self.setMaximumSize(1120, 1020)

    paleta = self.palette()
    paleta.setColor(QPalette.ColorRole.Window, QColor("gray"))
    self.setPalette(paleta)

    # Inicialización de elementos
    self.campo_texto = QLineEdit()
    self.campo_texto.setPlaceholderText("Tu nombre")
    self.etiqueta = QLabel("Introduce tu nombre:")
    self.boton = QPushButton("Presióname")
    self.boton.clicked.connect(
        self.al_hacer_clic
    )  # Conectar el botón al método

    # Caja vertical
    disposicion_vertical = QVBoxLayout()
    contenedor_vertical = QWidget()
    contenedor_vertical.setLayout(disposicion_vertical)

    # print(self.boton.text())

    # Añadiendo los elementos a la caja vertical
    disposicion_vertical.addWidget(self.etiqueta)
    disposicion_vertical.addWidget(self.campo_texto)
    disposicion_vertical.addWidget(self.boton)
    self.setCentralWidget(
        contenedor_vertical
    )  # Establecer el contenedor como widget principal

    self.show()

  # Método que se ejecuta cuando el usuario hace clic en el botón principal
  def al_hacer_clic(self):
    if not self.campo_texto.text():
      self.etiqueta.setText("Por favor, introduce tu nombre")
    else:
      self.etiqueta.setText("Hola " + str(self.campo_texto.text()))


if __name__ == "__main__":
  aplicacion = QApplication(sys.argv)
  ventana = VentanaPrincipal()
  aplicacion.exec()
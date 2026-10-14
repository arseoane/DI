import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QRadioButton
from PyQt6.QtGui import QColor, QPalette


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ESCUELA")
        self.resize(400, 400)
        self.setMaximumSize(400, 400)

        # Color de fondo de la ventana principal
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("lightblue"))
        self.setPalette(paleta)

        # Widget central y diseño principal
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        diseno_principal = QVBoxLayout(widget_central)

        # Selector de tipo de usuario
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(("Estudiante", "Padre", "Profesor"))
        self.combo_tipo.setCurrentIndex(0)
        self.combo_tipo.currentIndexChanged.connect(self.manejar_cambio_combo)
        diseno_principal.addWidget(self.combo_tipo)

        # Selector de materia/curso
        self.combo_materia = QComboBox()
        self.combo_materia.addItems(("Informática", "Matemáticas", "Derecho"))
        self.combo_materia.setCurrentIndex(0)
        self.combo_materia.currentIndexChanged.connect(self.manejar_cambio_combo)
        diseno_principal.addWidget(self.combo_materia)

        # Opciones de nivel o año
        diseno_principal.addWidget(QRadioButton("1.º", self))
        diseno_principal.addWidget(QRadioButton("2.º", self))
        diseno_principal.addWidget(QRadioButton("3.º", self))
        diseno_principal.addWidget(QRadioButton("4.º", self))

        self.show()

    def manejar_cambio_combo(self):
        # Lógica para manejar el cambio en los ComboBox
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()
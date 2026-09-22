import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout, QFrame
)
from PyQt6.QtCore import Qt


class ColorBox(QFrame):
    """Usamos QFrame en lugar de QWidget genérico para que aplique bien los colores."""

    def __init__(self, color_hex):
        super().__init__()
        # Se establece un estilo explícito con borde transparente para forzar el pintado
        self.setStyleSheet(f"background-color: {color_hex}; border: none; border-radius: 2px;")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo PyQt6")
        self.resize(500, 300)

        # Contenedor principal usando QFrame para garantizar que el fondo gris se pinte
        central_widget = QFrame()
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background-color: #ECECEC;")

        # Layout horizontal principal (3 columnas)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # ------------------- Columna Izquierda -------------------
        left_layout = QVBoxLayout()
        left_layout.setSpacing(10)

        red_box_left = ColorBox("red")
        yellow_box = ColorBox("yellow")
        purple_box_left = ColorBox("purple")

        left_layout.addWidget(red_box_left)
        left_layout.addWidget(yellow_box)
        left_layout.addWidget(purple_box_left)

        # ------------------- Columna Central -------------------
        green_box = ColorBox("green")

        # ------------------- Columna Derecha -------------------
        right_layout = QVBoxLayout()
        right_layout.setSpacing(10)

        red_box_right = ColorBox("red")
        purple_box_right = ColorBox("purple")

        right_layout.addWidget(red_box_right)
        right_layout.addWidget(purple_box_right)

        # ---------------- Añadir a la ventana ----------------
        main_layout.addLayout(left_layout)
        main_layout.addWidget(green_box)
        main_layout.addLayout(right_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
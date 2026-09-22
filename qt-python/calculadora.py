import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(300, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background-color: #202020;")

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.pantalla = QLineEdit()
        self.pantalla.setFixedHeight(60)
        self.pantalla.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.pantalla.setReadOnly(True)
        self.pantalla.setFont(QFont("Arial", 20))
        self.pantalla.setStyleSheet("background-color: #101010; color: white; border: none; padding: 10px;")
        layout.addWidget(self.pantalla)

        grid = QGridLayout()
        grid.setSpacing(5)

        botones = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2, 1, 2)
        ]

        for btn_info in botones:
            texto = btn_info[0]
            row = btn_info[1]
            col = btn_info[2]
            row_span = btn_info[3] if len(btn_info) > 3 else 1
            col_span = btn_info[4] if len(btn_info) > 4 else 1

            btn = QPushButton(texto)
            btn.setFont(QFont("Arial", 14))

            if texto in ['/', '*', '-', '+', '=']:
                btn.setStyleSheet("background-color: #FF9500; color: white; border-radius: 5px;")
            elif texto in ['C', '(', ')']:
                btn.setStyleSheet("background-color: #A5A5A5; color: black; border-radius: 5px;")
            else:
                btn.setStyleSheet("background-color: #333333; color: white; border-radius: 5px;")

            btn.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Expanding
            )

            btn.clicked.connect(self.al_pulsar_boton)
            grid.addWidget(btn, row, col, row_span, col_span)

        layout.addLayout(grid)

    def al_pulsar_boton(self):
        boton = self.sender()
        texto = boton.text()

        if texto == 'C':
            self.pantalla.clear()
        elif texto == '=':
            try:
                resultado = eval(self.pantalla.text())
                self.pantalla.setText(str(resultado))
            except Exception:
                self.pantalla.setText("Error")
        else:
            if self.pantalla.text() == "Error":
                self.pantalla.clear()
            self.pantalla.setText(self.pantalla.text() + texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())
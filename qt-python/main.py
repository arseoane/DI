import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout,QPushButton,QHBoxLayout,QWidget, QLabel, QLineEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Demo")
        self.setMinimumSize(700, 520)
        self.setMaximumSize(1100, 1000)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("white"))
        self.setPalette(palette)


        button = QPushButton("Click me")
        self.setCentralWidget(button)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()



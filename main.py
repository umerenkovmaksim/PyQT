import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вычисление выражений')

        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(175, 40)
        self.btn.resize(30, 30)
        self.btn.clicked.connect(self.calculator)

        self.input1 = QLineEdit(self)
        self.input1.move(10, 40)
        self.input1.resize(160, 30)
        self.input2 = QLineEdit(self)
        self.input2.move(210, 40)
        self.input2.resize(160, 30)

    def calculator(self):
        self.input2.setText(f'{eval(self.input1.text())}')
        self.input1.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

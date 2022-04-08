import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton
from PyQt5.QtWidgets import QLabel
from functools import partial


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.pole = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.pole[i][j] = QPushButton('', self)
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Вычисление выражений')
        self.label = QLabel(self)
        self.label.resize(100, 20)
        self.label.move(165, 340)
        self.first_step = QRadioButton('X', self)
        self.first_step.clicked.connect(self.start_edit)
        self.first_step.move(150, 30)
        self.first_step1 = QRadioButton('O', self)
        self.first_step.click()
        self.first_step1.clicked.connect(self.start_edit1)
        self.first_step1.move(200, 30)

        for i in range(3):
            for j in range(3):
                self.pole[i][j].resize(70, 70)
                self.pole[i][j].move(80 * i + 80, 80 * j + 80)
                self.pole[i][j].clicked.connect(partial(self.edit_button, i, j))

    def start_edit(self):
        self.start = True
        for i in range(3):
            for j in range(3):
                self.pole[i][j].setText('')

    def start_edit1(self):
        self.start = False
        for i in range(3):
            for j in range(3):
                self.pole[i][j].setText('')

    def analis(self):
        if self.pole[0][0].text() == self.pole[0][1].text() == self.pole[0][2].text() != '' or \
                self.pole[1][0].text() == self.pole[1][1].text() == self.pole[1][2].text() != '' or \
                self.pole[2][0].text() == self.pole[2][1].text() == self.pole[2][2].text() != '' or \
                self.pole[0][0].text() == self.pole[1][0].text() == self.pole[2][0].text() != '' or \
                self.pole[0][1].text() == self.pole[1][1].text() == self.pole[2][1].text() != '' or \
                self.pole[0][2].text() == self.pole[1][2].text() == self.pole[2][2].text() != '' or \
                self.pole[0][0].text() == self.pole[1][1].text() == self.pole[2][2].text() != '' or \
                self.pole[0][2].text() == self.pole[1][1].text() == self.pole[2][0].text() != '':
            if self.start:
                return 'Выиграл Х'

    def edit_button(self, i, j):

        if self.pole[i][j].text():
            return
        else:
            if self.start:
                self.pole[i][j].setText('X')
                time.sleep(1)
                self.start = False

            else:
                self.pole[i][j].setText('O')
                self.start = True
        self.label.setText(self.analis())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

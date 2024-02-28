from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLineEdit, QLabel
import matplotlib.pyplot as plt
import numpy as np


class Charting(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def accept_button(self):
        self.polynomial = self.entering_function.text()
        ax = plt.gca()
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        x1 = np.arange(-20, 20, 0.01)
        x2 = []
        for i in range(len(x1)):
            x2.append(eval(self.polynomial, {'x':x1[i]}))
        plt.axis((-20, 20, min(x2), max(x2)))
        plt.plot(x1, x2)
        plt.ylabel(f'{self.polynomial}')
        plt.show()
        self.accept()

    def initUI(self):
        self.setWindowTitle('Построение графиков функций')
        self.setMinimumWidth(300)
        grid = QGridLayout()
        self.setLayout(grid)
        self.entering_function = QLineEdit()
        grid.addWidget(self.entering_function, 0, 0, 1, 2)
        self.hint = QLabel()
        grid.addWidget(self.hint, 1, 0, 1, 2)
        self.hint.setText('Подсказка: Ввод осуществляется через клавиатуру. Возведение в степень пишется как "**", '
                          'запись "#x", ''где # - число, пишется как "# * x"')
        accept_button = QPushButton('Ок')
        accept_button.clicked.connect(self.accept_button)
        grid.addWidget(accept_button, 2, 0)
        reject_button = QPushButton('Отмена')
        reject_button.clicked.connect(self.reject)
        grid.addWidget(reject_button, 2, 1)

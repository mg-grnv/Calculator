from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLineEdit, QLabel
import matplotlib.pyplot as plt
import numpy as np


class Charting(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.left_border_default = -100
        self.right_border_default = 100
        self.initUI()

    def accept_button(self):
        self.polynomial = self.entering_function.text()
        ax = plt.gca()
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        if len(self.left_border.text()) != 0 and len(self.right_border.text()) != 0:
            x1 = np.arange(int(self.left_border.text()), int(self.right_border.text()), 0.01)
        elif len(self.left_border.text()) == 0 and len(self.right_border.text()) == 0:
            x1 = np.arange(self.left_border_default, self.right_border_default, 0.01)
        x2 = []
        for i in range(len(x1)):
            x2.append(eval(self.polynomial, {'x':x1[i]}))
        if len(self.left_border.text()) != 0 and len(self.right_border.text()) != 0:
            # plt.axis((int(self.left_border.text()), int(self.right_border.text()), min(x2), max(x2)))
            plt.xlim((int(self.left_border.text()), int(self.right_border.text())))
            # plt.ylim((int(self.left_border.text()), int(self.right_border.text())))
        elif len(self.left_border.text()) == 0 and len(self.right_border.text()) == 0:
            # plt.axis(self.left_border_default, self.right_border_default, min(x2), max(x2))
            plt.xlim(self.left_border_default, self.right_border_default)
            # plt.ylim(self.left_border_default, self.right_border_default)
        plt.plot(x1, x2)
        plt.ylabel(f'{self.polynomial}')
        plt.show()
        self.accept()

    def initUI(self):
        self.setWindowTitle('Построение графиков функций')
        self.setMinimumWidth(300)
        grid = QGridLayout()
        # self.left_border_default = -100
        # self.right_border_default = 100
        self.setLayout(grid)
        self.entering_function = QLineEdit()
        grid.addWidget(self.entering_function, 0, 0, 1, 2)
        self.entering_function.setPlaceholderText('Введите функцию')
        self.hint = QLabel()
        grid.addWidget(self.hint, 3, 0, 1, 2)
        self.left_border = QLineEdit()
        grid.addWidget(self.left_border, 1, 0, 1, 2)
        self.left_border.setPlaceholderText('Введите значение левой границы оси X')
        self.right_border = QLineEdit()
        grid.addWidget(self.right_border, 2, 0, 1, 2)
        self.right_border.setPlaceholderText('Введите значение правой границы оси X')
        self.hint.setText('Подсказка: Ввод осуществляется через клавиатуру. Возведение в степень пишется как "**", '
                          'запись "#x", ''где # - число, пишется как "# * x"')
        accept_button = QPushButton('Ок')
        accept_button.clicked.connect(self.accept_button)
        grid.addWidget(accept_button, 4, 0)
        reject_button = QPushButton('Отмена')
        reject_button.clicked.connect(self.reject)
        grid.addWidget(reject_button, 4, 1)

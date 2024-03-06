from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLineEdit, QLabel, QSlider, QMessageBox, QColorDialog
import matplotlib.pyplot as plt
import numpy as np


class Charting(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def accept_button(self):
        self.formatting_function()
        self.polynomial = self.entering_function.text()
        ax = plt.gca()
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        if self.left_border.value() > self.right_border.value():
            error = QMessageBox()
            error.setWindowTitle('Внимание!')
            error.setText('Введены некорректные значения границ! Выставлены значения по умолчанию')
            self.left_border.setValue(-20)
            self.right_border.setValue(20)
            error.exec_()
        x1 = np.arange(self.left_border.value(), self.right_border.value(), 0.01)
        x2 = []
        try:
            for i in range(len(x1)):
                x2.append(eval(self.polynomial, {'x':x1[i]}))
        except Exception:
            error = QMessageBox()
            error.setWindowTitle('Внимание!')
            error.setText('Введены некорректные значения')
            error.setMinimumSize(QSize(150, 100))
            error.exec_()
        else:
            if self.left_border.value() != 0 and self.right_border.value() != 0:
                plt.xlim(self.left_border.value(), self.right_border.value())
            if self.color_selection_call:
                plt.plot(x1, x2, color=self.selected_color)
            else:
                plt.plot(x1, x2)
            plt.ylabel(f'{self.polynomial}')
            plt.show()
            self.accept()

    def change_borders(self):
        self.axis_information.setText(f'Границы оси абсцисс: [{self.left_border.value()}; {self.right_border.value()}]')

    def formatting_function(self):
        self.entering_function.setText(self.entering_function.text().replace('^', '**'))
        for i in range(10):
            self.entering_function.setText(self.entering_function.text().replace(f'{i}x', f'{i} * x'))

    def color_selection(self):
        # self.color = QColorDialog.getColor().textvalue()
        color_dialog = QColorDialog()
        self.color = color_dialog.getColor()
        self.selected_color = self.color.name()
        self.color_selection_call = True

    def initUI(self):
        self.color_selection_call = False
        self.setWindowTitle('Построение графиков функций')
        self.setMinimumWidth(300)
        grid = QGridLayout()
        self.setLayout(grid)
        self.entering_function = QLineEdit()
        grid.addWidget(self.entering_function, 0, 0, 1, 2)
        self.entering_function.setPlaceholderText('Введите функцию')
        self.axis_information = QLabel()
        grid.addWidget(self.axis_information, 1, 0, 1, 2)
        self.hint = QLabel()
        self.hint.setWordWrap(True)
        grid.addWidget(self.hint, 3, 0, 1, 2)
        self.left_border = QSlider()
        grid.addWidget(self.left_border, 2, 0)
        self.left_border.setMinimum(-100)
        self.left_border.setMaximum(100)
        self.left_border.setValue(-20)
        self.left_border.setOrientation(Qt.Horizontal)
        self.left_border.valueChanged.connect(self.change_borders)
        self.left_border.setSingleStep(1)
        self.right_border = QSlider()
        grid.addWidget(self.right_border, 2, 1)
        self.right_border.setMinimum(-100)
        self.right_border.setMaximum(100)
        self.right_border.setValue(20)
        self.right_border.setOrientation(Qt.Horizontal)
        self.right_border.valueChanged.connect(self.change_borders)
        self.right_border.setSingleStep(1)
        self.change_borders()
        self.hint.setText('Подсказка: Ввод осуществляется через клавиатуру')
        accept_button = QPushButton('Ок')
        accept_button.clicked.connect(self.accept_button)
        grid.addWidget(accept_button, 4, 0)
        reject_button = QPushButton('Отмена')
        reject_button.clicked.connect(self.reject)
        grid.addWidget(reject_button, 4, 1)
        choice_color = QPushButton('Выбор цвета графика')
        choice_color.clicked.connect(self.color_selection)
        grid.addWidget(choice_color, 5, 0, 1, 2)

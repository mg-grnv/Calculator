import sys
import typing

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QMainWindow, QApplication, QLineEdit, QPushButton, QMessageBox, \
    QSizePolicy
from math import sqrt

from PyQt5.uic.properties import QtGui


class CalculatorWindow(QMainWindow):
    def text(self, key=None):
        # sender() - функция, которая возвращает объект, который вызвал текущую функцию
        if not key:
            key = self.sender().text()
        if self.need_change_number:
            if key != '.':
                a = key
            else:
                a = '0.'
        else:
            if key == '.':
                if '.' not in self.pole.text() and len(self.pole.text()) != 0:
                    a = self.pole.text() + key
                elif '.' in self.pole.text():
                    a = self.pole.text()
                else:
                    a = '0.'
            else:
                a = self.pole.text() + key
        self.pole.setText(self.del_lead_zero(a))
        self.need_change_number = False
        self.equals_repeat = False

    def del_lead_zero(self, text):
        while text.startswith('00'):
            text = text[1:]
        if len(text) > 1 and text[0] == '0' and text[1] in '123456789':
            text = text[1:]
        return text

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def arif_button_func(self):
        if '.' in self.pole.text():
            self.pole.setText((self.pole.text()).rstrip('0'))
        if self.pole.text().endswith('.'):
            self.pole.setText(self.pole.text()[:-1])
        self.number1 = float(self.pole.text())
        self.current_arif_operation = self.sender().text()
        self.need_change_number = True

    def equals_button_func(self):
        self.need_change_number = True
        if self.equals_repeat:
            self.number1 = float(self.pole.text())
        else:
            self.number2 = float(self.pole.text())
        try:
            self.pole.setText(str(eval(f'{self.number1} {self.current_arif_operation} {self.number2}')))
            self.equals_repeat = True
            if '.' in self.pole.text():
                self.pole.setText((self.pole.text()).rstrip('0'))
                self.pole.setText((self.pole.text()).rstrip('.'))
        except ZeroDivisionError:
            error = QMessageBox()
            error.setWindowTitle('Предупреждение')
            error.setText('Предпринята попытка деления на 0')
            error.exec_()

    def sqrt_button_func(self):
        self.number = float(self.pole.text())
        try:
            self.pole.setText(str(eval(f'{sqrt(self.number)}')))
            if '.' in self.pole.text():
                self.pole.setText((self.pole.text()).rstrip('0'))
                self.pole.setText(self.pole.text()[:-1])
            self.need_change_number = True
        except Exception as e:
            error = QMessageBox()
            error.setWindowTitle('Предупреждение')
            error.setText(f'Предпринята попытка извлечения корня из числа, меньшего нуля, {e}')
            error.exec_()

    def sigh_change(self):
        self.number = float(self.pole.text())
        if self.number != 0:
            self.pole.setText(str(self.number * (-1)))
        if '.' in self.pole.text():
            self.pole.setText((self.pole.text()).rstrip('0'))
        if self.pole.text().endswith('.'):
            self.pole.setText(self.pole.text()[:-1])

    def cancel(self):
        self.pole.setText('0')
        self.equals_repeat = False

    def persent(self):
        self.number2 = float(self.pole.text())
        persent_number = (self.number1 / 100) * self.number2
        try:
            if self.current_arif_operation == '+' or self.current_arif_operation == '-':
                self.pole.setText(str(eval(f'{self.number1} {self.current_arif_operation} {persent_number}')))
                self.need_change_number = True
            elif self.current_arif_operation == '*':
                self.pole.setText(str(persent_number))
            elif self.current_arif_operation == '/':
                self.pole.setText(str(self.number1 / self.number2 * 100))
            if '.' in self.pole.text():
                self.pole.setText((self.pole.text()).rstrip('0'))
            if self.pole.text().endswith('.'):
                self.pole.setText(self.pole.text()[:-1])
        except ZeroDivisionError:
            error = QMessageBox()
            error.setWindowTitle('Предупреждение')
            error.setText('Предпринята попытка деления на 0')
            error.exec_()

    def backspace(self):
        if self.equals_repeat == False:
            self.pole.setText(str(self.pole.text()[:-1]))

    def fractional_characters(self):
        number_pole = self.pole.text()
        if '.' in number_pole:
            cnt = len(number_pole.split('.')[1])
            if self.sender().text() == '+0':
                cnt += 1
                self.pole.setText(f'{float(number_pole): .{cnt}f}')
            elif self.sender().text() == '-0':
                cnt -= 1
                self.pole.setText(f'{float(number_pole): .{cnt}f}')
        else:
            if self.sender().text() == '+0':
                self.pole.setText(f'{float(number_pole)}')

    def keyPressEvent(self, a0):
        keys_list = (Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9)
        if a0.key() in keys_list:
            self.text(str(keys_list.index(a0.key())))

    def initUI(self):  # Пользовательский интерфейс
        self.need_change_number = False
        self.equals_repeat = False
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid = QGridLayout()
        central_widget.setLayout(grid)
        self.pole = QLineEdit('0')
        self.pole.setEnabled(False)
        grid.addWidget(self.pole, 0, 0, 1, 6)
        line = 1
        column = 0
        for i in range(1, 10):
            button = QPushButton(f'{i}')
            button.clicked.connect(self.text)
            grid.addWidget(button, line, column)
            column += 1
            if column % 3 == 0:
                line += 1
                column = 0
                continue
        button = QPushButton('0')
        button.clicked.connect(self.text)
        grid.addWidget(button, 4, 0)
        button = QPushButton('=')
        button.clicked.connect(self.equals_button_func)
        grid.addWidget(button, 4, 2)
        line = 1
        column = 3
        arif_operation = ('/', '*', '-', '+')
        for i in range(4):
            button = QPushButton(f'{arif_operation[i]}')
            button.clicked.connect(self.arif_button_func)
            grid.addWidget(button, line, column)
            line += 1
        button = QPushButton('√')
        button.clicked.connect(self.sqrt_button_func)
        grid.addWidget(button, 3, 4)
        button = QPushButton('±')
        button.clicked.connect(self.sigh_change)
        grid.addWidget(button, 2, 4)
        button = QPushButton('.')
        button.clicked.connect(self.text)
        grid.addWidget(button, 4, 1)
        button = QPushButton('//')
        button.clicked.connect(self.arif_button_func)
        grid.addWidget(button, 1, 4)
        button = QPushButton('AC')
        button.clicked.connect(self.cancel)
        grid.addWidget(button, 4, 4)
        button = QPushButton('%')
        button.clicked.connect(self.persent)
        grid.addWidget(button, 1, 5)
        button = QPushButton('←BS')
        button.clicked.connect(self.backspace)
        grid.addWidget(button, 2, 5)
        button = QPushButton('+0')
        button.clicked.connect(self.fractional_characters)
        grid.addWidget(button, 3, 5)
        button = QPushButton('-0')
        button.clicked.connect(self.fractional_characters)
        grid.addWidget(button, 4, 5)

        for item in central_widget.findChildren(QPushButton):
            item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        grid.setSpacing(10)
        self.setStyleSheet(open("style.qss", "r").read())
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('Calculator.svg'))
        self.setMinimumWidth(400)
        self.setMinimumHeight(600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    sys.exit(app.exec_())

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLineEdit


class Charting(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Построение графиков функций')
        self.setMinimumWidth(300)
        grid = QGridLayout()
        self.setLayout(grid)
        self.entering_function = QLineEdit()
        self.entering_function.setEnabled(False)
        grid.addWidget(self.entering_function, 0, 0, 1, 2)
        accept_button = QPushButton('Ок')
        accept_button.clicked.connect(self.accept)
        grid.addWidget(accept_button, 2, 0)
        reject_button = QPushButton('Отмена')
        reject_button.clicked.connect(self.reject)
        grid.addWidget(reject_button, 2, 1)
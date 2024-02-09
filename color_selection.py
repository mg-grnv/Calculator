from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout, QComboBox, QLabel


class ColorSelection(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Выбор цвета')
        self.setMinimumWidth(300)
        grid = QGridLayout()
        self.setLayout(grid)
        list_towns = [
            'Замок',
            'Оплот',
            'Башня',
            'Инферно',
            'Некрополис',
            'Темница',
            'Крепость',
            'Цитадель',
            'Причал',
            'Сопряжение',
            'Фабрика'
        ]
        self.color_selection_combo_box = QComboBox()
        self.color_selection_combo_box.addItems(list_towns)
        grid.addWidget(self.color_selection_combo_box, 0, 0, 1, 2)
        self.picture = QLabel()
        grid.addWidget(self.picture, 1, 0, 1, 2)
        pixmap = QPixmap('Themes/Heroes_3_Tower.jpg')
        pixmap = pixmap.scaled(self.color_selection_combo_box.width(), self.color_selection_combo_box.width(), Qt.KeepAspectRatio)
        self.picture.setPixmap(pixmap)
        accept_button = QPushButton('Ок')
        accept_button.clicked.connect(self.accept)
        grid.addWidget(accept_button, 2, 0)
        reject_button = QPushButton('Отмена')
        reject_button.clicked.connect(self.reject)
        grid.addWidget(reject_button, 2, 1)

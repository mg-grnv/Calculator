from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout, QComboBox, QLabel


class ColorSelection(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def change_image(self):
        current_theme = self.color_selection_combo_box.currentText()
        current_image = self.dict_towns[current_theme] + '.jpg'
        pixmap = QPixmap(f'Themes/{current_image}')
        pixmap = pixmap.scaled(self.color_selection_combo_box.width(), self.color_selection_combo_box.width(), Qt.KeepAspectRatio)
        self.picture.setPixmap(pixmap)

    def initUI(self):
        self.setWindowTitle('Выбор цвета')
        self.setMinimumWidth(300)
        grid = QGridLayout()
        self.setLayout(grid)
        self.dict_towns = {
            'Замок': 'Heroes_3_Castle',
            'Оплот': 'Heroes_3_Rampart',
            'Башня': 'Heroes_3_Tower',
            'Инферно': 'Heroes_3_Inferno',
            'Некрополис': 'Heroes_3_Necropolis',
            'Темница': 'Heroes_3_Dungeon',
            'Крепость': 'Heroes_3_Fortress',
            'Цитадель': 'Heroes_3_Stronghold',
            'Причал': 'Heroes_3_Cove',
            'Сопряжение': 'Heroes_3_Conflux',
            'Фабрика': 'Heroes_3_Factory'
        }
        self.color_selection_combo_box = QComboBox()
        self.color_selection_combo_box.addItems(list(self.dict_towns.keys()))
        self.color_selection_combo_box.currentIndexChanged.connect(self.change_image)
        grid.addWidget(self.color_selection_combo_box, 0, 0, 1, 2)
        self.picture = QLabel()
        self.change_image()
        grid.addWidget(self.picture, 1, 0, 1, 2)
        accept_button = QPushButton('Ок')
        accept_button.clicked.connect(self.accept)
        grid.addWidget(accept_button, 2, 0)
        reject_button = QPushButton('Отмена')
        reject_button.clicked.connect(self.reject)
        grid.addWidget(reject_button, 2, 1)

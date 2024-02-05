from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout


class ColorSelection(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Выбор цвета')
        self.setMinimumWidth(300)

        grid = QGridLayout()
        self.setLayout(grid)
        accept_button = QPushButton('Ок')
        accept_button.clicked.connect(self.accept)
        grid.addWidget(accept_button, 1, 1)
        reject_button = QPushButton('Отмена')
        reject_button.clicked.connect(self.reject)
        grid.addWidget(reject_button, 1, 2)

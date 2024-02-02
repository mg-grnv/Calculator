from PyQt5.QtWidgets import QDialog


class ColorSelection(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Выбор цвета')
        self.setMinimumWidth(300)

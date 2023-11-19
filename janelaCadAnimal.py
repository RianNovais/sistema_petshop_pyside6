from qtDesignFiles.janela_cadAnimal import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class AnimalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)


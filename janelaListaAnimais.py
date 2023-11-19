from qtDesignFiles.janela_ListarAnimais import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class ListAnimalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)


from qtDesignFiles.janela_listaClientes import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class ListClienteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)


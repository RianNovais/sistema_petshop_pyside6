from qtDesignFiles.janela_cadCliente import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

class ClienteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Cadastro de Clientes')


from qtDesignFiles.janela_principal import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

#Janela principal, que servirá de hub para as funcionalidades do programa.
#ela é exibida, quando o usuario tem sucesso na aba de login.

class PrincipalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)





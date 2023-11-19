from qtDesignFiles.janela_cadAnimal import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from janelaPrincipal import PrincipalWindow

class AnimalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.principalWindow = PrincipalWindow()
        self.btnVoltar.clicked.connect(self.voltarPaginaInicial)

    def voltarPaginaInicial(self):
        self.close()
        self.principalWindow.show()


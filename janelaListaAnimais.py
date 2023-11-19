from qtDesignFiles.janela_ListarAnimais import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from janelaPrincipal import PrincipalWindow
class ListAnimalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.principalWindow = PrincipalWindow()

        self.btnVoltar.clicked.connect(self.VoltarPaginaInicial)

    def VoltarPaginaInicial(self):
        self.close()
        self.principalWindow.show()



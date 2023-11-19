from qtDesignFiles.janela_principal import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from janelaCadCliente import ClienteWindow
from janelaListaClientes import ListClienteWindow
from janelaCadAnimal import AnimalWindow
from janelaListaAnimais import ListAnimalWindow


#Janela principal, que servirá de hub para as funcionalidades do programa.
#ela é exibida, quando o usuario tem sucesso na aba de login.

class PrincipalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        #instanciando as telas que poderão ser abertas a partir dessa janela principal
        self.janelaCadCliente = ClienteWindow()
        self.janelaListCliente = ListClienteWindow()
        self.janelaCadAnimal = AnimalWindow()
        self.janelaListAnimal = ListAnimalWindow()

        #estabelecendo a conexão entre o signal de click em cada botão, com o devido slot, cada um desses slots
        #tem a função de fechar a janela atual e abrir uma nova janela, respectivamente
        self.btnCadCliente.clicked.connect(self.exibirJanelaCadCliente)
        self.btnListarClientes.clicked.connect(self.exibirJanelaListClientes)
        self.btnCadAnimais.clicked.connect(self.exibirJanelaCadAnimal)
        self.btnListarAnimais.clicked.connect(self.exibirJanelaListAnimal)

    @Slot()
    def exibirJanelaCadCliente(self):
        self.close()
        self.janelaCadCliente.show()
    @Slot()
    def exibirJanelaListClientes(self):
        self.close()
        self.janelaListCliente.show()
    @Slot()
    def exibirJanelaCadAnimal(self):
        self.close()
        self.janelaCadAnimal.show()
    @Slot()
    def exibirJanelaListAnimal(self):
        self.close()
        self.janelaListAnimal.show()














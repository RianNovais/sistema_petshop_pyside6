from qtDesignFiles.janela_principal import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot


#Janela principal, que servirá de hub para as funcionalidades do programa.
#ela é exibida, quando o usuario tem sucesso na aba de login.

class PrincipalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent #janela pai, que é passada na instanciação, (janela login)
        #instanciando as telas que poderão ser abertas a partir dessa janela principal, elas iniciam como None

        self.janelaCadCliente = None
        self.janelaListCliente = None
        self.janelaCadAnimal = None
        self.janelaListAnimal = None


        #estabelecendo a conexão entre o signal de click em cada botão, com o devido slot, cada um desses slots
        #tem a função de fechar a janela atual e abrir uma nova janela, respectivamente
        self.btnCadCliente.clicked.connect(self.exibirJanelaCadCliente)
        self.btnListarClientes.clicked.connect(self.exibirJanelaListClientes)
        self.btnCadAnimais.clicked.connect(self.exibirJanelaCadAnimal)
        self.btnListarAnimais.clicked.connect(self.exibirJanelaListAnimal)

    #aqui a função verifica se o atributo é None, como já vem por padrão, se for ele importa a classe da janela respectiva
    #e adiciona ao atributo a classe instanciada, depois ocorre normalmente, fechando a janela principal e mostrando a
    #respectiva de cada botão
    @Slot()
    def exibirJanelaCadCliente(self):
        if not self.janelaCadCliente:
            #importações no meio do código, para evitar importação circular
            from janelaCadCliente import ClienteWindow
            self.janelaCadCliente = ClienteWindow(self)
        self.close()
        self.janelaCadCliente.show()
    @Slot()
    def exibirJanelaListClientes(self):
        if not self.janelaListCliente:
            from janelaListaClientes import ListClienteWindow
            self.janelaListCliente = ListClienteWindow(self)
        self.close()
        self.janelaListCliente.show()
    @Slot()
    def exibirJanelaCadAnimal(self):
        if not self.janelaCadAnimal:
            from janelaCadAnimal import AnimalWindow
            self.janelaCadAnimal = AnimalWindow(self)
        self.close()
        self.janelaCadAnimal.show()
    @Slot()
    def exibirJanelaListAnimal(self):
        if not self.janelaListAnimal:
            from janelaListaAnimais import ListAnimalWindow
            self.janelaListAnimal = ListAnimalWindow(self)

        self.close()
        self.janelaListAnimal.show()














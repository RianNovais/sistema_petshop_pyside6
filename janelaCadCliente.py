from qtDesignFiles.janela_cadCliente import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from janelaPrincipal import PrincipalWindow

from cliente import Cliente


class ClienteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Cadastro de Clientes')
        self.principalWindow = PrincipalWindow()

        self.listaCidades = ['Teste1','Teste2']
        self.cbCidade.addItems(self.listaCidades)

        self.btnVoltar.clicked.connect(self.voltarPaginaPrincipal)
        self.btnCadCliente.clicked.connect(self.cadastrarCliente)
    def voltarPaginaPrincipal(self):
        self.close()
        self.principalWindow.show()

    def cadastrarCliente(self):
        c = Cliente
        self.inputNome.text()
        self.inputSobrenome.text()
        self.inputCpf.text()
        self.inputEstado.text()
        self.cbCidade.currentText()
        self.inputEndereco.text()


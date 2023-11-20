from qtDesignFiles.janela_cadCliente import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from janelaPrincipal import PrincipalWindow

from cliente import Cliente

class ClienteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Cadastro de Clientes')
        self.parent = parent #essa parent é a janela pai, que no caso é a nossa janela principal

        self.listaCidades = ['Teste1','Teste2']
        self.cbCidade.addItems(self.listaCidades)

        self.btnVoltar.clicked.connect(self.voltarPaginaPrincipal)
        self.btnCadCliente.clicked.connect(self.cadastrarCliente)
    def voltarPaginaPrincipal(self):
        self.close()
        self.parent.show()

    def cadastrarCliente(self):
        nome = self.inputNome.text()
        sobrenome = self.inputSobrenome.text()
        cpf = self.inputCpf.text()
        estado = self.inputEstado.text()
        cidade = self.cbCidade.currentText()
        endereco = self.inputEndereco.text()
        c = Cliente(nome, sobrenome, cpf, estado, cidade, endereco)
        self.parent.listaClientes.append(c)
        print(self.parent.listaClientes)
        print('Cliente adicionado com sucesso')


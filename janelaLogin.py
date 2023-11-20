from qtDesignFiles.janela_login import Ui_Dialog #importa do arquivo .py que veio do arquivo .UI gerado pelo QTDesigner
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox
from utils import IsEmpty #importando a função isEmpty, que veio do modulo utils, onde existem funções, recorrentes no codigo.
from janelaPrincipal import PrincipalWindow #importando a janela principal

#classe da janela de Login, que herda do objeto QDialog, e também do UiDialog, gerado pelo QTDesigner
class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        #Estilizações
        self.setWindowTitle('Login')


        #aqui instanciamos uma janela principal como atributo da janela de login, ela só sera exibida
        #se o usuário conseguir logar
        self.janelaPrincipal = PrincipalWindow(self)

        #conectando o botão a função de verificar os campos do login, que verificará se os campos estão vazios
        #e se os campos de senha e login estão corretos
        self.btnLogin.clicked.connect(self.verificar_campos_login)

    #função que exibe uma mensagem na tela, quando o usuario digita login ou senha errados
    #ela também limpa os campos, para o usuário digitar denovo
    def mostrarMsgBoxErrorLogin(self):
        self.inputLogin.setText("")
        self.inputSenha.setText("")
        self.labelErroLogin.setText("")
        self.labelErroSenha.setText("")

        msgBox = QMessageBox(self)
        msgBox.setText('Senha ou login inválidos')
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.exec()

    #verifica se os campos de usuario e senha que o usuario digitou estão corretos
    def verificar_login_senha(self):
        self.labelErroLogin.setText("")
        self.labelErroSenha.setText("")
        return self.inputLogin.text() == "admin" and self.inputSenha.text() == "12345"

    #aqui é verificado os campos, verifica se algum dos campos estão vazios, chamando a função respectiva, escreve
    #uma mensagem de erro na tela, mandando preencher os campos vazios, caso não esteja vazio. verifica se o login
    #e a senha estão corretos, caso esteja, fecha a janela de login e starta a janela principal, caso esteja errados
    #exibe a msgBox de erro na tela com a função respectiva
    @Slot()
    def verificar_campos_login(self):
        if IsEmpty(self.inputLogin.text()):
            self.labelErroLogin.setText('preencha o campo de login')
        if IsEmpty(self.inputSenha.text()):
            self.labelErroSenha.setText('preencha o campo de senha')

        else:
            if self.verificar_login_senha():
                self.close()
                self.janelaPrincipal.show()
            else:
                self.mostrarMsgBoxErrorLogin()




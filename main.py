#Sistema de um petshop, onde o usuario(admin) pode entrar no sistema, cadastrar clientes, animais, serviços
#e listar-los
from PySide6.QtWidgets import QApplication
from janelaLogin import LoginDialog
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginDialog = LoginDialog()
    loginDialog.exec()
    app.exec()
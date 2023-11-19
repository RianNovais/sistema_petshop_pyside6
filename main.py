#Sistema de um petshop, onde o usuario(admin) pode entrar no sistema, cadastrar clientes, animais, serviços
#e listar-los


from PySide6.QtWidgets import QApplication
from loginDialog import LoginDialog

if __name__ == "__main__":
    app = QApplication()
    loginDialog = LoginDialog()
    loginDialog.exec()
    app.exec()
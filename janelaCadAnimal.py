from qtDesignFiles.janela_cadAnimal import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from janelaPrincipal import PrincipalWindow

from animal import Animal


class AnimalWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.cbTutor.addItem('Rian')
        self.cbTipo.addItems(['Canideo', 'Felino'])
        self.btnVoltar.clicked.connect(self.voltarPaginaInicial)
        self.btnCadAnimal.clicked.connect(self.cadastrarAnimal)

    def voltarPaginaInicial(self):
        self.close()
        self.parent.show()

    def cadastrarAnimal(self):
        nome = self.inputNome.text()
        tipo = self.cbTipo.currentText()
        raça = self.inputRaca.text()
        idade = self.inputIdade.text()
        tutor = self.cbTutor.currentText()
        a = Animal(nome, tipo, raça, idade, tutor)
        self.parent.listaAnimais.append(a)




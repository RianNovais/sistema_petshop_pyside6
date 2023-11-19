# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_cadCliente.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import assets.resources_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 497)
        MainWindow.setMinimumSize(QSize(700, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frameCadCliente = QFrame(self.centralwidget)
        self.frameCadCliente.setObjectName(u"frameCadCliente")
        self.frameCadCliente.setStyleSheet(u"background-color:rgb(D3D3D3);")
        self.frameCadCliente.setFrameShape(QFrame.StyledPanel)
        self.frameCadCliente.setFrameShadow(QFrame.Raised)
        self.tituloCadCliente = QLabel(self.frameCadCliente)
        self.tituloCadCliente.setObjectName(u"tituloCadCliente")
        self.tituloCadCliente.setGeometry(QRect(250, 30, 305, 36))
        font = QFont()
        font.setPointSize(20)
        self.tituloCadCliente.setFont(font)
        self.frameFormCad1 = QFrame(self.frameCadCliente)
        self.frameFormCad1.setObjectName(u"frameFormCad1")
        self.frameFormCad1.setGeometry(QRect(30, 90, 381, 171))
        font1 = QFont()
        font1.setPointSize(14)
        self.frameFormCad1.setFont(font1)
        self.frameFormCad1.setFrameShape(QFrame.StyledPanel)
        self.frameFormCad1.setFrameShadow(QFrame.Raised)
        self.labelNome = QLabel(self.frameFormCad1)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(10, 10, 361, 23))
        self.labelNome.setFont(font1)
        self.labelSobrenome = QLabel(self.frameFormCad1)
        self.labelSobrenome.setObjectName(u"labelSobrenome")
        self.labelSobrenome.setGeometry(QRect(10, 63, 361, 22))
        self.labelSobrenome.setFont(font1)
        self.inputNome = QLineEdit(self.frameFormCad1)
        self.inputNome.setObjectName(u"inputNome")
        self.inputNome.setGeometry(QRect(10, 39, 341, 21))
        font2 = QFont()
        font2.setPointSize(12)
        self.inputNome.setFont(font2)
        self.inputNome.setStyleSheet(u"border-radius:4px;")
        self.labelCpf = QLabel(self.frameFormCad1)
        self.labelCpf.setObjectName(u"labelCpf")
        self.labelCpf.setGeometry(QRect(10, 115, 361, 22))
        self.labelCpf.setFont(font1)
        self.inputSobrenome = QLineEdit(self.frameFormCad1)
        self.inputSobrenome.setObjectName(u"inputSobrenome")
        self.inputSobrenome.setGeometry(QRect(10, 91, 331, 21))
        self.inputSobrenome.setFont(font2)
        self.inputSobrenome.setStyleSheet(u"border-radius:4px;")
        self.inputCpf = QLineEdit(self.frameFormCad1)
        self.inputCpf.setObjectName(u"inputCpf")
        self.inputCpf.setGeometry(QRect(10, 143, 231, 21))
        self.inputCpf.setFont(font2)
        self.inputCpf.setStyleSheet(u"border-radius:4px;")
        self.frameFormCad2 = QFrame(self.frameCadCliente)
        self.frameFormCad2.setObjectName(u"frameFormCad2")
        self.frameFormCad2.setGeometry(QRect(30, 260, 441, 101))
        self.frameFormCad2.setFont(font1)
        self.frameFormCad2.setFrameShape(QFrame.StyledPanel)
        self.frameFormCad2.setFrameShadow(QFrame.Raised)
        self.labelCidade = QLabel(self.frameFormCad2)
        self.labelCidade.setObjectName(u"labelCidade")
        self.labelCidade.setGeometry(QRect(184, 10, 71, 26))
        self.labelCidade.setFont(font1)
        self.inputEstado = QLineEdit(self.frameFormCad2)
        self.inputEstado.setObjectName(u"inputEstado")
        self.inputEstado.setGeometry(QRect(77, 14, 101, 21))
        self.inputEstado.setFont(font2)
        self.inputEstado.setStyleSheet(u"border-radius:4px\n"
"")
        self.labelEstado = QLabel(self.frameFormCad2)
        self.labelEstado.setObjectName(u"labelEstado")
        self.labelEstado.setGeometry(QRect(10, 10, 61, 26))
        self.labelEstado.setFont(font1)
        self.cbCidade = QComboBox(self.frameFormCad2)
        self.cbCidade.setObjectName(u"cbCidade")
        self.cbCidade.setGeometry(QRect(259, 14, 171, 20))
        self.cbCidade.setFont(font2)
        self.cbCidade.setStyleSheet(u"border-radius:4px;\n"
"")
        self.inputEndereco = QLineEdit(self.frameFormCad2)
        self.inputEndereco.setObjectName(u"inputEndereco")
        self.inputEndereco.setGeometry(QRect(105, 50, 261, 21))
        self.inputEndereco.setFont(font2)
        self.inputEndereco.setStyleSheet(u"border-radius:4px\n"
"")
        self.labelEndereco = QLabel(self.frameFormCad2)
        self.labelEndereco.setObjectName(u"labelEndereco")
        self.labelEndereco.setGeometry(QRect(8, 46, 91, 26))
        self.labelEndereco.setFont(font1)
        self.btnCadCliente = QPushButton(self.frameCadCliente)
        self.btnCadCliente.setObjectName(u"btnCadCliente")
        self.btnCadCliente.setGeometry(QRect(610, 410, 151, 51))
        self.btnVoltar = QPushButton(self.frameCadCliente)
        self.btnVoltar.setObjectName(u"btnVoltar")
        self.btnVoltar.setGeometry(QRect(450, 410, 141, 51))
        self.labelImgCliente = QLabel(self.frameCadCliente)
        self.labelImgCliente.setObjectName(u"labelImgCliente")
        self.labelImgCliente.setGeometry(QRect(410, 80, 191, 171))
        self.labelImgCliente.setMinimumSize(QSize(100, 0))
        self.labelImgCliente.setStyleSheet(u"image: url(:/assets/userIcon2.png);")

        self.verticalLayout_2.addWidget(self.frameCadCliente)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.inputNome, self.inputSobrenome)
        QWidget.setTabOrder(self.inputSobrenome, self.inputCpf)
        QWidget.setTabOrder(self.inputCpf, self.inputEstado)
        QWidget.setTabOrder(self.inputEstado, self.cbCidade)
        QWidget.setTabOrder(self.cbCidade, self.inputEndereco)
        QWidget.setTabOrder(self.inputEndereco, self.btnVoltar)
        QWidget.setTabOrder(self.btnVoltar, self.btnCadCliente)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tituloCadCliente.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE CLIENTES", None))
        self.labelNome.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.labelSobrenome.setText(QCoreApplication.translate("MainWindow", u"Sobrenome:", None))
        self.labelCpf.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.inputCpf.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.labelCidade.setText(QCoreApplication.translate("MainWindow", u"Cidade:", None))
        self.labelEstado.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.labelEndereco.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.btnCadCliente.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Novo Usu\u00e1rio", None))
        self.btnVoltar.setText(QCoreApplication.translate("MainWindow", u"Voltar a P\u00e1gina Principal", None))
        self.labelImgCliente.setText("")
    # retranslateUi


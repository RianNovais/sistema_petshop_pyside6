# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import assets.resources_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelTituloJanelaPrincipal = QLabel(self.centralwidget)
        self.labelTituloJanelaPrincipal.setObjectName(u"labelTituloJanelaPrincipal")
        self.labelTituloJanelaPrincipal.setGeometry(QRect(10, 20, 781, 71))
        font = QFont()
        font.setPointSize(30)
        self.labelTituloJanelaPrincipal.setFont(font)
        self.labelTituloJanelaPrincipal.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(610, 100, 121, 31))
        self.btnListarAnimais = QPushButton(self.centralwidget)
        self.btnListarAnimais.setObjectName(u"btnListarAnimais")
        self.btnListarAnimais.setGeometry(QRect(250, 420, 311, 71))
        self.btnListarClientes = QPushButton(self.centralwidget)
        self.btnListarClientes.setObjectName(u"btnListarClientes")
        self.btnListarClientes.setGeometry(QRect(250, 234, 311, 71))
        self.btnCadCliente = QPushButton(self.centralwidget)
        self.btnCadCliente.setObjectName(u"btnCadCliente")
        self.btnCadCliente.setGeometry(QRect(250, 141, 311, 61))
        self.btnCadAnimais = QPushButton(self.centralwidget)
        self.btnCadAnimais.setObjectName(u"btnCadAnimais")
        self.btnCadAnimais.setGeometry(QRect(250, 327, 311, 71))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Petshop", None))
        self.labelTituloJanelaPrincipal.setText(QCoreApplication.translate("MainWindow", u"PETSHOP", None))
        self.label.setText("")
        self.btnListarAnimais.setText(QCoreApplication.translate("MainWindow", u"Listar Animais", None))
        self.btnListarClientes.setText(QCoreApplication.translate("MainWindow", u"Listar Clientes", None))
        self.btnCadCliente.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
        self.btnCadAnimais.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Animais", None))
    # retranslateUi


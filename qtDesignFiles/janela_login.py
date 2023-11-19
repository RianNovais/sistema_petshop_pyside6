# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_qrc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 430)
        Dialog.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetLogin = QWidget(Dialog)
        self.widgetLogin.setObjectName(u"widgetLogin")
        self.widgetLogin.setMinimumSize(QSize(300, 300))
        self.titleLogin = QLabel(self.widgetLogin)
        self.titleLogin.setObjectName(u"titleLogin")
        self.titleLogin.setGeometry(QRect(0, 10, 381, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(21)
        self.titleLogin.setFont(font)
        self.titleLogin.setAlignment(Qt.AlignCenter)
        self.inputLogin = QLineEdit(self.widgetLogin)
        self.inputLogin.setObjectName(u"inputLogin")
        self.inputLogin.setGeometry(QRect(60, 180, 281, 31))
        self.inputLogin.setStyleSheet(u"border-radius:3px;")
        self.inputSenha = QLineEdit(self.widgetLogin)
        self.inputSenha.setObjectName(u"inputSenha")
        self.inputSenha.setGeometry(QRect(60, 240, 281, 31))
        self.inputSenha.setStyleSheet(u"border-radius:3px;")
        self.inputSenha.setEchoMode(QLineEdit.Password)
        self.btnLogin = QPushButton(self.widgetLogin)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(70, 340, 101, 41))
        self.btnLogin.setStyleSheet(u"background-color:rgb(0, 0, 128);\n"
"color:white;\n"
"border-radius:4px;\n"
"\n"
"")
        self.labelLogin = QLabel(self.widgetLogin)
        self.labelLogin.setObjectName(u"labelLogin")
        self.labelLogin.setGeometry(QRect(60, 160, 49, 16))
        self.labelSenha = QLabel(self.widgetLogin)
        self.labelSenha.setObjectName(u"labelSenha")
        self.labelSenha.setGeometry(QRect(60, 220, 49, 16))
        self.labelImagem = QLabel(self.widgetLogin)
        self.labelImagem.setObjectName(u"labelImagem")
        self.labelImagem.setGeometry(QRect(150, 50, 90, 90))
        self.labelImagem.setMinimumSize(QSize(90, 90))
        self.labelImagem.setStyleSheet(u"background-image:url(:/assets/userIcon.png);\n"
"background-repeat:no-repeat;")
        self.btnRegistrar = QPushButton(self.widgetLogin)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setGeometry(QRect(230, 340, 101, 41))
        self.btnRegistrar.setStyleSheet(u"background-color:rgb(0, 0, 128);\n"
"color:white;\n"
"border-radius:4px;\n"
"\n"
"")
        self.labelErroLogin = QLabel(self.widgetLogin)
        self.labelErroLogin.setObjectName(u"labelErroLogin")
        self.labelErroLogin.setGeometry(QRect(60, 280, 181, 16))
        self.labelErroLogin.setStyleSheet(u"color:red;")
        self.labelErroSenha = QLabel(self.widgetLogin)
        self.labelErroSenha.setObjectName(u"labelErroSenha")
        self.labelErroSenha.setGeometry(QRect(60, 300, 191, 16))
        self.labelErroSenha.setStyleSheet(u"color:red;")

        self.verticalLayout.addWidget(self.widgetLogin)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.titleLogin.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.inputLogin.setPlaceholderText(QCoreApplication.translate("Dialog", u"Insira seu login", None))
        self.inputSenha.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite sua senha", None))
        self.btnLogin.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.labelLogin.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.labelSenha.setText(QCoreApplication.translate("Dialog", u"Senha", None))
        self.labelImagem.setText("")
        self.btnRegistrar.setText(QCoreApplication.translate("Dialog", u"Registrar-se", None))
        self.labelErroLogin.setText("")
        self.labelErroSenha.setText("")
    # retranslateUi


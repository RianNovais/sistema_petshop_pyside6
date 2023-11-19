# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_ListarClientes.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableClientes = QTableWidget(self.centralwidget)
        self.tableClientes.setObjectName(u"tableClientes")
        self.tableClientes.setGeometry(QRect(20, 100, 761, 411))
        font = QFont()
        font.setPointSize(13)
        self.tableClientes.setFont(font)
        self.tableClientes.setShowGrid(True)
        self.tableClientes.setGridStyle(Qt.DashDotLine)
        self.tableClientes.setRowCount(0)
        self.tableClientes.setColumnCount(0)
        self.tableClientes.horizontalHeader().setStretchLastSection(False)
        self.labelTituloListarClientes = QLabel(self.centralwidget)
        self.labelTituloListarClientes.setObjectName(u"labelTituloListarClientes")
        self.labelTituloListarClientes.setGeometry(QRect(28, 19, 751, 61))
        self.labelTituloListarClientes.setFont(font)
        self.labelTituloListarClientes.setAlignment(Qt.AlignCenter)
        self.btnVoltar = QPushButton(self.centralwidget)
        self.btnVoltar.setObjectName(u"btnVoltar")
        self.btnVoltar.setGeometry(QRect(620, 530, 151, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTituloListarClientes.setText(QCoreApplication.translate("MainWindow", u"Listagem de Clientes", None))
        self.btnVoltar.setText(QCoreApplication.translate("MainWindow", u"Voltar a P\u00e1gina Inicial", None))
    # retranslateUi


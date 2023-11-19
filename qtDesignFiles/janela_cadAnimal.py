# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_cadAnimal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import assets.resources_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 562)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameCadAnimal = QFrame(self.centralwidget)
        self.frameCadAnimal.setObjectName(u"frameCadAnimal")
        self.frameCadAnimal.setFrameShape(QFrame.StyledPanel)
        self.frameCadAnimal.setFrameShadow(QFrame.Raised)
        self.labelTituloCadAnimal = QLabel(self.frameCadAnimal)
        self.labelTituloCadAnimal.setObjectName(u"labelTituloCadAnimal")
        self.labelTituloCadAnimal.setGeometry(QRect(0, 0, 781, 81))
        font = QFont()
        font.setPointSize(20)
        self.labelTituloCadAnimal.setFont(font)
        self.labelTituloCadAnimal.setAlignment(Qt.AlignCenter)
        self.frameFormCadAnimal1 = QFrame(self.frameCadAnimal)
        self.frameFormCadAnimal1.setObjectName(u"frameFormCadAnimal1")
        self.frameFormCadAnimal1.setGeometry(QRect(40, 100, 361, 171))
        font1 = QFont()
        font1.setPointSize(14)
        self.frameFormCadAnimal1.setFont(font1)
        self.frameFormCadAnimal1.setFrameShape(QFrame.StyledPanel)
        self.frameFormCadAnimal1.setFrameShadow(QFrame.Raised)
        self.labelNome = QLabel(self.frameFormCadAnimal1)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(10, 10, 361, 23))
        self.labelNome.setFont(font1)
        self.labelTipo = QLabel(self.frameFormCadAnimal1)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(10, 63, 361, 22))
        self.labelTipo.setFont(font1)
        self.inputNome = QLineEdit(self.frameFormCadAnimal1)
        self.inputNome.setObjectName(u"inputNome")
        self.inputNome.setGeometry(QRect(10, 39, 341, 21))
        font2 = QFont()
        font2.setPointSize(12)
        self.inputNome.setFont(font2)
        self.inputNome.setStyleSheet(u"border-radius:4px;")
        self.labelRaca = QLabel(self.frameFormCadAnimal1)
        self.labelRaca.setObjectName(u"labelRaca")
        self.labelRaca.setGeometry(QRect(10, 115, 361, 22))
        self.labelRaca.setFont(font1)
        self.inputRaca = QLineEdit(self.frameFormCadAnimal1)
        self.inputRaca.setObjectName(u"inputRaca")
        self.inputRaca.setGeometry(QRect(10, 143, 231, 21))
        self.inputRaca.setFont(font2)
        self.inputRaca.setStyleSheet(u"border-radius:4px;")
        self.cbTipo = QComboBox(self.frameFormCadAnimal1)
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(10, 90, 141, 22))
        self.frameFormCadAnimal2 = QFrame(self.frameCadAnimal)
        self.frameFormCadAnimal2.setObjectName(u"frameFormCadAnimal2")
        self.frameFormCadAnimal2.setGeometry(QRect(40, 270, 441, 101))
        self.frameFormCadAnimal2.setFont(font1)
        self.frameFormCadAnimal2.setFrameShape(QFrame.StyledPanel)
        self.frameFormCadAnimal2.setFrameShadow(QFrame.Raised)
        self.inputIdade = QLineEdit(self.frameFormCadAnimal2)
        self.inputIdade.setObjectName(u"inputIdade")
        self.inputIdade.setGeometry(QRect(77, 14, 51, 21))
        self.inputIdade.setFont(font2)
        self.inputIdade.setStyleSheet(u"border-radius:4px\n"
"")
        self.labelIdade = QLabel(self.frameFormCadAnimal2)
        self.labelIdade.setObjectName(u"labelIdade")
        self.labelIdade.setGeometry(QRect(10, 10, 61, 26))
        self.labelIdade.setFont(font1)
        self.cbTutor = QComboBox(self.frameFormCadAnimal2)
        self.cbTutor.setObjectName(u"cbTutor")
        self.cbTutor.setGeometry(QRect(200, 10, 141, 23))
        self.cbTutor.setFont(font2)
        self.cbTutor.setStyleSheet(u"border-radius:4px;\n"
"")
        self.labelTutor = QLabel(self.frameFormCadAnimal2)
        self.labelTutor.setObjectName(u"labelTutor")
        self.labelTutor.setGeometry(QRect(140, 8, 49, 26))
        self.labelTutor.setFont(font1)
        self.pushButton = QPushButton(self.frameCadAnimal)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(440, 450, 131, 41))
        self.pushButton_2 = QPushButton(self.frameCadAnimal)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(580, 450, 131, 41))
        self.label = QLabel(self.frameCadAnimal)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 110, 151, 131))
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setStyleSheet(u"image: url(:/images/petIcon.png);")

        self.horizontalLayout.addWidget(self.frameCadAnimal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTituloCadAnimal.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Animais", None))
        self.labelNome.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.labelTipo.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.labelRaca.setText(QCoreApplication.translate("MainWindow", u"Ra\u00e7a:", None))
        self.inputRaca.setInputMask("")
        self.labelIdade.setText(QCoreApplication.translate("MainWindow", u"Idade:", None))
        self.labelTutor.setText(QCoreApplication.translate("MainWindow", u"Tutor:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Voltar a Pagina Inicial", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Novo Animal", None))
        self.label.setText("")
    # retranslateUi


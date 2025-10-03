# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_repaso2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(759, 1013)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 711, 20))
        self.label.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 74, 731, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Nombre = QLineEdit(self.verticalLayoutWidget)
        self.Nombre.setObjectName(u"Nombre")

        self.verticalLayout.addWidget(self.Nombre)

        self.boxRol = QComboBox(self.verticalLayoutWidget)
        self.boxRol.setObjectName(u"boxRol")

        self.verticalLayout.addWidget(self.boxRol)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout.addWidget(self.checkBox)

        self.enviar = QPushButton(self.verticalLayoutWidget)
        self.enviar.setObjectName(u"enviar")

        self.verticalLayout.addWidget(self.enviar)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 470, 721, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.Repaso31label = QLabel(self.centralwidget)
        self.Repaso31label.setObjectName(u"Repaso31label")
        self.Repaso31label.setGeometry(QRect(270, 510, 201, 20))
        self.Repaso31label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Repaso31label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.iniciarBoton = QPushButton(self.centralwidget)
        self.iniciarBoton.setObjectName(u"iniciarBoton")
        self.iniciarBoton.setGeometry(QRect(330, 590, 79, 24))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 620, 701, 23))
        self.progressBar.setValue(24)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 680, 721, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.Repaso32_label = QLabel(self.centralwidget)
        self.Repaso32_label.setObjectName(u"Repaso32_label")
        self.Repaso32_label.setGeometry(QRect(260, 710, 201, 20))
        self.Repaso32_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Repaso32_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lista = QListWidget(self.centralwidget)
        self.lista.setObjectName(u"lista")
        self.lista.setGeometry(QRect(250, 750, 256, 192))
        self.lista.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Progreso = QLabel(self.centralwidget)
        self.Progreso.setObjectName(u"Progreso")
        self.Progreso.setGeometry(QRect(350, 560, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 759, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Texto de la etiqueta", None))
        self.Nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduzca su nombre", None))
#if QT_CONFIG(accessibility)
        self.boxRol.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.boxRol.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduzca su rol:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Acepto las normas:", None))
        self.enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar datos", None))
        self.Repaso31label.setText(QCoreApplication.translate("MainWindow", u"REPASO 3.1", None))
        self.iniciarBoton.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.Repaso32_label.setText(QCoreApplication.translate("MainWindow", u"REPASO 3.2", None))
        self.Progreso.setText(QCoreApplication.translate("MainWindow", u"Progreso", None))
    # retranslateUi


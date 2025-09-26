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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(729, 530)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 711, 20))
        self.label.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 241, 661, 24))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Nombre = QLineEdit(self.verticalLayoutWidget)
        self.Nombre.setObjectName(u"Nombre")

        self.verticalLayout.addWidget(self.Nombre)

        self.boxRol = QComboBox(self.centralwidget)
        self.boxRol.setObjectName(u"boxRol")
        self.boxRol.setGeometry(QRect(512, 290, 141, 24))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(230, 430, 131, 20))
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.enviar = QPushButton(self.centralwidget)
        self.enviar.setObjectName(u"enviar")
        self.enviar.setGeometry(QRect(510, 430, 101, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 729, 33))
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
#endif // QT_CONFIG(accessibility)
        self.boxRol.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduzca su rol:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Acepto las normas:", None))
        self.enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar datos", None))
    # retranslateUi


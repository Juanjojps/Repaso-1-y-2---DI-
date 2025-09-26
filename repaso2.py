import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QCheckBox, QWidget, QPushButton, QVBoxLayout, QLineEdit, QMenuBar, QStatusBar
from ui_repaso2 import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        self.setupUi(self)

        print("Iniciado")


        self.boxRol.addItems(["Invitado", "Profe", "Alumno"])
        self.boxRol.setCurrentText("Introduzca su rol:")

        self.enviar.clicked.connect(self.on_aceptar)

    def on_comprobar(self):
        if self.Nombre.text() == "" or not self.checkBox.isChecked():
            print("Faltan datos")
            return False
        return True

    def on_aceptar(self):
        if self.on_comprobar():
            print("Datos correctos")
            print()
            self.checkBox.setChecked(False)
            self.boxRol.setCurrentIndex(-1)
            self.Nombre.setText("")
        else:
            print("Complete los datos")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    app.exec()
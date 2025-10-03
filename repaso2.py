import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QCheckBox, QWidget, QPushButton, QVBoxLayout, QLineEdit, QMenuBar, QStatusBar, QListWidget, QProgressBar
from ui_repaso2 import Ui_MainWindow
from PySide6.QtCore import QTimer

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        self.setupUi(self)

        print("Iniciado")

        #añadir items al comboBox y su texto principal
        self.boxRol.addItems(["Invitado", "Profe", "Alumno"])
        self.boxRol.setCurrentText("Introduzca su rol:")

        #accion enviar (limpia todos los campos)
        self.enviar.clicked.connect(self.on_aceptar)

        #temporizador
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self._tick)

        self.iniciarBoton.clicked.connect(self.iniciar)

        #barra
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)

        #lista
        self.lista.addItems(["Tarea 1", "Tarea 2", "Tarea 3"])
        self.lista.itemDoubleClicked.connect(self.on_seleccionado)

    def on_seleccionado(self, item):
        print("Has seleccionado: "+item.text())



    def _tick(self):
        valor = self.progressBar.value() + 1
        self.progressBar.setValue(valor)

        if valor >= self.progressBar.maximum():
            self.timer.stop()

    def iniciar(self):
        self.timer.start()


    #funcion que comprueba datos
    def on_comprobar(self):
        if self.Nombre.text() == "" or not self.checkBox.isChecked():
            print("Faltan datos")
            return False
        return True

    #funcion que al aceptar, si está correcto limpia los campos y si no, imprime datos incorrectos en consola
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
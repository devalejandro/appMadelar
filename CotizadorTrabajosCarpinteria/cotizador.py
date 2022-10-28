from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("CotizadorTrabajosCarpinteria/cotizador.ui", self)


aplicacion = QApplication([])
ventana = Vista()
ventana.show()
aplicacion.exec_()
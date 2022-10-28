from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic

class Vista(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("CotizadorTrabajosCarpinteria/cotizador.ui", self)
        self.btnAgregar.clicked.connect(self.agregar_item)
        self.btnEditar.clicked.connect(self.editar_item)
        self.btnEliminar.clicked.connect(self.eliminar_item)
        self.rbCepillado.toggled.connect(self.agregar_item)
        self.rbFlete.toggled.connect(self.agregar_item)

    def agregar_item(self):
        pass

    def editar_item(self):
        pass

    def eliminar_item(self):
        pass


aplicacion = QApplication([])
ventana = Vista()
ventana.show()
aplicacion.exec_()
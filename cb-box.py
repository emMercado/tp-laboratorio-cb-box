#A partir de la siguiente interfaz de usuario, implementar en Python lo siguiente:

#Agregar un elemento a la lista (ComboBox) empleando un diálogo de entrada. 
#Editar un elemento de la lista empleando un diálogo de entrada.
#Quitar un elemento de la lista consultando primero al usuario mediante un cuadro de msg.
#Quitar todos los elementos de la lista consultando primero al usuario mediante un cuadro de msg.
#Mostrar en una etiqueta el elemento de la lista actualmente elegido
#Subir tanto el archivo de Qt Designer como el de Python

from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cb-box.ui", self)
        self.agregar.clicked.connect(self.onCreate)
        self.editar.clicked.connect(self.onUpdate)
        self.quitar.clicked.connect(self.onDelete)
        self.quitarTodos.clicked.connect(self.onDeleteAllItem)

    def onCreate(self):
        msg = QMessageBox()
        nuevo_texto, ok = QInputDialog.getText(self, 'ingresar', 'Ingrese nuevo item', text='item')
        if ok and nuevo_texto:
            self.cbBox.addItem(nuevo_texto)
            msg.setWindowTitle('Creado')
            msg.setTextFormat("Item creado con exito")
            msg.setStandardButtons(QMessageBox.Yes)

    def onUpdate(self):
        nuevo_texto, ok = QInputDialog.getText(self, 'Editar', 'Ingrese nuevo nombre', text='Texto a editar')
        if ok and nuevo_texto:
            lista = self.cbBox.currentIndex()
            self.cbBox.setItemText(lista, nuevo_texto)

    def onDelete(self):
        msg = QMessageBox()
        msg.setWindowTitle('Eliminar')
        msg.setText('Esta seguro de querer eliminar este Item?')
        item = self.cbBox.currentText()
        #msg.setText(item)
        msg.setInformativeText(item)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resultado = msg.exec()
        if resultado == QMessageBox.Yes:
            lista = self.cbBox.currentIndex()
            self.cbBox.removeItem(lista)
        elif resultado == QMessageBox.No:
            self.cbBox.currentIndex()

    def onDeleteAllItem(self):
        msg = QMessageBox()
        msg.setWindowTitle('Eliminar')
        msg.setText('¿Eliminar todos los items?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resultado = msg.exec()
        if resultado == QMessageBox.Yes:
            self.cbBox.clear()
        elif resultado == QMessageBox.No:
            self.cbBox.currentIndex()

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
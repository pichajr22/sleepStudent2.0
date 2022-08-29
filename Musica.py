import sys
from pygame import mixer
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QPixmap
app = QApplication([])
mixer.init()
labelMusica = QLabel('')

class SeleccionArchivoVentana(QMainWindow):

    def seleccionar_archivo(self):
        archivo, ok = QFileDialog.getOpenFileName(self, 'Seleccionar archivo de imagen...', 'C:\\', '*')
        if ok:
            labelMusica.setPixmap(QPixmap(archivo))
            print(archivo)
        return archivo


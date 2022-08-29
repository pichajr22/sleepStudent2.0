from ssl import VerifyMode
from Musica import *
from pygame import mixer
import time

mixer.init()

ventana = SeleccionArchivoVentana()
print("ESCOGE CANCION")
sonido=ventana.seleccionar_archivo()
print("SONIDO ",sonido)
sound = mixer.Sound(sonido)
sound.play()
sound.stop()
time.sleep(5)

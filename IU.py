from glob import glob
import imp
import tkinter as tk
import cv2
from PIL import Image,ImageTk
import os
import imutils
#Ubicar la ejecución en la carpeta actual del proyecto
os.chdir(os.path.dirname(os.path.abspath(__file__)))
video= cv2.VideoCapture(0)


class Editor(tk.Tk):


    def __init__(self):
        super().__init__()
        
        self.iconbitmap('imagenes/icon.ico')
        self.title('Detección de Somnolencia')
        # Configuración tamaño mínimo de la venta
        self.rowconfigure(0, minsize=600, weight=1)
        # Configuración mínima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        # Atributo de campo de imagen
        # Creación de componentes
        Boton1 = tk.Button(self,text='Iniciar')
        self._crear_componentes()

    def bienvenido(self):
        self.ventana_nuevo = tk.Toplevel()
        self.ventana_nuevo.title('Bienvenido')
        self.ventana_nuevo.geometry('600x338')
        imag4 = ImageTk.PhotoImage(Image.open('imagenes/BIENVENIDO.jpg'))
        lbl = tk.Label(self.ventana_nuevo, image=imag4).place(x=0, y=0)
        self.ventana_nuevo.mainloop()

    def ventana_sonido(self):
        self.ventana_nuevo = tk.Toplevel()
        self.ventana_nuevo.title('Ajuste de Sonido')
        self.ventana_nuevo.iconbitmap('imagenes/son.ico')
        self.ventana_nuevo.geometry('560x287')
        imag4 = ImageTk.PhotoImage(Image.open('imagenes/fondosonido.jpg'))
        lbl= tk.Label(self.ventana_nuevo,image=imag4).place(x=0, y=0)
        lbl = tk.Label(self.ventana_nuevo, text='Cambiar sonido',bg='pink').place(x=0, y=0)
        #entrada para sonido
        e1 = tk.Entry(self.ventana_nuevo, bg='gray').place(x=25 , y = 40)
        boton_sonido = tk.Button(self.ventana_nuevo,text='SUBIR').place(x=25,y=35)
        self.ventana_nuevo.mainloop()

    

    def iniciar(self):
        print("HOLA")
        global video
        
        contador=0
        ret,frame = video.read()
        contador = contador+1
        print(contador)
        frame = imutils.resize(frame, width=640)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        image= ImageTk.PhotoImage(image=img)
        etiq_de_video = tk.Label(self, bg="black")
        etiq_de_video.place(x=187,y=75)
        etiq_de_video.configure(image=image)
        etiq_de_video.image = image
        etiq_de_video.after(10,self.iniciar)
       
        




    def _crear_componentes(self):

        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2,bg='black')
        self.img = tk.PhotoImage(file='imagenes/empezar.png')
        self.img2 = tk.PhotoImage(file='imagenes/parar.png')
        self.img3 = tk.PhotoImage(file='imagenes/ajuste.png')
        self.imag7 = tk.PhotoImage(file='imagenes/home.png')
        boton_abrir = tk.Button(frame_botones, text='Iniciar',image=self.img,height=90, width=163, bg='black',relief =tk.RAISED ,highlightthickness=2,bd=0)
        boton_guardar = tk.Button(frame_botones, text='Terminar',image=self.img2,height=90, width=163, bg='black',relief = tk.RAISED,bd=0)
        boton_ajustes = tk.Button(frame_botones, text= 'Ajustes',image=self.img3,height=90, width=163, bg='black', command=self.ventana_sonido,relief = tk.GROOVE,bd=0)
        boton_home = tk.Button(frame_botones, text='Home', image=self.imag7,command=self.bienvenido,height=112, width=150, bg='black',bd=0, relief=tk.GROOVE)
        # Los botones los expandimos de manera horizontal (sticky='we')
        boton_abrir.grid(row=0, column=0, sticky='we')
        boton_guardar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        boton_ajustes.grid(row = 2, column=0, padx=5, pady=5)
        boton_home.grid( padx=5, pady=5)
        # Se coloca el frame de manera vertical
        frame_botones.grid(row=0, column=0, sticky='ns')
        # Agregamos el campo de texto, se expandirá por completo el espacio disponible
        self.campo_video = tk.Frame()
        self.imag5 = ImageTk.PhotoImage(Image.open('imagenes/sleep.jpg'))
        lbl = tk.Label(self.campo_video, image=self.imag5).place(x=0, y=0)
        self.campo_video.grid(row=0, column=1, sticky='nswe')
        self.iniciar()
        
        

    




if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()
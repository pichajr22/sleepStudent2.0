from email.mime import application
from glob import glob
import imp
from tkinter.ttk import Label
import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer
from timeit import default_timer
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import imutils
from Musica import *
from Login import *
from Master import *

os.path.dirname(sys.executable)
application_path = os.path.dirname(sys.executable)
#Ubicar la ejecución en la carpeta actual del proyecto
print("UBICADO")
os.chdir(os.path.dirname(os.path.abspath(__file__)))
reproducir=True
tiempo = 0
#Para reproducir la alarma cuando se duermen
mixer.init()
#Cancion por defecto AC/DC
sound = mixer.Sound('Música/alarm.wav')

#Utilizamos opencv con cascadeClassifier
face = cv2.CascadeClassifier('haar cascade files/haarcascade_frontalface_alt.xml')
leye = cv2.CascadeClassifier('haar cascade files/haarcascade_lefteye_2splits.xml')
reye = cv2.CascadeClassifier('haar cascade files/haarcascade_righteye_2splits.xml')
tiempo  = 0
conn = psycopg2.connect(database="vdtlugyl", user="vdtlugyl", password="MtgLesCauzESzl9MzklRMh2mzS7OZLzS", host="satao.db.elephantsql.com", port="5432")
base=conn.cursor()
lbl=['Close','Open']

model = load_model('models/CNNdeteccion.h5')
path = os.getcwd()

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
count=0
score=0
global thicc
thicc=2
rpred=[99]
lpred=[99]
reproduciendo=False
iniciado=False



class Editor(tk.Tk):
    
    print("Grabando")

    def __init__(self):
        super().__init__()
        self.video= cv2.VideoCapture(0)
        self.iconbitmap('imagenes/icon.ico')
        self.title('Detección de Somnolencia y Desconcentración')
        # Configuración tamaño mínimo de la venta
        self.rowconfigure(0, minsize=600, weight=1)
        # Configuración mínima de la segunda columna
        self.columnconfigure(1, minsize=700, weight=1)
        self.resizable(width=False, height=False)
        # Creación de componentes
        Boton1 = tk.Button(self,text='Iniciar')
        self._crear_componentes()

    def bienvenido(self):
        self.ventana_nuevo = tk.Toplevel()
        self.ventana_nuevo.title('Bienvenido')
        self.ventana_nuevo.geometry('600x338')
        #Con jpg se necesita este metodo
        imag4 = ImageTk.PhotoImage(Image.open('imagenes/BIENVENIDO.jpg'))
        lbl = tk.Label(self.ventana_nuevo, image=imag4).place(x=0, y=0)
        self.ventana_nuevo.mainloop()

    def ventana_sonido(self):

    # self.ventana_nuevo = tk.Toplevel()
    # self.ventana_nuevo.title('Ajuste de Sonido')
    # self.ventana_nuevo.resizable(width=False, height=False)
    # self.ventana_nuevo.iconbitmap('imagenes/son.ico')
    # self.ventana_nuevo.geometry('400x300')
    # self.imag8 = ImageTk.PhotoImage(Image.open('imagenes/fondosonido.jpg'))
    # lbl= tk.Label(self.ventana_nuevo,image=self.imag8).place(x=0, y=0)
    # self.imag7 = tk.PhotoImage(file='imagenes/subir.png')
    # texto = tk.StringVar()
    # texto.set("Un nuevo texto")
    # #entrada para sonido

    # label=tk.Label(self.ventana_nuevo, textvariable=texto)
    # boton_Cambiar.grid(row=0, column=0, sticky='we')
    # e1 = tk.Entry(self.ventana_nuevo, bg='gray').place(x=25 , y = 40)
    # boton_sonido = tk.Button(self.ventana_nuevo,text='SUBIR').place(x=25,y=35)
    #
    # self.ventana_nuevo.mainloop()

        self.ventana_nuevo = tk.Toplevel()
        self.ventana_nuevo.title('Ajuste de Sonido')
        self.ventana_nuevo.resizable(width=False, height=False)
        self.ventana_nuevo.iconbitmap('imagenes/son.ico')
        self.ventana_nuevo.geometry('560x287')
        imag4 = ImageTk.PhotoImage(Image.open('imagenes/fondosonido.jpg'))
        lbl= tk.Label(self.ventana_nuevo,image=imag4).place(x=0, y=0)
        lbl = tk.Label(self.ventana_nuevo, text='Subir sonido',bg='pink').place(x=0, y=0)
        #entrada para sonido
        self.imag7 = tk.PhotoImage(file='imagenes/subir.png')
        boton_Cambiar = tk.Button(self.ventana_nuevo, text='Home', image=self.imag7, command=self.cambiar_Sonido,
                               height=125, width=130, bg='white', bd=0).place(x=10, y=25)
        lbl = tk.Label(self.ventana_nuevo, text='Elegir sonido', bg='pink').place(x=0, y=150)
                #Botones para las canciones
        boton_musica1 = tk.Button(self.ventana_nuevo, text='Smallville',command=self.cambiar_Sonidos1).place(x=0, y=174)
        boton_musica2 = tk.Button(self.ventana_nuevo, text='"We will rock you',command=self.cambiar_Sonidos2).place(x=0,y=198)
        boton_musica3 = tk.Button(self.ventana_nuevo, text='Alarma',command=self.cambiar_Sonidos3).place(x=0, y=222)
        boton_musica4 = tk.Button(self.ventana_nuevo, text='Avengers',command=self.cambiar_Sonidos4).place(x=0, y=246)
        self.ventana_nuevo.mainloop()

#VENTANA PARA MAESTRO
    def ventana_Master(self):
        self.ventana_nuevo = tk.Toplevel()
        self.ventana_nuevo.title('Master')
        self.ventana_nuevo.resizable(width=False, height=False)
        self.ventana_nuevo.iconbitmap('imagenes/son.ico')
        self.ventana_nuevo.geometry('400x300')
        imag4 = ImageTk.PhotoImage(Image.open('imagenes/fondoMaster.jpg'))
        lbl= tk.Label(self.ventana_nuevo,image=imag4).place(x=0, y=0)
        #entrada para sonido
        boton_Cambiar = tk.Button(self.ventana_nuevo, text='Home', image=self.imag7,command=self.cambiar_Sonido,height=112, width=150, bg='black',bd=0, relief=tk.GROOVE).place(x=100,y=100)
        boton_Cambiar.grid(row=0, column=0, sticky='we')
        e1 = tk.Entry(self.ventana_nuevo, bg='gray').place(x=25 , y = 40)
        boton_sonido = tk.Button(self.ventana_nuevo,text='SUBIR').place(x=25,y=35)
        self.ventana_nuevo.mainloop()


    #Sonidos
    def cambiar_Sonido(self):
        ventana = SeleccionArchivoVentana()
        print("ESCOGE CANCION")
        sonido=ventana.seleccionar_archivo()
        print("SONIDO ",sonido)
        global sound
        sound = mixer.Sound(sonido)

    def cambiar_Sonidos1(self):
        global sound
        sound = mixer.Sound('Música/Sound1.wav')
        print("CAMBIO")

    def cambiar_Sonidos2(self):
        global sound
        sound = mixer.Sound('Música/Sound2.mp3')

    def cambiar_Sonidos3(self):
        global sound
        sound = mixer.Sound('Música/Sound3.mp3')

    def cambiar_Sonidos4(self):
        global sound
        sound = mixer.Sound('Música/Sound4.mp3')

    #Componentes
    def _crear_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2,bg='black')
        self.img = tk.PhotoImage(file='imagenes/empezar.png')
        self.img2 = tk.PhotoImage(file='imagenes/parar.png')
        self.img3 = tk.PhotoImage(file='imagenes/ajuste.png')
        self.imag7 = tk.PhotoImage(file='imagenes/home.png')
        boton_abrir = tk.Button(frame_botones, text='Iniciar',image=self.img,height=90, width=163, bg='black',relief =tk.RAISED , command=self.iniciar, highlightthickness=2,bd=0)
        boton_guardar = tk.Button(frame_botones, text='Terminar',image=self.img2,height=90, width=163, bg='black',command=self.detener, relief = tk.RAISED,bd=0)
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

    def detener(self):
        global reproducir
        global score
        score=0
        reproducir=False
        sound.stop()
        

    def iniciar(self):
        global reproducir
        etiq_de_video = tk.Label(self, bg="black")
        etiq_de_video.place(x=200,y=75)
        if(reproducir==True):
            global rpred
            global lpred
            
            ret, frame = self.video.read()
            height,width = frame.shape[:2] 

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
            left_eye = leye.detectMultiScale(gray)
            right_eye =  reye.detectMultiScale(gray)

            cv2.rectangle(frame, (0,height-50) , (650,height) , (0,0,0) , thickness=cv2.FILLED )

            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y) , (x+w,y+h) , (100,100,100) , 1 )

            for (x,y,w,h) in right_eye:
                r_eye=frame[y:y+h,x:x+w]
                global count
                count=count+1
                r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
                r_eye = cv2.resize(r_eye,(24,24))
                r_eye= r_eye/255
                r_eye=  r_eye.reshape(24,24,-1)
                r_eye = np.expand_dims(r_eye,axis=0)
                rpred = model.predict_classes(r_eye)
                if(rpred[0]==1):
                    lbl='Abierto'
                if(rpred[0]==0):
                    lbl='Cerrado'
                break

            for (x,y,w,h) in left_eye:
                l_eye=frame[y:y+h,x:x+w]

                
                count=count+1
                l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
                l_eye = cv2.resize(l_eye,(24,24))
                l_eye= l_eye/255
                l_eye=l_eye.reshape(24,24,-1)
                l_eye = np.expand_dims(l_eye,axis=0)
                lpred = model.predict_classes(l_eye)
                if(lpred[0]==1):
                    lbl='Abierto'
                if(lpred[0]==0):
                    lbl='Cerrado'
                break

            global score
            if(rpred[0]==0 and lpred[0]==0):
                
                score=score+1
                cv2.putText(frame,"Cerrado",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            # if(rpred[0]==1 or lpred[0]==1):
            else:
                
                score=score-1
                cv2.putText(frame,"Abierto",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            
                
            if(score<0):
                global reproduciendo
                global conn
                global base
                sql='UPDATE '+'"Attention"'+"set"+ '"attentionSlave"='+"'Si' WHERE "+'"idAttention"=%d'
                
                base.execute(sql%3)
                print("CMABIO")
                
                conn.commit()
                reproduciendo=False
                score=0   
            cv2.putText(frame,'Conteo:'+str(score),(150,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            #Calculo para la desconcetracion (mejorar el calculo)
            cv2.putText(frame, 'Desconcetracion:', (300, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

            if (score > 5 and rpred[0]==0 and lpred[0]==0):
                cv2.putText(frame, "No atiende", (504, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

            else:
                cv2.putText(frame, "Atiende", (504, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

            global thicc

            if(score>20):

                
                cv2.imwrite(os.path.join(path,'image.jpg'),frame)
                try:
                    print("INTENTANDO")
                    if(reproduciendo == False):
                        print("REPRODUCIENDO")
                        reproduciendo=True
                        sound.play()
                        
                        sql='UPDATE '+'"Attention"'+"set"+ '"attentionSlave"='+"'NOOO' WHERE "+'"idAttention"=%d'
                        
                        base.execute(sql%3)
                        print("CMABIO")
                        
                        conn.commit()
                        
                        sql='SELECT * FROM '+'"Attention"'+"where"+ '"idAttention"='+"%d"
                        base.execute(sql%3)
                        user=base.fetchone()
                        print("USUARIO: ",user)
                        base.execute(sql%3)
                        user=base.fetchone()
                        print("USUARIO: ",user)
                        conn.commit()
                        
                    else:
                        print("Ya se esta reproduciendo")


                
                except:
                    pass
                if(thicc<16):
                    thicc= thicc+2
                else:
                    thicc=thicc-2
                    if(thicc<2):
                        thicc=2
                cv2.rectangle(frame,(0,0),(width,height),(0,0,255),thicc)
            
            frame = imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            image= ImageTk.PhotoImage(image=img)
            
            etiq_de_video.configure(image=image)
            etiq_de_video.image = image
            etiq_de_video.after(10,self.iniciar)
            
        else:
            etiq_de_video2 = ImageTk.PhotoImage(Image.open('imagenes/fondosonido.jpg'))
            etiq_de_video.place_forget()
            print("OLVIDADO")
          
            

        
        reproducir=True

if __name__ == '__main__':
    iniciado=True
    page()
    usuario=obtenerUsuario()
    print("Usuario Iniciado",usuario)
    sql='SELECT * FROM '+'"Slave"'+"where"+ '"userSlave"='+"'%s'"
    base.execute(sql%usuario)
    user=base.fetchone()
    print("USUARIO: ",user)
    sql='SELECT * FROM '+'"Master"'+"where"+ '"userMaster"='+"'%s'"
    base.execute(sql%usuario)
    master=base.fetchone()
    print("MASTER: ",master)
    tipoUsuario=""
    if(user!= None):
        tipoUser="slave"
        print("ES UN ESCLAVO")
        editor = Editor()
        editor.mainloop()


    
    

    






















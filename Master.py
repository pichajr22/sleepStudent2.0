from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os
from urllib import robotparser
import psycopg2


os.chdir(os.path.dirname(os.path.abspath(__file__)))
conn = psycopg2.connect(database="vdtlugyl", user="vdtlugyl", password="MtgLesCauzESzl9MzklRMh2mzS7OZLzS", host="satao.db.elephantsql.com", port="5432")
base=conn.cursor()
base.execute('Select * from "Attention"')
rows=base.fetchall()
sql='SELECT * FROM '+'"Attention"'+"where"+ '"idAttention"='+"%d"
base.execute(sql%1)
user=base.fetchone()


class Master(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.geometry("700x450")
        self.title("Treeview")
        self.imag5 = ImageTk.PhotoImage(Image.open('imagenes/fondoMaster.jpg'))
        self.lbl = ttk.Label(self, image=self.imag5).place(x=0, y=0)
        self.arbol = ttk.Treeview(self)
        self.img = tk.PhotoImage(file='imagenes/refresh.png')
        boton_abrir = tk.Button(self, text='Iniciar',image=self.img,height=50, width=50, command=self.actualizar ,bg='white',relief =tk.RAISED , highlightthickness=2,bd=0)
        boton_abrir.place(x=50,y=400)
        self.arbol['columns']=('Name', 'Badge')
        self.arbol.column('Name', anchor=CENTER, width=200)
        self.arbol.column('Badge', anchor=CENTER, width=40)

        for row in rows:
            nombre=row[2]
            id=row[0]
            print(id," Atendiendo: ",nombre)
            sql='SELECT * FROM '+'"Slave"'+"where"+ '"idSlave"='+"'%s'"
            base.execute(sql%row[1])
            user=base.fetchone()
            print(row[1],"  ",user)
            self.arbol.insert("",END,text=user[1],values=(row[2]))

        self.arbol.place(x=210,y=150)

    def actualizar(self):
        print("ACTUALIZANDO")
        for item in self.arbol.get_children():
            self.arbol.delete(item)
        print("DESTRUIDO")
        base.execute('Select * from "Attention"')
        rows=base.fetchall()
        sql='SELECT * FROM '+'"Attention"'+"where"+ '"idAttention"='+"%d"
        base.execute(sql%1)
        user=base.fetchone()
        print("USUARIO: ",user)
        self.arbol.place(x=210,y=150)
        for row in rows:
            nombre=row[2]
            id=row[0]
            print(id," Atendiendo: ",nombre)
            sql='SELECT * FROM '+'"Slave"'+"where"+ '"idSlave"='+"'%s'"
            base.execute(sql%row[1])
            user=base.fetchone()
            print(row[1],"  ",user)
            self.arbol.insert("",END,text=user[1],values=(row[2]))


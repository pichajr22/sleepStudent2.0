from tkinter import *
from PIL import ImageTk, Image
import os
from urllib import robotparser
import psycopg2
from tkinter import messagebox as MessageBox
from Master import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))
tipoUser=''
contra=''
conn = psycopg2.connect(database="vdtlugyl", user="vdtlugyl", password="MtgLesCauzESzl9MzklRMh2mzS7OZLzS", host="satao.db.elephantsql.com", port="5432")
base=conn.cursor()
base.execute("select version()")
row = base.fetchone()
base.execute('Select * from "Master"')
rows=base.fetchall()
nombre=""
id=0
for row in rows:
    nombre=row[1]
    id=row[0]
    print(id," Nombre: ",nombre)

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1300x750')
        self.window.resizable(0, 0)
        
        self.window.title('Pantalla de inicio')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('imagenes\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "BIENVENIDO"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('imagenes\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('imagenes\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('imagenes\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('imagenes\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command= self.verificar)

        self.login.place(x=20, y=10)
        # ========================================================================

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('imagenes\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='imagenes\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='imagenes\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def verificar(self):
        usuario = self.username_entry.get()
        global tipoUser
        tipoUser=usuario
        global contra
        contra = self.password_entry.get()
        sql='SELECT * FROM '+'"Slave"'+"where"+ '"userSlave"='+"'%s'"
        base.execute(sql%usuario)
        user=base.fetchone()
        print("USUARIO: ",user)
        sql='SELECT * FROM '+'"Master"'+"where"+ '"userMaster"='+"'%s'"
        base.execute(sql%usuario)
        master=base.fetchone()
        print("MASTER: ",master)
        if(user==None and master==None):
            print('Usuario no encontrado')
            MessageBox.showinfo("Error!", "Usuario: "+ usuario +" no encontrado") # título, mensaje
            
        else:
            if(master!= None and master[3]==contra):
                self.window.destroy()
                master = Master()
                master.mainloop()
                
            elif(user!= None and user[3]==contra):
                self.window.destroy()
            else:
                MessageBox.showinfo("Error!", "Contraseña Incorrecta") # título, mensaje
        
        #drowsiness_detection()

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()

def obtenerUsuario():
    return tipoUser

def obtenerContraseña():
    return contra
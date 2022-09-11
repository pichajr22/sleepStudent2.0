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

        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='Sin cuenta aún?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='imagenes\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405", command=self.TipoRol)
        self.signup_button_label.place(x=670, y=555, width=111, height=35)
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


         #Indica el tipo de usuario a registrarse
    def TipoRol(self):
        mywindow = Tk()
        mywindow.geometry("300x180")
        mywindow.title("Tipo Usuario")
        mywindow.resizable(False, False)
        mywindow.config(background="black")
        self.username_label = Label(mywindow, text="ELIJA SU ROL:", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=22, y=15)
        submit_btn = Button(mywindow, text="SOY ESTUDIANTE! ", width="25", height="2", command=self.registerEstudiante, bg="#56CD63")
        submit_btn.place(x=22, y=70)
        submit_btn2 = Button(mywindow, text="SOY PROFESOR! ", width="25", height="2", command=self.registerProfesor,
                            bg="#56CD63")
        submit_btn2.place(x=22, y=120)

        #Interfaz de registro de usuario
    def registerEstudiante(self):
        #Pantalla
        mywindow2 = Tk()
        mywindow2.geometry("550x400")
        mywindow2.title("Registro de estudiante")
        mywindow2.resizable(False, False)
        mywindow2.config(background="black")

        main_title = Label(text="Python Form | TRUZZ BLOGG", font=("Cambria", 14), bg="#56CD63", fg="black",
                           width="500",
                           height="2")
        main_title.pack()

        # Define Label Fields
        self.username_label = Label(mywindow2, text="               REGISTRO DE ESTUDIANTE", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=22, y=30)
        self.username_label = Label(mywindow2, text="Username", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=22, y=70)
        self.password_label = Label(mywindow2, text="Password", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=22, y=130)
        self.fullname_label = Label(mywindow2, text="Nombre completo", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.fullname_label.place(x=22, y=190)
        self.rol_label = Label(mywindow2, text="Clave de ingreso para la clase", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.rol_label.place(x=22, y=250)

        # Obtengo los datos
        username = StringVar()
        password = StringVar()
        fullname = StringVar()
        clave = StringVar()

        username = Entry(mywindow2, textvariable=username, width="40")
        password = Entry(mywindow2, textvariable=password, width="40", show="*")
        fullname = Entry(mywindow2, textvariable=fullname, width="40")
        clave= Entry(mywindow2, textvariable=clave, width="40")

        username.place(x=22, y=100)
        password.place(x=22, y=160)
        fullname.place(x=22, y=220)
        clave.place(x=22, y=280)

        #método para obtener datos
        def send_data():
            username_info = username.get()
            password_info = password.get()
            fullname_info = fullname.get()
            clave_info = clave.get()
            print(username_info, "\t", password_info, "\t", fullname_info, "\t", clave_info)
            print("Estudiante registrado.")

        # Boton de registro
        submit_btn = Button(mywindow2, text="REGISTRARSE", width="25", height="2", command=send_data, bg="#56CD63",font=("yu gothic ui", 13, "bold"))
        submit_btn.place(x=22, y=320)
        mywindow2.mainloop()

    #Interfaz de registro de profesor
    def registerProfesor(self):
        #Pantalla
        mywindow = Tk()
        mywindow.geometry("550x400")
        mywindow.title("Registro de docente")
        mywindow.resizable(False, False)
        mywindow.config(background="black")

        main_title = Label(text="Python Form | TRUZZ BLOGG", font=("Cambria", 14), bg="#56CD63", fg="black",
                           width="500",
                           height="2")
        main_title.pack()

        # Define Label Fields
        self.username_label = Label(mywindow, text="                          REGISTRO DE DOCENTE", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=22, y=30)
        self.username_label = Label(mywindow, text="Username", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=22, y=70)
        self.password_label = Label(mywindow, text="Password", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=22, y=130)
        self.fullname_label = Label(mywindow, text="Nombre completo", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.fullname_label.place(x=22, y=190)
        self.rol_label = Label(mywindow, text="Crear clave para la clase:", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.rol_label.place(x=22, y=250)

        # Obtengo los datos
        username = StringVar()
        password = StringVar()
        fullname = StringVar()
        clave = StringVar()

        username = Entry(mywindow, textvariable=username, width="40")
        password = Entry(mywindow, textvariable=password, width="40", show="*")
        fullname = Entry(mywindow, textvariable=fullname, width="40")
        clave= Entry(mywindow, textvariable=clave, width="40", show="*")

        username.place(x=22, y=100)
        password.place(x=22, y=160)
        fullname.place(x=22, y=220)
        clave.place(x=22, y=280)

        #método para obtener datos
        def send_data():
            username_info = username.get()
            password_info = password.get()
            fullname_info = fullname.get()
            clave_info =clave.get()
            print(username_info, "\t", password_info, "\t", fullname_info, "\t", clave_info)
            print("Docente registrado.")

        # Boton de registro
        submit_btn = Button(mywindow, text="REGISTRARSE", width="22", height="1", command=send_data, bg="#56CD63",font=("yu gothic ui", 10, "bold"))
        submit_btn.place(x=22, y=320)
        mywindow.mainloop()

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
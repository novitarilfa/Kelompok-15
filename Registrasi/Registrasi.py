from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import time
import csv

Accountsystem = Tk()
Accountsystem.rowconfigure(0,weight=1)
Accountsystem.columnconfigure(0,weight=1)
Accountsystem.geometry('1200x720')
Accountsystem.state('zoomed')
Accountsystem.resizable(0,0)
Accountsystem.title('Login Page')

#Navigation
sign_in = Frame(Accountsystem)
sign_up = Frame(Accountsystem)

for frame in (sign_in, sign_up):
    frame.grid(row=0,column=0,sticky='nsew')

def show_frame(frame):
    frame.tkraise()

#===============================================================================================
#========================================== LOADING  ===========================================
#===============================================================================================
latar = Frame(Accountsystem, width=1500, height=1000, bg='#F6D58E').place(x=0,y=0)

food_picker=PhotoImage(file='food picker.png')
fbLabel=Label(Accountsystem,image=food_picker,bg='#F6D58E')
fbLabel.place(x=320,y=150)

Label(latar,text='Loading...',font=('yu gothic ui bold',25,'bold'),bg='#F6D58E',fg='brown').place(x=30,y=670)


b = ImageTk.PhotoImage(Image.open('kosong.png'))
a = ImageTk.PhotoImage(Image.open('ubi.png'))

for i in range(4):
    l1 = Label(latar,image=a, border=0, relief=SUNKEN).place(x=210,y=400)
    l2 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=460,y=400)
    l3 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=710,y=400)
    l4 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=960,y=400)
    Accountsystem.update_idletasks()
    time.sleep(0.5)

    l1 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=210,y=400)
    l2 = Label(latar,image=a, border=0, relief=SUNKEN).place(x=460,y=400)
    l3 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=710,y=400)
    l4 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=960,y=400)
    Accountsystem.update_idletasks()
    time.sleep(0.5)

    l1 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=210,y=400)
    l2 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=460,y=400)
    l3 = Label(latar,image=a, border=0, relief=SUNKEN).place(x=710,y=400)
    l4 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=960,y=400)
    Accountsystem.update_idletasks()
    time.sleep(0.5)

    l1 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=210,y=400)
    l2 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=460,y=400)
    l3 = Label(latar,image=b, border=0, relief=SUNKEN).place(x=710,y=400)
    l4 = Label(latar,image=a, border=0, relief=SUNKEN).place(x=960,y=400)
    Accountsystem.update_idletasks()
    time.sleep(0.5)

show_frame(sign_in)

#===============================================================================================
#========================================== BUAT AKUN  =========================================
#===============================================================================================
#======================================= Background Image ======================================
bg = ImageTk.PhotoImage(file='3.png')
background2 = Label(sign_up,image=bg)
background2.place(x=0,y=0)

#===================================== Kumpulan Fungsi =======================================
def email_enter(event):
    if email.get()=='Email':
        email.delete(0,END)

def user(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def konfirmasi_password_enter(event):
    if konfirmasi_password.get()=='Konfirmasi Password':
        konfirmasi_password.delete(0,END)

def connect_database():
    if email.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or konfirmasi_password.get()=='':
        messagebox.showerror('Error','Jangan kosong')
        
    elif passwordEntry.get() != konfirmasi_password.get():
        messagebox.showerror('Error', 'Password kok beda?')
    
    elif check.get()==0:
        messagebox.showerror('Error', 'centang bestie')
    
    else:
        try:
            con=csv.connect(host='localhost',username='root',password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'sorry ulangi ya blm ke simpen')
            return
            
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        
        except:
            mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query,(passwordEntry.get()))
        
        row=mycursor.fetchone()
        if row !=None:
            messagebox.showinfo('Error','username udah ada')
        
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(email.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','registrasi sukses')
            clear()
            Accountsystem.destroy()


def clear():
    email.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    konfirmasi_password.delete(0,END)
    check.set(0)


# ==================================== Tampilan login ========================================
heading=Label(background2,text='BUAT AKUN',font=('yu gothic ui bold',30,'bold'),bg='#FCFDFE',fg='brown')
heading.place(x=560,y=160)

email=Entry(background2,width=25,font=('Microsoft Yeahei UI Light',11,'bold'),bd=0,bg='#FCFDFE',fg='brown')
email.place(x=500,y=240)
email.insert(0,'Email')
email.bind('<FocusIn>',email_enter)

emailLabel=Label(background2,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='#FCFDFE',fg='brown')
emailLabel.place(x=500,y=240)

emailEntry=Entry(background2,width=44,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg='#FCFDFE',bg='brown')
emailEntry.place(x=500,y=265)

usernameLabel=Label(background2,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='#FCFDFE',fg='brown')
usernameLabel.place(x=500,y=290)

usernameEntry=Entry(background2,width=44,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg='#FCFDFE',bg='brown')
usernameEntry.place(x=500,y=315)

passwordLabel=Label(background2,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='#FCFDFE',fg='brown')
passwordLabel.place(x=500,y=340)

passwordEntry=Entry(background2,width=44,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg='#FCFDFE',bg='brown')
passwordEntry.place(x=500,y=365)

konfirmasiLabel=Label(background2,text='Konfirmasi Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='#FCFDFE',fg='brown')
konfirmasiLabel.place(x=500,y=390)

konfirmasi_password=Entry(background2,width=44,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,fg='#FCFDFE',bg='brown')
konfirmasi_password.place(x=500,y=415)

check=IntVar()
termsandconditions=Checkbutton(background2,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',9,'bold'),fg='brown',bg='#FCFDFE',activebackground='#FCFDFE',activeforeground='brown',cursor='hand2',variable=check)
termsandconditions.place(x=500,y=437)

signupButton=Button(background2,text='Buat Akun',font=('Open Sans',15,'bold'),bd=0,bg='brown',fg='#FCFDFE',activebackground='brown',activeforeground='#FCFDFE',width=20,cursor='hand2',command=connect_database)
signupButton.place(x=550,y=480)

signupLabel=Label(background2,text="Sudah punya akun?",font=('Open Sans',9),fg='brown',bg='#FCFDFE')
signupLabel.place(x=590,y=533)

akun_lamaButton=Button(background2,text='Login',font=('Open Sans',9,'bold underline'),
                        fg='brown',bg='#FCFDFE',activeforeground='brown',activebackground='#FCFDFE',
                        cursor='hand2',bd=0,command=lambda:show_frame(sign_in))
akun_lamaButton.place(x=705,y=533)

#===================================================================================================
#=========================================== LOGIN =================================================
#===================================================================================================
        
# =================================== Background Image =======================================
Login_backgroundImage = ImageTk.PhotoImage(file='3.png')
background = Label(sign_in,image=Login_backgroundImage)
background.place(x=0,y=0)


# ==================================== Kumpulan fungsi =======================================
def lupa_password():

    lupa = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = lupa.winfo_screenwidth()
    screen_height = lupa.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    lupa.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    lupa.title('Lupa Password')
    # win.iconbitmap('images\\aa.ico')
    lupa.configure(background='#F6D58E')
    lupa.resizable(False, False)

    # =================== Email ====================
    email_baru = Entry(lupa, bg='#FCFDFE', font=("yu gothic ui semibold", 12),bd=0,fg='brown')
    email_baru.place(x=50, y=60, width=256, height=35)
    email_label = Label(lupa, text='Email', fg="brown", bg='#F6D58E',font=("yu gothic ui", 11, 'bold'))
    email_label.place(x=50, y=30)

    # ============== Password Baru ==================
    password_baru = Entry(lupa, bg="#FCFDFE", font=("yu gothic ui semibold", 12), show='•',bd=0,fg='brown')
    password_baru.place(x=50, y=130, width=256, height=35)
    password_label = Label(lupa, text='Password Baru', fg="brown", bg='#F6D58E',font=("yu gothic ui", 11, 'bold'))
    password_label.place(x=50, y=100)

    # ============== Konfirmasi Password Baru ==================
    konfirmasi_password_baru = Entry(lupa, bg="#FCFDFE", font=("yu gothic ui semibold", 12), show='•',bd=0,fg='brown')
    konfirmasi_password_baru.place(x=50, y=200, width=256, height=35)
    konfirmasi_password_label = Label(lupa, text='Konfirmasi Password Baru', fg="brown", bg='#F6D58E',font=("yu gothic ui", 11, 'bold'))
    konfirmasi_password_label.place(x=50, y=170)

    # ============== Update password Button ====================
    update_pass = Button(lupa, fg='#FCFDFE', text='Update Password', bg='brown', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="brown")
    update_pass.place(x=50, y=260, width=256, height=45)

def hide():
    openeye.config(file='closeye.png')
    password.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    password.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if username.get()=='Username':
        username.delete(0,END)

def password_enter(event):
    if password.get()=='Password':
        password.delete(0,END)

def login_user():

    if username.get()=='' or password.get()=='':
        messagebox.showerror('Error', 'Jangan kosong')

    else:
        try:
            con=csv.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        
        except:
            messagebox.showerror('Error','akun ga ada, bikin dulu yuk')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select *from data where username=%s and password=%s'
        mycursor.execute(query,username.get(),password.get())
        row=mycursor.fetchone()
        
        if row==None:
            messagebox.showerror('Error','Invalid Username or Password')
            
        else:
            messagebox.showinfo('Welcome','Login berhasil')

# ==================================== Tampilan login ========================================
heading=Label(background,text='LOGIN',font=('yu gothic ui bold',30,'bold'),bg='#FCFDFE',fg='brown')
heading.place(x=610,y=160)

username=Entry(background,width=25,font=('Microsoft Yeahei UI Light',11,'bold'),bd=0,bg='#FCFDFE',fg='brown')
username.place(x=500,y=280)
username.insert(0,'Username')
username.bind('<FocusIn>',user_enter)

frame1=Frame(background,width=350,height=2,bg='brown').place(x=500,y=305)

password=Entry(background,width=25,font=('Microsoft Yeahei UI Light',11,'bold'),bd=0,bg='#FCFDFE',fg='brown')
password.place(x=500,y=350)
password.insert(0,'Password')
password.bind('<FocusIn>',password_enter)

frame2 = Frame(background,width=350,height=2,bg='brown').place(x=500,y=375)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(background,image=openeye,bd=0,bg='#FCFDFE',activebackground='#FCFDFE',
                   cursor='hand2',command=hide)
eyeButton.place(x=820,y=347)

forgetButton=Button(background,text='Lupa Password?',bd=0,bg='#FCFDFE',activebackground='#FCFDFE',
                    cursor='hand2',font=('Microsoft Yeahei UI Light',9,'bold'),fg='brown',
                    activeforeground='brown',command=lambda : lupa_password())
forgetButton.place(x=750,y=385)

loginButton=Button(background,text='Login',font=('Open Sans',15,'bold'),fg='#FCFDFE',
                   bg='brown',activeforeground='#FCFDFE',activebackground='brown',cursor='hand2',
                   bd=0,width=20,command=login_user)

loginButton.place(x=550,y=480)

signupLabel=Label(background,text="Belum punya akun?",font=('Open Sans',9),fg='brown',bg='#FCFDFE')
signupLabel.place(x=578,y=533)

newaccountButton=Button(background,text='Buat akun',font=('Open Sans',9,'bold underline'),
                        fg='brown',bg='#FCFDFE',activeforeground='brown',activebackground='#FCFDFE',
                        cursor='hand2',bd=0, command=lambda : show_frame(sign_up))
newaccountButton.place(x=693,y=533)

Accountsystem.mainloop()
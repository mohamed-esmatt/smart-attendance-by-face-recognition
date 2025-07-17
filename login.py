from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student
from student_user import Student_readonly
from train import Train
from face_recognition import Face_Recognition
import os
from help import help
import re
import tkinter
import pyttsx3  
from about_us import About_US


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1250x740")
        self.root.resizable(0,0)

        #test
        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open(r'images\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.root, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=150, y=70)
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open(r'images\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open(r'images\hyy.png')
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
        self.username_icon = Image.open(r'images\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open(r'images\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label,command=self.login, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame,command=self.forgot_password_window, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)
        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text="Don't have an account?", font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file=r'images\register.png')
        self.signup_button_label = Button(self.lgn_frame,command=self.register_window, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=715, y=555, width=111, height=35)

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
        self.password_icon = Image.open(r'images\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file=r'images\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file=r'images\hide.png')

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




    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.username_entry.get() == "admin" and self.password_entry.get() == "123":
            speak_va("Welcome to the Face recognition app SIR")
            messagebox.showinfo("success", "Welcome To Face recognition App")
            self.new_window=Toplevel(self.root)
            self.app=Admin(self.new_window)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="data")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.username_entry.get(),
                self.password_entry.get()
                     ))
            row=my_cursor.fetchone()
            if row==None:
                speak_va("Invalid username and password!")
                messagebox.showerror("Error","Invalid Username or Password")
            else:                
                    self.new_window=Toplevel(self.root)
                    self.app=User(self.new_window)
                    return
            conn.commit()
            conn.close()
        

            #************************************Reset password button *******************
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
                messagebox.showerror("Error","select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
                messagebox.showerror("Error","select your answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
                messagebox.showerror("Error","please enter your new password",parent=self.root2) 
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="data")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s ")
            value=(self.username_entry.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                speak_va("Wrong Security Answer")
                messagebox.showerror("Error","Invalid security answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpassword.get(),self.username_entry.get())
                my_cursor.execute(query,value)
                speak_va("Your password has been reset successfully.")
                messagebox.showinfo("Info","Your Password Has Been Reset Succesfully",parent=self.root2)
            conn.commit()
            conn.close()
            self.root2.destroy()
               


                
                
 #   ************************forget password****************
    def forgot_password_window(self):
        if self.username_entry.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="data")
            my_cursor = conn.cursor()
            query=("select *from register where email=%s")   ##### <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< see thissssssss
            value=(self.username_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2= Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("350x400+610+170")
                self.root2.resizable(0,0)
                self.root2.configure(background='black')
                l=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"),bg="black", fg="red")
                l.place(x=0,y=0,relwidth=1)
                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="black",fg="white")
                security_Q.place(x=50, y=80)
                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Your First Car","Your Pet's Name","Your Birth Place")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)
                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="black",fg="white")
                security_A.place(x=50, y=150)
                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)
                new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"), bg="black",fg="white")
                new_password.place(x=50, y=220)
                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpassword.place(x=50, y=250, width=250)
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"), bg="blue",fg="white")
                btn.place(x=140,y=320)





#>>>>>>>>>>>>>>>>>>>>>>>>Signup>>

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Sign Up')
        self.root.geometry("1100x700+0+0")
        self.root.resizable(0,0)

        # ***************variabletr
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background img
        self.bg = ImageTk.PhotoImage(
            file=r"images\background1.png")
        lbl_lbl = Label(self.root, image=self.bg)
        lbl_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # #left image
        lftimage=Image.open(r"images\leftimg.png")

# Resize the image in the given (width, height)
        lftimg=lftimage.resize((450, 450))
        self.bg1 = ImageTk.PhotoImage(lftimg)
        left_lbl = Label(self.root, image=self.bg1,bg="black")
        left_lbl.place(x=30, y=100, width=500, height=500)
        # main frame
        frame = Frame(self.root, bg="black")
        frame.place(x=520, y=100, width=550, height=500)
        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # ***lebal and entry
        # column 1
        
        Register_frame=LabelFrame(frame,bd=2,bg="black",relief=RIDGE,text="REGISTER HERE",font=("times new roman",20,"bold"), fg="blue")
        Register_frame.place(x=5,y=5,width=510,height=400)
        fname=Label(Register_frame,text="First Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        fname.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        fname_entry=ttk.Entry(Register_frame,textvariable=self.var_fname,width=25,font=("times new roman",13,"bold"))
        fname_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)     
        validate_fname=self.root.register(self.checkname)
        fname_entry.config(validate='key',validatecommand=(validate_fname,'%P'))

        lname=Label(Register_frame,text="Last Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        lname.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        lname_entry=ttk.Entry(Register_frame,textvariable=self.var_lname,width=25,font=("times new roman",13,"bold"))
        lname_entry.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        validate_lname=self.root.register(self.checklname)
        fname_entry.config(validate='key',validatecommand=(validate_lname,'%P'))


        # =====================================column 2=====================================

        contact=Label(Register_frame,text="Contact No.",font=("times new roman",15,"bold"),bg="black",fg="white")
        contact.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        contact_entry=ttk.Entry(Register_frame,textvariable=self.var_contact,width=25,font=("times new roman",13,"bold"))
        contact_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        validate_phone=self.root.register(self.checkphone)
        contact_entry.config(validate='key',validatecommand=(validate_phone,'%P'))
        email=Label(Register_frame,text="Email",font=("times new roman",15,"bold"),bg="black",fg="white")
        email.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        email_entry=ttk.Entry(Register_frame,textvariable=self.var_email,width=25,font=("times new roman",13,"bold"))
        email_entry.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        email=Label(Register_frame,text="*Please enter valid email: ex123@gmail.com",font=("times new roman",8,"bold"),fg="red",bg="black")
        email.place(x=250, y=139)
        security_Q=Label(Register_frame,text="Security Question",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_Q.grid(row=6,column=1,padx=5,pady=5,sticky=W)

        Security_combo=ttk.Combobox(Register_frame,textvariable=self.var_securityQ,font=("times new roman",13,"bold"),state="readonly",width=23)
        Security_combo["values"]=("Your First Car","Your Pet's Name","Your Birth Place")
        Security_combo.current(0)
        Security_combo.grid(row=7,column=1,padx=5,pady=10,sticky=W)
        security_A=Label(Register_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_A.grid(row=6,column=2,padx=10,pady=5,sticky=W)

        security_entry=ttk.Entry(Register_frame,textvariable=self.var_securityA,width=25,font=("times new roman",13,"bold"))
        security_entry.grid(row=7,column=2,padx=10,pady=5,sticky=W)


        # ......colum 5
        pswd=Label(Register_frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        pswd.grid(row=8,column=1,padx=10,pady=5,sticky=W)
        pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_pass,width=25,font=("times new roman",13,"bold"))
        pswd_entry.grid(row=9,column=1,padx=10,pady=5,sticky=W)
        pswd=Label(Register_frame,text="*Please enter strong password",font=("times new roman",10,"bold"),fg="red",bg="black")
        pswd.place(x=35, y=305)
        confirm_pswd=Label(Register_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        confirm_pswd.grid(row=8,column=2,padx=10,pady=5,sticky=W)
        confirm_pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_confpass,width=25,font=("times new roman",13,"bold"))
        confirm_pswd_entry.grid(row=9,column=2,padx=10,pady=5,sticky=W)

        # ......check button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree with terms and conditions", font=(
            "times new roman", 12, "bold"),bg='black', fg='white', activebackground='black', activeforeground='white',selectcolor="black", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=370)
       

        # button

        img = Image.open(r"images\register1.png")
        img = img.resize((200, 70), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data,
                    image=self.photoimage, borderwidth=0, cursor="hand2",bg="black")
        b1.place(x=140, y=415, width=250)
        


    def checkname(self,name):
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
        return True

    def checklname(self,name):
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
        return True

    def checkphone(self,phone):
        if len(phone) <=11:
          if phone.isdigit():
            return True
          if len(str(phone))==0:
            return True
          else:
            messagebox.showerror('Invalid','Invalid entry. Please enter phone (example:01000048888)', parent=self.root)
            return False                                                               
            
        else:
            messagebox.showwarning('Alert','invalid phone. Please enter phone (example:01000048888)',parent=self.root)
            return False



        
       
       



# ................fuction

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password and confirm password must be same",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree to our terms and conditions",parent=self.root)

        elif not ("@" or ".com") in self.var_email.get():
            messagebox.showerror("Error",'Invalid email Enter valid email like example@mail.com ',parent=self.root)
        
        elif not ("@" or "!" or "$" or "-" or "." or "#" ) in self.var_pass.get():
            messagebox.showerror("Error",'Invalid Password\n a minimum of 1 lower case letter [a-z] and a minimum of 1 upper case letter [A-Z] and a minimum of 1 numeric character [0-9] and a minimum of 1 special character: ~`!@$%^&*()-_+={}[]|\;:"<>,./?  ',parent=self.root)

    
        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="data")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")   ### <<<<<<<<<<<<<<<<<<seee
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "user already exists ,try another email", parent=self.root )
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                messagebox.showinfo("Success", "Register Successfully", parent=self.root )
            conn.commit()
            conn.close()
    def return_login(self):
        self.root.destroy()



   

            
# #>>>>>>>>>>>>>>>>>main page 
class Admin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Admin")
        self.root.resizable(0,0)

         # first image
        img1 = Image.open("Images/HU2.png")
        img1 = img1.resize((465, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=2.5, y=0, width=465, height=150)

        # second image
        img2 = Image.open("Images/eye.jpg")
        img2 = img2.resize((465, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=467.5, y=0, width=465, height=150)

        # # third image
        img3 = Image.open("Images/helwan campus.jpg")
        img3 = img3.resize((465, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=932.5, y=0, width=465, height=150)

        # background image
        img4 = Image.open(r"Images/bg.png")
        img4 = img4.resize((1400, 609), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=150, width=1400, height=609)

        title_lbl = Label(bg_img, text="Face Recognition(Admin Mode)",
                          font=("Algerian", 35, "bold"), fg="red")
        title_lbl.place(x=0, y=0, width=1395, height=45)  # using .place u can place things at any part of the window


        # student button

        btn1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("Algerian", 20, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=100, y=100, width=300, height=150)

        # Face Detection button
   
        btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("Algerian", 20, "bold"),
                        bg="darkblue", fg="white")
        btn2_2.place(x=520, y=100, width=300, height=150)

       

        # Help Desk button
    
        btn4_4 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.helpp ,font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
        btn4_4.place(x=1195, y=2, width=195, height=40)

        # train data button
        btn5_5 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("Algerian", 20, "bold"),
                        bg="darkblue", fg="white")
        btn5_5.place(x=100, y=350, width=300, height=150)

        # Photos button     
        btn6_6 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("Algerian", 20, "bold"),
                        bg="darkblue", fg="white")
        btn6_6.place(x=520, y=350, width=300, height=150)

        # about us button
        btn7_7 = Button(bg_img, text="About US", cursor="hand2",command=self.AboutUs, font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
        btn7_7.place(x=5, y=2, width=195, height=40)

        # Exit button
        img12 = Image.open("Images/exit-sign-neon-style_77399-144.jpg")
        img12 = img12.resize((195, 195), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        btn8_8 = Button(bg_img, text="Exit",command=self.iexit,cursor="hand2", font=("Algerian", 20, "bold"),
                        bg="darkblue", fg="white")
        btn8_8.place(x=980, y=350, width=300, height=150)


    def open_img(self):
        os.startfile("data")

    # =================================== Functions =========================================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)  
        
    def helpp(self):
        self.new_window = Toplevel(self.root)
        self.app=help(self.new_window)

    def AboutUs(self):
        self.new_window = Toplevel(self.root)
        self.app=About_US(self.new_window)

    
     

# .................exit button
    def iexit(self):
        speak_va("Are you sure you want to exit this project?")
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return

class User:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition App")
        self.root.resizable(0,0)

         # first image
        img1 = Image.open("Images/HU2.png")
        img1 = img1.resize((465, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=2.5, y=0, width=465, height=150)

        # second image
        img2 = Image.open("Images/eye.jpg")
        img2 = img2.resize((465, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=467.5, y=0, width=465, height=150)

        # # third image
        img3 = Image.open("Images/helwan campus.jpg")
        img3 = img3.resize((465, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=932.5, y=0, width=465, height=150)

        # background image
        img4 = Image.open(r"Images/bg.png")
        img4 = img4.resize((1400, 609), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=150, width=1400, height=609)

        title_lbl = Label(bg_img, text="Face Recognition App",
                          font=("Algerian", 35, "bold"), fg="green")
        title_lbl.place(x=0, y=0, width=1395, height=45)  # using .place u can place things at any part of the window


        # student button

        btn1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("Algerian", 20, "bold"),
                        bg="darkblue", fg="white")
        btn1_1.place(x=100, y=230, width=300, height=150)

        # Face Detection button
   
        btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("Algerian", 20, "bold"),
                        bg="darkblue", fg="white")
        btn2_2.place(x=900, y=230, width=300, height=150)

        

        # Help Desk button
    
        btn4_4 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.helpp, font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
        btn4_4.place(x=1195, y=2, width=195, height=40)


        # about us button
        btn5_5 = Button(bg_img, text="About US", cursor="hand2",command=self.AboutUs, font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
        btn5_5.place(x=5, y=2, width=195, height=40)

        # Exit button
        
        btn6_6 = Button(bg_img, text="Exit",command=self.iexit,cursor="hand2", font=("Algerian", 20, "bold"),
                        bg="darkblue", fg="white")
        btn6_6.place(x=520, y=350, width=300, height=150)


    def open_img(self):
        os.startfile("data")

    # =================================== Functions =========================================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student_readonly(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)  
 
    def helpp(self):
        self.new_window = Toplevel(self.root)
        self.app=help(self.new_window)

    def AboutUs(self):
        self.new_window = Toplevel(self.root)
        self.app=About_US(self.new_window)
    
    
     

# .................exit button
    def iexit(self):
        speak_va("Are you sure you want to exit this project?")
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return





                                                                                                 
if __name__ == "__main__":
    main()
    root= Tk()
    app=login_window(root)
    root.mainloop()
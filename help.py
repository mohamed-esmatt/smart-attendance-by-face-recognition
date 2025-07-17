from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog


class help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition App")
        self.root.resizable(0,0)

        title_lbl=Label(self.root,text="Help",font=("Algerian",20,"bold"),bg="lightblue",fg="blue")
        title_lbl.place(x=0,y=0,width=1280,height=50)

        # bg image
        bg=Image.open(r"Images\information.jpg")
        bg = bg.resize((1280, 720),Image.ANTIALIAS)
        self.photobg=ImageTk.PhotoImage(bg)

        n_lbl=Label(self.root,image=self.photobg)
        n_lbl.place(x=0,y=50,width=1280,height=720)
        self.bg_frame = Frame(self.root, bg='#040405', width=980, height=620)
        self.bg_frame.place(x=150, y=75)
        self.txt = "Getting around"
        self.heading = Label(self.bg_frame, text=self.txt, font=('Times New Roman', 40, "bold"), bg="#040405",
                             fg='light blue',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=325, y=30, width=350, height=60)

        img_createAcc = Image.open(r"Images\Sign Up.png")
        img_createAcc=img_createAcc.resize((250, 150),Image.ANTIALIAS)
        self.photoimg_name=ImageTk.PhotoImage(img_createAcc)
        createAcc_lbl=Label(self.root,image=self.photoimg_name,bg="black")
        createAcc_lbl.place(x=200,y=225,width=250,height=150)
        createAcc_lbl=Label(self.root,text="1. First create Account",font=("yu gothic ui",10,"italic"),bg="black",fg="lightblue")
        createAcc_lbl.place(x=200,y=375,width=150,height=40)

        img_login = Image.open(r"Images\Login.png")
        img_login=img_login.resize((250, 150),Image.ANTIALIAS)
        self.photoimg_lin=ImageTk.PhotoImage(img_login)
        login_lbl=Label(self.root,image=self.photoimg_lin,bg="black")
        login_lbl.place(x=800,y=225,width=250,height=150)
        login_lbl=Label(self.root,text="2. Then login",font=("yu gothic ui",10,"italic"),bg="black",fg="lightblue")
        login_lbl.place(x=800,y=375,width=100,height=40)

        img_face = Image.open(r"Images\face rec.png")
        img_face=img_face.resize((250, 150),Image.ANTIALIAS)
        self.photoimg_face=ImageTk.PhotoImage(img_face)
        face_lbl=Label(self.root,image=self.photoimg_face,bg="black")
        face_lbl.place(x=200,y=480,width=250,height=150)
        face_lbl=Label(self.root,text="3. Start Viewing Students",font=("yu gothic ui",10,"italic"),bg="black",fg="lightblue")
        face_lbl.place(x=200,y=630,width=150,height=40)

        img_forget = Image.open(r"Images\Forget password.png")
        img_forget=img_forget.resize((250, 150),Image.ANTIALIAS)
        self.photoimg_forget=ImageTk.PhotoImage(img_forget)
        forget_lbl=Label(self.root,image=self.photoimg_forget,bg="black")
        forget_lbl.place(x=800,y=480,width=250,height=150)
        forget_lbl=Label(self.root,text="4. Incase Password Forgotten ",font=("yu gothic ui",10,"italic"),bg="black",fg="lightblue")
        forget_lbl.place(x=800,y=630,width=200,height=40)





        
if __name__ == "__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()

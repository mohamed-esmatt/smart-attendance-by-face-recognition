from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog


class About_US:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition App")
        self.root.resizable(0,0)

        title_lbl=Label(self.root,text="About US",font=("Algerian",20,"bold"),bg="lightblue",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1280,height=50)

        # bg image
        bg=Image.open(r"Images\aboutus.png")
        bg = bg.resize((1280, 720),Image.ANTIALIAS)
        self.photobg=ImageTk.PhotoImage(bg)

        n_lbl=Label(self.root,image=self.photobg)
        n_lbl.place(x=0,y=50,width=1280,height=720)
        self.bg_frame = Frame(self.root, bg='#040405', width=980, height=620)
        self.bg_frame.place(x=150, y=75)
        self.txt = "Contact Us"
        self.heading = Label(self.bg_frame, text=self.txt, font=('Times New Roman', 40, "bold"), bg="#040405",
                             fg='light blue',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=325, y=30, width=300, height=60)

        img_name = Image.open(r"Images\profile.png")
        img_name=img_name.resize((40, 40),Image.ANTIALIAS)
        self.photoimg_name=ImageTk.PhotoImage(img_name)
        n_lbl=Label(self.root,image=self.photoimg_name,bg="black")
        n_lbl.place(x=200,y=300,width=40,height=40)
        n_lbl=Label(self.root,text="Mohamed esmat, Mohamed Wael, Kerolos karem,Moaz Gamal",font=("yu gothic ui",20,"italic"),bg="black",fg="lightblue")
        n_lbl.place(x=240,y=300,width=750,height=40)

        img_lin = Image.open(r"Images\Linkedin.png")
        img_lin=img_lin.resize((50, 50),Image.ANTIALIAS)
        self.photoimg_lin=ImageTk.PhotoImage(img_lin)
        lin_lbl=Label(self.root,image=self.photoimg_lin,bg="black")
        lin_lbl.place(x=196,y=400,width=50,height=50)
        lin_lbl=Label(self.root,text="linkedin.com/in/mohamed-al-gamal-9a6b34266",font=("yu gothic ui",20,"italic"),bg="black",fg="lightblue")
        lin_lbl.place(x=250,y=400,width=600,height=40)

        img_mail = Image.open(r"Images\mail.png")
        img_mail=img_mail.resize((40, 40),Image.ANTIALIAS)
        self.photoimg_mail=ImageTk.PhotoImage(img_mail)
        mail_lbl=Label(self.root,image=self.photoimg_mail,bg="black")
        mail_lbl.place(x=203,y=500,width=40,height=40)
        mail_lbl=Label(self.root,text="mohamed.esmat75@gmail.com",font=("yu gothic ui",20,"italic"),bg="black",fg="lightblue")
        mail_lbl.place(x=250,y=500,width=400,height=40)




        
if __name__ == "__main__":
    root=Tk()
    obj=About_US(root)
    root.mainloop()

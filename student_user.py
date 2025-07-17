
from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class Student_readonly:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x720+0+0")
        self.root.title("ITAFR")
        self.root.resizable(0,0)

        ##### Variables  #####
        self.var_major=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_face_id=StringVar()
        self.var_std_name=StringVar()
        self.var_sec=StringVar()
        self.var_std_id=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_gpa=StringVar()
        self.var_teacher=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()
       

   
        img2 = Image.open("Images/re1.jpg")
        img2 = img2.resize((1400,100),Image.ANTIALIAS)  #Antialias 
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0, y=0,width=1400,height=100)   
 #Background image 
        img3 = Image.open("Images/face.jpg")
        img3 = img3.resize((1530,730),Image.ANTIALIAS)  #Antialias 
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=130,width=1530,height=730)
        title_lbl=Label(text="STUDENT DETAIL'S",font=("Algerian",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0, y=80, width=1400,height=70)
        main_frame=Frame(bg_img,bd=2,bg="white",)
        main_frame.place(x=20,y=35,width=1345,height=530)

 #label frame
        center_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail's",font=("Algerian",12,"bold"))
        center_frame.place(x=0,y=5,width=1335,height=515)
        img_right = Image.open("images/helwan.jpg")
        img_right = img_right.resize((650,75),Image.ANTIALIAS)  #Antialias 
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        img_left = Image.open("Images/Helwan logo.jpg")
        img_left = img_left.resize((660,100),Image.ANTIALIAS)  #Antialias 
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(center_frame,image=self.photoimg_right)
        f_lbl.place(x=0, y=0,width=670,height=75)
        f_lbl=Label(center_frame,image=self.photoimg_left)
        f_lbl.place(x=665, y=0,width=665,height=75)


##Search System
        search_frame=LabelFrame(center_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Algerian",12,"bold"))
        search_frame.place(x=5,y=75,width=1400,height=70)
        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",13,"bold"),state="readonly",width=11)
        search_combo["values"]=("Select","StdID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        search_entry=ttk.Entry(search_frame,textvariable=self.var_searchtxt,width=17,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        search_btn=Button(search_frame,text="Search",command=self.search_data,width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        showAll_btn=Button(search_frame,text="Show All",width=10,command=self.show_all,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)



#Table frame
        table_frame=Frame(center_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=150,width=1320,height=350)


#scroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("major","course","year","sem","face_id","name","sec","std_id","gender","dob","email","phone","gpa","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("major",text="Major")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("face_id",text="FaceID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("std_id",text="StdID") 
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("gpa",text="GPA")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("name",width=100)
         
        self.student_table.column("std_id",width=100)
        self.student_table.column("major",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("gpa",width=100)
        self.student_table.column("course",width=100)    
        self.student_table.column("sem",width=100)
        self.student_table.column("face_id",width=100) 
        self.student_table.column("gender",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)     
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)        
        self.fetch_data()




######======Fetch data ==============#####
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#=================== get cursor ======================#
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_major.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]), 
        self.var_semester.set(data[3]),
        self.var_face_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_sec.set(data[6]),  
        self.var_std_id.set(data[7]),     
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_gpa.set(data[12]),      
        self.var_teacher.set(data[13]),
        self.var_photo_stat.set(data[14])
        
                 
     # search data     
    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select Option":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="data")               
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_search.get())+" LIKE '%"+str(self.var_searchtxt.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        speak_va("Data Not Found")
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                speak_va("An Exception Occurred!")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

            # show all 
    def show_all(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="data")       
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


           



            

                


           



if __name__=="__main__":
    root=Tk()
    obj=Student_readonly(root)
    root.mainloop()









from logging import root
from os import SEEK_CUR, close
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import datetime  
from time import strptime
import re
from tkcalendar import DateEntry
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x720+0+0")
        self.root.title("Face recognition app")
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
       

        StatisticsCS =["Select Course","data base","software eng","system analysis","special course","R","measure theory"]
        MathsCS=["Select Course","measure theory","data base","software eng","system analysis","modiling and simulation"]
        PhysicsCS=["Select Course","quantum phy","data base","software eng","system analysis","modiling and simulation"]
        SpecialMaths=["Select Course","measure teary","difrintial equations","special functins","relativity","mechanics"]

      #choose major
        def pick_major(e):
         if major_combo.get() == "Statistics & CS":
            course_combo.config(value=StatisticsCS)
            course_combo.current(0)
         elif major_combo.get() == "Maths & CS":
            course_combo.config(value=MathsCS)
            course_combo.current(0)
         elif major_combo.get() == "Physics & CS":
            course_combo.config(value=PhysicsCS)
            course_combo.current(0)
         elif major_combo.get() == "Special Maths":
            course_combo.config(value=SpecialMaths)
            course_combo.current(0)
         else:
           course_combo["values"]=("Select Course")
           course_combo.current(0)




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

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail's",font=("Algerian",12,"bold"))
        left_frame.place(x=5,y=5,width=670,height=515)
        img_left = Image.open("Images/Helwan logo.jpg")
        img_left = img_left.resize((660,100),Image.ANTIALIAS)  #Antialias 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0,width=660,height=70)

     #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=75,width=660,height=115)

    #Major
        major_label=Label(current_course_frame,text="Major",font=("times new roman",13,"bold"),bg="white")
        major_label.grid(row=0,column=0,padx=10,sticky=W)
        major_combo=ttk.Combobox(current_course_frame,textvariable=self.var_major,font=("times new roman",13,"bold"),state="readonly",width=18)
        major_combo["values"]=("Select Major","Statistics & CS","Maths & CS","Physics & CS","Special Maths")
        major_combo.current(0)
        major_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        major_combo.bind("<<ComboboxSelected>>",pick_major)

    #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=18)
        course_combo["values"]=("Select Course","data base","software eng","system analysis","special course","R","measure theory","modiling and simulation")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


    #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=18)
        year_combo["values"]=("Select Year","First","Second","Third","Fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


    #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=18)
        semester_combo["values"]=("Select Semester","1","2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


     #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=190,width=660,height=320)


     #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=0,padx=10,sticky=W)
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=18,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=1,padx=10,sticky=W)

     # call back and validation
        validate_name=self.root.register(self.checkname)
        studentName_entry.config(validate='key',validatecommand=(validate_name,'%P'))


     #StdID
        StdID_label=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        StdID_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        StdID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",13,"bold"))
        StdID_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        validate_StdID=self.root.register(self.checkS_ID)
        StdID_entry.config(validate='key',validatecommand=(validate_StdID,'%P'))



    #Face ID 
        FaceId_label=Label(class_student_frame,text="Face ID:",font=("times new roman",13,"bold"),bg="white")
        FaceId_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        FaceId_entry=ttk.Entry(class_student_frame,textvariable=self.var_face_id,width=18,font=("times new roman",13,"bold"))
        FaceId_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        validate_id=self.root.register(self.checkF_ID)
        FaceId_entry.config(validate='key',validatecommand=(validate_id,'%P'))
        




                
    #section
        section_label=Label(class_student_frame,text="Section:",font=("times new roman",13,"bold"),bg="white")
        section_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        sec_combo=ttk.Combobox(class_student_frame,textvariable=self.var_sec,font=("times new roman",13,"bold"),state="readonly",width=16)
        sec_combo["values"]=("Select Section","1","2","3","4","5")
        sec_combo.current(0)
        sec_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

    

    #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=16)
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


    #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        cal = DateEntry(class_student_frame,textvariable=self.var_dob, width=23, year=2000, month=1, day=1, 
         background='darkblue', foreground='white', borderwidth=2)
        cal.grid(row=2,column=3,padx=10, pady=10)
      
       
        
    #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        email=Label(class_student_frame,text="*ex123@gmail.com",font=("times new roman",6,"bold"),fg="red",bg="white")
        email.place(x=150, y=149)
        

       
    #Phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        validate_phone=self.root.register(self.checkphone)
        phone_entry.config(validate='key',validatecommand=(validate_phone,'%P'))
    
   

    #GPA
        GPA_label=Label(class_student_frame,text="GPA:",font=("times new roman",13,"bold"),bg="white")
        GPA_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        GPA_entry=ttk.Entry(class_student_frame,textvariable=self.var_gpa,width=18,font=("times new roman",13,"bold"))
        GPA_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        validate_GPA=self.root.register(self.checkgpa)
        GPA_entry.config(validate='key',validatecommand=(validate_GPA,'%P'))
    

    

    #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=18,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        validate_Teacher=self.root.register(self.checkTeachername)
        teacher_entry.config(validate='key',validatecommand=(validate_Teacher,'%P'))

      
    
    #Photo Status
        self.var_photo_stat=StringVar()
        photo_yes=ttk.Radiobutton(class_student_frame,variable=self.var_photo_stat,text="Take Photo Sample",value="Yes")
        photo_yes.grid(row=5,column=0)
        photo_no=ttk.Radiobutton(class_student_frame,variable=self.var_photo_stat,text="No Photo Sample",value="NO")
        photo_no.grid(row=5,column=1)

    #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=215,width=655,height=80)
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)   
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)       
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

    #frame for take photo and update photo
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=655,height=80)
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=65,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

       

 #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail's",font=("Algerian",12,"bold"))
        right_frame.place(x=680,y=5,width=650,height=515)
        img_right = Image.open("Images/helwan.jpg")
        img_right = img_right.resize((650,75),Image.ANTIALIAS)  #Antialias 
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5, y=0,width=640,height=75)


##Search System
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Algerian",12,"bold"))
        search_frame.place(x=5,y=75,width=640,height=70)
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
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=150,width=640,height=350)


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


# call back sytem

#check name
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            speak_va('Error! Name Not allowed.')
            messagebox.showerror('Erorr','Not allowed' +name[-1])
    def checkname(self,name):
       for char in name:
           if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
       return True
   #check gpa
    
    def checkgpa(self,GPA):   
       if len(GPA) <=4:
            for i in GPA:
              if  not (('0' <= i and i <= '9') or (i == '.')):
                 return False 
            return True
         
       else:
          speak_va('Invalid GPA')
          messagebox.showerror('Error','Invalid GPA. Please Enter Valid GPA. (example:4.0)')
          return False 
                   
            
    def checkTeachername(self,name):
       for char in name:
           if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
       return True
       

    # # checkphone number

    def checkphone(self,phone):
        if len(phone) <=11:
          if phone.isdigit():
            return True
          if len(str(phone))==0:
            return True
          else:
              speak_va('Invalid phone number Format')
              messagebox.showerror('Error','Invalid entry. Please Enter Valid Phone No. (example:01000000099)')
              return False
            
        else:
            speak_va('Alert!!! Invalid Phone Number')
            messagebox.showwarning('Alert','Invalid Number. Please Enter 11 Digits (example:01000000099)')
            return False

    #     # FaceID Check 
    def checkF_ID(self,F_ID):
        if len(F_ID) <=5:
          if F_ID.isdigit():
            return True
          if len(str(F_ID))==0:
            return True
          else:
              speak_va('Invalid Face ID. Please enter ID as integer value')
              messagebox.showerror('Error','Invalid entry. Please enter ID as integer value (example: ID :- 1 2 3 4 5 6 7...)')
              return False
        else:
            speak_va('Invalid ID.')
            messagebox.showwarning('Error','invalid ID. Please Enter valid ID.')
            return False

    #     # StdID validation
    def checkS_ID(self,S_ID):
        if len(S_ID) <=10:
          if S_ID.isdigit():
            return True
          if len(str(S_ID))==0:
            return True
          else:
             speak_va('Invalid Student ID Format. Please Enter a valid ID.')
             messagebox.showerror('Error','Invalid ID please enter Student ID in Valid Format (example: StdID No: 1951710001)')
             return False
        else:
            speak_va('Invalid Student ID.')
            messagebox.showwarning('Error','invalid Student ID. Please Enter Valid ID (example: StdID No: 1951710001)')
            return False
   

    




####function decleration ######
    def add_data(self):
        if self.var_major.get()=="Select Major" or self.var_std_name.get()=="" or self.var_face_id.get()=="":
            speak_va("Alert!!! All Fields are Mandatory.")
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)

        elif not ("@" or ".com") in self.var_email.get():
            speak_va('Try valid email address!!')
            messagebox.showerror("Error",'Invalid email Enter valid email like student@gmail.com ',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="data")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                                self.var_major.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_face_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_sec.get(), 
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_gpa.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_photo_stat.get()


                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                speak_va('Student Details has been added successfully.')
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                speak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


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


#============= Update function =========================

    def update_data(self):
        if self.var_major.get()=="Select Major" or self.var_std_name.get()=="" or self.var_face_id.get()=="":
            speak_va('Alert!!! All fields are required.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)

        else:
            try:
                speak_va("Do you want to Update this Student's Details?")
                Update = messagebox.askyesno("Update","Do You Want To Update This Student Details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="data")                   
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Major=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,StdID=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,GPA=%s,Teacher=%s,PhotoSample=%s where FaceID=%s",(

                                                                                                                                                                                        self.var_major.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_sec.get(),    
                                                                                                                                                                                        self.var_std_id.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_gpa.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_photo_stat.get(),
                                                                                                                                                                                        self.var_face_id.get()
                                                                                                                                                                                    ))   
                
                
                else:
                    if not Update:
                        return
                speak_va('Student Details updated successfully.')
                messagebox.showinfo("Success","Student Details updated Successfully.",parent=self.root)                                                                                                                                              
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
               speak_va('An Exception Occurred!')
               messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



# ===================Delete Function===================
    def delete_data(self):
        if self.var_face_id.get()=="":           
            messagebox.showerror("Error","Face Id Required",parent=self.root)
        else:
            try:
                speak_va("Do you want to Delete this Student's Details?")
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student Details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="data")                   
                    my_cursor=conn.cursor()
                    sql="delete from student where FaceID=%s"
                    val=(self.var_face_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                speak_va('Student Details deleted successfully.')
                messagebox.showinfo("Delete","Student Details Successfully deleted",parent=self.root)

            except Exception as es:
                speak_va('An exception occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#============Reset Function =============================
    def reset_data(self):
        self.var_major.set("Select Major")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_face_id.set("")
        self.var_std_name.set("")
        self.var_sec.set("Select Section")
        self.var_std_id.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_gpa.set("")
        self.var_teacher.set("")
        self.var_photo_stat.set("")

# ..............Generate data set or take photo sample

    def generate_dataset(self):
        if (self.var_major.get()=="Select Major" 
            or self.var_course.get()=="Select Course" 
            or self.var_year.get()=="Select Year" 
            or self.var_semester.get()=="Select Semester" 
            or self.var_sec.get()=="Select Section" 
            or self.var_gender.get()=="Select Gender"  
            or self.var_std_name.get()=="" 
            or self.var_face_id.get()==""
            or self.var_std_id.get()==""
            or self.var_dob.get()==""
            or self.var_email.get()==""
            or self.var_email.get()==""
            or self.var_phone.get()==""
            or self.var_gpa.get()==""
            or self.var_teacher.get()==""
            or self.var_photo_stat.get()==""
           ):
            speak_va('All Fields are mandatory.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="data")               
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Major=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,StdID=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,GPA=%s,Teacher=%s,PhotoSample=%s where FaceID=%s",(

                                                                                                                                                                                        self.var_major.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_sec.get(),
                                                                                                                                                                                        self.var_std_id.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_gpa.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_photo_stat.get(),
                                                                                                                                                                                        self.var_face_id.get()==id+1
                                                                                                                                                                                    ))   
                conn.commit()
                self.fetch_data()
                conn.close()

                # ..................load predefined data  face forntal from opencv.............
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)             


                
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/"+"user"+"."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==150:
                        break
                cap.release()
                cv2.destroyAllWindows()

                speak_va("Generation of Data Set completed.")
                messagebox.showinfo("Result","Generation of data set completed!!!",parent=self.root)
            except Exception as es:
                speak_va("An Exception occurred")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                

               
                
            


     # search data     
    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
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
    obj=Student(root)
    root.mainloop()








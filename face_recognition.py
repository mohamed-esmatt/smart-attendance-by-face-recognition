from ntpath import join

from pyttsx3 import speak

from student import Student
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re
import os
import numpy as np
from time import strftime
from datetime import datetime, timedelta
import cv2 as cv
import pyttsx3
from os.path import isfile,join
from os import listdir
import time
import pandas as pd
import csv
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()





class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition App")
        self.root.resizable(0,0)
        self.attendance_times={}

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Algerian",20,"bold"),bg="white",fg="blue",anchor="center")
        title_lbl.place(x=0,y=0,width=1280,height=70)

        # bg image
        img_bottom=Image.open(r"Images\frec.png")
        img_bottom = img_bottom.resize((1700, 650),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=70,width=1280,height=650)
        
        # Button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Algerian",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=400,y=250,width=300,height=150)

        

    #############Atendance############


    
    def mark_attendance(self,n,i,d,r):
        if n == "None" or i == "None" or d == "None" or r == "None":
         return
        now = datetime.now()
        if i in self.attendance_times and now - self.attendance_times[i] < timedelta(minutes=5):
            return
        with open("attendance deatails.csv","r+" , newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in  myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            
            if((i not in name_list) and (n not in name_list) and (d not in name_list)and (r not in name_list)):
               now=datetime.now()
               d1=now.strftime("%d/%m/%Y") 
               dtString=now.strftime("%H:%M:%S")
               f.writelines(f"\n{i},{n},{d},{r},{dtString},{d1} , present")
               self.attendance_times[i] = now



        #############face recognation #############3


                
    def face_recog(self):
        
        

        

        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)   

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h+20,x:x+w+20])
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="data")
                my_cursor=conn.cursor()
                my_cursor.execute("select Name from student where FaceID = "+str(id))
                n = my_cursor.fetchone()
                n = str(n)
                my_cursor.execute("select GPA from student where FaceID = "+str(id))
                r=my_cursor.fetchone()
                r = str(r)
                my_cursor.execute("select Year from student where FaceID = "+str(id))
                d=my_cursor.fetchone()
                d = str(d)
                my_cursor.execute("select StdID from student where FaceID = "+str(id))
                i=my_cursor.fetchone()
                i = str(i)

                
 
                
                # accuracy calculation

                if predict < 500:
                    confidence=int((100*(1-predict/300)))
                    cv2.putText(img,f"Accuracy:{confidence}%",(x, y-125), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)



                if confidence> 70:
                    cv2.putText(img,f"Name: {n}",(x,y-95),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ID:{i}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Year:{d}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"GPA:{r}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,i,d,r)

                    

                else:
                    cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[y+h,x+w]

            return coord 
        
        
            
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)   
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition App",img)


            if cv2.waitKey(1)==13:
                
                break
        video_cap.release()
        cv2.destroyAllWindows()

       


        



        




        

                    
                      




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()

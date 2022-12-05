from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.title("Tải Dữ Liệu")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\banner2.png")
        img=img.resize((1220,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1280,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\bg-traindata2.jpg")
        bg1=bg1.resize((1250,500),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=145,width=1280,height=500)


        #title section
        title_lb1 = Label(bg_img,text="VKU - Tải dữ liệu gương mặt",font=("verdana",20,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1280,height=40)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\t_btn1.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        """ std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180) """ 

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Tải Dữ Liệu",cursor="hand2",font=("tahoma",15,"bold"),bg="navyblue",fg="white")
        std_b1_1.place(x=230,y=430,width=250,height=40)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            """ cv2.resize(imageNp,(500,500)) """
            faces.append(imageNp)
            ids.append(id)
            
            cv2.imshow("Train Data",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Kết quả","Tải dữ liệu thành công!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")
        
# This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\banner2.png")
        img=img.resize((1280,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1280,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\bg4.jpg")
        bg1=bg1.resize((1280,500),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=145,width=1280,height=500)


        #title section
        title_lb1 = Label(bg_img,text="VKU - Thông tin nhà phát triển",font=("verdana",20,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1280,height=40)


        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        
        att_img_btn=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\phong.jpg")
        att_img_btn=att_img_btn.resize((250,250),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=350,y=120,width=250,height=250)

        att_b1_1 = Button(bg_img,text="Nguyễn Thanh Phong",cursor="hand2",font=("tahoma",10,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=350,y=370,width=250,height=50)


        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=600,y=120,width=400,height=300)
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Thông tin nhà phát triển",font=("verdana",10,"bold"),fg="navyblue")
        right_frame.place(x=7,y=7,width=380,height=280)

        #label Name
        name_label=Label(right_frame,text="Họ tên:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        name_label.grid(row=0,column=0,padx=5,pady=12)
        #Name
        name=Label(right_frame,text="Nguyễn Thanh Phong",font=("verdana",12),bg="white")
        name.grid(row=0,column=1,padx=5,pady=12,sticky=W)
        
        #label ID
        idstd_label=Label(right_frame,text="Mã Sinh viên:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        idstd_label.grid(row=1,column=0,padx=5,pady=12)
        #ID
        idstd=Label(right_frame,text="20IT735",font=("verdana",12),bg="white")
        idstd.grid(row=1,column=1,padx=5,pady=12,sticky=W)

        #label class
        classStd_label=Label(right_frame,text="Lớp sinh hoạt:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        classStd_label.grid(row=2,column=0,padx=5,pady=12)
        #class
        classStd=Label(right_frame,text="20SE2",font=("verdana",12),bg="white")
        classStd.grid(row=2,column=1,padx=5,pady=12,sticky=W)

        #label phone
        phone_label=Label(right_frame,text="Di động:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        phone_label.grid(row=3,column=0,padx=5,pady=12)
        #phone
        phone=Label(right_frame,text="0934.404.954",font=("verdana",12),bg="white")
        phone.grid(row=3,column=1,padx=5,pady=12,sticky=W)

        #label email
        email_label=Label(right_frame,text="Email:",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        email_label.grid(row=4,column=0,padx=5,pady=12)
        #email
        email=Label(right_frame,text="ntphong.20it12@vku.udn",font=("verdana",12),bg="white")
        email.grid(row=4,column=1,padx=5,pady=12,sticky=W)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
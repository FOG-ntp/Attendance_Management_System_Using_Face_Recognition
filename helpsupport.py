from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpsupport:
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
        bg1=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\bg1.jpg")
        bg1=bg1.resize((1280,500),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=145,width=1280,height=500)


        #title section
        title_lb1 = Label(bg_img,text="VKU - Hỗ trợ",font=("verdana",20,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1280,height=40)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\web.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=210,y=160,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=210,y=340,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\fb.png")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=440,y=160,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=440,y=340,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\yt.png")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=670,y=160,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=670,y=340,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"D:\VKU\DoAnCoSo4\Attendance_Management_System_Using_Face_Recognition\Images_GUI\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=900,y=160,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=900,y=340,width=180,height=45)


        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = "https://github.com/FOG-ntp"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/ntphong.2901/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()
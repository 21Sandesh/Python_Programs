from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from Student import Student
import os
from train import Train
from facerecognition import Facerecognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Background Image
        backimg = Image.open(
            r"D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\Images\Background.jpeg")
        backimg = backimg.resize((1530, 790), Image.Resampling.LANCZOS)
        self.backgorundimage = ImageTk.PhotoImage(backimg)

        backgroundlabel = Label(self.root, image=self.backgorundimage)
        backgroundlabel.place(x=0, y=0, width=1530, height=790)

        titleLabel = Label(backgroundlabel, text="Face Recognition System", font=(
            "times new roman", 30, "bold"), bg="white", fg="black")
        titleLabel.place(x=0, y=0, width=1530, height=45)

        # Student
        studentimg = Image.open(
            r"D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\Images\Student.jpeg")
        studentimg = studentimg.resize((220, 220), Image.Resampling.LANCZOS)
        self.studentimg = ImageTk.PhotoImage(studentimg)

        Studentbutton = Button(
            backgroundlabel, image=self.studentimg, command=self.StudentDetails, cursor="hand2")
        Studentbutton.place(x=200, y=100, width=220, height=220)

        Studentbutton1 = ttk.Button(
            backgroundlabel, text="Student Details", command=self.StudentDetails, cursor="hand2")
        Studentbutton1.place(x=200, y=320, width=220, height=40)

        # Detect Face
        detectimg = Image.open(
            r"D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\Images\Detect.jpg")
        detectimg = detectimg.resize((220, 220), Image.Resampling.LANCZOS)
        self.detectimg = ImageTk.PhotoImage(detectimg)

        Studentbutton = Button(
            backgroundlabel, image=self.detectimg, cursor="hand2", command=self.facedata)
        Studentbutton.place(x=500, y=100, width=220, height=220)

        Studentbutton1 = ttk.Button(
            backgroundlabel, text="Detect Face", cursor="hand2", command=self.facedata)
        Studentbutton1.place(x=500, y=320, width=220, height=40)

        # Attendance
        attendanceimg = Image.open(
            r"D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\Images\Attendance.png")
        attendanceimg = attendanceimg.resize((220, 220), Image.Resampling.LANCZOS)
        self.attendanceimg = ImageTk.PhotoImage(attendanceimg)

        Studentbutton = Button(
            backgroundlabel, image=self.attendanceimg, cursor="hand2")
        Studentbutton.place(x=800, y=100, width=220, height=220)

        Studentbutton1 = ttk.Button(
            backgroundlabel, text="Attendance", cursor="hand2")
        Studentbutton1.place(x=800, y=320, width=220, height=40)

        # Images Frame
        imagesframeimg = Image.open(
            r"D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\Images\Frame.jpg")
        imagesframeimg = imagesframeimg.resize((220, 220), Image.Resampling.LANCZOS)
        self.imagesframeimg = ImageTk.PhotoImage(imagesframeimg)

        imagesframebutton = Button(
            backgroundlabel, image=self.imagesframeimg, cursor="hand2", command=self.openimages)
        imagesframebutton.place(x=500, y=450, width=220, height=220)

        imagesframebutton1 = ttk.Button(
            backgroundlabel, text="Images", cursor="hand2", command=self.openimages)
        imagesframebutton1.place(x=500, y=670, width=220, height=40)

        #Train Data
        traindataframeimg = Image.open(
            r"D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\Images\Frame.jpg")
        traindataframeimg = imagesframeimg.resize((220, 220), Image.Resampling.LANCZOS)
        self.traindataframeimg = ImageTk.PhotoImage(traindataframeimg)

        traindataframebutton = Button(
            backgroundlabel, image=self.traindataframeimg, cursor="hand2", command=self.traindata)
        traindataframebutton.place(x=200, y=450, width=220, height=220)

        traindataframebutton1 = ttk.Button(
            backgroundlabel, text="Train Data", cursor="hand2", command=self.traindata)
        traindataframebutton1.place(x=200, y=670, width=220, height=40)


#////////////////////////#

# Function Buttons


    def StudentDetails(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def openimages(self):
        os.startfile("imagedataset")

    def traindata(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def facedata(self):
        self.new_window = Toplevel(self.root)
        self.app = Facerecognition(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

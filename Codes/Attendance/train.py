from email import message
from socketserver import StreamRequestHandler
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np


class Train:
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

        titleLabel = Label(self.root, text="Train Data Set", font=(
            "times new roman", 30, "bold"), bg="white", fg="black")
        titleLabel.place(x=0, y=0, width=1530, height=45)

        #Buttonbutton1
        trainbutton = ttk.Button(self.root, command=self.trainclassifier ,text = "Train Data",cursor="hand2")
        trainbutton.place(x=690, y = 380,height=60)
    
    #################################

    #Algorithm
    def trainclassifier(self):
        datadir=(r"D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\imagedataset")
        path=[os.path.join(datadir,file) for file in os.listdir(datadir)]

        faces=[]
        ids=[]
        conn = mysql.connector.connect(
            host="localhost", username="root", password="", database="")
        mycursor = conn.cursor()

        for image in path:
            img=Image.open(image).convert('L')   #Grayscale Image
            imagenp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train Classifier

        clf=cv2.face.LBPHFaceRecognizer_create() #Local Binary Pattern Histogram
        clf.train(faces,ids)
        clf.write("D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\classfied.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
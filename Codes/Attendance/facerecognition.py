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


class Facerecognition:
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

        titleLabel = Label(self.root, text="Face Recognition", font=(
            "times new roman", 30, "bold"), bg="white", fg="black")
        titleLabel.place(x=0, y=0, width=1530, height=45)

        facerecg = ttk.Button(
            backgroundlabel, text="Recognize Face", command=self.facerecogn, cursor="hand2")
        facerecg.place(x=200, y=400, width=200, height=40)

        ####################

        # Face Recognition

    def facerecogn(self):
        def drawboundry(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            grayimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                grayimage, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(grayimage[y:y+h, x:x+w])
                confidence = int((100*(1-(predict/300))))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="")
                mycursor = conn.cursor()

                mycursor.execute(
                    "select `Name` from student where `PRN`="+str(id))
                namevar = mycursor.fetchone()
                namevar = "".join(str(namevar))

                mycursor.execute(
                    "select `Roll` from student where `PRN`="+str(id))
                rollvar = mycursor.fetchone()
                rollvar = "".join(str(rollvar))

                mycursor.execute(
                    "select `PRN` from student where `PRN`="+str(id))
                PRNvar = mycursor.fetchone()
                PRNvar = "".join(str(PRNvar))

                if confidence > 70:
                    cv2.putText(img, f"Roll:{rollvar}", (x, y-55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(img, f"Name:{namevar}", (x, y-30),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(
                        img, f"PRN:{PRNvar}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = drawboundry(img, faceCascade, 1.1, 10,
                                (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create() #Local Binary Pattern Histogram
        clf.read(
            "D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\classfied.xml")

        videocap = cv2.VideoCapture(0)

        while True:
            ret, img = videocap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        videocap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Facerecognition(root)
    root.mainloop()

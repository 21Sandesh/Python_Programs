from email import message
from socketserver import StreamRequestHandler
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.vardepartment = StringVar()
        self.varcourse = StringVar()
        self.varyear = StringVar()
        self.varsemester = StringVar()
        self.varprn = StringVar()
        self.varname = StringVar()
        self.vardivision = StringVar()
        self.varrollnumber = StringVar()
        self.varemail = StringVar()
        self.varmobilenumber = StringVar()
        self.varguide = StringVar()

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

        main_frame = Frame(backgroundlabel, bd=2)
        main_frame.place(x=10, y=50, width=1520, height=700)

        # Left Label
        leftlabel = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        leftlabel.place(x=10, y=40, width=650, height=580)

        # Course Information
        courselabel = LabelFrame(leftlabel, bd=2, relief=RIDGE, text="Course Information", font=(
            "times new roman", 12, "bold"))
        courselabel.place(x=5, y=15, width=630, height=200)

        departmentlabel = Label(courselabel, text="Department", font=(
            "times new roman", 15, "bold"))
        departmentlabel.grid(row=0, column=0, padx=10)

        departmentcombo = ttk.Combobox(courselabel, textvariable=self.vardepartment, font=(
            "times new roman", 12, "bold"),  state="readonly")  # *#
        departmentcombo["values"] = (
            "Select Department", "Computer", "IT", "ENTC", "AI&DS", "Mechanical", "Indus & Prod", "Chemical", "Instrumentation")
        departmentcombo.current(0)
        departmentcombo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        Courselabel = Label(courselabel, text="Course", font=(
            "times new roman", 15, "bold"))
        Courselabel.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        coursecombo = ttk.Combobox(courselabel, textvariable=self.varcourse, font=(
            "times new roman", 13, "bold"), state="readonly")
        coursecombo["values"] = ("B-Tech")
        coursecombo.current(0)
        coursecombo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        yearlabel = Label(courselabel, text="Year",
                          font=("times new roman", 15, "bold"))
        yearlabel.grid(row=1, column=0, padx=20, pady=10, sticky=W)

        yearcombo = ttk.Combobox(courselabel, textvariable=self.varyear, font=(
            "times new roman", 12, "bold"), state="readonly")
        yearcombo["values"] = ("Select Year", "First",
                               "Second", "Third", "Fourth")
        yearcombo.current(0)
        yearcombo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semesterlabel = Label(courselabel, text="Semester", font=(
            "times new roman", 15, "bold"))
        semesterlabel.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        semestercombo = ttk.Combobox(courselabel, textvariable=self.varsemester, font=(
            "times new roman", 13, "bold"), state="readonly")
        semestercombo["values"] = (
            "Select Semester", "1", "2")
        semestercombo.current(0)
        semestercombo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student Information
        Studentlabel = LabelFrame(leftlabel, bd=2, relief=RIDGE, text="Student Information", font=(
            "times new roman", 12, "bold"))
        Studentlabel.place(x=5, y=220, width=630, height=320)

        # Student PRN
        Studentprnlabel = Label(Studentlabel, text="PRN:", font=(
            "times new roman", 12, "bold"))
        Studentprnlabel.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        Studentprnenrty = ttk.Entry(Studentlabel, textvariable=self.varprn, width=20, font=(
            "times new roman", 12, "bold"))
        Studentprnenrty.grid(row=0, column=1, padx=10, sticky=W)

        # Student Name
        Studentnamelabel = Label(Studentlabel, text="Name:", font=(
            "times new roman", 12, "bold"))
        Studentnamelabel.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        Studentnameentry = ttk.Entry(Studentlabel, textvariable=self.varname, width=20, font=(
            "times new roman", 12, "bold"))
        Studentnameentry.grid(row=0, column=3, padx=10, sticky=W)

        # Division
        Studentdivisionlabel = Label(Studentlabel, text="Division:", font=(
            "times new roman", 12, "bold"))
        Studentdivisionlabel.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        divisioncombo = ttk.Combobox(Studentlabel, textvariable=self.vardivision, font=(
            "times new roman", 10, "bold"), state="readonly")
        divisioncombo["values"] = (
            " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "S", "T")
        divisioncombo.current(0)
        divisioncombo.grid(row=1, column=1, padx=10, sticky=W)

        # Student Roll Number
        Studentrollnumberlabel = Label(Studentlabel, text="Roll Number:", font=(
            "times new roman", 12, "bold"))
        Studentrollnumberlabel.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        Studentrollnumberentry = ttk.Entry(Studentlabel, textvariable=self.varrollnumber, width=20, font=(
            "times new roman", 12, "bold"))
        Studentrollnumberentry.grid(row=1, column=3, padx=10, sticky=W)

        # Contact Details
        Studentmobilelabel = Label(Studentlabel, text="Mobile:", font=(
            "times new roman", 12, "bold"))
        Studentmobilelabel.grid(row=2, column=0, padx=2, pady=10, sticky=W)

        Studentmobileentry = ttk.Entry(Studentlabel, textvariable=self.varmobilenumber, width=20, font=(
            "times new roman", 12, "bold"))
        Studentmobileentry.grid(row=2, column=1, padx=10, sticky=W)

        Studentemaillabel = Label(Studentlabel, text="Email (vit.edu):", font=(
            "times new roman", 12, "bold"))
        Studentemaillabel.grid(row=2, column=2, padx=2, pady=10, sticky=W)

        Studentemailentry = ttk.Entry(Studentlabel,  textvariable=self.varemail, width=20, font=(
            "times new roman", 12, "bold"))
        Studentemailentry.grid(row=2, column=3, padx=10, sticky=W)

        # Guide Name
        Studentguidelabel = Label(Studentlabel, text="Guide Name:", font=(
            "times new roman", 12, "bold"))
        Studentguidelabel.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        Studentguideentry = ttk.Entry(Studentlabel, textvariable=self.varguide, width=20, font=(
            "times new roman", 12, "bold"))
        Studentguideentry.grid(row=3, column=2, padx=10, sticky=W)

        # # Radio Button
        # self.varradio1 = StringVar()

        # faceregister = Label(Studentlabel, text="Register Face: ", font=(
        #     "times new roman", 12, "bold"))
        # faceregister.grid(row=5, column=0)
        # radiobutton1 = ttk.Radiobutton(
        #     Studentlabel, variable=self.varradio1, text="Yes", value="Yes")
        # radiobutton1.grid(row=5, column=1)

        # radiobutton1 = ttk.Radiobutton(
        #     Studentlabel, variable=self.varradio1, text="No", value="No")
        # radiobutton1.grid(row=5, column=2)

        # Button Frame
        buttonframe = Frame(Studentlabel, bd=2, relief=RIDGE, bg="white")
        buttonframe.place(x=10, y=230, width=610, height=60)

        savebutton = ttk.Button(buttonframe, command=self.adddata, text="Save")
        savebutton.grid(row=0, column=0, padx=32, pady=15)

        updatebutton = ttk.Button(
            buttonframe, command=self.upadatedata, text="Update")
        updatebutton.grid(row=0, column=1, padx=32, pady=15)

        deletebutton = ttk.Button(
            buttonframe, command=self.deletedata, text="Delete")
        deletebutton.grid(row=0, column=2, padx=32, pady=15)

        resetbutton = ttk.Button(
            buttonframe, command=self.resetdata, text="Reset")
        resetbutton.grid(row=0, column=3, padx=32, pady=15)

        takephotobutton = ttk.Button(
            Studentlabel, command=self.generatedataset, text="Take Photo")
        takephotobutton.grid(row=3, column=3)

        updatephotobutton = ttk.Button(Studentlabel, text="Update Photo")
        updatephotobutton.grid(row=4, column=3)

        ##############################

        # Right Label
        rightlabel = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Search", font=(
            "times new roman", 12, "bold"))
        rightlabel.place(x=750, y=40, width=650, height=580)

        Searchlabel = LabelFrame(rightlabel, bd=2, relief=RIDGE, text="Search", font=(
            "times new roman", 12, "bold"))
        Searchlabel.place(x=5, y=15, width=630, height=70)

        searchlabel = Label(Searchlabel, text="Search By:", font=(
            "times new roman", 12, "bold"))
        searchlabel.grid(row=0, column=0, padx=0, pady=0, sticky=W)

        searchcombo = ttk.Combobox(Searchlabel, font=(
            "times new roman", 11, "bold"), state="readonly")
        searchcombo["values"] = ("Select", "PRN", "Roll Number")
        searchcombo.current(0)
        searchcombo.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        # Button
        Searchentry = ttk.Entry(Searchlabel, width=20, font=(
            "times new roman", 12, "bold"))
        Searchentry.grid(row=0, column=3, padx=10, sticky=W)

        Searchbutton = ttk.Button(Searchlabel, text="Search")
        Searchbutton.grid(row=0, column=4, padx=5, pady=5)

        Showallbutton = ttk.Button(Searchlabel, text="Show All")
        Showallbutton.grid(row=0, column=5, padx=5, pady=5)

        # Table Frame
        tableframe = Frame(rightlabel, bd=2, relief=RIDGE, bg="white")
        tableframe.place(x=5, y=90, width=630, height=460)

        xscroll = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(tableframe, orient=VERTICAL)

        self.datatable = ttk.Treeview(tableframe, columns=(
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        xscroll.config(command=self.datatable.xview)
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.datatable.yview)

        self.datatable.heading("1", text="PRN")
        self.datatable.heading("2", text="Student Name")
        self.datatable.heading("3", text="Roll No")
        self.datatable.heading("4", text="Div")
        self.datatable.heading("5", text="Department")
        self.datatable.heading("6", text="Sem")
        self.datatable.heading("7", text="Year")
        self.datatable.heading("8", text="Course")
        self.datatable.heading("9", text="Mobile")
        self.datatable.heading("10", text="Email")
        self.datatable.heading("11", text="Guide")
        self.datatable["show"] = "headings"

        self.datatable.column("1", width=70)
        self.datatable.column("2", width=110)
        self.datatable.column("3", width=50)
        self.datatable.column("4", width=40)
        self.datatable.column("5", width=110)
        self.datatable.column("6", width=50)
        self.datatable.column("7", width=50)
        self.datatable.column("8", width=60)
        self.datatable.column("9", width=90)
        self.datatable.column("10", width=170)
        self.datatable.column("11", width=100)

        self.datatable.pack(fill=BOTH, expand=1)
        self.datatable.bind("<ButtonRelease>", self.getcursor)
        self.fetchdata()

    #/*****************************/#

    def adddata(self):
        if self.vardepartment == "Select Department" or self.varname == " " or self.varprn == " ":
            messagebox.showerror(
                "Error,", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="")
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.varprn.get(),
                    self.varname.get(),
                    self.varrollnumber.get(),
                    self.vardivision.get(),
                    self.vardepartment.get(),
                    self.varsemester.get(),
                    self.varyear.get(),
                    self.varcourse.get(),
                    self.varmobilenumber.get(),
                    self.varemail.get(),
                    self.varguide.get()
                ))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student Details have been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # Fetch Data
    def fetchdata(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="", database="")
        mycursor = conn.cursor()
        mycursor.execute("select * from student")
        data = mycursor.fetchall()

        if len(data) != 0:
            self.datatable.delete(*self.datatable.get_children())
            for x in data:
                self.datatable.insert("", END, values=x)
            conn.commit()
        conn.close()

    # Get Cursor
    def getcursor(self, event=""):
        cursorfocus = self.datatable.focus()
        content = self.datatable.item(cursorfocus)
        data = content["values"]

        self.varprn.set(data[0]),
        self.varname.set(data[1]),
        self.varrollnumber.set(data[2]),
        self.vardivision.set(data[3]),
        self.vardepartment.set(data[4]),
        self.varsemester.set(data[5]),
        self.varyear.set(data[6]),
        self.varcourse.set(data[7]),
        self.varmobilenumber.set(data[8]),
        self.varemail.set(data[9]),
        self.varguide.set(data[10])

    # Update
    def upadatedata(self):
        if self.vardepartment == "Select Department" or self.varname == " " or self.varprn == " ":
            messagebox.showerror(
                "Error,", "All Fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Proceed?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="")
                    mycursor = conn.cursor()
                    mycursor.execute("UPDATE `studentdatabase`.`student` SET `PRN` = %s, `Name` = %s, `Roll` = %s, `Div` = %s, `Department` = %s, `Sem` = %s, `Year` = %s, `Course` = %s, `Mobile` = %s, `Email` = %s, `Guide` = %s WHERE (`PRN` = %s);", (
                        self.varprn.get(),
                        self.varname.get(),
                        self.varrollnumber.get(),
                        self.vardivision.get(),
                        self.vardepartment.get(),
                        self.varsemester.get(),
                        self.varyear.get(),
                        self.varcourse.get(),
                        self.varmobilenumber.get(),
                        self.varemail.get(),
                        self.varguide.get(),
                        self.varprn.get()
                    ))
                    conn.commit()
                    self.fetchdata()
                    conn.close()
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Details Updated", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # Delete
    def deletedata(self):
        if self.varprn.get() == "":
            messagebox.showerror("Error", "PRN is Required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Delete", "Proceed?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="", database="")
                    mycursor = conn.cursor()
                    sql = "delete from student where PRN=%s"
                    val = (self.varprn.get(),)
                    mycursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted Student Details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # Reset
    def resetdata(self):
        self.varprn.set(""),
        self.varname.set(""),
        self.varrollnumber.set(""),
        self.vardivision.set(""),
        self.vardepartment.set("Select Department"),
        self.varsemester.set("Select Semester"),
        self.varyear.set("Select Year"),
        self.varcourse.set("B-Tech"),
        self.varmobilenumber.set(""),
        self.varemail.set(""),
        self.varguide.set("")

##############################################

# Generate Data Set and Take Photo Sample
    def generatedataset(self):
        if self.vardepartment == "Select Department" or self.varname == " " or self.varprn == " ":
            messagebox.showerror(
                "Error,", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="")
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myresult = mycursor.fetchall()
                id = 0
                for x in myresult:
                    mycursor.execute("UPDATE `studentdatabase`.`student` SET `PRN` = %s, `Name` = %s, `Roll` = %s, `Div` = %s, `Department` = %s, `Sem` = %s, `Year` = %s, `Course` = %s, `Mobile` = %s, `Email` = %s, `Guide` = %s WHERE (`PRN` = %s);", (
                                     self.varprn.get(),
                                     self.varname.get(),
                                     self.varrollnumber.get(),
                                     self.vardivision.get(),
                                     self.vardepartment.get(),
                                     self.varsemester.get(),
                                     self.varyear.get(),
                                     self.varcourse.get(),
                                     self.varmobilenumber.get(),
                                     self.varemail.get(),
                                     self.varguide.get(),
                                     self.varprn.get() == id+1
                                     ))
                    id = self.varprn.get()
                    conn.commit()
                    self.fetchdata()
                    self.resetdata()
                    conn.close()

                    # Load Predefined Data on face frontal from openCV
                    faceclassifier = cv2.CascadeClassifier(
                        "haarcascade_frontalface_default.xml")

                    def cropface(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = faceclassifier.detectMultiScale(gray, 1.3, 5)

                        # Scaling Factor = 1.3
                        # Minimum Neighbour = 5

                        for (x, y, w, h) in faces:
                            cropface = img[y:y+h, x:x+w]
                            return cropface

                    cap = cv2.VideoCapture(0)
                    imgid = 0
                    while True:
                        ret, myframe = cap.read()
                        if cropface(myframe) is not None:
                            imgid += 1
                            face = cv2.resize(cropface(myframe), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            filenamepath = "D:\VIT Pune\SEM 2\CWP (Python)\Course Project\Attendance\imagedataset/user."+str(id)+"."+str(imgid)+".jpg"
                            cv2.imwrite(filenamepath, face)
                            cv2.putText(
                                face, str(imgid), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(imgid) == 100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo(
                        "Result", "Generating Data Set Successfull")

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

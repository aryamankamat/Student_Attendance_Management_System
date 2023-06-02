from tkinter import *
from Student_Details import Student
from train import Training
from Face_Recog import Face_Recognition
from attendance import Attendance
import os


class Face_Recognization_System:
    def __init__(self, root, show, train, face, attend, ext):
        self.root = root
        self.root.geometry("1300x650+0+0")
        self.root.title("face Recognition System")
        self.root.configure(bg='#e0bea0')

        # Title Label
        title_lbl = Label(self.root, text="Student Attendance Management System", font=("Forte", 35, "bold"),
                          bg="#e0bea0", fg="black")
        title_lbl.place(x=250, y=0)

        # Student Button
        b1 = Button(self.root, command=show, cursor="hand2", text="Student Details", font=("Times new Roman", 11, "bold"),
                    bg="#fc2847")
        b1.place(x=200, y=200, width=110, height=100)

        # Face Detection Button
        b2 = Button(self.root, cursor="hand2", command=face, text="Face Detector", font=("Times new Roman", 11, "bold"),
                    bg="#ffa343")
        b2.place(x=500, y=200, width=110, height=100)

        # Attendance Button
        b3 = Button(self.root, cursor="hand2", command=attend, text="Attendance", font=("Times new Roman", 11, "bold"),
                    bg="#fdfc74")
        b3.place(x=800, y=200, width=110, height=100)

        # Train Button
        b4 = Button(self.root, cursor="hand2", command=train, text="Training", font=("Times new Roman", 11, "bold"),
                    bg="#71bc78")
        b4.place(x=1100, y=200, width=110, height=100)

        # Photos Button
        b5 = Button(self.root, cursor="hand2", command=self.open_imag, text="T-Photos", font=("Times new Roman", 11, "bold"),
                    bg="#7442c8")
        b5.place(x=500, y=400, width=110, height=100)

        # Exit Button
        b6 = Button(self.root, command=ext, cursor="hand2", text="EXIT", font=("Times new Roman", 11, "bold"),
                    bg="#fb7efd")
        b6.place(x=800, y=400, width=110, height=100)

    def open_imag(self):
        os.startfile("data")


if __name__ == '__main__':
    root = Tk()

    # Button Functions
    def student_details():
        new_window = Toplevel(root)
        app = Student(new_window)
        return

    # Button Functions
    def training_data():
        new_window = Toplevel(root)
        app = Training(new_window)
        return

    # Button Functions
    def Face_r():
        new_window = Toplevel(root)
        app = Face_Recognition(new_window)
        return

    # Button Functions
    def attendance():
        new_window = Toplevel(root)
        app = Attendance(new_window)
        return

    def Exitfuc():
        root.destroy()
        return

    show = student_details
    train = training_data
    face = Face_r
    attend = attendance
    ext = Exitfuc
    f1 = Face_Recognization_System(root, show, train, face, attend, ext)
    root.mainloop()

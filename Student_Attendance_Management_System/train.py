from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import cv2
import mysql.connector
import numpy as np
from PIL import Image, ImageTk


class Training:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x650+0+0")
        self.root.title("Data Training")
        self.root.configure(bg='#e0bea0')

        # Title Label
        title_lbl = Label(self.root, text="Student Attendance Management System", font=("Times new Roman", 35, "bold"),
                          bg="#e0bea0", fg="black")
        title_lbl.place(x=250, y=0)

        train_btn = Button(self.root, text="Train data", command=self.Train_classifier, font=("Times new Roman", 20, "bold"),
                           bg="#915E4A")
        train_btn.place(x=600, y=300, width=200, height=60)

    def Train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # convert to grayscale image
            imageNp = np.array(img, 'uint8')
            i = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(i)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Traint the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training dataset created successfully", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    f1 = Training(root)
    root.mainloop()

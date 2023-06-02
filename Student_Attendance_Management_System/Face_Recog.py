from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import cv2
import mysql.connector
import numpy as np
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime


class Face_Recognition(object):
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x650+0+0")
        self.root.title("Data Training")
        self.root.configure(bg='#BADDDD')

        # Title Label
        title_lbl = Label(self.root, text="Face Detection System", font=("Times new Roman", 35, "bold"),
                          bg="#BADDDD", fg="black")
        title_lbl.place(x=450, y=0)

        face_btn = Button(self.root, text="Recogize Face", command=self.F_recognize, font=("Times new Roman", 20, "bold"),
                          bg="#63D5D5")
        face_btn.place(x=600, y=300, width=200, height=60)

    # Attendaces
    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []

            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in myDatalist) and (n not in myDatalist) and (d not in myDatalist)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")

    # Face Recognition

    def F_recognize(self):

        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Aryaman@1000", database="studentdb")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from Student where Student_id = "+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "select Roll from Student where Student_id = "+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "select Dep from Student where Student_id = "+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute(
                    "select Student_id from Student where Student_id = "+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"ROLL:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "UNKOWN FACE", (x, y-55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,
                                  10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition Module", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    root = Tk()
    f1 = Face_Recognition(root)
    root.mainloop()

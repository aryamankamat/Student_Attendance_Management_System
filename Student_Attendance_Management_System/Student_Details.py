from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import cv2
import mysql.connector


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x650+0+0")
        self.root.title("Student Details")
        self.root.configure(bg='#e0bea0')

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # Title Label
        title_lbl = Label(self.root, text="Student Attendance Management System", font=("Times new Roman", 35, "bold"),
                          bg="#e0bea0", fg="black")
        title_lbl.place(x=250, y=0)

        main_frame = Frame(self.root, bd=2, bg="#eda464")
        main_frame.place(x=0, y=80, width=1365, height=625)

        # Left Label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,
                                text="Student Details", font=("forte", 12, "bold"))
        left_frame.place(x=10, y=10, width=700, height=600)

        # Department
        dep_lab = Label(left_frame, text="Department",
                        font=("Times new Roman", 12, "bold"))
        dep_lab.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(left_frame, textvariable=self.var_dep, font=("Times new Roman", 12, "bold"), width=17,
                                 state="readonly")
        dep_combo['values'] = ("Select Department",
                               "Computer", "Civil", "Business")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Course
        course_lab = Label(left_frame, text="Courses",
                           font=("Times new Roman", 12, "bold"))
        course_lab.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(left_frame, textvariable=self.var_course, font=("Times new Roman", 12, "bold"),
                                    width=17, state="readonly")
        course_combo['values'] = (
            "Select Course", "BBACA", "BSC", "BBA", "BCA-science", "BCOM")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # YEAR
        year_lab = Label(left_frame, text="Year",
                         font=("Times new Roman", 12, "bold"))
        year_lab.grid(row=2, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(left_frame, textvariable=self.var_year, font=("Times new Roman", 12, "bold"),
                                  width=17, state="readonly")
        year_combo['values'] = (
            "Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024")
        year_combo.current(0)
        year_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # Semester
        sem_lab = Label(left_frame, text="Semester",
                        font=("Times new Roman", 12, "bold"))
        sem_lab.grid(row=2, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(left_frame, textvariable=self.var_semester, font=("Times new Roman", 12, "bold"),
                                 width=17, state="readonly")
        sem_combo['values'] = ("Select Semester", "Sem-1",
                               "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6")
        sem_combo.current(0)
        sem_combo.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # Student ID
        studID_lab = Label(left_frame, text="Student ID : ",
                           font=("Times new Roman", 12, "bold"))
        studID_lab.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        studID_entry = ttk.Entry(left_frame, textvariable=self.var_std_id, width=20,
                                 font=("Times new Roman", 12, "bold"))
        studID_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Student name
        studname_lab = Label(left_frame, text="Student Name : ",
                             font=("Times new Roman", 12, "bold"))
        studname_lab.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        studname_entry = ttk.Entry(left_frame, textvariable=self.var_std_name, width=20,
                                   font=("Times new Roman", 12, "bold"))
        studname_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Class division
        class_div_lab = Label(left_frame, text="Class Division : ", font=(
            "Times new Roman", 12, "bold"))
        class_div_lab.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(left_frame, textvariable=self.var_div, width=20,
                                    font=("Times new Roman", 12, "bold"))
        class_div_entry.grid(row=6, column=1, padx=10, pady=5, sticky=W)

        # Roll no
        rollno_lab = Label(left_frame, text="Roll number : ",
                           font=("Times new Roman", 12, "bold"))
        rollno_lab.grid(row=7, column=0, padx=10, pady=5, sticky=W)

        rollno_entry = ttk.Entry(left_frame, textvariable=self.var_roll, width=20, font=(
            "Times new Roman", 12, "bold"))
        rollno_entry.grid(row=7, column=1, padx=10, pady=5, sticky=W)

        # Gender
        gender_lab = Label(left_frame, text="Gender : ",
                           font=("Times new Roman", 12, "bold"))
        gender_lab.grid(row=8, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(left_frame, textvariable=self.var_gender, font=("Times new Roman", 11, "bold"),
                                    width=17, state="readonly")
        gender_combo['values'] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=8, column=1, padx=2, pady=10, sticky=W)

        # Phone no
        phoneno_lab = Label(left_frame, text="Phone no : ",
                            font=("Times new Roman", 12, "bold"))
        phoneno_lab.grid(row=9, column=0, padx=10, pady=5, sticky=W)

        phoneno_entry = ttk.Entry(left_frame, textvariable=self.var_phone, width=20,
                                  font=("Times new Roman", 12, "bold"))
        phoneno_entry.grid(row=9, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_lab = Label(left_frame, text="DOB : ",
                        font=("Times new Roman", 12, "bold"))
        dob_lab.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(left_frame, textvariable=self.var_dob, width=20,
                              font=("Times new Roman", 12, "bold"))
        dob_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_lab = Label(left_frame, text="Email : ",
                          font=("Times new Roman", 12, "bold"))
        email_lab.grid(row=10, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(left_frame, textvariable=self.var_email, width=20, font=(
            "Times new Roman", 12, "bold"))
        email_entry.grid(row=10, column=1, padx=10, pady=5, sticky=W)

        # Address
        address_lab = Label(left_frame, text="Address : ",
                            font=("Times new Roman", 12, "bold"))
        address_lab.grid(row=11, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(left_frame, textvariable=self.var_address, width=20,
                                  font=("Times new Roman", 12, "bold"))
        address_entry.grid(row=11, column=1, padx=10, pady=5, sticky=W)

        # Teacher
        teach_lab = Label(left_frame, text="Teacher : ",
                          font=("Times new Roman", 12, "bold"))
        teach_lab.grid(row=12, column=0, padx=10, pady=5, sticky=W)

        teach_entry = ttk.Entry(left_frame, textvariable=self.var_teacher, width=20,
                                font=("Times new Roman", 12, "bold"))
        teach_entry.grid(row=12, column=1, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            left_frame, variable=self.var_radio1, text="Take Photo", value="Yes")
        radiobtn1.grid(row=13, column=0, padx=10, pady=5)

        radiobtn2 = ttk.Radiobutton(
            left_frame, variable=self.var_radio1, text="No Photo", value="No")
        radiobtn2.grid(row=13, column=1, padx=10, pady=5)

        # Buttons
        save_btn = Button(left_frame, command=self.add_data, text="Save data", font=("Times new Roman", 12, "bold"),
                          bg="Green")
        save_btn.grid(row=14, column=0, padx=10, pady=5)

        update_btn = Button(left_frame, command=self.update_data, text="Update data",
                            font=("Times new Roman", 12, "bold"), bg="yellow")
        update_btn.grid(row=14, column=1, padx=10, pady=5)

        delete_btn = Button(left_frame, command=self.delete_data, text="Delete data",
                            font=("Times new Roman", 12, "bold"), bg="red")
        delete_btn.grid(row=14, column=3, padx=10, pady=5)

        reset_btn = Button(left_frame, command=self.reset_data, text="Reset data", font=("Times new Roman", 12, "bold"),
                           bg="orange")
        reset_btn.grid(row=14, column=4, padx=10, pady=5)

        take_photo_btn = Button(left_frame, command=self.generate_dataset, text="Take Photo", font=(
            "Times new Roman", 12, "bold"), bg="purple")
        take_photo_btn.grid(row=15, column=1, padx=10, pady=5)

        update_photo_btn = Button(left_frame, text="Update Photo", font=(
            "Times new Roman", 12, "bold"), bg="grey")
        update_photo_btn.grid(row=15, column=3, padx=10, pady=5)

        # Right Label frame
        right_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Student Details", font=("forte", 12, "bold"))
        right_frame.place(x=720, y=10, width=630, height=600)

        # Search System
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System",
                                  font=("Times new Roman", 12, "bold"), bg="#D3DFE7")
        search_frame.place(x=5, y=10, width=620, height=100)

        search_lab = Label(search_frame, text="Search By : ",
                           font=("Times new Roman", 12, "bold"))
        search_lab.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "Times new Roman", 12, "bold"), width=17, state="readonly")
        search_combo['values'] = ("Select", "roll_no", "phone_no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=20, font=("Times new Roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", font=(
            "Times new Roman", 12, "bold"), bg="white")
        search_btn.grid(row=0, column=3, padx=10, pady=5)

        showall_btn = Button(search_frame, text="Show", font=(
            "Times new Roman", 12, "bold"), bg="white")
        showall_btn.grid(row=0, column=4, padx=10, pady=5)

        # Table Frame to show data from database
        table_frame = Frame(right_frame, bd=2, bg="#D3DFE7", relief=RIDGE)
        table_frame.place(x=5, y=130, width=620, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone",
            "address", "teacher"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="ROLL-NO")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="DIV")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        # self.student_table.heading("photo", text="Photos")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        # self.student_table.column("photo", width=150)
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # Function for database
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_std_name.get().isnumeric() or self.var_std_id.get().isalpha() or self.var_div.get().isnumeric() or self.var_roll.get().isalpha() or self.var_phone.get().isalpha():
            messagebox.showerror(
                "Error", "All the fields are required or Please insert valid data.", parent=self.root)
        else:

            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Aryaman@1000",
                                               database="studentdb")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_dep.get(),
                                   self.var_course.get(),
                                   self.var_year.get(),
                                   self.var_semester.get(),
                                   self.var_std_id.get(),
                                   self.var_std_name.get(),
                                   self.var_div.get(),
                                   self.var_roll.get(),
                                   self.var_gender.get(),
                                   self.var_dob.get(),
                                   self.var_email.get(),
                                   self.var_phone.get(),
                                   self.var_address.get(),
                                   self.var_teacher.get(),
                                   self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "Data Saved Successfully")
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Due to :{str(e)}", parent=self.root)

    # Fetch data from database
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aryaman@1000",
                                       database="studentdb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # Update data
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All the fields are required", parent=self.root)

        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update the data?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Aryaman@1000",
                                                   database="studentdb")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Name=%s,Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photos=%s where Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()))

                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student data updated Successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as e:
                messagebox.showerror(
                    "Error", f"Due to :{str(e)}", parent=self.root)

    # Delete Data
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Delete Data", "Do you want to delete data?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Aryaman@1000",
                                                   database="studentdb")
                    my_cursor = conn.cursor()

                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Deleted", "Student data Deleted Successfully", parent=self.root)

            except Exception as e:
                messagebox.showerror(
                    "Error", f"Due to :{str(e)}", parent=self.root)

    # Reset data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # Generate data set & Take photo samples
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All the fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Aryaman@1000",
                                               database="studentdb")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1

                my_cursor.execute(
                    "update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Name=%s,Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photos=%s where Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id+1))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontal from opencv

                cam = cv2.VideoCapture(0)
                detector = cv2.CascadeClassifier(
                    'haarcascade_frontalface_default.xml')

                img_id = 0
                while (True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(
                            img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # incrementing sample number
                        img_id = img_id + 1

                        # saving the captured face in the dataset folder
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, gray)

                        # print("Images Saved for Enrollment :")
                        cv2.putText(gray, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        # ********************************
                        cv2.imshow('Face', img)

                    # wait for 100 miliseconds
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                    # # break if the sample number is morethan 100
                    elif img_id >= 100:
                        break

                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Data set generation completed successfully")

                # def face_cropped(img):
                #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                #     # Scaling Factor = 1.3
                #     # Minimum Neighbor = 5

                #     for (x, y, w, h) in faces:
                #         face_cropped = img[y:y+h, x:x+w]
                #         return face_cropped

                #     cap = cv2.VideoCapture(0)
                #     img_id = 0
                #     while True:
                #         ret, my_frame = cap.read()
                #         if face_cropped(my_frame) is not None:
                #             img_id += 1

                #             face = cv2.resize(
                #                 face_cropped(my_frame), (450, 450))
                #             face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                #             file_name_path = "data/user." + \
                #                 str(id)+"."+str(img_id)+".jpg"
                #             cv2.imwrite(file_name_path, face)
                #             cv2.putText(face, str(img_id), (50, 50),
                #                         cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                #             cv2.imshow("Cropped Face", face)

                #         if cv2.waitKey(1) == 13 or int(img_id) == 100:
                #             break

                #     cap.release()
                #     cv2.destroyAllWindows()
                #     messagebox.showinfo(
                #         "Result", "Data set generation completed successfully")

            except Exception as e:
                messagebox.showerror(
                    "Error", f"Due to :{str(e)}", parent=self.root)


if __name__ == '__main__':
    root = Tk()
    f1 = Student(root)
    root.mainloop()

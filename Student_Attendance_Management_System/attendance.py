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
import csv
from tkinter import filedialog


mydata = []  # global variable


class Attendance(object):
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x650+0+0")
        self.root.title("Data Training")
        self.root.configure(bg='#F7D06F')

        # Text variables
        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()

        # Title Label
        title_lbl = Label(self.root, text="Student Attendance Management System", font=("Times new Roman", 35, "bold"),
                          bg="#F7D06F", fg="black")
        title_lbl.place(x=250, y=0)

        main_frame = Frame(self.root, bd=2, bg="#F7D06F")
        main_frame.place(x=0, y=80, width=1365, height=625)

        # Left Label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,
                                text="Student Attendance Details", font=("forte", 12, "bold"))
        left_frame.place(x=10, y=10, width=700, height=600)

        # Label entry

        # Student ID
        studID_lab = Label(left_frame, text="Student ID : ",
                           font=("Times new Roman", 12, "bold"))
        studID_lab.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        studID_entry = ttk.Entry(left_frame, textvariable=self.var_attend_id, width=20,
                                 font=("Times new Roman", 12, "bold"))
        studID_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Name
        name_lab = Label(left_frame, text="Name : ",
                         font=("Times new Roman", 12, "bold"))
        name_lab.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(left_frame, textvariable=self.var_attend_name, width=20,
                               font=("Times new Roman", 12, "bold"))
        name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Date
        date_lab = Label(left_frame, text="Date : ",
                         font=("Times new Roman", 12, "bold"))
        date_lab.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(left_frame, textvariable=self.var_attend_date, width=20,
                               font=("Times new Roman", 12, "bold"))
        date_entry.grid(row=6, column=1, padx=10, pady=5, sticky=W)

        # Department
        dep_lab = Label(left_frame, text="Department : ",
                        font=("Times new Roman", 12, "bold"))
        dep_lab.grid(row=6, column=2, padx=10, pady=5, sticky=W)

        dep_entry = ttk.Entry(left_frame, textvariable=self.var_attend_dep, width=20,
                              font=("Times new Roman", 12, "bold"))
        dep_entry.grid(row=6, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_lab = Label(left_frame, text="Time : ",
                         font=("Times new Roman", 12, "bold"))
        time_lab.grid(row=8, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(left_frame, textvariable=self.var_attend_time, width=20,
                               font=("Times new Roman", 12, "bold"))
        time_entry.grid(row=8, column=1, padx=10, pady=5, sticky=W)

        # Attendance
        attend_lab = Label(left_frame, text="Attendance",
                           font=("Times new Roman", 12, "bold"))
        attend_lab.grid(row=8, column=2, padx=10, sticky=W)

        attend_combo = ttk.Combobox(left_frame, textvariable=self.var_attend_attendance, font=("Times new Roman", 12, "bold"),
                                    width=17, state="readonly")
        attend_combo['values'] = ("Present", "Absent")
        attend_combo.current(0)
        attend_combo.grid(row=8, column=3, padx=2, pady=10, sticky=W)

        # Roll
        roll_lab = Label(left_frame, text="Rollno : ",
                         font=("Times new Roman", 12, "bold"))
        roll_lab.grid(row=9, column=0, padx=10, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_frame, textvariable=self.var_attend_roll, width=20,
                               font=("Times new Roman", 12, "bold"))
        roll_entry.grid(row=9, column=1, padx=10, pady=5, sticky=W)

        # Buttons
        import_btn = Button(left_frame, command=self.importCSV, text="Import csv", font=("Times new Roman", 12, "bold"),
                            bg="#FFDC83")
        import_btn.grid(row=10, column=0, padx=10, pady=5)

        export_btn = Button(left_frame, command=self.export_csv, text="Export csv",
                            font=("Times new Roman", 12, "bold"), bg="#FFDC83")
        export_btn.grid(row=10, column=1, padx=10, pady=5)

        # update_btn = Button(left_frame, text="Update",
        #                     font=("Times new Roman", 12, "bold"), bg="#FFDC83")
        # update_btn.grid(row=10, column=2, padx=10, pady=5)

        # reset_btn = Button(left_frame, command=self.reset_data, text="Reset data", font=("Times new Roman", 12, "bold"),
        #                    bg="#FFDC83")
        # reset_btn.grid(row=10, column=3, padx=10, pady=5)

        # Right Label frame
        right_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=("forte", 12, "bold"))
        right_frame.place(x=720, y=10, width=630, height=600)

        table_frame = Frame(right_frame, bd=2, bg="#D3DFE7", relief=RIDGE)
        table_frame.place(x=5, y=10, width=620, height=570)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Attendance_table = ttk.Treeview(table_frame, columns=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendance_table.xview)
        scroll_y.config(command=self.Attendance_table.yview)

        self.Attendance_table.heading("id", text="Attendance ID")
        self.Attendance_table.heading("roll", text="Roll")
        self.Attendance_table.heading("name", text="Name")
        self.Attendance_table.heading("department", text="Department")
        self.Attendance_table.heading("time", text="Time")
        self.Attendance_table.heading("date", text="Date")
        self.Attendance_table.heading("attendance", text="Attendance")

        self.Attendance_table["show"] = "headings"

        self.Attendance_table.column("id", width=100)
        self.Attendance_table.column("roll", width=100)
        self.Attendance_table.column("name", width=100)
        self.Attendance_table.column("department", width=100)
        self.Attendance_table.column("time", width=100)
        self.Attendance_table.column("date", width=100)
        self.Attendance_table.column("attendance", width=100)

        self.Attendance_table.pack(fill=BOTH, expand=1)
        self.Attendance_table.bind("<ButtonRelease>", self.get_cursor)

    # Fetch data

    def fetch_data(self, rows):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        for i in rows:
            self.Attendance_table.insert("", END, values=i)

    # Import CSV

    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV File", filetypes=(
            ("CSV File", "*.csv"), ("All file", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")

            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # Export CSV
    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data Available",
                                     "No data Available", parent=self.root)
                return False

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV File", filetypes=(
                ("CSV File", "*.csv"), ("All file", "*.*")), parent=self.root)

            with open(fln, mode='w', newline='') as myfile:
                exp_write = csv.writer(myfile, delimiter=',')
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Exported", "Your data exported successfully", parent=self.root)

        except Exception as e:
            messagebox.showerror(
                "Error", f"Due to :{str(e)}", parent=self.root)

    # Get Cursor

    def get_cursor(self, event=""):
        cursor_row = self.Attendance_table.focus()
        content = self.Attendance_table.item(cursor_row)
        rows = content['values']

        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    # Reset
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("Present")


if __name__ == '__main__':
    root = Tk()
    f1 = Attendance(root)
    root.mainloop()

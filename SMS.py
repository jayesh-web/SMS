from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1300x700+0+0")
        title = Label(self.root, text="Student Management System", relief=GROOVE, font=("times new roman", 40, "bold"),
                      bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        # ===========All Variable===================
        self.rollno_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.mobile_var = StringVar()
        self.address_var = StringVar()
        self.search_by=StringVar()
        self.search_text = StringVar()

        # ===========Manage Frame=========================
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        manage_frame.place(x=20, y=100, width=450, height=560)

        m_title = Label(manage_frame, text="Manage Student", bg="crimson", fg="white",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(manage_frame, text="Roll No", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, padx=20, pady=10, sticky="W")

        txt_roll = Entry(manage_frame, textvariable=self.rollno_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll.grid(row=1, column=1, padx=20, pady=10, sticky="W")

        lbl_name = Label(manage_frame, text="Name", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="W")

        txt_name = Entry(manage_frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=20, pady=10, sticky="W")

        lbl_email = Label(manage_frame, text="Email", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, padx=20, pady=10, sticky="W")

        txt_email = Entry(manage_frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_email.grid(row=3, column=1, padx=20, pady=10, sticky="W")

        lbl_gender = Label(manage_frame, text="Gender", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, padx=20, pady=10, sticky="W")

        combo_gender = ttk.Combobox(manage_frame, textvariable=self.gender_var, font=("times new roman", 14, "bold"),
                                    state="readonly")
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)
        combo_gender.current(0)
        lbl_mobile = Label(manage_frame, text="Mobile", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_mobile.grid(row=5, column=0, padx=20, pady=10, sticky="W")

        txt_mobile = Entry(manage_frame, textvariable=self.mobile_var, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
        txt_mobile.grid(row=5, column=1, padx=20, pady=10, sticky="W")

        lbl_address = Label(manage_frame, text="Address", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_address.grid(row=6, column=0, padx=20, pady=10, sticky="W")

        self.txt_address = Text(manage_frame, width=26, height=4, font=("times new roman", 12, "bold"))
        self.txt_address.grid(row=6, column=1, padx=20, pady=10, sticky="W")

        btn_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="crimson")
        btn_frame.place(x=10, y=470, width=430)

        add_btn = Button(btn_frame, text="Add", width=10, command=self.add_student).grid(row=0, column=0, padx=10,
                                                                                         pady=10)
        update_btn = Button(btn_frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_frame, text="Clear", width=10, command=self.clear_data).grid(row=0, column=3, padx=10,
                                                                                            pady=10)

        # ===========Details Frame=========================

        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frame.place(x=500, y=100, width=750, height=560)

        lbl_search = Label(detail_frame, text="Search By", bg="crimson", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, padx=5, pady=10, sticky="W")

        combo_search = ttk.Combobox(detail_frame, font=("times new roman", 14, "bold"), state="readonly",textvariable=self.search_by)
        combo_search['values'] = ("rollno", "name", "mobile")
        combo_search.grid(row=0, column=1, padx=5, pady=10, sticky="W")
        combo_search.current(0)

        txt_search = Entry(detail_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE,textvariable=self.search_text)
        txt_search.grid(row=0, column=2, padx=5, pady=10, sticky="W")

        btn_search = Button(detail_frame, text="Search", width=10,command=self.search_data).grid(row=0, column=3, padx=5, pady=10)
        btn_show_all = Button(detail_frame, text="Show All", width=10, command=self.fetch_data).grid(row=0, column=4,
                                                                                                     padx=5, pady=10)

        # ============Table Frame===============================

        table_frame = Frame(detail_frame, bd=4, bg="crimson", relief=RIDGE)
        table_frame.place(x=10, y=70, width=720, height=470)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,
                                          column=("rollno", "name", "email", "gender", "mobile", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview())
        scroll_y.config(command=self.student_table.yview())
        self.student_table.heading("rollno", text="Roll No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("mobile", text="Mobile")
        self.student_table.heading("address", text="Address")
        self.student_table.column('rollno', width=50)
        self.student_table.column('name', width=150)
        self.student_table.column('email', width=150)
        self.student_table.column('mobile', width=100)
        self.student_table.column('gender', width=100)
        self.student_table.column('address', width=150)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table['show'] = 'headings'
        self.student_table.pack()
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_student(self):
        if self.rollno_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.mobile_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s)", (self.rollno_var.get(),
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.mobile_var.get(),
                                                                          self.txt_address.get("1.0", END)
                                                                          ))
            con.commit()
            self.fetch_data()
            self.clear_data()
            con.close()
            messagebox.showinfo("Success","Record inserted successfully")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear_data(self):
        self.rollno_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.mobile_var.set("")
        self.txt_address.delete('1.0', END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.rollno_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.mobile_var.set(row[4])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[5])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,mobile=%s,address=%s where rollno=%s", (self.name_var.get(),
                                                                      self.email_var.get(),
                                                                      self.gender_var.get(),
                                                                      self.mobile_var.get(),
                                                                      self.txt_address.get("1.0", END),
                                                                      self.rollno_var.get()
                                                                      ))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()

    def delete_data(self):

        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from student where rollno=%s",self.rollno_var.get())
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()
        messagebox.showinfo("Success","Record deleted")

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
obj = Student(root)
root.mainloop()

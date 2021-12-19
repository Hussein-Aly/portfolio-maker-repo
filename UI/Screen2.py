import tkinter.messagebox
import webbrowser
from tkinter import *
from tkinter import ttk

from modifiers import InfoContainers as IC


class Screen2(Frame):
    def __init__(self, win):
        Frame.__init__(self, win)
        self.win = win
        self.subjects = []
        self.configure(bg="#83568a")
        self.canvas = Canvas(
            self,
            bg="#83568a",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)


        self.entry0_img = PhotoImage(file=f"resources/images/screen2/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            264.0, 439.5,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            font=("Arial", 12, "normal"),
            bg="#dfdfdf",
            highlightthickness=0)

        self.entry0.place(
            x=115.0, y=415,
            width=298.0,
            height=47)

        self.entry1_img = PhotoImage(file=f"resources/images/screen2/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            1280.0, 470.0,
            image=self.entry1_img)

        self.entry1 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry1.place(
            x=1266.0, y=446,
            width=28.0,
            height=46)

        self.entry2_img = PhotoImage(file=f"resources/images/screen2/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(
            1280.0, 298.0,
            image=self.entry2_img)

        self.entry2 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry2.place(
            x=1266.0, y=275,
            width=28.0,
            height=44)

        self.entry3_img = PhotoImage(file=f"resources/images/screen2/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            501.5, 440.5,
            image=self.entry3_img)

        self.entry3 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry3.place(
            x=466.0, y=417,
            width=71.0,
            height=45)

        self.entry4_img = PhotoImage(file=f"resources/images/screen2/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image(
            625.5, 440.5,
            image=self.entry4_img)

        self.entry4 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry4.place(
            x=590.0, y=417,
            width=71.0,
            height=45)

        self.entry5_img = PhotoImage(file=f"resources/images/screen2/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(
            1280.0, 384.0,
            image=self.entry5_img)

        self.entry5 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry5.place(
            x=1266.0, y=362,
            width=28.0,
            height=42)

        self.entry6_img = PhotoImage(file=f"resources/images/screen2/img_textBox6.png")
        self.entry6_bg = self.canvas.create_image(
            1280.0, 552.0,
            image=self.entry6_img)

        self.entry6 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry6.place(
            x=1266.0, y=531,
            width=28.0,
            height=40)

        self.entry7_img = PhotoImage(file=f"resources/images/screen2/img_textBox7.png")
        self.entry7_bg = self.canvas.create_image(
            1280.0, 644.0,
            image=self.entry7_img)

        self.entry7 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry7.place(
            x=1266.0, y=623,
            width=28.0,
            height=40)

        self.entry8_img = PhotoImage(file=f"resources/images/screen2/img_textBox8.png")
        self.entry8_bg = self.canvas.create_image(
            1280.0, 728.0,
            image=self.entry8_img)

        self.entry8 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry8.place(
            x=1266.0, y=707,
            width=28.0,
            height=40)

        self.entry9_img = PhotoImage(file=f"resources/images/screen2/img_textBox9.png")
        self.entry9_bg = self.canvas.create_image(
            1280.0, 811.0,
            image=self.entry9_img)

        self.entry9 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry9.place(
            x=1266.0, y=790,
            width=28.0,
            height=40)

        self.entry10_img = PhotoImage(file=f"resources/images/screen2/img_textBox10.png")
        self.entry10_bg = self.canvas.create_image(
            1056.0, 296.5,
            image=self.entry10_img)

        self.entry10 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry10.place(
            x=907.0, y=272,
            width=298.0,
            height=47)

        self.entry11_img = PhotoImage(file=f"resources/images/screen2/img_textBox11.png")
        self.entry11_bg = self.canvas.create_image(
            1056.0, 386.0,
            image=self.entry11_img)

        self.entry11 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry11.place(
            x=907.0, y=362,
            width=298.0,
            height=46)

        self.entry12_img = PhotoImage(file=f"resources/images/screen2/img_textBox12.png")
        self.entry12_bg = self.canvas.create_image(
            1056.0, 469.5,
            image=self.entry12_img)

        self.entry12 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry12.place(
            x=907.0, y=445,
            width=298.0,
            height=47)

        self.entry13_img = PhotoImage(file=f"resources/images/screen2/img_textBox13.png")
        self.entry13_bg = self.canvas.create_image(
            1056.0, 553.5,
            image=self.entry13_img)

        self.entry13 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry13.place(
            x=907.0, y=529,
            width=298.0,
            height=47)

        self.entry14_img = PhotoImage(file=f"resources/images/screen2/img_textBox14.png")
        self.entry14_bg = self.canvas.create_image(
            264.0, 628.5,
            image=self.entry14_img)

        self.entry14 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry14.place(
            x=115.0, y=604,
            width=298.0,
            height=47)

        self.entry15_img = PhotoImage(file=f"resources/images/screen2/img_textBox15.png")
        self.entry15_bg = self.canvas.create_image(
            264.0, 718.5,
            image=self.entry15_img)

        self.entry15 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry15.place(
            x=115.0, y=694,
            width=298.0,
            height=47)

        self.entry16_img = PhotoImage(file=f"resources/images/screen2/img_textBox16.png")
        self.entry16_bg = self.canvas.create_image(
            1056.0, 643.5,
            image=self.entry16_img)

        self.entry16 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry16.place(
            x=907.0, y=619,
            width=298.0,
            height=47)

        self.entry17_img = PhotoImage(file=f"resources/images/screen2/img_textBox17.png")
        self.entry17_bg = self.canvas.create_image(
            1056.0, 729.5,
            image=self.entry17_img)

        self.entry17 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry17.place(
            x=907.0, y=705,
            width=298.0,
            height=47)

        self.entry18_img = PhotoImage(file=f"resources/images/screen2/img_textBox18.png")
        self.entry18_bg = self.canvas.create_image(
            1056.0, 810.5,
            image=self.entry18_img)

        self.entry18 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry18.place(
            x=907.0, y=786,
            width=298.0,
            height=47)

        self.img0 = PhotoImage(file=f"resources/images/screen2/img0.png")
        self.img0_hover = PhotoImage(file="resources/images/screen2/img0_hover.png")

        self.b0 = Label(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b0.place(
            x=892, y=890,
            width=209,
            height=62)

        self.changeOnHover(self.b0, self.img0_hover, self.img0)
        self.b0.bind("<Button-1>", lambda e: self.btn_clicked_add())

        self.img1 = PhotoImage(file=f"resources/images/screen2/img1.png")
        self.img1_hover = PhotoImage(file=f"resources/images/screen2/img1_hover.png")

        self.b1 = Label(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b1.place(
            x=1140, y=890,
            width=209,
            height=62)

        self.changeOnHover(self.b1, self.img1_hover, self.img1)
        self.b1.bind("<Button-1>", lambda e: self.btn_clicked_done())

        self.background_img = PhotoImage(file=f"resources/images/screen2/background.png")
        self.background = self.canvas.create_image(
            688.5, 490.0,
            image=self.background_img)

        self.entry19_img = PhotoImage(file=f"resources/images/screen2/img_textBox19.png")
        self.entry19_bg = self.canvas.create_image(
            263.0, 528.5,
            image=self.entry19_img)

        self.entry19 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 12, "normal"),
            highlightthickness=0)

        self.entry19.place(
            x=114.0, y=504,
            width=298.0,
            height=47)
        self.fill_entries()

        self.img14 = PhotoImage(file=f"resources/images/screen4/img14.png")
        self.img14_hover = PhotoImage(file=f"resources/images/screen4/img14_hover.png")
        self.b14 = Label(
            image=self.img14,
            bg="#83568a",
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b14.place(
            x=1279, y=24,
            width=50,
            height=50)
        self.b14.bind("<Button-1>", lambda e: self.openurl("https://github.com/SpadeQ22/portfolio-maker-repo/"))

        self.img15 = PhotoImage(file=f"resources/images/screen4/img15.png")
        self.img15_hover = PhotoImage(file=f"resources/images/screen4/img15_hover.png")
        self.b15 = Label(
            image=self.img15,
            bg="#83568a",
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b15.place(
            x=1139, y=36,
            width=100,
            height=25)

        self.b15.bind("<Button-1>", lambda e: self.openurl("https://www.linkedin.com/in/omaco2211/"))

        self.changeOnHover(self.b14, self.img14_hover, self.img14)
        self.changeOnHover(self.b15, self.img15_hover, self.img15)

    def openurl(self, url):
        webbrowser.open_new(url)

    def fill_entries(self):
        if self.win.current_subject is not None:
            sub = self.win.current_subject
            self.entry0.insert(0, sub.ASU_course_name)
            self.entry1.insert(0, sub.quizzes.total[1])
            self.entry2.insert(0, sub.assignments.total)
            self.entry3.insert(0, sub.UEL_module_code)
            self.entry4.insert(0, sub.ASU_course_code)
            self.entry5.insert(0, sub.quizzes.total[0])
            self.entry6.insert(0, sub.quizzes.total[2])
            self.entry7.insert(0, sub.project.total)
            self.entry8.insert(0, sub.labs.total)
            self.entry9.insert(0, sub.midterms.total)
            self.entry10.insert(0, sub.assignments.grade)
            self.entry11.insert(0, sub.quizzes.grade[0])
            self.entry12.insert(0, sub.quizzes.grade[1])
            self.entry13.insert(0, sub.quizzes.grade[2])
            self.entry14.insert(0, sub.instructor_signature)
            self.entry15.insert(0, sub.assistant_signature)
            self.entry16.insert(0, sub.project.grade)
            self.entry17.insert(0, sub.labs.grade)
            self.entry18.insert(0, sub.midterms.grade)
            self.entry19.insert(0, sub.UEL_module_name)

    def btn_clicked_done(self):
        correct = self.btn_clicked_add()
        if correct:
            self.win.change_to_screen3()
        else:
            return

    def btn_clicked_add(self):
        asu_course_name = self.entry0.get()
        quiz2_total = self.entry1.get()
        assign_total = self.entry2.get()
        uel_course_code = self.entry3.get()
        asu_course_code = self.entry4.get()
        quiz1_total = self.entry5.get()
        quiz3_total = self.entry6.get()
        project_total = self.entry7.get()
        lab_total = self.entry8.get()
        mid_total = self.entry9.get()
        assign_mark = self.entry10.get()
        quiz1_mark = self.entry11.get()
        quiz2_mark = self.entry12.get()
        quiz3_mark = self.entry13.get()
        instructor_name = self.entry14.get()
        ta_name = self.entry15.get()
        project_mark = self.entry16.get()
        lab_mark = self.entry17.get()
        mid_mark = self.entry18.get()
        uel_course_name = self.entry19.get()
        subject = IC.Subject()
        quiz = IC.Quiz(grade=[quiz1_mark, quiz2_mark, quiz3_mark], total=[quiz1_total, quiz2_total, quiz3_total])
        lab = IC.Lab(grade=lab_mark, total=lab_total)
        assignment = IC.Assignment(grade=assign_mark, total=assign_total)
        project = IC.Project(grade=project_mark, total=project_total)
        midterm = IC.Midterm(grade=mid_mark, total=mid_total)
        if self.win.check_filled(asu_course_code, asu_course_name, uel_course_name, uel_course_code, instructor_name,
                                 ta_name, assign_mark):
            self.entry0.delete(0, END)
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.entry3.delete(0, END)
            self.entry4.delete(0, END)
            self.entry5.delete(0, END)
            self.entry6.delete(0, END)
            self.entry7.delete(0, END)
            self.entry8.delete(0, END)
            self.entry9.delete(0, END)
            self.entry10.delete(0, END)
            self.entry11.delete(0, END)
            self.entry12.delete(0, END)
            self.entry13.delete(0, END)
            self.entry14.delete(0, END)
            self.entry15.delete(0, END)
            self.entry16.delete(0, END)
            self.entry17.delete(0, END)
            self.entry18.delete(0, END)
            self.entry19.delete(0, END)
            subject.ASU_course_code = asu_course_code
            subject.ASU_course_name = asu_course_name
            subject.instructor_signature = instructor_name
            subject.UEL_module_name = uel_course_name
            subject.UEL_module_code = uel_course_code
            subject.assistant_signature = ta_name
            subject.quizzes = quiz
            subject.assignments = assignment
            subject.project = project
            subject.labs = lab
            subject.midterms = midterm
            if self.win.current_subject is None:
                self.subjects.append(subject)
                self.win.subjects = self.subjects
            else:
                index = self.win.subjects.index(self.win.current_subject)
                self.win.subjects[index] = subject
                self.win.current_subject = None
            return True

        else:
            tkinter.messagebox.showerror("Error", "Some fields are missing!!")
            return False

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            image=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
            image=colorOnLeave))

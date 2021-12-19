import os
import threading
import webbrowser
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from modifiers.threader import BaseThread

from UI.Screen2 import Screen2
from UI.Screen4 import Screen4
from Autofill.filler import createSubjectFiller

class Screen3(Frame):
    def __init__(self, window):

        Frame.__init__(self, window)
        self.win = window
        window.configure(bg="#83568a")
        self.customFont = tkFont.Font(family="RobotoCondensed-normal", size=14, weight="normal")
        self.current_row = 379
        self.current_column = 168
        self.first_row = 379
        self.first_column = 168
        self.row_step = 164
        self.col_step = 414
        self.subjects_count = 0
        self.canvas = Canvas(
            self,
            bg="#83568a",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)


        self.background_img = PhotoImage(file=f"resources/images/screen3/background.png")
        self.background = self.canvas.create_image(
            689.5, 141.5,
            image=self.background_img)

        for subject in self.win.subjects:
            self.add_subject(subject)

        self.img3 = PhotoImage(file=f"resources/images/screen3/img3.png")
        self.img3_hover = PhotoImage(file=f"resources/images/screen3/img3_hover.png")
        self.b3 = Label(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b3.place(
            x=1137, y=895,
            width=214,
            height=62)

        self.b3.bind("<Button-1>", lambda e: self.btn_clicked())
        self.changeOnHover(self.b3, self.img3_hover, self.img3)

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

    def btn_clicked(self):
        t1 = BaseThread(target=self.win.download_splash, callback=self.win.change_to_screen4, callback_args=1)
        t1.start()



    def return_to_edit(self, subject):
        self.win.current_subject = subject
        self.win.change_to_screen2()

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            image=colorOnHover, fg="#B258B4"))
        button.bind("<Leave>", func=lambda e: button.config(
            image=colorOnLeave, fg="#ffffff"))

    def add_subject(self, subject):

        img0 = PhotoImage(file=f"resources/images/screen3/img0.png")
        img0_hover = PhotoImage(file=f"resources/images/screen3/img0_hover.png")
        b0 = Label(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            text=f"{subject.ASU_course_code}",
            compound="center",
            font=self.customFont,
            fg="#ffffff")

        b0.place(
            x=self.current_column, y=self.current_row,
            width=275,
            height=102)
        self.subjects_count += 1
        if self.subjects_count % 3 == 0:
            self.current_row += self.row_step
            self.current_column = self.first_column
        else:
            self.current_column += self.col_step

        self.changeOnHover(b0, img0_hover, img0)
        b0.bind("<Button-1>", lambda e: self.return_to_edit(subject))

    # def close(self):
    #     os._exit (0)
    #
    # def frame_mapped(self, e):
    #     self.win.update_idletasks ()
    #     self.win.overrideredirect (True)
    #     self.win.state('normal')
    #
    # def minimize(self):
    #     self.win.update_idletasks ()
    #     self.win.overrideredirect (False)
    #     self.win.state ('iconic')

    # self.img4 = PhotoImage (file=f"resources/images/screen1/img4.png")
    # self.img4_hover = PhotoImage (file=f"resources/images/screen1/img4_hover.png")
    # self.b4 = Label (
    #     image=self.img4,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     relief="flat")
    # self.b4.place (
    #     x=1393, y=0,
    #     width=48,
    #     height=37)
    #
    # self.img6 = PhotoImage (file=f"resources/images/screen1/img6.png")
    # self.img6_hover = PhotoImage (file=f"resources/images/screen1/img6_hover.png")
    # self.b6 = Label (
    #     image=self.img6,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     relief="flat")
    # self.b6.place (
    #     x=1346, y=0,
    #     width=48,
    #     height=37)
    #
    # self.changeOnHover (self.b4, self.img4_hover, self.img4)
    # self.changeOnHover (self.b6, self.img6_hover, self.img6)
    #
    # self.b4.bind("<Button-1>", lambda e: self.close())
    # self.b6.bind("<Button-1>", lambda e: self.minimize())
    #
    # self.bind("<Map>", self.frame_mapped)

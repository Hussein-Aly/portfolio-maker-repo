import os
import tkinter.messagebox
import webbrowser
from tkinter import *
from UI.Screen2 import Screen2
from modifiers import InfoContainers as IC
from tkinter import filedialog, ttk


class Screen1(Frame):

    def __init__(self, window):

        Frame.__init__(self, window)
        self.win = window
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

        self.background_img = PhotoImage(file=f"resources/images/screen1/background.png")
        self.background = self.canvas.create_image(
            776.5, 301.5,
            image=self.background_img)

        self.entry0_img = PhotoImage(file=f"resources/images/screen1/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            445.5, 372.0,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 16, "normal"),
            highlightthickness=0)

        self.entry0.place(
            x=229.0, y=344,
            width=433.0,
            height=54)

        self.entry1_img = PhotoImage(file=f"resources/images/screen1/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            445.5, 479.0,
            image=self.entry1_img)

        self.entry1 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 16, "normal"),
            highlightthickness=0)

        self.entry1.place(
            x=229.0, y=451,
            width=433.0,
            height=54)

        self.entry2_img = PhotoImage(file=f"resources/images/screen1/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image (
            445.5, 596.0,
            image=self.entry2_img)

        self.entry2 = Entry(
            bd=0,
            bg="#dfdfdf",
            show="*",
            font=("Arial", 16, "normal"),
            highlightthickness=0)

        self.entry2.place(
            x=229.0, y=568,
            width=433.0,
            height=54)

        self.entry3_img = PhotoImage(file=f"resources/images/screen1/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            986.5, 596.0,
            image=self.entry3_img)

        self.entry3 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 16, "normal"),
            highlightthickness=0)

        self.entry3.place(
            x = 770.0, y = 568,
            width = 433.0,
            height = 54)

        self.entry4_img = PhotoImage(file=f"resources/images/screen1/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image (
            986.5, 372.0,
            image=self.entry4_img)

        self.entry4 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 16, "normal"),
            highlightthickness=0)

        self.entry4.place(
            x = 770.0, y = 344,
            width = 433.0,
            height = 54)

        self.entry5_img = PhotoImage(file=f"resources/images/screen1/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(
            986.5, 479.0,
            image=self.entry5_img)

        self.entry5 = Entry(
            bd=0,
            bg="#dfdfdf",
            font=("Arial", 16, "normal"),
            highlightthickness=0)

        self.entry5.place(
            x=770.0, y=451,
            width=433.0,
            height=54)


        self.img0 = PhotoImage(file=f"resources/images/screen1/img0.png")
        self.img0_hover = PhotoImage(file=f"resources/images/screen1/img0_hover.png")
        self.b0 = Label(
            image=self.img0_hover,
            borderwidth=0,
            highlightthickness=0,
            relief=FLAT)

        self.b0.bind("<Button-1>", lambda e: self.btn_clicked())

        self.b0.place(
            x=589, y=811,
            width=233,
            height=87)

        self.changeOnHover(self.b0, self.img0, self.img0_hover)

        self.getportfolioimage_hover = PhotoImage(file=f"resources/images/screen1/getportfolioimage_hover.png")
        self.getportfolioimage = PhotoImage(file=f"resources/images/screen1/getportfolioimage.png")
        self.b1 = Label(
            image=self.getportfolioimage,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")
        self.b1.bind("<Button-1>", lambda e: self.choose_portfolio_image())
        self.b1.place(
            x=201, y=675,
            width=155,
            height=56)
        self.changeOnHover(self.b1, self.getportfolioimage_hover, self.getportfolioimage)


        self.l1 = Label(
            text="",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            bg="#83568a",
            font=("Arial", 10, "normal")
        )
        self.l1.place(x=380, y=695)
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

    def choose_portfolio_image(self):
        name = filedialog.askopenfilename(filetypes=[('image files', '.png')])
        self.l1.configure(text=name)

    def btn_clicked(self):
        name = self.entry0.get()
        email = self.entry1.get()
        password = self.entry2.get()
        asu_id = self.entry3.get()
        uel_id = self.entry4.get()
        program = self.entry5.get()
        picture_path = self.l1.cget("text")
        if self.win.check_filled(name, email, password, asu_id, uel_id, program, picture_path):
            student_data = IC.Student(name=name, email=email, password=password, ID=asu_id,
                                      UEL_ID=uel_id, picture_name=picture_path, program_name=program)
            self.win.student = student_data
            self.win.change_to_screen(Screen=Screen2)
        else:
            tkinter.messagebox.showerror("Error", "Error Occured: Some fields are empty!!")

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind ("<Enter>", func=lambda e: button.config (
            image=colorOnHover))
        button.bind ("<Leave>", func=lambda e: button.config (
            image=colorOnLeave))

    def close(self):
        os._exit (0)




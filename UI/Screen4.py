import os
import threading
import tkinter.messagebox
from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from pdf2image import convert_from_path
from threading import *


class Card:

    def __init__(self, path, label):
        self.label = label
        self.selected = False
        self.path = path


class Screen4(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.count = 0
        self.switch = False
        self.x_option = 97
        self.y_option = 209
        self.drop_switch = False
        self.row = 0
        self.col = 0
        self.images = []
        self.cards = []
        self.files = []
        self.section = None
        self.selected_cards = []
        self.options = []
        self.window = window
        self.currIndex: None

        self.window.configure(bg="#83568a")
        self.canvas = Canvas(
            self,
            bg="#83568a",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"resources/images/screen4/background.png")
        self.background = self.canvas.create_image(
            177.0, 86.0,
            image=self.background_img)

        self.img0 = PhotoImage(file=f"resources/images/screen4/img0.png")
        self.b0 = Label(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b0.place (
            x=-10, y=228,
            width=339,
            height=749)

        self.img1 = PhotoImage (file=f"resources/images/screen4/img1.png")
        self.img1_hover = PhotoImage (file=f"resources/images/screen4/img1_hover.png")
        self.b1 = Label (
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b1.place (
            x=21, y=164,
            width=56,
            height=42)

        self.b1.bind ("<Button-1>", lambda e: self.animate())

        self.img2 = PhotoImage (file=f"resources/images/screen4/img2.png")
        self.img2_hover = PhotoImage (file=f"resources/images/screen4/img2_hover.png")
        self.b2 = Button (
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b2.place (
            x=35, y=279,
            width=238,
            height=86)

        self.b2.bind("<Button-1>", lambda e: self.initialize_new_section(self.window.current_subject.assignments))

        self.img3 = PhotoImage(file=f"resources/images/screen4/img3.png")
        self.img3_hover = PhotoImage(file=f"resources/images/screen4/img3_hover.png")
        self.b3 = Button(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b3.place (
            x=33, y=405,
            width=238,
            height=86)

        self.b3.bind("<Button-1>", lambda e: self.initialize_new_section(self.window.current_subject.quizzes))

        self.img4 = PhotoImage(file=f"resources/images/screen4/img4.png")
        self.img4_hover = PhotoImage(file=f"resources/images/screen4/img4_hover.png")
        self.b4 = Button(
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b4.place (
            x=33, y=538,
            width=238,
            height=86)

        self.b4.bind("<Button-1>", lambda e: self.initialize_new_section(self.window.current_subject.midterms))

        self.img5 = PhotoImage (file=f"resources/images/screen4/img5.png")
        self.img5_hover = PhotoImage (file=f"resources/images/screen4/img5_hover.png")
        self.b5 = Button (
            image=self.img5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b5.place (
            x=33, y=671,
            width=238,
            height=86)

        self.b5.bind("<Button-1>", lambda e: self.initialize_new_section(self.window.current_subject.labs))

        self.img6 = PhotoImage (file=f"resources/images/screen4/img6.png")
        self.img6_hover = PhotoImage (file=f"resources/images/screen4/img6_hover.png")
        self.b6 = Button (
            image=self.img6,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b6.place (
            x=33, y=798,
            width=238,
            height=86)
        self.b6.bind("<Button-1>", lambda e: self.initialize_new_section(self.window.current_subject.project))

        self.img7 = PhotoImage (file=f"resources/images/screen4/img7.png")
        self.entry0_img = PhotoImage (file=f"resources/images/screen4/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image (
            213.0, 185.0,
            image=self.entry0_img)

        self.entry0 = Entry (
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.entry0.place (
            x=127.0, y=155,
            width=172.0,
            height=58)

        self.img9 = PhotoImage (file=f"resources/images/screen4/img9.png")
        self.img9_hover = PhotoImage (file=f"resources/images/screen4/img8_hover.png")
        self.b9 = Label (
            image=self.img9,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b9.place (
            x=318, y=153,
            width=62,
            height=62)

        self.b9.bind ("<Button-1>", lambda e: self.dropdown ())

        self.img10 = PhotoImage (file=f"resources/images/screen4/img10.png")
        self.img10_hover = PhotoImage (file=f"resources/images/screen4/img9_hover.png")
        self.b10 = Label(
            image=self.img10,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b10.place (
            x=1190, y=156,
            width=208,
            height=53)

        self.b10.bind("<Button-1>", func=lambda e: self.window.merger_interface())

        self.img11 = PhotoImage (file=f"resources/images/screen4/img11.png")
        self.img11_hover = PhotoImage (file=f"resources/images/screen4/img10_hover.png")
        self.b11 = Label (
            image=self.img11,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b11.place (
            x=952, y=155,
            width=208,
            height=53)

        self.b11.bind("<Button-1>", lambda e: self.file_dialogue())


        self.img12 = PhotoImage(file=f"resources/images/screen4/img12.png")
        self.img12_hover = PhotoImage(file=f"resources/images/screen4/img11_hover.png")
        self.b12 = Label(
            image=self.img12,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b12.place(
            x=714, y=155,
            width=208,
            height=53)

        self.b12.bind("<Button-1>", lambda e: self.remove_selected_files())

        self.img13_hover = PhotoImage(file=f"resources/images/screen4/switch_hover.png")
        self.img13 = PhotoImage(file=f"resources/images/screen4/switch.png")
        self.b13 = Label(
            image=self.img13,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b13.place(
            x=476, y=155,
            width=208,
            height=53)

        self.b13.bind("<Button-1>", func=lambda e: self.switch_files())

        self.wrapper = LabelFrame(self.canvas)
        self.wrapper.pack(padx=405, pady=241)
        self.canvas2 = Canvas(self.wrapper, height=703, width=969, bg="#fff", highlightthickness=0,
            relief="ridge")
        self.canvas2.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar = ttk.Scrollbar(self.wrapper, orient=VERTICAL, command=self.canvas2.yview)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.canvas2.configure(yscrollcommand=self.vbar.set)
        self.canvas2.bind("<Configure>", func=lambda e: self.canvas2.configure(scrollregion=self.canvas2.bbox("all")))
        self.myframe = Frame(self.canvas2, bg="#fff")
        self.canvas2.create_window((0,0), window=self.myframe, anchor=NW)
        self.myframe.bind("<Configure>", self.reset_scrollregion)




        self.changeOnHoverButtons (self.b1, self.img1_hover, self.img1)
        self.changeOnHoverButtons (self.b2, self.img2_hover, self.img2)
        self.changeOnHoverButtons (self.b3, self.img3_hover, self.img3)
        self.changeOnHoverButtons (self.b4, self.img4_hover, self.img4)
        self.changeOnHoverButtons (self.b5, self.img5_hover, self.img5)
        self.changeOnHoverButtons (self.b6, self.img6_hover, self.img6)
        self.changeOnHoverButtons (self.b9, self.img9_hover, self.img9)
        self.changeOnHoverButtons (self.b10, self.img10_hover, self.img10)
        self.changeOnHoverButtons (self.b11, self.img11_hover, self.img11)
        self.changeOnHoverButtons (self.b12, self.img12_hover, self.img12)
        self.changeOnHoverButtons(self.b13, self.img13_hover, self.img13)

        for subject in self.window.subjects:
            self.add_option(subject)

        self.initialize_new_subject()

    def initialize_new_subject(self):
        self.entry0.delete(0, END)
        self.entry0.insert(0, self.window.current_subject.ASU_course_code)
        self.initialize_new_section(self.window.current_subject.assignments)

    def initialize_new_section(self, section):
        self.section = section
        self.files = self.section.file_paths
        self.cards = []
        self.selected_cards = []
        self.remove_cards()
        self.set_cards()

    def set_cards(self):
        for path in self.files:
            self.add_preview(path)

    def reset_scrollregion(self, e):
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all"))

    def changeOnHoverButtons(self, button, colorOnHover, colorOnLeave):
        button.bind ("<Enter>", func=lambda e: button.config(
            image=colorOnHover))
        button.bind ("<Leave>", func=lambda e: button.config(
            image=colorOnLeave))

    def remove_cards(self):
        self.row = 0
        self.col = 0
        for child in self.myframe.winfo_children():
            child.destroy()

    def remove_selected_files(self):
        if len(self.selected_cards) > 0:
            for child in self.selected_cards:
                child.label.destroy()
            self.cards = list(set(self.cards) - set(self.selected_cards))
            self.files = [card.path for card in self.cards]
            self.section.file_paths = self.files
            self.selected_cards = []
            self.reorganize()

    def reorganize(self):
        self.row = 0
        self.col = 0
        for file in self.cards:
            file.label.grid(column=self.col % 4, row=self.row, padx=35, pady=20)
            self.col += 1
            if self.col % 4 == 0:
                self.row += 1

    def file_dialogue(self):
        names = filedialog.askopenfilenames(filetypes=[('files', '.pdf')])
        for name in names:
            if name != "":
                self.files.append(name)
                self.add_preview(name)
        self.section.file_paths = self.files

    def add_preview(self, path):
        print(path)
        pages = convert_from_path(path, poppler_path="resources/poppler-0.68.0/bin", first_page=1, last_page=1)
        img = pages[0]
        img = img.resize((175, 248), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(img)
        self.images.append(photoImg)
        self.add_file(path, os.path.basename(path).replace(".png", ".pdf"), self.images[len(self.images) - 1])

    def add_file(self, path, file_name, img):
        label = Label(self.myframe,
                      image=img,
                      bg="white",
                      height=300,
                      width=175,
                      borderwidth=0,
                      highlightthickness=0,
                      compound='top',
                      text=f"{file_name}",
                      fg="blue",
                      wraplength=170,
                      justify=CENTER)
        label.grid(column=self.col % 4, row=self.row, padx=35, pady=20)
        self.col += 1
        if self.col % 4 == 0:
            self.row += 1
        card = Card(path, label)
        self.changeOnHover(card)
        self.cards.append(card)

    def switch_files(self):
        if len(self.selected_cards) == 2:
            info_1 = self.selected_cards[0].label.grid_info()
            info_2 = self.selected_cards[1].label.grid_info()
            self.selected_cards[0].label.grid(info_2)
            self.selected_cards[1].label.grid(info_1)
        else:
            tkinter.messagebox.showerror("Error", "Error 101: Exactly 2 Files Need to be Selected")

    def select(self, button):
        button.unbind("<Leave>")
        button.config(bg="#93B5C6")

    def unselect(self, button):
        button.config(bg="white")
        button.bind("<Leave>", func=lambda e: button.config(
            bg="white"))

    def clicked_file(self, card):
        card.selected = not card.selected
        if card.selected:
            self.select(card.label)
            self.selected_cards.append(card)
        else:
            self.unselect(card.label)
            self.selected_cards.remove(card)

    def changeOnHover(self, card):
        card.label.bind("<Enter>", func=lambda e: card.label.configure(
            bg="#93B5C6"))
        card.label.bind("<Leave>", func=lambda e: card.label.configure(
            bg="white"))
        card.label.bind("<Button-1>", lambda e: self.clicked_file(card), add=True)

    def display(self):
        self.count -= 1
        xcor = self.b0.winfo_x()
        ycor = self.b0.winfo_y()
        xcor2 = self.b2.winfo_x()
        ycor2 = self.b2.winfo_y()
        xcor3 = self.b3.winfo_x()
        ycor3 = self.b3.winfo_y()
        xcor4 = self.b4.winfo_x()
        ycor4 = self.b4.winfo_y()
        xcor5 = self.b5.winfo_x()
        ycor5 = self.b5.winfo_y()
        xcor6 = self.b6.winfo_x()
        ycor6 = self.b6.winfo_y()
        if self.count > 0 and not self.switch:
            self.b0.place(x=xcor + 4.8, y=ycor)
            self.b2.place(x=xcor2 + 4.8, y=ycor2)
            self.b3.place(x=xcor3 + 4.8, y=ycor3)
            self.b4.place(x=xcor4 + 4.8, y=ycor4)
            self.b5.place(x=xcor5 + 4.8, y=ycor5)
            self.b6.place(x=xcor6 + 4.8, y=ycor6)
            display_event = self.window.after(10, self.display)

    def hide(self):
        self.count += 1
        xcor = self.b0.winfo_x()
        ycor = self.b0.winfo_y()
        xcor2 = self.b2.winfo_x()
        ycor2 = self.b2.winfo_y()
        xcor3 = self.b3.winfo_x()
        ycor3 = self.b3.winfo_y()
        xcor4 = self.b4.winfo_x()
        ycor4 = self.b4.winfo_y()
        xcor5 = self.b5.winfo_x()
        ycor5 = self.b5.winfo_y()
        xcor6 = self.b6.winfo_x()
        ycor6 = self.b6.winfo_y()
        if self.count < 70 and self.switch:
            self.b0.place(x=xcor - 5, y=ycor)
            self.b2.place(x=xcor2 - 5, y=ycor2)
            self.b3.place(x=xcor3 - 5, y=ycor3)
            self.b4.place(x=xcor4 - 5, y=ycor4)
            self.b5.place(x=xcor5 - 5, y=ycor5)
            self.b6.place(x=xcor6 - 5, y=ycor6)
            hide_event = self.window.after(10, self.hide)

    def animate_up(self, button):
        xcor = button.winfo_x()
        ycor = button.winfo_y()
        if ycor != 209:
            button.place(x=xcor, y=ycor-1)
            self.window.after(5, self.animate, button)

    def animate(self):
        self.switch = not self.switch
        if self.switch:
            self.hide()
        else:
            self.display()

    def drop(self):
        xcor = self.x_option
        ycor = self.y_option
        for option in self.options:
            option.place(x=xcor, y=ycor)
            ycor += 60

    def up(self):
        for option in self.options:
            option.place_forget()

    def dropdown(self):
        self.drop_switch = not self.drop_switch
        if self.drop_switch:
            self.drop()
        else:
            self.up()

    def add_option(self, subject):
        option = Label(
            image=self.img7,
            borderwidth=1,
            highlightthickness=1,
            text=subject.ASU_course_code,
            compound=CENTER,
            relief="flat",
            width=220,
            height=60)
        option.bind("<Button-1>", lambda e: self.set_current_subject(subject))
        option.bind("<Enter>", func=lambda e: option.configure(
            bg="#93B5C6"))
        option.bind("<Leave>", func=lambda e: option.configure(
            bg="white"))
        self.options.append(option)

    def set_current_subject(self, subject):
        self.window.current_subject = subject
        self.initialize_new_subject()
        self.dropdown()
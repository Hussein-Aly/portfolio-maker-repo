import os
import sys
import threading
import tkinter as tk
import tkinter.messagebox
import traceback
from os import listdir
from os.path import isfile, join
from tkinter import ttk
from UI.LoadingScreen import LoadingWin

from modifiers import merge, converter
from Autofill.filler import createSubjectFiller
from UI.Screen1 import Screen1
from UI.Screen2 import Screen2
from UI.Screen3 import Screen3
from UI.Screen4 import Screen4
from Downloader.Downloader import Downloader


class Application(tk.Tk):

    def __init__(self, *args):
        super().__init__()
        self.subjects = []
        self.student = None
        self.current_subject = None
        self.title("Potfolio Maker App")
        self.geometry("1440x1024")
        self.configure(bg="#83568a")
        self.currentScreen = None

        self.change_to_screen(Screen1)

        self.resizable(False, False)
        self.mainloop()

    # def change_to_screen(self, Screen):
    #     screen = Screen(self)
    #     screen.pack(fill="both", expand=True)
    #     if self.currentScreen is not None:
    #         self.currentScreen.forget()
    #     # self.main_canvas.create_window((0,0), window=screen, anchor="nw")
    #     self.currentScreen = screen

    def change_to_screen4(self,n):
        screen = Screen4(self)
        screen.pack(fill="both", expand=True)
        if self.currentScreen is not None:
            self.currentScreen.forget()
        self.currentScreen = screen

    def change_to_screen2(self):
        screen = Screen2(self)
        screen.pack(fill="both", expand=True)
        if self.currentScreen is not None:
            self.currentScreen.forget()
        self.currentScreen = screen

    def change_to_screen3(self):
        screen = Screen3(self)
        screen.pack(fill="both", expand=True)
        if self.currentScreen is not None:
            self.currentScreen.forget()
        self.currentScreen = screen

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            image=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
            image=colorOnLeave))

    def check_filled(self, *args) -> bool:
        cnt = 0
        for arg in list(args):
            print(arg)
            if len(arg) > 0:
                cnt += 1
        if cnt == len(args):
            return True
        else:
            return False

    def download_splash(self):
        loading_win = LoadingWin()
        try:
            loading_win.progress['value'] = 5
            downloader = Downloader(self.student.email, self.student.password)
            loading_win.progress['value'] = 20
            loading_win.label['text'] = 'Downloading files...'
            subject_codes = [subject.ASU_course_code for subject in self.subjects]
            downloader.get_files(subject_codes)
            downloader.get_quizzes(subject_codes)
            loading_win.progress['value'] == 80
            loading_win.label['text'] = 'Organizing files and setting file paths...'
            self.current_subject = self.subjects[0]
            loading_win.progress['value'] = 90
            self.classify()
            loading_win.progress['value'] = 100
            loading_win.destroy()

        except Exception as err:
            loading_win.destroy()
            print(Exception, err)
            print(traceback.format_exc())
            ans = tk.messagebox.askretrycancel("Error 400",
                                               "Connection Error: Couldn't Connect to Server, Try Again!")
            if ans:
                self.download_splash()
            else:
                sys.exit(0)

    def classify(self):
        for subject in self.subjects:
            if os.path.exists(f"Subjects/{subject.ASU_course_code}"):
                if os.path.exists(f"Subjects/{subject.ASU_course_code}/ass"):
                    mypath = f"Subjects/{subject.ASU_course_code}/ass"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.assignments.file_paths = onlyfiles

                if os.path.exists(f"Subjects/{subject.ASU_course_code}/lab"):
                    mypath = f"Subjects/{subject.ASU_course_code}/lab"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    print(onlyfiles)
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.labs.file_paths = onlyfiles

                if os.path.exists(f"Subjects/{subject.ASU_course_code}/project"):
                    mypath = f"Subjects/{subject.ASU_course_code}/project"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.project.file_paths = onlyfiles

                if os.path.exists(f"Subjects/{subject.ASU_course_code}/quizzes"):
                    mypath = f"Subjects/{subject.ASU_course_code}/quizzes"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.quizzes.file_paths = onlyfiles

                if os.path.exists(f"Subjects/{subject.ASU_course_code}/midterm"):
                    mypath = f"Subjects/{subject.ASU_course_code}/midterm"
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    converter.convert_to_pdf(onlyfiles)
                    onlyfiles = [f"{mypath}/{f}" for f in listdir(mypath) if isfile(join(mypath, f))]
                    subject.midterms.file_paths = onlyfiles

    def merger_interface(self):
        loading_win = LoadingWin()
        try:
            step = 100/2*len(self.subjects)
            loading_win.label['text'] = 'Generating Covers Files, Please Wait.....'

            for subject in self.subjects:
                loading_win.progress['value'] += step
                createSubjectFiller(self.student, subject)

            loading_win.label['text'] = 'Merging Files, Please Wait.....'
            pdfs_to_merge = []
            for subject in self.subjects:
                pdfs_to_merge = [f"Subjects/{subject.ASU_course_code}/My Header.pdf"] + subject.assignments.file_paths + \
                                subject.quizzes.file_paths + subject.midterms.file_paths \
                                + subject.labs.file_paths + subject.project.file_paths
                merge.merge_pdfs(pdfs_to_merge, f"Subjects/{subject.ASU_course_code}")
                loading_win.progress['value'] += step

            loading_win.destroy()
            tkinter.messagebox.showinfo("Success", "Portfolios Generated Successfully, You can find "
                                                   "the generated portfolio in the Subjects Folder ")

        except Exception as err:
            loading_win.destroy()
            print(Exception, err)
            print(traceback.format_exc())
            ans = tk.messagebox.askretrycancel("Error 500",
                                               "Error During Merging, Please submit the issue on our github repository")
            if ans:
                self.merger_interface()
            else:
                sys.exit(0)




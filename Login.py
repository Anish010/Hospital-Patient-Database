import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from hospital import Hospital


def main():
    root = Tk()
    ob = MainWindow(root)
    root.mainloop()
# MAIN WINDOW FOR LOG IN


class MainWindow:

    def login(self):
        username = "anish"
        password = "12345"
        if self.username_entry.get() == username and self.password_entry.get() == password:
            self.newWindow = Toplevel(self.master)
            self.app = Hospital(self.newWindow)
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    # constructor
    def __init__(self, master):
        # public data mambers
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")
        self.master.configure(bg='#333333')

        frame = tkinter.Frame(bg='#333333')

        # Creating widgets
        self.login_label = tkinter.Label(
            frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
        self.username_label = tkinter.Label(
            frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.username_entry = tkinter.Entry(frame, font=("Arial", 16))
        self.password_entry = tkinter.Entry(
            frame, show="*", font=("Arial", 16))
        self.password_label = tkinter.Label(
            frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.login_button = tkinter.Button(
            frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.login)

        # Placing widgets on the screen
        self.login_label.grid(
            row=0, column=0, columnspan=2, sticky="news", pady=40)
        self.username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        self.password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=30)

        frame.pack()
    # Function for Exit

    def Exit(self):
        self.master.destroy()


if __name__ == "__main__":
    main()

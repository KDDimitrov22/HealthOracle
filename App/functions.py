import os
import pyautogui
import tkinter as tk
from tkinter import Canvas
import readchar
from Model.models.model_cardiovascular_disease import predictCardiovascular

# Function to open a new window
def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Page")
    new_window.geometry("400x300")
    tk.Label(new_window, text="Welcome to the new page!", font=("Arial", 16)).pack(pady=20)

# Menu class using Tkinter
class Menu:
    def __init__(self, root, options):
        self.root = root
        self.options = options
        self.selected = 0
        self.labels = []

        self.title_label = tk.Label(root, text="Health Oracle", font=("Arial", 28, "bold"), fg="white", bg="#5eaf5e")
        self.title_label.place(relx=0.5, y=100, anchor="center")

        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        self.canvas = Canvas(root, width=1280, height=960)
        self.canvas.pack(fill="both", expand=True)

        for i in range(960):
            color = f"#5e{hex(180 - i // 8)[2:].zfill(2)}5e"  # Greenish gradient
            self.canvas.create_line(0, i, 1280, i, fill=color)

        for option in options:
            label = tk.Label(self.frame, text=option, font=("Arial", 16), pady=5)
            label.pack()
            self.labels.append(label)

        self.update_menu()  # Make sure this function exists

        root.bind("<Up>", self.up_key)
        root.bind("<Down>", self.down_key)
        root.bind("<Return>", self.enter_key)

    def update_menu(self):  # ✅ Make sure this exists
        for i, label in enumerate(self.labels):
            if i == self.selected:
                label.config(fg="cyan", font=("Arial", 16, "bold"))
            else:
                label.config(fg="black", font=("Arial", 16))

    def up_key(self, event):
        self.selected = (self.selected - 1) % len(self.options)
        self.update_menu()

    def down_key(self, event):
        self.selected = (self.selected + 1) % len(self.options)
        self.update_menu()

    def enter_key(self, event):
        if self.selected == 0:
            open_new_window()
        elif self.selected == 1:
            self.root.quit()




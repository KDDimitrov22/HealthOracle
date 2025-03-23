import functions
import time
import tkinter as tk

from functions import Menu


if __name__ == "__main__":
    root = tk.Tk()
    root.title("HealthOracle")
    root.geometry("1280x960")
    root.configure(bg="#5eaf5e") 
    menu = Menu(root, ["Start", "Exit"])
    root.mainloop()
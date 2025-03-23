import tkinter as tk
from functions import create_menu

def main():
    root = tk.Tk()
    create_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
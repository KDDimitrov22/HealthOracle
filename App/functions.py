import os
import tkinter as tk
from questionaire import create_new_page

def create_menu(root):
    for widget in root.winfo_children():
        widget.destroy()
        
    root.title("Health Oracle")
    root.configure(bg="#1b964e")
    root.geometry("800x600")  # Set a larger initial window size

    title = tk.Label(root, text="Health Oracle", bg="#1b964e", fg="white", font=("Helvetica", 24))
    title.pack(pady=(50, 20))  # Add more padding at the top

    start_button = tk.Button(root, text="Start", command=lambda: create_new_page(root), bg="#1b964e", fg="white", bd=2, relief="solid", font=("Helvetica", 16), width=20, height=2, highlightbackground="#112e0e", highlightcolor="#112e0e", highlightthickness=2)
    start_button.pack(pady=(20, 10), padx=20)
    start_button.bind("<Enter>", lambda e: start_button.config(highlightbackground="#155e33", highlightcolor="#155e33"))
    start_button.bind("<Leave>", lambda e: start_button.config(highlightbackground="#112e0e", highlightcolor="#112e0e"))

    exit_button = tk.Button(root, text="Exit", command=lambda: open_exit_confirmation(root), bg="#1b964e", fg="white", bd=2, relief="solid", font=("Helvetica", 16), width=20, height=2, highlightbackground="#112e0e", highlightcolor="#112e0e", highlightthickness=2)
    exit_button.pack(pady=10, padx=20)
    exit_button.bind("<Enter>", lambda e: exit_button.config(highlightbackground="#155e33", highlightcolor="#155e33"))
    exit_button.bind("<Leave>", lambda e: exit_button.config(highlightbackground="#112e0e", highlightcolor="#112e0e"))

def animate_border_color(button, target_color):
    current_color = button.cget("highlightbackground")
    if current_color != target_color:
        button.config(highlightbackground=target_color, highlightcolor=target_color)
        button.after(50, lambda: animate_border_color(button, target_color))

def open_exit_confirmation(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    confirmation_label = tk.Label(root, text="Are you sure?", bg="#1b964e", fg="white", font=("Helvetica", 24))
    confirmation_label.pack(pady=20)

    yes_button = tk.Button(root, text="Yes", command=root.quit, bg="#1b964e", fg="white", bd=2, relief="solid", font=("Helvetica", 16), width=20, height=2, highlightbackground="#112e0e", highlightcolor="#112e0e", highlightthickness=2)
    yes_button.pack(pady=10, padx=20)
    yes_button.bind("<Enter>", lambda e: yes_button.config(highlightbackground="#155e33", highlightcolor="#155e33"))
    yes_button.bind("<Leave>", lambda e: yes_button.config(highlightbackground="#112e0e", highlightcolor="#112e0e"))

    no_button = tk.Button(root, text="No", command=lambda: create_menu(root), bg="#1b964e", fg="white", bd=2, relief="solid", font=("Helvetica", 16), width=20, height=2, highlightbackground="#112e0e", highlightcolor="#112e0e", highlightthickness=2)
    no_button.pack(pady=10, padx=20)
    no_button.bind("<Enter>", lambda e: no_button.config(highlightbackground="#155e33", highlightcolor="#155e33"))
    no_button.bind("<Leave>", lambda e: no_button.config(highlightbackground="#112e0e", highlightcolor="#112e0e"))

def start_program():
    # Add functionality for the Start button here
    print("Starting the program...")
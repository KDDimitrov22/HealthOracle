import tkinter as tk
import pickle
import os

def create_new_page(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    new_page_title = tk.Label(root, text="Welcome to the new page!", bg="#1b964e", fg="white", font=("Helvetica", 24))
    new_page_title.pack(pady=20)


    model = load_model()

    # Display model information or use the model for predictions
    model_info = tk.Label(root, text=f"Model loaded: {model}", bg="#1b964e", fg="white", font=("Helvetica", 16))
    model_info.pack(pady=20)

def load_model():
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "Model", "model.pkl")
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model
import os
import pyautogui
from rich.console import Console
from rich.text import Text

console=Console() # so you don't have to create a new console object every time you run a function using the "rich" library

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def fullscreen():
    pyautogui.hotkey('F11')

def centerText(text, color): # note: 
    if color:
        console.print(f"[{color}]{text}[/{color}]", justify="center")
    else:
        console.print(text, justify="center")
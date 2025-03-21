import os
import pyautogui
from rich.console import Console
from rich.text import Text
import readchar

console=Console() # so you don't have to create a new console object every time you run a function using the "rich" library

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def fullscreen():
    pyautogui.hotkey('F11')

def centerText(text, color): # note: leave the 'color' argument's value blank if you want the text to be the normal white
    if color:
        console.print(f"[{color}]{text}[/{color}]", justify="center")
    else:
        console.print(text, justify="center")

class Menu:
    def __init__(self, options):
        self.options=options
        self.selected=0

    def show_menu(self):
        while True:
            clear()
            print('\n' * 5)
            for i,option in enumerate(self.options):
                if i == self.selected:
                    centerText(option+'\n',"bold cyan")
                else:
                    centerText(option+'\n',"")

            key=readchar.readkey()

            if key == readchar.key.UP:
                if self.selected == 0:
                    self.selected=len(self.options)-1
                else:
                    self.selected-=1
            elif key == readchar.key.DOWN:
                if self.selected == len(self.options)-1:
                    self.selected=0
                else:
                    self.selected+=1
            elif key == "\r": # 'enter' key
                centerText(f"Key pressed: {self.selected}", "pink")
                break
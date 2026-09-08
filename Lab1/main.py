from tkinter import *
from tkinter import ttk

from module_1 import Module1 as mod_1
from Lab1.module_2 import Module2 as mod_2

root = Tk()
root.title("Lab 1")
root.geometry("250x200")
 
def dismiss(window):
    window.grab_release() 
    window.destroy()

# testing
def handle_text(received_text):
    print(received_text)
 
def open_module_1():
    mod_1(dismiss)

def open_module_2():
    mod_2(dismiss, on_confirm=handle_text)

arr = [
    ['Modul 1', open_module_1], 
    ['Modul 2', open_module_2]
]

for i in arr: 
    open_button = ttk.Button(text=i[0], command=i[1])
    open_button.pack(anchor="center", expand=1)
 
root.mainloop()
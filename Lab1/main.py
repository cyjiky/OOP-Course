from tkinter import *
from tkinter import ttk

from module_1 import Module1 as mod_1
from module_2 import Module2 as mod_2

root = Tk()
root.title("Lab 1")
root.geometry("250x200")

main_label = Label(root, text="", font=("Arial", 12))
main_label.pack(pady=20)
 
def dismiss(window):
    window.grab_release() 
    window.destroy()

def handle_text(received_text: str):
    main_label.config(text=received_text)

modules = [
    ('Modul 1', mod_1),
    ('Modul 2', mod_2),
]

main_menu = Menu()
for label, mod in modules:
    main_menu.add_command(
        label=label, 
        command=lambda 
        m=mod: m(
            dismiss, 
            on_confirm=handle_text
        )
    )

root.config(menu=main_menu)
root.mainloop()
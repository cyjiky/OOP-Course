from tkinter import *
from tkinter import ttk

from typing import List 

class Module1:
    GROUP_LIST = ['IM-o51', 'IM-51', 'IM-52', 'IM-53', 'IM-54', 'IM-55']
    BUTTONS = ['Відміна', 'Так']

    def __init__(
        self, 
        dissmiss
    ):
        self.dsmiss = dissmiss
        self.main_func()

    def main_func(self):
        window = Toplevel()
        window.title("Modul_1")
        window.geometry("250x200")
        window.protocol("WM_DELETE_WINDOW", lambda: self.dsmiss(window))

        self.menu_func()

        for el in self.BUTTONS:
            self.btn_func(
                wnd=window, 
                txt=el
            )
            
        window.grab_set()

    def menu_func(self):
        pass

    def btn_func(self, wnd, txt: str):
        button = ttk.Button(
            wnd, text=txt, 
            command=lambda: self.dsmiss(wnd)
        )
        button.pack(side="bottom", pady=5)
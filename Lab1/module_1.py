from tkinter import *
from tkinter import ttk


class Module1:
    GROUP_LIST = ['IM-o51', 'IM-51', 'IM-52', 'IM-53', 'IM-54', 'IM-55']
    BUTTONS = ['Відміна', 'Так']

    def __init__(
        self, 
        dissmiss, 
        on_confirm = None
    ):
        self.dsmiss = dissmiss
        self.label = None
        self.on_cfm = on_confirm
        self.combobox_ = None
        self.main_func()


    def main_func(self):
        window = Toplevel()
        window.title("Modul_1")
        window.geometry("250x200")
        window.protocol(
            "WM_DELETE_WINDOW", 
            lambda: self.dsmiss(window)
        )

        self.combobox_func(window)

        for el in self.BUTTONS:
            self.btn_func(
                wnd=window, 
                txt=el
            )
            
        window.grab_set()

    def combobox_func(self, wnd):
        self.combobox_ = ttk.Combobox(
            wnd, 
            values=self.GROUP_LIST, 
            state="readonly"
        )
        self.combobox_.current(0)
        self.combobox_.pack(
            anchor=NW, 
            fill=X, 
            padx=5, 
            pady=5
        )

    def on_click_y(self, wnd, option: str):
        if option == 'Так':
            data = self.combobox_.get()
            if self.on_cfm:
                self.on_cfm(data)
        self.dsmiss(wnd)

    def btn_func(self, wnd, txt: str):
        button = ttk.Button(
            wnd, text=txt, 
            command=lambda: self.on_click_y(wnd, txt)
        )
        button.pack(side="bottom", pady=5)
from tkinter import *
from tkinter import ttk


class Module2:
    BUTTONS = ('Відміна', 'Так')

    def __init__(
        self, 
        dissmiss, 
        on_confirm = None
    ):
        self.dsmiss = dissmiss
        self.on_cfm = on_confirm
        self.editor = None
        self.main_func()


    def main_func(self):
        window = Toplevel()
        window.title("Modul_2")
        window.geometry("250x200")
        window.protocol(
            "WM_DELETE_WINDOW", 
            lambda: self.dsmiss(window)
        )

        btn_frame = ttk.Frame(window)
        btn_frame.pack(side="bottom", fill="x", pady=5)

        self.text_field(window)

        for el in self.BUTTONS:
            self.btn_func(
                frame=btn_frame, 
                wnd=window, 
                txt=el
            )
        window.grab_set()


    def text_field(self, wnd):
        self.editor = Text(wnd)
        self.editor.pack(fill=BOTH, expand=1)

    def on_click_y(self, wnd, option: str):
        if option == 'Так':
            data = self.editor.get("1.0", "end-1c")
            if self.on_cfm:
                self.on_cfm(data)
        self.dsmiss(wnd)

    def btn_func(self, frame, wnd, txt: str):
        button = ttk.Button(
            frame, text=txt, 
            command=lambda: self.on_click_y(wnd, txt)
        )
        button.pack(side="bottom", pady=5)
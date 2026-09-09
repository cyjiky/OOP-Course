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

        text_frame = ttk.Frame(
            window, 
            borderwidth=1, 
            relief=SOLID, 
            padding=[8, 10]
        )
        text_frame.pack(fill="x", padx=10, pady=10)
        self.text_field(text_frame)

        for el in self.BUTTONS:
            self.btn_func(
                btn_frame=btn_frame, 
                wnd=window, 
                txt=el
            )
        window.grab_set()


    def text_field(self, frame):
        name_label = ttk.Label(
            frame, 
            text="Write your message"
        )
        name_label.pack(anchor=NW)
    
        self.editor = Text(frame)
        self.editor.pack(
            fill=BOTH, 
            expand=1, 
            pady=(5, 0)
        )

    def on_click_y(self, wnd, option: str):
        if option == 'Так':
            data = self.editor.get("1.0", "end-1c")
            if data != "" or data != None:
                if self.on_cfm:
                    self.on_cfm(data)
        self.dsmiss(wnd)

    def btn_func(self, btn_frame, wnd, txt: str):
        button = ttk.Button(
            btn_frame, text=txt, 
            command=lambda: self.on_click_y(wnd, txt)
        )
        button.pack(side="bottom", pady=5)
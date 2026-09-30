from tkinter import Toplevel 
from tkinter import ttk

class InfoWindow:
    def __init__(self, dsmiss):
        self.dsmiss = dsmiss
        self.main_func()

    def main_func(self):
        window = Toplevel()
        window.title('Довідка')
        window.geometry("300x200")
        window.protocol(
            "WM_DELETE_WINDOW", 
            lambda: self.dsmiss(window)
        )

        frame = ttk.LabelFrame(window, text='Iнформацiя', padding=15)
        frame.pack(fill='both', expand=True, padx=15, pady=15)
    
        label = ttk.Label(
            frame,
            text=(
                "" \
                "Лабораторна робота 2\n" \
                "Варіант 15\n" \
                "Студент: Уманець Вікторія\n" \
                "Група: ІМ-o51"
            ), 
            font=("Arial", 11),
            justify='left',
        )
        label.pack(anchor="w")
        window.grab_set()

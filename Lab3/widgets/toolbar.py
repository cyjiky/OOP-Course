from __future__ import annotations
from tkinter import *
from tkinter import ttk

class ToolbarClass:
    def __init__(self, root, obj_arr, set_fnc, logo, logo_1, logo_2, logo_3):
        self.root = root
        self.OBJ = obj_arr
        self.set_obj = set_fnc
        self.logo = logo
        self.logo_1 = logo_1
        self.logo_2 = logo_2
        self.logo_3 = logo_3
        self.main_func()

    def toolbar_commads(self, button):
        tab_index = button.widget.index("current")
        val = list(self.OBJ.keys())[tab_index]
        self.set_obj(val)

    def main_func(self) -> None:
        toolbar = ttk.Notebook(self.root)
        toolbar.pack(fill=X)

        frame = ttk.Frame(toolbar)
        frame_1 = ttk.Frame(toolbar)
        frame_2 = ttk.Frame(toolbar)
        frame_3 = ttk.Frame(toolbar)

        frame.pack(fill=BOTH, expand=True)
        frame_1.pack(fill=BOTH, expand=True)
        frame_2.pack(fill=BOTH, expand=True)
        frame_3.pack(fill=BOTH, expand=True)
        toolbar.add(frame, image=self.logo, compound=LEFT)  # point
        toolbar.add(frame_1, image=self.logo_1, compound=LEFT)  # line
        toolbar.add(frame_2, image=self.logo_2, compound=LEFT)  # rectangle
        toolbar.add(frame_3, image=self.logo_3, compound=LEFT)  # ellipse

        toolbar.bind("<<NotebookTabChanged>>", self.toolbar_commads)

import os
from tkinter import *
from tkinter import ttk

class ToolbarClass:
    def __init__(self, root, logo, logo_1, logo_2, logo_3):
        self.root = root
        self.logo = logo
        self.logo_1 = logo_1
        self.logo_2 = logo_2
        self.logo_3 = logo_3
        self.main_func()

    def main_func(self):
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

        toolbar.add(frame, image=self.logo, compound=LEFT)
        toolbar.add(frame_1, image=self.logo_1, compound=LEFT)
        toolbar.add(frame_2, image=self.logo_2, compound=LEFT)
        toolbar.add(frame_3, image=self.logo_3, compound=LEFT)
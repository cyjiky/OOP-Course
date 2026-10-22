from __future__ import annotations
from tkinter import *
from tkinter import ttk

# https://www.tutorialspoint.com/article/how-do-i-display-tooltips-in-tkinter
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
    
    def show_tooltip(self, event):
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        
        self.tooltip = Toplevel()
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        label = Label(self.tooltip, text=self.text, # background="lightyellow",
            relief="solid", borderwidth=1,
            font=("Arial", 8))
        label.pack()
    
    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None


class ToolbarClass:
    def __init__(self, root, obj_arr, set_fnc):
        self.root = root
        self.OBJ = obj_arr
        self.set_obj = set_fnc
        self.curr_tool = StringVar(value='')

        self.main_func()

    def btn_func(self, root, img = None, tip: str = None, comm = None) -> None:
        button = ttk.Button(
            root, image=img, command=comm
        )
        button.pack(side='top', anchor='w', padx=5, pady=5)
        ToolTip(button, tip)

    def main_func(self) -> None:
        frame = ttk.Frame(self.root)
        frame.pack(side=LEFT, fill=Y, padx=5, pady=5)
        
        for info in self.OBJ.keys():
            self.btn_func(
                root=frame, 
                img=self.OBJ[info]['img'], 
                tip=info, 
                comm=lambda name=info, ct=self.curr_tool: self.set_obj(name=name, curr_tool=ct)
            )
from typing import List, Dict, NamedTuple
from tkinter import *
from tkinter import ttk

class CoordData(NamedTuple):
    tool: str = ''
    x1: int
    x2: int
    x3: int
    x4: int

class TableClass:
    def __init__(self, root, arr_data: CoordData = None, tools: List = []):
        self.root = root
        self.arr_data = arr_data
        self.arr: CoordData = {'', 0, 0, 0, 0}
        self.root.configure(index=0, weight=1)
        self.root.columnconfigure(index=0, weight=1)
        self.COLUMS = {
            'name': 'Назва', 
            'x1': 'x1', 
            'x2': 'x2', 
            'x3': 'x3', 
            'x4': 'x4'
        }
        self.tree = ttk.Treeview(columns=self.columns, show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)

        self.main_func()

    def irgendwelche_name(self) -> CoordData | None:
        for x in self.arr_data:
            pass 

    def main_func(self) -> None:
        # headings
        i = 1
        for k, v in self.colums:
            self.tree.heading(k, text=v, anchor=W)
            if i == 1:
                self.tree.column(
                    f'#{i}', stretch=NO, width=100
                ) 
            self.tree.column(
                f'#{i}', stretch=NO, width=60
            ) 
            i += 1

        x = 0
        if self.arr:
            for obj in self.arr: 
                self.tree.insert('', END, values=obj)
                x += 1

        if x > 5:
            self.tree.configure(yscroll=self.scrollbar.set)
            self.scrollbar.grid(row=0, column=1, sticky="ns")

    def printer(message: str | None = None, times: int = 1) -> None:
        i = 1
        if i <= times:
            if type(message) == str: 
                print(message)
            i += 1
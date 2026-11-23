from dataclasses import dataclass, field, InitVar
from typing import List, Dict, NamedTuple, Tuple
from tkinter import *
from tkinter import ttk

class TupleCoordData(NamedTuple):
    tool: str = ''
    x1: int
    x2: int
    x3: int
    x4: int

@dataclass(init=True, frozen=True)
class CoordData:
    tool: str 
    x1: int 
    x2: int = field(repr=False)
    x3: int = field(repr=False)
    x4: int = field(repr=False)
    checking: InitVar[bool] = True

    def data_checking(self, checking: bool):
        if checking:
            if self.tool != '':
                pass 
            else:
                raise ValueError

    def main_data_class(self) -> Dict[str, int] | None:
        return TupleCoordData(self.tool, self.x1, self.x2, self.x3, self.x4)

class TableClass:
    def __init__(self, root, coords: Tuple[int, int, int, int], tools: List = []):
        self.root = root
        self.arr_coords = coords
        self.tools = tools
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
        self.count: int = 1

        self.main_func()


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

        # use data class 
        def arr(self) -> TupleCoordData | None:
            name_item: str = f'item{self.count}'
            for tool in self.tools: 
                name_item = CoordData(
                    tool, self.arr_coords[0], self.arr_coords[2], self.arr_coords[3], self.arr_coords[4]
                )

        # add data
        x = 0
        if TupleCoordData:
            for obj in TupleCoordData: 
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
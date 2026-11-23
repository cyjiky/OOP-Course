from dataclasses import dataclass, field, InitVar
from typing import List, Dict, NamedTuple, Tuple
from tkinter import *
from tkinter import ttk

class TupleCoordData(NamedTuple):
    tool: str = ''
    x1: int = 0
    x2: int = 0
    x3: int = 0
    x4: int = 0


@dataclass(init=True, frozen=True)
class CoordData:
    tool: str = ''
    x1: int = 0
    x2: int = field(default=0, repr=False)
    x3: int = field(default=0, repr=False)
    x4: int = field(default=0, repr=False)
    checking: InitVar[bool] = True

    def __post_init__(self, checking: bool):
        self.data_checking(checking)

    def data_checking(self, checking: bool = True) -> None:
        if checking:
            if not self.tool:
                raise ValueError

    def main_data_class(self) -> TupleCoordData:
        return TupleCoordData(
            self.tool, self.x1, self.x2, self.x3, self.x4
        )


class TableClass:
    def __init__(
        self, 
        root, 
        coords: Tuple[int, int, int, int] = (0, 0, 0, 0), 
        tools: List = None,
    ):
        self.root = root

        self.window = Toplevel(root)
        self.window.title("Таблиця")
        self.window.geometry("380x250")
        self.window.protocol("WM_DELETE_WINDOW", self.hide)

        self.arr_coords = coords
        self.tools = tools if tools is not None else []
        self.arr: List[TupleCoordData] = []
        self.count: int = 1

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.COLUMS = {
            'name': 'Назва', 
            'x1': 'x1', 
            'x2': 'x2', 
            'x3': 'x3', 
            'x4': 'x4'
        }
        self.columns = tuple(self.COLUMS.keys())

        self.tree = ttk.Treeview(
            self.window, columns=self.columns, show="headings"
        )
        self.scrollbar = ttk.Scrollbar(
            self.window, orient=VERTICAL, command=self.tree.yview
        )
        self.tree.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.main_func()

    def main_func(self) -> None:
        for i, (k, v) in enumerate(self.COLUMS.items(), start=1):
            self.tree.heading(k, text=v, anchor=W)
            if i == 1:
                self.tree.column(f'#{i}', stretch=NO, width=120)
            else:
                self.tree.column(f'#{i}', stretch=NO, width=55)

        for tool in self.tools:
            self.add_row(tool, self.arr_coords)

    def add_row(
            self, 
            tool: str, 
            coords: Tuple[int, int, int, int] = (0, 0, 0, 0)
        ) -> TupleCoordData:
        c = (coords + (0, 0, 0, 0))[:4]
        coord_item = CoordData(
            tool=tool, 
            x1=c[0], 
            x2=c[1], 
            x3=c[2], 
            x4=c[3], 
            checking=False
        )
        tuple_item = coord_item.main_data_class()
        self.arr.append(tuple_item)
        self.tree.insert('', END, values=tuple(tuple_item))
        self.count += 1
        return tuple_item

    def clear(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.arr.clear()
        self.count = 1

    def show(self) -> None:
        self.window.deiconify()
        self.window.lift()

    def hide(self) -> None:
        self.window.withdraw()

    def toggle(self) -> None:
        if self.window.winfo_viewable():
            self.hide()
        else:
            self.show()
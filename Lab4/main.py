from __future__ import annotations
from pathlib import Path 
from typing import Type
from tkinter import *

BASE_DIR = Path(__file__).resolve().parent

from shapes import Storage
from figures import (
    Point, Line, 
    Rectangle, Ellipse, 
    LineConnector, Cube
)
from info import InfoWindow
from widgets.menu import MenuClass
from widgets.toolbar import ToolbarClass

TITLE = 'Графічний редактор'
ShapeType = type[Point | Line | Rectangle | Ellipse]

class MainClass:
    def __init__(self, root: Tk):
        self.root = root 
        self.root.title(TITLE)
        self.root.geometry("500x300") 
        self.root.option_add("*tearOff", FALSE)

        self.logo_point = PhotoImage(file="./icons/point.png")
        self.logo_line = PhotoImage(file="./icons/line.png")
        self.logo_rectangle = PhotoImage(file="./icons/rectangle.png")
        self.logo_ellipse = PhotoImage(file="./icons/ellipse.png")
        self.line_connector = PhotoImage(file="./icons/line_connector.png")
        self.logo_cube = PhotoImage(file="./icons/cube.png")

        self.OBJ = {
            'Крапка': {'command': Point, 'img': self.logo_point},
            'Лінія': {'command': Line, 'img': self.logo_line},
            'Прямокутник': {'command': Rectangle, 'img': self.logo_rectangle},
            'Еліпс': {'command': Ellipse, 'img': self.logo_ellipse},
            'LineConnector': {'command': LineConnector, 'img': self.line_connector},
            'Cube': {'command': Cube, 'img': self.logo_cube},
        }

        self.ShapeType = type[Point | Line | Rectangle | Ellipse]

        self.storage = Storage()
        self.curr: ShapeType | None = None
        self.start_x: int = 0 
        self.start_y: int = 0
        self.is_drawing: bool = False
        self.curr_tool: StringVar = StringVar(value='')

        self.toolbar_class = ToolbarClass(
            root, 
            self.OBJ, 
            self.set_obj,
            curr_tool=self.curr_tool
        )

        self.canvas = Canvas(
            bg="white", 
            width=550, 
            height=330, 
            relief="groove", 
            bd=1
        )
        self.canvas.pack(
            fill=BOTH, 
            expand=True, 
            padx=10, 
            pady=10
        )

        self.menu_class = MenuClass(
            root=root, 
            obj=self.OBJ, 
            set_fnc=self.set_obj, 
            clear_fnc=self.clear_wnd, 
            info_fnc=self.info_func,
            curr_tool=self.curr_tool
        )

        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def set_obj(self, name: str = None, curr_tool: StringVar = '') -> None:
        obj_data = self.OBJ.get(name, {})
        self.curr = obj_data.get('command')
        if curr_tool:
            curr_tool.set(name)

        tool_value = curr_tool.get() if curr_tool else ''
        root.title(f'{TITLE} - {tool_value}')
        self.notify("TOOL_CHANGED", name)

    def notify(self, message: str = None, *args) -> None:
        pass 

    def dismiss(self, window) -> None:
        window.grab_release() 
        window.destroy()

    def clear_wnd(self) -> None:
        self.storage.clear()
        self.canvas.delete('all')

    def info_func(self) -> None:
        InfoWindow(dsmiss=self.dismiss) 

    def on_press(self, new: Event[Canvas]) -> None: 
        self.start_x, self.start_y = new.x, new.y
        self.is_drawing = True

    def on_motion(self, new: Event[Canvas]) -> None:
        if not self.is_drawing or not self.curr:
            return None
        
        self.canvas.delete("rubber_band")
        cur_x, cur_y = new.x, new.y

        if self.curr == Line: 
            temp_line = Line(
                self.start_x, self.start_y, cur_x, cur_y
            )
            temp_line.draw(
                self.canvas,
                dash=(4, 2), 
                fill="black", 
                tags="rubber_band", 
            )
        elif self.curr == Rectangle:
            temp_rectangle = Rectangle(
                self.start_x, self.start_y, cur_x, cur_y
            )
            temp_rectangle.draw(
                self.canvas,
                dash=(4, 2),
                tags="rubber_band",
                fill=None
            )
        elif self.curr == Ellipse:
            temp_ellipse = Ellipse(
                self.start_x, self.start_y, cur_x, cur_y
            )
            temp_ellipse.draw(
                self.canvas,
                dash=(4, 2), 
                outline="black",
                tags="rubber_band",
                fill=None
            )
        elif self.curr == Cube:
            temp_cube = Cube(
                self.start_x, self.start_y, cur_x, cur_y
            )
            temp_cube.draw(
                self.canvas,
                dash=(4, 2),
                tags="rubber_band"
            )
        elif self.curr == LineConnector:
            temp_lineConn = LineConnector(
                self.start_x, self.start_y, cur_x, cur_y
            )
            temp_lineConn.draw(
                self.canvas,
                dash=(4, 2),
                tags="rubber_band",
                point_fill=None,
                line_fill=None
            )

    def on_release(self, new: Event[Canvas]) -> None:
        if not self.is_drawing or not self.curr:
            return None

        self.canvas.delete('rubber_band')
        self.is_drawing = False

        dx, dy = new.x, new.y

        instance = self.curr(
            self.start_x, self.start_y, dx, dy
        )

        try:
            self.storage.add(instance)
            instance.draw(self.canvas)
        except OverflowError as e:
            print(e)

if __name__ == "__main__":
    root = Tk()
    app = MainClass(root)
    root.mainloop()

from __future__ import annotations
from tkinter import *
from tkinter import ttk
from shapes import Storage
from figures import Point, Line, Rectangle, Ellipse

from menu import MenuClass
from info import InfoWindow


TITLE = 'Графічний редактор'

root = Tk()
root.title(TITLE)
root.geometry("500x300") 

root.option_add("*tearOff", FALSE)

canvas = Canvas(bg="white", width=550, height=330, relief="groove", bd=1)
canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)

storage = Storage()
curr = None
curr_name = ""
start_x, start_y = 0, 0
is_drawing = False

OBJ = {
    'Крапка': Point,
    'Лінія': Line,
    'Прямокутник': Rectangle,
    'Еліпс': Ellipse,
}

def dismiss(window) -> None:
    window.grab_release() 
    window.destroy()

def set_obj(name) -> None:
    global curr, curr_name
    curr = OBJ.get(name)
    curr_name = name
    root.title(f'{TITLE} - {name}')

def clear_wnd() -> None:
    storage.clear()
    canvas.delete('all')

def info_func() -> None:
    InfoWindow(dsmiss=dismiss) 

MenuClass(root=root, obj=OBJ, set_fnc=set_obj, clear_fnc=clear_wnd, info_fnc=info_func)

def on_press(new) -> None: 
    global start_x, start_y, is_drawing
    start_x, start_y = new.x, new.y
    is_drawing = True

def on_motion(new) -> None:
    if not is_drawing or not curr:
        return None
    
    canvas.delete("rubber_band")
    cur_x, cur_y = new.x, new.y

    if curr == Point:
        pass 
    elif curr == Line:
        canvas.create_line(
            start_x, start_y,
            cur_x, cur_y,
            dash=(4, 2), fill="black",
            tags="rubber_band"
        )
    elif curr == Rectangle:
        x2 = 2 * start_x - cur_x
        y2 = 2 * start_y - cur_y
        canvas.create_rectangle(
            cur_x, cur_y,
            x2, y2,
            dash=(4, 2), 
            outline="black",
            tags="rubber_band"
        )
    elif curr == Ellipse:
        canvas.create_oval(
            start_x, start_y,
            cur_x, cur_y,
            dash=(4, 2), 
            outline="black",
            tags="rubber_band"
        )

def on_release(new):
    global is_drawing
    if not is_drawing or not curr:
        return 

    canvas.delete('rubber_band')
    is_drawing = False

    dx, dy = new.x, new.y

    instance = curr(start_x, start_y, dx, dy)

    try:
        storage.add(instance)
        instance.draw(canvas)
    except OverflowError as e:
        print(e)

canvas.bind("<Button-1>", on_press)
canvas.bind("<B1-Motion>", on_motion)
canvas.bind("<ButtonRelease-1>", on_release)

if __name__ == "__main__":
    root.mainloop()

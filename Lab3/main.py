from tkinter import *
from shapes import Storage
from figures import Point, Line, Rectangle, Ellipse

from info import InfoWindow
from widgets.menu import MenuClass
from widgets.toolbar import ToolbarClass

TITLE = 'Графічний редактор'

root = Tk()
root.title(TITLE)
root.geometry("500x300") 

root.option_add("*tearOff", FALSE)

logo_point = PhotoImage(file="./icons/point.png")
logo_line = PhotoImage(file="./icons/line.png")
logo_rectangle = PhotoImage(file="./icons/rectangle.png")
logo_ellipse = PhotoImage(file="./icons/ellipse.png")

OBJ = {
    'Крапка': {'command': Point, 'img': logo_point},
    'Лінія': {'command': Line, 'img': logo_line},
    'Прямокутник': {'command': Rectangle, 'img': logo_rectangle},
    'Еліпс': {'command': Ellipse, 'img': logo_ellipse},
}

def set_obj(name: str = None) -> None:
    global curr, curr_name
    obj_data = OBJ.get(name, {})
    curr = obj_data.get('command')
    curr_name = name
    root.title(f'{TITLE} - {name}')

ToolbarClass(root, OBJ, set_obj, logo_point, logo_line, logo_rectangle, logo_ellipse)

canvas = Canvas(
    bg="white", 
    width=550, 
    height=330, 
    relief="groove", 
    bd=1
)
canvas.pack(
    fill=BOTH, 
    expand=True, 
    padx=10, 
    pady=10
)

ShapeType = type[Point | Line | Rectangle | Ellipse]

storage = Storage()
curr: ShapeType | None = None
curr_name: str = ""
start_x, start_y = 0, 0
is_drawing: bool = False


def dismiss(window) -> None:
    window.grab_release() 
    window.destroy()

def clear_wnd() -> None:
    storage.clear()
    canvas.delete('all')

def info_func() -> None:
    InfoWindow(dsmiss=dismiss) 

MenuClass(
    root=root, 
    obj=OBJ, 
    set_fnc=set_obj, 
    clear_fnc=clear_wnd, 
    info_fnc=info_func
)

def on_press(new) -> None: 
    global start_x, start_y, is_drawing
    start_x, start_y = new.x, new.y
    is_drawing = True

def on_motion(new) -> None:
    if not is_drawing or not curr:
        return None
    
    canvas.delete("rubber_band")
    cur_x, cur_y = new.x, new.y

    if curr == Line:
        canvas.create_line(
            start_x, start_y,
            cur_x, cur_y,
            fill="black",
            tags="rubber_band"
        )
    elif curr == Rectangle:
        canvas.create_rectangle(
            start_x, start_y,
            cur_x, cur_y,

            outline="black",
            tags="rubber_band"
        )
    elif curr == Ellipse:
        x2 = 2 * start_x - cur_x
        y2 = 2 * start_y - cur_y
        canvas.create_oval(
            cur_x, cur_y,
            x2, y2,

            outline="black",
            tags="rubber_band"
        )

def on_release(new) -> None:
    global is_drawing
    if not is_drawing or not curr:
        return None

    canvas.delete('rubber_band')
    is_drawing = False

    dx, dy = new.x, new.y

    instance = curr(
        start_x, start_y, dx, dy
    )

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

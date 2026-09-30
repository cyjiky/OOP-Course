from tkinter import *
from tkinter import ttk
from shapes import Storage
from figures import Point, Line, Rectangle, Ellipse

TITLE = 'Графічний редактор'

root = Tk()
root.title(TITLE)
root.geometry("500x300") 

root.option_add("*tearOff", FALSE)

canvas = Canvas(bg="white", width=400, height=250, relief="groove", bd=1)
canvas.pack(anchor=CENTER, expand=True, pady=10)

storage = Storage()
curr = None
start_x, start_y = 0, 0

obj_menu = Menu()
main_menu = Menu()

MENU = [
    {"name": 'Файл', "command": None, "menu": None},
    {"name": "Oб'єкти", "command": None, "menu": obj_menu},
    {"name": 'Довідка', "command": None, "menu": None},
]

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
    global curr 
    curr = OBJ.get(name)
    root.title(f'{TITLE} - {name}')

def on_press(new) -> None: 
    global start_x, start_y
    start_x, start_y = new.x, new.y

def on_release(new):
    if not curr:
        return 

    instance = curr(start_x, start_y, new.x, new.y)
    instance.draw(canvas)

    try:
        storage.add(instance)
    except OverflowError as e:
        print(e)

canvas.bind("<Button-1>", on_press)
canvas.bind("<ButtonRelease-1>", on_release)

# main_menu
for item in MENU: 
    main_menu.add_cascade(
        label=item["name"],
        command=item["command"],
        menu=item["menu"]
    )

# obj_menu
for key, val in OBJ.items():
    obj_menu.add_cascade(
        label=key, 
        command=lambda name=key: set_obj(name)
    )

root.config(menu=main_menu)
root.mainloop()

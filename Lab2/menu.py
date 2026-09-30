from tkinter import *
from tkinter import ttk

class MenuClass:

    def __init__(self, root, obj, set_fnc, clear_fnc=None, info_fnc=None):
        self.root = root 
        self.OBJ = obj 
        self.set_obj = set_fnc
        self.clear_fnc = clear_fnc
        self.info_fnc = info_fnc
        self.build_menu()

    def build_menu(self):
        main_menu = Menu(self.root)
        obj_menu = Menu(main_menu)
        file_menu = Menu(main_menu)

        MENU = [
            {"name": 'Файл', "command": None, "menu": file_menu},
            {"name": "Oб'єкти", "command": None, "menu": obj_menu},
            {"name": 'Довідка', "command": self.info_fnc, "menu": None},
        ]

        # main_menu
        for item in MENU: 
            main_menu.add_cascade(
                label=item["name"],
                command=item["command"],
                menu=item["menu"]
            )

        # obj_menu
        for key, val in self.OBJ.items():
            obj_menu.add_command(
                label=key, 
                command=lambda name=key: self.set_obj(name)
            )

        # file_menu
        file_menu.add_command(label="Очистити", command=self.clear_fnc)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=self.root.quit)

        self.root.config(menu=main_menu)
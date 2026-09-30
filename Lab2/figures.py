from tkinter import Canvas
from shapes import PointsShape

class Point(PointsShape):
    def draw(self, canvas: Canvas) -> None:
        canvas.create_oval(
            self.org_x - 1, 
            self.org_y - 1, 
            self.org_x + 1, 
            self.org_y + 1, 
            fill="black", 
            outline="black"
        )

class Line(PointsShape):
    def draw(self, canvas: Canvas) -> None:
        canvas.create_line(*self.coords, fill="black")

class Ellipse(PointsShape):
    def draw(self, canvas: Canvas) -> None:
        canvas.create_oval(*self.coords, outline="black")

class Rectangle(PointsShape):
    def draw(self, canvas: Canvas) -> None:
        canvas.create_rectangle(*self.coords, outline="black")
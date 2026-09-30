from tkinter import Canvas
from shapes import PointsShape

class Point(PointsShape):
    def draw(self, canvas: Canvas) -> None:
        r = 2
        canvas.create_oval(
            self.org_x - r, 
            self.org_y - r, 
            self.org_x + r, 
            self.org_y + r, 
            fill="black", 
            outline="black"
        )

class Line(PointsShape):
    def draw(self, canvas: Canvas) -> None:
        canvas.create_line(*self.coords, fill="purple")

class Ellipse(PointsShape):
    def draw(self, canvas: Canvas) -> None:
        canvas.create_oval(*self.coords, outline="black", fill='light sky blue')

class Rectangle(PointsShape):
    def draw(self, canvas: Canvas) -> None:
        self.org_x, self.org_y, dx, dy = self.coords

        dx2 = 2 * self.org_x - dx 
        dy2 = 2 * self.org_y - dy
        canvas.create_rectangle(dx, dy, dx2, dy2, outline="black", fill='pink')
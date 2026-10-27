from tkinter import Canvas
from shapes import PointsShape
import math

class Point(PointsShape):
    def draw(self, canvas: Canvas, fill: str | bool = "black", radius: int = 2) -> None:
        r = radius
        canvas.create_oval(
            self.org_x - r, 
            self.org_y - r, 
            self.org_x + r, 
            self.org_y + r, 
            fill=fill, 
            outline="black"
        )

class Line(PointsShape):
    def draw(self, canvas: Canvas, fill: str | None = "purple") -> None:
        canvas.create_line(*self.coords, fill=fill)

class Ellipse(PointsShape):
    def draw(self, canvas: Canvas) -> None:
        self.org_x, self.org_y, dx, dy = self.coords
        dx2 = 2 * self.org_x - dx 
        dy2 = 2 * self.org_y - dy
        canvas.create_oval(dx, dy, dx2, dy2, outline="black", fill='#FF9933')

class Rectangle(PointsShape):
    def draw(self, canvas: Canvas, fill: str | bool = '#FFB226') -> None:
        canvas.create_rectangle(
            *self.coords, 
            outline="black", 
            fill=fill
        )

class LineConnector(Line, Point):
    def draw(self, canvas: Canvas, point_fill: str | bool = None, line_fill: str | bool = None, r=8) -> None:
        x1, y1, x2, y2 = self.coords
        self.org_x, self.org_y = x1, y1
        Point.draw(self, canvas, radius=r, fill=point_fill)

        dx = x2 - x1
        dy = y2 - y1 
        distance = math.hypot(dx, dy) # відстань між точками

        new_x1 = x1 + r * (dx / distance)
        new_y1 = y1 + r * (dy / distance)

        _old_coords = self.coords
        self.coords = (new_x1, new_y1, x2, y2)
        Line.draw(self, canvas, line_fill)
        
        self.coords = _old_coords

        new_org_x2 = x2 + r * (dx / distance)
        new_org_y2 = y2 + r * (dy / distance)
        self.org_x, self.org_y = new_org_x2, new_org_y2
        Point.draw(self, canvas, radius=r, fill=point_fill)

class Cube(Rectangle, Line):
    def draw(self, canvas: Canvas) -> None:
        x1, y1, x2, y2 = self.coords
        
        offset_x, offset_y = 15, -15
        x1_2, y1_2, x2_2, y2_2 = x1 + offset_x, y1 + offset_y, x2 + offset_x, y2 + offset_y
        Rectangle.draw(self, canvas, fill=None)

        _old_coords = self.coords
        arr_1 = [(x1, y1), (x2, y1), (x2, y1), (x2, y2)]
        arr_2 = [(x1_2, y1_2), (x2_2, y1_2), (x2_2, y1_2), (x2_2, y2_2)]

        for (c1_x, c1_y), (c2_x, c2_y) in zip(arr_1, arr_2):
            self.coords = (c1_x, c1_y, c2_x, c2_y)
            Line.draw(self, canvas, fill=None)

        self.coords = (x1_2, y1_2, x2_2, y2_2)
        Rectangle.draw(self, canvas, fill=None)
        
        self.coords = _old_coords
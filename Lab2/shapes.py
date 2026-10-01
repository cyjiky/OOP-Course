from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator

from tkinter import Canvas

class Shape(ABC):
    @abstractmethod
    def draw(self, canvas: Canvas):
        pass 

class PointsShape(Shape):
    def __init__(self, start_x: int, start_y: int, x: int, y: int):
        self.org_x = start_x
        self.org_y = start_y
        self.dx = x 
        self.dy = y

    @property
    def coords(self) -> Tuple[int, int, int, int]: 
        return (self.org_x, self.org_y, self.dx, self.dy)

class Storage:
    MAX = 115 

    def __init__(self): 
        self._shapes: List[Shape] = []

    def add(self, other: Shape) -> None:
        if not isinstance(other, Shape):
            raise TypeError('...')

        if len(self._shapes) > self.MAX:
            raise OverflowError('...')

        self._shapes.append(other)

    def __len__(self) -> int:
        return len(self._shapes)

    def __iter__(self) -> Iterator[Shape]:
        return iter(self._shapes)

    def clear(self) -> None:
        self._shapes.clear()
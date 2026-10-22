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
    MAX: int = 116

    def __init__(self): 
        self._shapes: List[Shape | None] = [None] * self.MAX
        self._count: int = 0

    def add(self, other: Shape) -> None:
        if not isinstance(other, Shape):
            raise TypeError('Expected Shape')

        if self._count >= self.MAX:
            raise OverflowError('Storage is full')

        self._shapes[self._count] = other
        self._count += 1 

    def __len__(self) -> int:
        return self._count

    def __iter__(self) -> Iterator[Shape]:
        return iter(self._shapes[:self._count])

    def clear(self) -> None:
        self._shapes = [None] * self.MAX
        self._count = 0
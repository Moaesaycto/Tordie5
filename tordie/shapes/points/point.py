from tordie.shapes.base.vertex import Vertex
from math import cos, sin, atan2, sqrt


class Point(Vertex):
    def __init__(self, x: float, y: float, polar: bool = False) -> None:
        if polar:
            self._x = x * cos(y)
            self._y = x * sin(y)
        else:
            self._x = x
            self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        self._y = value

    @property
    def r(self) -> float:
        return sqrt(self._x ** 2 + self._y ** 2)

    @r.setter
    def r(self, value: float) -> None:
        theta = self.theta
        self._x = value * cos(theta)
        self._y = value * sin(theta)

    @property
    def theta(self) -> float:
        return atan2(self._y, self._x)

    @theta.setter
    def theta(self, value: float) -> None:
        r = self.r
        self._x = r * cos(value)
        self._y = r * sin(value)

    def render(self):
        pass

    def __str__(self) -> str:
        return f"Cartesian Point: ({round(self.x, 3)}, {round(self.y, 3)})"

    def __repr__(self) -> str:
        return str(self)

    def simple_str(self) -> str:
        return f"({round(self.x, 3)}, {round(self.y, 3)})"

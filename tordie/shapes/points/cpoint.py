from tordie.shapes.base.point import Point


class CPoint(Point):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def render(self):
        pass

    def __str__(self) -> str:
        return f"Cartesian Point: ({round(self.x, 3)}, {round(self.y, 3)})"

    def __repr__(self):
        return str(self)

    def simple_str(self) -> str:
        return f"({round(self.x, 3)}, {round(self.y, 3)})"

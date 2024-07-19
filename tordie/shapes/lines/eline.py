from tordie.shapes.base import Point, Line


class ELine(Line):
    def __init__(self, start: Point, end: Point) -> None:
        super().__init__(start, end)

    def render(self):
        pass

    def __str__(self) -> str:
        return f"Euclidean Line: {self.start.simple_str()} -> {self.end.simple_str()}"

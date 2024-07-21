from tordie.shapes.base import Vertex, Line


class ELine(Line):
    def __init__(self, start: Vertex, end: Vertex) -> None:
        """Create a new Euclidean line.

        Args:
            start (Vertex): Start of the line.
            end (Vertex): End of the line.
        """
        super().__init__(start, end)

    def render(self):
        pass

    def __str__(self) -> str:
        return f"Euclidean Line: {self.start.simple_str()} -> {self.end.simple_str()}"

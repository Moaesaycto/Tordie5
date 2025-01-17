from tordie.shapes.base import Vertex
from tordie.options import Options
from tordie.shapes.base import Line

class ELine(Line):
    def __init__(
        self,
        start: Vertex,
        end: Vertex,
        show_ends: bool = False,
        stroke: str = None,
        stroke_width: float = None,
        alt: int = 0
    ) -> None:
        """Create a new Euclidean line.

        Args:
            start (Vertex): Start of the line.
            end (Vertex): End of the line.
            show_ends (bool, optional): If True, show the start and end points of the line. Defaults to False.
        """
        super().__init__(stroke, stroke_width, alt)
        self.start = start
        self.end = end
        self.show_ends = show_ends

    def render(self, options: Options) -> str:
        """Render the line on an SVG drawing.

        Args:
            options (Options): The rendering options.

        Returns:
            str: SVG element as string.
        """
        startx, starty = options.relative(self.start.x, self.start.y)
        endx, endy = options.relative(self.end.x, self.end.y)
        
        stroke = self.determine_stroke(options)
        stroke_width = self.determine_stroke_width(options)
        
        line_svg = (f'<line x1="{startx}" y1="{starty}" '
                    f'x2="{endx}" y2="{endy}" '
                    f'stroke="{stroke}" '
                    f'stroke-width="{stroke_width}" />')
        
        if self.show_ends:
            start_svg = self.start.render(options)
            end_svg = self.end.render(options)
            return line_svg + start_svg + end_svg

        return line_svg

    def __str__(self) -> str:
        return f"Euclidean Line: {self.start.simple_str()} -> {self.end.simple_str()}"

    def __repr__(self) -> str:
        return str(self)

from tordie.shapes.base.shape import Shape
from abc import ABC
from tordie.options import Options

class Line(Shape, ABC):
    def __init__(self, stroke: str = None, stroke_width: float = None, alt: int = 0) -> None:
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.alt = alt

    def determine_stroke(self, options: Options) -> str:
        stroke = options.line_stroke
        if self.stroke is None:
            if self.alt >= 1:
                index = min(max(self.alt - 1, 0), len(options.line_stroke_alts) - 1)
                stroke = options.line_stroke_alts[index]
        else:
            stroke = self.stroke
        return stroke

    def determine_stroke_width(self, options: Options) -> float:
        return options.stroke_width if self.stroke_width is None else self.stroke_width

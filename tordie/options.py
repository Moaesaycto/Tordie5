from typing import List, Tuple

# DEFAULT OPTIONS FOR TORDIE
# GENERAL
DEFAULT_FILENAME = "drawing.svg"

# POINT OPTIONS
POINT_DEFAULT_RADIUS: int = 3
POINT_DEFAULT_STROKE: str = "black"

# LINE OPTIONS
LINE_DEFAULT_WIDTH: int = 2
LINE_DEFAULT_STROKE: str = "black"
LINE_DEFAULT_STROKE_ALTS: List[str] = ["red", "blue", "black"]

# DOCUMENT OPTIONS
DOCUMENT_BACKGROUND: str = "white"
DOCUMENT_WIDTH: int = 800
DOCUMENT_HEIGHT: int = 800
DOCUMENT_BOUNDS: int = 16

# MATHEMATICS OPTIONS
MATHEMATICS_SCALE: Tuple[int, int] = (1, 1)

class Options():
    def __init__(
        self,
        filename: str = DEFAULT_FILENAME,
        stroke_width: int = LINE_DEFAULT_WIDTH,
        point_radius: int = POINT_DEFAULT_RADIUS,
        point_stroke: str = POINT_DEFAULT_STROKE,
        line_stroke: str = LINE_DEFAULT_STROKE,
        line_stroke_alts: List[str] = LINE_DEFAULT_STROKE_ALTS,
        document_background: str = DOCUMENT_BACKGROUND,
        document_width: int = DOCUMENT_WIDTH,
        document_height: int = DOCUMENT_HEIGHT,
        document_bounds: int = DOCUMENT_BOUNDS,
        mathematics_scale: Tuple[int, int] = MATHEMATICS_SCALE,
    
    ) -> None:
        self.filename = filename
        self.point_radius = point_radius
        self.point_stroke = point_stroke
        self.line_stroke = line_stroke
        self.line_stroke_alts = line_stroke_alts
        self.stroke_width = stroke_width
        self.document_background = document_background
        self.document_width = document_width
        self.document_height = document_height
        self.document_bounds = document_bounds
        self.mathematics_scale = mathematics_scale

    def relative(self, x: float, y: float) -> Tuple[float, float]:
        """Calculate the relative position of a point in the drawing.

        Args:
            x (float): Coordinate x
            y (float): Coordinate y

        Returns:
            Tuple[float]: Relative position of the point
        """
        return (
            x / 2 * float(self.document_width / self.mathematics_scale[0]) + (
                self.document_width + self.document_bounds) / 2,
            -y / 2 * float(self.document_height / self.mathematics_scale[1]) + (
                self.document_height + self.document_bounds) / 2
        )

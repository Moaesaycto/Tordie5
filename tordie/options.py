from typing import Tuple

# DEFAULT OPTIONS FOR TORDIE
# GENERAL
DEFAULT_FILENAME = "drawing.svg"
DEFAULT_STROKE: str = "black"

# POINT OPTIONS
POINT_DEFAULT_RADIUS: int = 3

# LINE OPTIONS
LINE_DEFAULT_WIDTH: int = 2

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
        stroke: str = DEFAULT_STROKE,
        point_radius: int = POINT_DEFAULT_RADIUS,
        line_width: int = LINE_DEFAULT_WIDTH,
        document_background: str = DOCUMENT_BACKGROUND,
        document_width: int = DOCUMENT_WIDTH,
        document_height: int = DOCUMENT_HEIGHT,
        document_bounds: int = DOCUMENT_BOUNDS,
        mathematics_scale: Tuple[int, int] = MATHEMATICS_SCALE,
    ) -> None:
        self.filename = filename
        self.stroke = stroke
        self.point_radius = point_radius
        self.line_width = line_width
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

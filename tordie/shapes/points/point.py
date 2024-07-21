from tordie.shapes.base.vertex import Vertex
from math import cos, sin, atan2, sqrt
from tordie.options import Options

class Point(Vertex):
    def __init__(
        self,
        x: float,
        y: float,
        polar: bool = False,
        stroke: str = None,
        point_radius: float = None,
    ) -> None:
        """Create a new point.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
            polar (bool, optional): If True, the coordinates are interpreted as polar coordinates. Defaults to False.
            stroke (str, optional): The stroke color of the point. Defaults to 'black'.
            point_radius (float, optional): The radius of the point. Defaults to 5.0.
        """
        super().__init__(stroke, point_radius)
        if polar:
            self._x = x * cos(y)
            self._y = x * sin(y)
        else:
            self._x = x
            self._y = y

    @property
    def x(self) -> float:
        """The x-coordinate of the point."""
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        """Set the x-coordinate of the point."""
        self._x = value

    @property
    def y(self) -> float:
        """The y-coordinate of the point."""
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        """Set the y-coordinate of the point."""
        self._y = value

    @property
    def r(self) -> float:
        """The distance from the origin to the point."""
        return sqrt(self._x ** 2 + self._y ** 2)

    @r.setter
    def r(self, value: float) -> None:
        """Set the distance from the origin to the point."""
        theta = self.theta
        self._x = value * cos(theta)
        self._y = value * sin(theta)

    @property
    def theta(self) -> float:
        """The angle between the positive x-axis and the line segment connecting the origin and the point."""
        return atan2(self._y, self._x)

    @theta.setter
    def theta(self, value: float) -> None:
        """Set the angle between the positive x-axis and the line segment connecting the origin and the point."""
        r = self.r
        self._x = r * cos(value)
        self._y = r * sin(value)

    def __str__(self) -> str:
        return f"Cartesian Point: ({round(self.x, 3)}, {round(self.y, 3)})"

    def __repr__(self) -> str:
        return str(self)

    def simple_str(self) -> str:
        """Return a simplified string representation of the point in Cartesian coordinates."""
        return f"({round(self.x, 3)}, {round(self.y, 3)})"

    def render(self, options: Options) -> str:
        """Render the point on an SVG drawing.

        Args:
            options (Options): The rendering options.

        Returns:
            str: SVG element as string.
        """
        cx, cy = options.relative(self.x, self.y)

        stroke = self.determine_stroke(options)
        point_radius = self.determine_point_radius(options)

        svg_circle = f'<circle cx="{cx}" cy="{cy}" r="{point_radius}" fill="{stroke}" stroke="{stroke}" stroke-width="0"/>'
        return svg_circle

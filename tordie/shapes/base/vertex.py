from abc import ABC, abstractmethod
from tordie.shapes.base.shape import Shape
from tordie.options import Options

class Vertex(Shape, ABC):
    def __init__(self, stroke: str = None, point_radius: float = None) -> None:
        self.stroke = stroke
        self.point_radius = point_radius

    def determine_stroke(self, options: Options) -> str:
        return options.point_stroke if self.stroke is None else self.stroke

    def determine_point_radius(self, options: Options) -> float:
        return options.point_radius if self.point_radius is None else self.point_radius

    @abstractmethod
    def simple_str(self) -> str:
        """Return a simple string representation of the vertex.

        Returns:
            str: A simple string representation of the vertex.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the vertex.

        Returns:
            str: A string representation of the vertex.
        """
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        """Return a string representation of the vertex.

        Returns:
            str: A string representation of the vertex.
        """
        pass
    
    @abstractmethod
    def render(self, options: Options) -> str:
        """Render the vertex onto an SVG document.

        Args:
            drawing (SVGDocument): The SVG document to render onto.

        Returns:
            str: SVG element as string.
        """
        pass

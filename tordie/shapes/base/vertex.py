from abc import ABC, abstractmethod
from tordie.shapes.base.shape import Shape
from tordie.options import Options

class Vertex(Shape, ABC):
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
    def render(self, options: Options) -> None:
        """Render the vertex onto an SVG document.

        Args:
            drawing (SVGDocument): The SVG document to render onto.
        """
        pass
    
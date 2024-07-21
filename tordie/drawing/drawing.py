from typing import List, Optional
from .svgdocument import SVGDocument
from tordie.shapes.base.shape import Shape
from ..options import Options
from svgwrite.drawing import Drawing as SVGDrawing
import xml.etree.ElementTree as ET

DEFAULT_OPTIONS = Options()


class Drawing(SVGDocument):
    def __init__(self, options: Options = DEFAULT_OPTIONS) -> None:
        """Create a new drawing.

        Args:
            options (Options, optional): Custom options for the drawing. Defaults to DEFAULT_OPTIONS.
        """
        super().__init__(options)
        self._shapes: List[Shape] = []
        self._drawing: Optional[SVGDrawing] = None

    def __str__(self) -> str:
        """Returns the description of the drawing.

        Returns:
            str: Description of the drawing.
        """
        return f"Drawing: {len(self._shapes)} shapes"

    def __repr__(self) -> str:
        """Returns the string representation of the drawing.

        Returns:
            str: String representation of the drawing.
        """
        return self.__str__()

    def __len__(self) -> int:
        """Return the number of shapes in the drawing.

        Returns:
            int: Number of shapes in the drawing.
        """
        return len(self._shapes)

    def __iter__(self):
        """Iterate over the shapes in the drawing.

        Returns:
            _type_: An iterator over the shapes in the drawing.
        """
        return iter(self._shapes)

    def __getitem__(self, index: int) -> Shape:
        """Get a shape from the drawing.

        Args:
            index (int): Index of the shape to get.

        Returns:
            Shape: The shape at the index.
        """
        return self._shapes[index]

    def __setitem__(self, index: int, value: Shape) -> None:
        """Set a shape in the drawing.

        Args:
            index (int): Index of the shape to set.
            value (Shape): The shape to set.
        """
        self._shapes[index] = value

    def __delitem__(self, index: int) -> None:
        """Remove a shape from the drawing.

        Args:
            index (int): Index of the shape to remove.
        """
        del self._shapes[index]

    def save(self, filename: str = "drawing.svg") -> None:
        """Save the drawing to an SVG file.

        Args:
            filename (str, optional): Filename for saved SVG file. Defaults to "drawing.svg".
        """
        self.render()
        if self._drawing:
            self._drawing.saveas(filename)

    def add_shape(self, *shapes: Shape) -> None:
        """Add a shape to the drawing.
        """
        for shape in shapes:
            self._shapes.append(shape)

    def remove_shape(self, shape: Shape) -> None:
        """Remove a shape from the drawing.

        Args:
            shape (Shape): The shape to remove.
        """
        self._shapes.remove(shape)

    def clear(self) -> None:
        """Clear the drawing of all shapes.
        """
        self._shapes.clear()

    def render(self) -> None:
        """Render the drawing to an SVG document."""
        self._drawing = SVGDrawing(size=(f"{self._options.document_width + self._options.document_bounds}px",
                                         f"{self._options.document_height + self._options.document_bounds}px"))
        self._drawing.add(
            self._drawing.rect(
                insert=(0, 0),
                size=('100%', '100%'),
                fill=self._options.document_background
            )
        )

        shape_funcs = {
            'circle': lambda a: self._drawing.circle(center=(a['cx'], a['cy']), r=a['r'], fill=a['fill'], stroke=a['stroke'], stroke_width=a.get('stroke-width', 0)),
            'rect': lambda a: self._drawing.rect(insert=(a['x'], a['y']), size=(a['width'], a['height']), fill=a['fill'], stroke=a['stroke'], stroke_width=a.get('stroke-width', 0)),
            'line': lambda a: self._drawing.line(start=(a['x1'], a['y1']), end=(a['x2'], a['y2']), stroke=a['stroke'], stroke_width=a.get('stroke-width', 0)),
            'ellipse': lambda a: self._drawing.ellipse(center=(a['cx'], a['cy']), r=(a['rx'], a['ry']), fill=a['fill'], stroke=a['stroke'], stroke_width=a.get('stroke-width', 0)),
            'polygon': lambda a: self._drawing.polygon(points=a['points'], fill=a['fill'], stroke=a['stroke'], stroke_width=a.get('stroke-width', 0)),
            'path': lambda a: self._drawing.path(d=a['d'], fill=a['fill'], stroke=a['stroke'], stroke_width=a.get('stroke-width', 0))
        }

        for shape in self._shapes:
            svg_elements = shape.render(self._options)
            
            # Wrap multiple elements in a root element
            elements = ET.fromstring(f"<root>{svg_elements}</root>")
            for element in elements:
                tag = element.tag.split('}')[-1]  # Remove namespace if present
                if tag in shape_funcs:
                    self._drawing.add(shape_funcs[tag](element.attrib))

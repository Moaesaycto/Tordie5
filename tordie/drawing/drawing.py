from typing import List, Optional
from abc import ABC, abstractmethod
from .svgdocument import SVGDocument
from tordie.shapes.base.shape import Shape
from ..options import Options
from svgwrite.drawing import Drawing as SVGDrawing

DEFAULT_OPTIONS = Options()


class Drawing(SVGDocument, ABC):
    def __init__(
        self,
        options: Options = DEFAULT_OPTIONS
    ) -> None:
        super().__init__(options)
        self._shapes: List[Shape] = []
        self._drawing: Optional[SVGDrawing] = None

    def save(self, filename: str = "drawing.svg") -> None:
        self.render()
        if self._drawing:
            self._drawing.saveas(filename)

    def add_shape(self, shape: Shape) -> None:
        self._shapes.append(shape)

    def remove_shape(self, shape: Shape) -> None:
        self._shapes.remove(shape)

    def clear(self) -> None:
        self._shapes.clear()

    def render(self) -> None:
        del self._drawing
        size = (
            f"{self._options.document_width + self._options.document_bounds}px",
            f"{self._options.document_height + self._options.document_bounds}px"
        )
        self._drawing = SVGDrawing(filename=self._options.filename, size=size)

    def __str__(self) -> str:
        return f"Drawing: {len(self._shapes)} shapes"

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self._shapes)

    def __iter__(self):
        return iter(self._shapes)

    def __getitem__(self, index: int) -> Shape:
        return self._shapes[index]

    def __setitem__(self, index: int, value: Shape) -> None:
        self._shapes[index] = value

    def __delitem__(self, index: int) -> None:
        del self._shapes[index]

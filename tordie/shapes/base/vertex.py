from abc import ABC, abstractmethod
from tordie.shapes.base.shape import Shape


class Vertex(Shape, ABC):
    pass

    @abstractmethod
    def simple_str(self) -> str:
        pass

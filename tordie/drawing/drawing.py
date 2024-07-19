from .svgdocument import SVGDocument
from tordie.shapes.base.shape import Shape


class Drawing(SVGDocument):
    def __init__(self):
        self._shapes = []

    def save(self, filename: str):
        pass

    def add_shape(self, shape: Shape):
        self._shapes.append(shape)

    def remove_shape(self, shape: Shape):
        self._shapes.remove(shape)

    def clear(self):
        self._shapes.clear()

    def render(self):
        pass

    def __str__(self):
        print(f"Drawing: {len(self._shapes)} shapes")

    def __repr__(self):
        return f"Drawing: {len(self._shapes)} shapes"

    def __len__(self):
        return len(self._shapes)

    def __iter__(self):
        return iter(self._shapes)

    def __getitem__(self, index):
        return self._shapes[index]

    def __setitem__(self, index, value):
        self._shapes[index] = value

    def __delitem__(self, index):
        del self._shapes[index]

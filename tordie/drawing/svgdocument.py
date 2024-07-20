from abc import ABC, abstractmethod
from ..options import Options


class SVGDocument(ABC):
    def __init__(self, options):
        self._options : Options = options

    @abstractmethod
    def save(self, filename: str):
        pass

    @abstractmethod
    def add_shape(self, shape):
        pass

    @abstractmethod
    def remove_shape(self, shape):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __getitem__(self, index):
        pass

    @abstractmethod
    def __setitem__(self, index, value):
        pass

    @abstractmethod
    def __delitem__(self, index):
        pass

from abc import ABC, abstractmethod
from ..options import Options

class SVGDocument(ABC):
    def __init__(self, options):
        """Create a new SVG document.

        Args:
            options (Options): The options for the SVG document.
        """
        self._options : Options = options
    
    @property
    def options(self):
        """Get the options for the SVG document.

        Returns:
            Options: The options for the SVG document.
        """
        return self._options
    
    @options.getter
    def options(self):
        """Get the options for the SVG document.

        Returns:
            Options: The options for the SVG document.
        """
        return self._options

    @abstractmethod
    def save(self, filename: str):
        """Save the SVG document to a file.

        Args:
            filename (str): The name of the file to save the SVG document to.
        """
        pass

    @abstractmethod
    def add_shape(self, shape):
        """Add a shape to the SVG document.

        Args:
            shape: The shape to add to the SVG document.
        """
        pass

    @abstractmethod
    def remove_shape(self, shape):
        """Remove a shape from the SVG document.

        Args:
            shape: The shape to remove from the SVG document.
        """
        pass

    @abstractmethod
    def clear(self):
        """Clear all shapes from the SVG document."""
        pass

    @abstractmethod
    def render(self):
        """Render the SVG document."""
        pass

    @abstractmethod
    def __str__(self):
        """Get a string representation of the SVG document.

        Returns:
            str: A string representation of the SVG document.
        """
        pass

    @abstractmethod
    def __repr__(self):
        """Get a string representation of the SVG document.

        Returns:
            str: A string representation of the SVG document.
        """
        pass

    @abstractmethod
    def __len__(self):
        """Get the number of shapes in the SVG document.

        Returns:
            int: The number of shapes in the SVG document.
        """
        pass

    @abstractmethod
    def __iter__(self):
        """Iterate over the shapes in the SVG document.

        Yields:
            shape: The next shape in the SVG document.
        """
        pass

    @abstractmethod
    def __getitem__(self, index):
        """Get the shape at the specified index in the SVG document.

        Args:
            index: The index of the shape to get.

        Returns:
            shape: The shape at the specified index in the SVG document.
        """
        pass

    @abstractmethod
    def __setitem__(self, index, value):
        """Set the shape at the specified index in the SVG document.

        Args:
            index: The index of the shape to set.
            value: The value to set the shape to.
        """
        pass

    @abstractmethod
    def __delitem__(self, index):
        """Delete the shape at the specified index from the SVG document.

        Args:
            index: The index of the shape to delete.
        """
        pass

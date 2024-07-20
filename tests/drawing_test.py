import unittest
from unittest.mock import MagicMock, patch
from tordie.drawing import Drawing
from tordie.shapes.base.shape import Shape
from tordie.options import Options
from svgwrite.drawing import Drawing as SVGDrawing


class DrawingTests(unittest.TestCase):
    def setUp(self):
        self.options = Options()
        self.drawing = Drawing(self.options)
        self.shape = MagicMock(spec=Shape)

    def test_add_shape(self):
        self.drawing.add_shape(self.shape)
        self.assertIn(self.shape, self.drawing._shapes)

    def test_remove_shape(self):
        self.drawing.add_shape(self.shape)
        self.drawing.remove_shape(self.shape)
        self.assertNotIn(self.shape, self.drawing._shapes)

    def test_clear(self):
        self.drawing.add_shape(self.shape)
        self.drawing.clear()
        self.assertEqual(len(self.drawing), 0)

    def test_len(self):
        self.assertEqual(len(self.drawing), 0)
        self.drawing.add_shape(self.shape)
        self.assertEqual(len(self.drawing), 1)

    def test_iter(self):
        self.drawing.add_shape(self.shape)
        shapes = list(self.drawing)
        self.assertEqual(shapes, [self.shape])

    def test_getitem(self):
        self.drawing.add_shape(self.shape)
        self.assertEqual(self.drawing[0], self.shape)

    def test_setitem(self):
        self.drawing.add_shape(self.shape)
        new_shape = MagicMock(spec=Shape)
        self.drawing[0] = new_shape
        self.assertEqual(self.drawing[0], new_shape)

    def test_delitem(self):
        self.drawing.add_shape(self.shape)
        del self.drawing[0]
        self.assertEqual(len(self.drawing), 0)

    def test_str(self):
        self.assertEqual(str(self.drawing), "Drawing: 0 shapes")
        self.drawing.add_shape(self.shape)
        self.assertEqual(str(self.drawing), "Drawing: 1 shapes")

    def test_repr(self):
        self.assertEqual(repr(self.drawing), "Drawing: 0 shapes")
        self.drawing.add_shape(self.shape)
        self.assertEqual(repr(self.drawing), "Drawing: 1 shapes")


if __name__ == '__main__':
    unittest.main()

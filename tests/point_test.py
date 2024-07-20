import unittest
from math import pi, sqrt, cos, sin, atan2, isclose
from tordie import Point


class TestPoint(unittest.TestCase):
    def test_cartesian_initialization(self):
        p = Point(3, 4)
        self.assertAlmostEqual(p.x, 3)
        self.assertAlmostEqual(p.y, 4)
        self.assertAlmostEqual(p.r, 5)
        self.assertAlmostEqual(p.theta, atan2(4, 3))

    def test_polar_initialization(self):
        r, theta = 5, pi / 4
        p = Point(r, theta, polar=True)
        self.assertAlmostEqual(p.x, r * cos(theta))
        self.assertAlmostEqual(p.y, r * sin(theta))
        self.assertAlmostEqual(p.r, r)
        self.assertAlmostEqual(p.theta, theta)

    def test_x_setter(self):
        p = Point(3, 4)
        p.x = 6
        self.assertAlmostEqual(p.x, 6)
        self.assertAlmostEqual(p.y, 4)
        self.assertAlmostEqual(p.r, sqrt(6**2 + 4**2))
        self.assertAlmostEqual(p.theta, atan2(4, 6))

    def test_y_setter(self):
        p = Point(3, 4)
        p.y = 8
        self.assertAlmostEqual(p.x, 3)
        self.assertAlmostEqual(p.y, 8)
        self.assertAlmostEqual(p.r, sqrt(3**2 + 8**2))
        self.assertAlmostEqual(p.theta, atan2(8, 3))

    def test_r_setter(self):
        p = Point(3, 4)
        p.r = 10
        self.assertAlmostEqual(p.r, 10)
        self.assertAlmostEqual(p.x, 10 * cos(atan2(4, 3)))
        self.assertAlmostEqual(p.y, 10 * sin(atan2(4, 3)))
        self.assertTrue(isclose(p.theta, atan2(4, 3), rel_tol=1e-9))

    def test_theta_setter(self):
        p = Point(3, 4)
        new_theta = pi / 2
        p.theta = new_theta
        self.assertAlmostEqual(p.theta, new_theta)
        self.assertAlmostEqual(p.x, p.r * cos(new_theta))
        self.assertAlmostEqual(p.y, p.r * sin(new_theta))


if __name__ == '__main__':
    unittest.main()

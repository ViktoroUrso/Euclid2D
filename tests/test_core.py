import pytest
from euclid2D.core import Plane


class TestPlaneClass:
    """Test class Plane features."""
    def test_roundcoords_none(self):
        """Check round mask - ZERO."""
        X_CONST = 5.5
        Y_CONST = 1.1
        cartesian = Plane()
        x, y = cartesian.round_coords((X_CONST, Y_CONST))
        assert X_CONST == pytest.approx(x) and Y_CONST == pytest.approx(y), (
            'Проверьте, корректность работы режима без округления')

        """Check round mask - MATH"""
        """Check round mask - MAX"""
        """Check round mask - MIN"""


# тест работы с границами плоскости

#  тест работы с закрытостью/открытостью плоскости

class TestEuclidClass:
    pass

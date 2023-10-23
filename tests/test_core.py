import pytest
from euclid2D.core import Plane, Coords
from euclid2D.aksioma import ROUND_MASK

class TestPlaneClass:
    """Test class Plane features."""

    # Тестирование режимов округления
    def test_roundcoords_none(self):
        """Check round mask - ZERO."""

        cartesian = Plane()
        point_temp = Coords()
        point_temp = cartesian.round_coords(Coords(5.5, 1.1))
        assert (5.5 == pytest.approx(point_temp.x)
                and 1.1 == pytest.approx(point_temp.y)), (
                    'Проверьте, корректность работы режима без округления')

    def test_roundcoords_math(self):
        """Check round mask - MATH"""

        cartesian = Plane()
        point_temp = Coords()
        cartesian.round = ROUND_MASK["MATH"]
        point_temp = cartesian.round_coords(Coords(5.5, 1.1))
        assert (6 == point_temp.x) and (1 == point_temp.y), (
            'Проверьте, корректность работы режима математического округления')

    def test_roundcoords_max(self):
        """Check round mask - MAX"""

        cartesian = Plane()
        point_temp = Coords()
        cartesian.round = ROUND_MASK["MAX"]
        point_temp = cartesian.round_coords(Coords(5.5, 1.1))
        assert (6 == point_temp.x) and (2 == point_temp.y), (
            'Проверьте, корректность работы режима округления к большему целому')

    def test_roundcoords_min(self):
        """Check round mask - MIN"""

        cartesian = Plane()
        point_temp = Coords()
        cartesian.round = ROUND_MASK["MIN"]
        point_temp = cartesian.round_coords(Coords(5.5, 1.1))
        assert (5 == point_temp.x) and (1 == point_temp.y), (
            'Проверьте, корректность работы режима округления к меньшему целому')

    def test_roundcoords_round(self):
        """Check round mask - ROUND"""

        cartesian = Plane()
        point_temp = Coords()
        cartesian.round = ROUND_MASK["ROUND"]
        point_temp = cartesian.round_coords(Coords(5.5, 1.1))
        assert (6 == point_temp.x) and (1 == point_temp.y), (
            'Проверьте, корректность работы режима стандартного округления')

# тест проверки координат на выход за границы плоскости

    def test_iscoordsvalid_beyondlimits(self):
        """Checks if correct - checking coords in plane """

        cartesian = Plane()
        cartesian.round = ROUND_MASK["MATH"]
        cartesian.x_max_lim = 10
        cartesian.x_min_lim= -10
        cartesian.y_max_lim = 10
        cartesian.y_min_lim = -10

        point_temp = Coords(11, 11)
        point_temp = cartesian.round_coords(point_temp)
        assert not(cartesian.is_coords_valid(point_temp))

#  тест работы с закрытостью/открытостью плоскости

class TestEuclidClass:
    pass

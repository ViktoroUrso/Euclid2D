"""Core module for Euclid basic class"""
import math
import typing as typo
from abc import ABC, abstractmethod
from .aksioma import ROUND_MASK, EUCLID_OBJECT_TYPE


class TransformMask:
    """Класс для хранения информации о маске трансформации (два числа)
        которые предполагается применить к координатам точки/точек/фигур
    """
    trans_x:typo.Int = 0
    trans_y = 0

    def __init__(self, delta_x, delta_y):
        self.trans_x = delta_x
        self.trans_y = delta_y

    @property
    def x(self):
        return self.trans_x

    @property
    def y(self):
        return self.trans_y


class Euclid(ABC):
    '''
    Абстрактный базовый класс для генерации классов пакета
    в качестве методов - 5 аффинных преобразований

    The base class for all geometrical entities.
    This class doesn’t represent any
    particular geometric entity,
    it only provides the implementation of some
    methods common to all subclasses.
    '''
    # ==================== Fields of class Euclid======================
    _id = None
    _name = "Euclid's object"
    _euclid_type = EUCLID_OBJECT_TYPE["NONE"]

    # ==================== Properties of class Euclid==================
    @property
    def bounds(self):
        return

    @property
    def bbox(self):
        ''' returns a bounding box containing p.
        :param self:
        :return:
        Note that bounding boxes are not parameterized with whatsoever.
        '''

    @property
    def affine_rank(self, *args):
        '''The affine rank of a set of points.'''

    # ==================== Magic metods of class Euclid================
    def __init__(self, plane, *kwargs, **args):
        ''''''
        if plane is Plane:
            plane = plane + self
        else:
            raise TypeError("параметр plane должен быть объектом класса Plane")

    def __str__(self):
        return self._name

    # ========== Comparison magic methods
    # __eq__(self, other): Defines behavior for the equality operator, ==.
    # __ne__(self, other): Defines behavior for the inequality operator, !=.
    # __lt__(self, other): Defines behavior for the less-than operator, <.
    # __gt__(self, other): Defines behavior for the greater-than operator, >.
    # __le__(self, other): Defines behavior for the operator <=.
    # __ge__(self, other): Defines behavior for the operator >=.

    # ========== Numeric magic methods
    # __round__(self,n): Implements behavior for the built-in round()
    # __invert__(self): Implements behavior for inversion using the ~ operator.
    # __abs__(self): Implements behavior for the built-in abs()
    # __neg__(self): Implements behavior for negation
    # __pos__(self): Implements behavior for unary positive

    # ==================== Classmetods of class Euclid=======================
    @abstractmethod
    def distance_to(self, obj):
        pass

    @abstractmethod
    def rotate(self, angle, mes=0, pt=None):
        pass

    @abstractmethod
    def scale(self, x=1, y=1, pt=None):
        pass

    @abstractmethod
    def transform(self, matrix):
        pass

    @abstractmethod
    def translate(self, x=0, y=0):
        pass


class EuclidCollection():
    """Class for set of Euclid objects"""


class Coords():
    """Class for coordinations."""
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


class Plane:
    '''Euclidean plane (ExE) class'''
    plane_list = {}  # Ye;yj gthtytcnb d rkfcc
    # ==================== Fields of class Plane=============================
    _id = None  # N плоскости
    _name = "Euclid's plane"
    _objects = {}  # список/словарь(?) объектов на этой плоскости
    _metric = None  # размерность плоскости: 1-прямая (Х), 2-плоскость (Х*У)

    # ==================== Properties of class Plane=========================
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        """Show name of a plane"""
        return self._name

    @name.setter
    def name(self, name):
        """Set a name of a plane."""
        self._name = name

    @property
    def metric(self):
        """Show a metric level of plane: None-None, 1-Line, 2-Plane."""
        return self._metric

    @property
    def openess(self):
        """Show ability to Mebius's transbordering"""
        return self._openess

    @property
    def round(self):
        """Show roundness type."""
        return self._round

    @property
    def quantity(self):
        """Return an amount of objects on the plane"""
        return len(self._objects)

    # ==================== Magic metods of class Plane=======================
    def __init__(self, x_max_lim=None, x_min_lim=None,
                 y_max_lim=None, y_min_lim=None, openess=False, metric='2'):
        """Plane's constructor method."""
        self._id = len(Plane.plane_list)+1
        Plane.plane_list[self._id] = self
        self._metric = metric
        self._openess = openess
        self._round = ROUND_MASK["ZERO"]

        if ((x_max_lim is None or x_max_lim >= 0) and
            (x_min_lim is None or x_min_lim <= 0)):
            self.x_max_lim = x_max_lim
            self.x_min_lim = x_min_lim
        else:
            raise IndexError("Try to setup incorrect"
                             "plane's limits for x-axis")

        if ((y_max_lim is None or y_max_lim >= 0) and
            (y_min_lim is None or y_min_lim <= 0)):
            self.y_max_lim = y_max_lim
            self.y_min_lim = y_min_lim
        else:
            raise IndexError("Try to setup incorrect"
                             "plane's limits for y-axis")

    def __del__(self):
        """Destructor of plane class"""
        del Plane.plane_list[self.id]

    def __class__(self):
        pass

    def __name__(self):
        pass

    def __doc__(self):
        pass

    def __init_subclass__(self):
        pass

    def __reduce__(self):
        pass

    def __reduce_ex__(self):
        pass

    def __subclasshook__(self):
        pass

    # ========== Arithmetic operators
    def __add__(self, obj):
        """Add Euclid obj to plane."""
        self._objects[obj.id] = obj
        return self

    def __sub__(self, obj):
        """Delete Euclid obj with id from plane."""
        # Вставить удаление объекта с плоскостью
        del self._objects[obj.id]
        return self

    # ========== String Magic Methods
    def __str__(self):
        '''Return string representation of plane.'''
        # сформировать строковое представление
        return "".join(self._name)

    def __repr__(self):
        """Return machine representation of plane."""
        # сформировать строковое представление
        return str(self.metric, self.x_max_lim, self.y_max_lim,
                   self.x_min_lim, self.y_min_lim, self.openess)

    def __format__(self, formatstr):
        """return a new style of string."""
        return self.__str__()

    def __hash__(self):
        """It has to return an integer, and its result is
        used for quick key comparison in dictionaries."""
        return hash_int

    def __nonzero__(self):
        """Defines behavior for when bool()
        is called on an instance of your class."""
        return True

    # ==================== Classmetods of class Plane========================
    def round_coords(self, coords):
        """Function for round coordinates."""
        def ar_round(value):
            '''function for arithmetic rounding.'''
            value = int(value + (0.5 if value > 0 else -0.5))
            return value

        if self.round == ROUND_MASK["ZERO"]:
            return coords
        elif self.round == ROUND_MASK["MATH"]:
            coords.x = ar_round(coords.x)
            coords.y = ar_round(coords.y)
            return coords
        elif self.round == ROUND_MASK["MAX"]:
            coords.x = math.ceil(coords.x)
            coords.y = math.ceil(coords.y)
            return coords
        elif self.round == ROUND_MASK["MIN"]:
            coords.x = math.floor(coords.x)
            coords.y = math.floor(coords.y)
            return coords
        elif self.round == ROUND_MASK["ROUND"]:
            coords.x = round(coords.x, None)
            coords.y = round(coords.y, None)
            return coords

    def is_coords_valid(self, coords):
        flag = True
        if self.x_max_lim and self.x_max_lim < coords.x:
            flag = False
        if self.x_min_lim and self.x_min_lim > coords.x:
            flag = False
        if self.y_max_lim and self.y_max_lim < coords.y:
            flag = False
        if self.y_min_lim and self.y_min_lim > coords.y:
            flag = False
        return flag


class Plane3D:
    # n.p = k, where n is normal, p is point on plane, k is constant scalar
    __slots__ = ['n', 'k']

    def __init__(self, *args):
        if len(args) == 3:
            assert isinstance(args[0], Point3) and \
                   isinstance(args[1], Point3) and \
                   isinstance(args[2], Point3)
            self.n = (args[1] - args[0]).cross(args[2] - args[0])
            self.k = self.n.dot(args[0])
        elif len(args) == 2:
            if isinstance(args[0], Point3) and isinstance(args[1], Vector3):
                self.n = args[1].copy()
                self.k = self.n.dot(args[0])
            elif isinstance(args[0], Vector3) and type(args[1]) == float:
                self.n = args[0].copy()
                self.k = args[1]
            else:
                raise (AttributeError, '%r' % (args,))

        else:
            raise (AttributeError, '%r' % (args,))

        if not self.n:
            raise (AttributeError, 'Points on plane are colinear')

    def __copy__(self):
        return self.__class__(self.n, self.k)

    copy = __copy__

    def __repr__(self):
        return 'Plane(<%.2f, %.2f, %.2f>.p = %.2f)' % \
            (self.n.x, self.n.y, self.n.z, self.k)

    def _get_point(self):
        # Return an arbitrary point on the plane
        if self.n.z:
            return Point(0., self.k / self.n.z)
        else:
            return Point(self.k / self.n.x, 0.)

    def _apply_transform(self, t):
        p = t * self._get_point()
        self.n = t * self.n
        self.k = self.n.dot(p)

    def intersect(self, other):
        return other._intersect_plane(self)

    def _intersect_line(self, other):
        return _intersect_line_plane(other, self)

    def _intersect_plane(self, other):
        return _intersect_plane_plane(self, other)

    def connect(self, other):
        return other._connect_plane(self)

    def _connect_point(self, other):
        return _connect_point_plane(other, self)

    def _connect_line(self, other):
        return _connect_line_plane(other, self)

    def _connect_plane(self, other):
        return _connect_plane_plane(other, self)

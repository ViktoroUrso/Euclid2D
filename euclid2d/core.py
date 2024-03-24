"""Core module for Euclid basic class"""

import math
from abc import ABC, abstractmethod
from .aksioma import ROUND_MASK, EUCLID_OBJECT_TYPE


class TransformMask:
    """Class for store the transformation mask."""

    def __init__(self, delta_x, delta_y):
        self._trans_x = delta_x
        self._trans_y = delta_y

    @property
    def x(self):
        return self._trans_x

    @property
    def y(self):
        return self._trans_y


class Coords():
    """Class for store the pair of coordinates."""
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


class Euclid(ABC):
    ''' THe base abstract class of package for all geometrical entities.'''

    # ==================== Properties of class Euclid==================
    @property
    def bounds(self):
        return

    @property
    def bbox(self):
        ''' 
        returns a bounding box containing p.
        :param self:
        :return:
        Note that bounding boxes are not parameterized with whatsoever.
        '''
        pass

    @property
    def affine_rank(self, *args):
        '''The affine rank of a set of points.'''
        pass

    # ==================== Magic metods of class Euclid================
    def __init__(self, plane, *kwargs, **args):
        '''Constructor method.'''
        self._id = None
        self._name = "Euclid's object"
        self._euclid_type = EUCLID_OBJECT_TYPE["NONE"]

        if plane is Plane:
            plane = plane + self
        else:
            raise TypeError("параметр plane должен быть объектом класса Plane")

    def __str__(self):
        return self._name

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



class Plane:
    '''Euclidean planes (ExE) class'''
    plane_list = {}  # Нужно перенести в класс
    # ==================== Fields of class Plane=============================
    _id = None  # № плоскости
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

    @round.setter
    def round(self, value):
        """Set a roundness type of plane."""
        self._round = value

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

        if ((x_max_lim is None or x_max_lim >= 0)
                and (x_min_lim is None or x_min_lim <= 0)):
            self.x_max_lim = x_max_lim
            self.x_min_lim = x_min_lim
        else:
            raise IndexError("Try to setup incorrect"
                             "plane's limits for x-axis")

        if ((y_max_lim is None or y_max_lim >= 0)
                and (y_min_lim is None or y_min_lim <= 0)):
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

    def __doc__(self):
        pass

    def __init_subclass__(self):
        pass

    def __reduce__(self):
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
        # Вставить удаление объекта с плоскости
        del self._objects[obj.id]
        return self

    # ========== Representation Magic Methods
    def __str__(self):
        '''Return string representation of plane.'''
        # сформировать строковое представление
        return "".join(self._name)
    
    def __bytes__(self):
        '''Return bytes representation of plane.'''
        # сформировать строковое представление из данных объекта
        return b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    def __repr__(self):
        """Return machine representation of plane."""
        # сформировать машинно-ориентированное строковое представление
        return str("Plane:", self.metric, self.x_max_lim, self.y_max_lim,
                   self.x_min_lim, self.y_min_lim, self.openess)

    def __format__(self, formatstr):
        """return a new style of string."""
        # вызывается при вызове функции format(...) и используется 
        # для форматировании строки с использованием строковых литералов.
        return self.__str__()

    def __hash__(self):
        """It has to return an integer, and its result is
        used for quick key comparison in dictionaries."""
        return hash_int

    def __bool__(self):
        """Defines behavior for when bool()
        is called on an instance of your class."""
        return True

    # ==================== Classmethods of class Plane========================
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
        """Check if coordinates is valid."""
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

    def connect(self, other):
        """Connect other object to plane"""
        return other._connect_plane(self)

    def transform(self, another_plane):
        """Transform plane to another plane"""
        return
    
    def copy(self):
        """Create new plane, transform and return"""
        return plane_copy
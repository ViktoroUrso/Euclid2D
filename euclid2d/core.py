"""Core module for Euclid basic class"""
import math
from abc import ABC, abstractmethod
from .aksioma import ROUND_MASK, EUCLID_OBJECT_TYPE, plane_list


class TransformMask:
    """Класс для хранения информации о маске трансформации (два числа)
        которые предполагается применить к координатам точки/точек/фигур
    """
    trans_x = 0
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
        ''' The affine rank of a set of points''' 

    # ==================== Magic metods of class Euclid================
    def __init__(self, plane, *kwargs, **args):

        if plane is Plane:
            plane.objects.append(self)
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

    # ==================== Fields of class Plane=============================
    _id = None # N плоскости 
    _name = "Euclid's plane"
    _objects = []  # список/словарь(?) объектов на этой плоскости
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
        self._id = len(plain_list)+1
        plane_list[self._id]=self
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
        
        
        '''Нужно удалить плоскость из plane_list'''
        super.__del__


    #========== Numeric magic methods
    # __round__(self,n): Implements behavior for the built-in round()
    # __invert__(self): Implements behavior for inversion using the ~ operator.
    # __abs__(self): Implements behavior for the built-in abs()
    # __neg__(self): Implements behavior for negation
    # __pos__(self): Implements behavior for unary positive 

    #========== Arithmetic operators
    def __add__(str, obj):
        """Add Euclid obj to plane."""
        self._objects[].append(obj)
        return self
 
    def __sub__(str, obj_id):
        """Delete Euclid obj with id from plane."""
        # Вставить удаление объекта с п
        return self



    # __mul__(self, other): Implements behavior for math.floor()
    # __floordiv__(self, other): Implements behavior for the built-in round()
    # __div__(self, other): Implements behavior for inversion using the ~ operator.
    # __truediv__(self, other): Implements behavior for the built-in abs()
    # __mod__(self, other): Implements behavior for negation
    # __divmod__(self, other): Implements behavior for unary positive 
    # __pow__: Implements behavior for exponents using the ** operator.
    # __lshift__(self, other): Implements left bitwise shift using the << operator.
    # __rshift__(self, other): Implements right bitwise shift using the >> operator.
    # __and__(self, other): Implements bitwise and using the & operator.
    # __or__(self, other): Implements bitwise or using the | operator.
    # __xor__(self, other): Implements bitwise xor using the ^ operator.

    #========== Comparison magic methods
    # __eq__(self, other): Defines behavior for the equality operator, ==.
    # __ne__(self, other): Defines behavior for the inequality operator, !=.
    # __lt__(self, other): Defines behavior for the less-than operator, <.
    # __gt__(self, other): Defines behavior for the greater-than operator, >.
    # __le__(self, other): Defines behavior for the less-than-or-equal-to operator, <=.
    # __ge__(self, other): Defines behavior for the greater-than-or-equal-to operator, >=.

    #========== String Magic Methods
    def __str__(self):
        '''Return string representation of plane.'''
        return self._name

    def __repr__(self):
        """Return machine representation of plane."""
        return (self.metric, self.x_max_lim, self.y_max_lim,
                self.x_min_lim, self.y_min_lim, self.openess)

    # __format__(self, formatstr): return a new style of string.
    # __hash__(self): It has to return an integer, and its result is used for quick key comparison in dictionaries.
    # __nonzero__(self): Defines behavior for when bool() is called on an instance of your class. 

''' Magic methods of object class
__class__'
'__delattr__'
'__dir__'
'__doc__'
'__eq__'
'__format__'
'__ge__'
'__getattribute__'
'__gt__'
'__hash__'
'__init__'
'__init_subclass__'
'__le__'
'__lt__'
'__ne__'
'__new__'
'__reduce__'
'__reduce_ex__'
'__repr__'
'__setattr__'
'__sizeof__'
'__str__'
'__subclasshook__'
'''

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

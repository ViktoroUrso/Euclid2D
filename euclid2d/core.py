"""Core module for Euclid basic class"""
import math
from abc import ABC, abstractmethod
from .aksioma import ROUND_MASK


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
        ''' The affine rank of a set of points is
        the dimension of the smallest affine space
        containing all the points. For example,
        if the points lie on a line (and are not
        all the same - affine rank = 0) their affine
        rank is 1. If the points lie on a plane but
        not a line, their affine rank is 2. By convention,
        the empty set has affine rank -1.'''
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
    '''2-dimensional Euclidean space'''
    ''' Класс хранит информацию о плоскости'''
    ''' the two-dimensional Euclidean plane ExE.
    Хранит размеры плоскости или информацию об их бесконечности'''

    # ==================== Fields of class Plane=============================


    # ==================== Properties of class Plane=========================

    # ==================== Magic metods of class Plane=======================
    def __init__(self, x_max_lim = None, x_min_lim = None, 
                 y_max_lim = None, y_min_lim = None, openess = False):
        """Plane's constructor method."""
        self.name = "Euclid's plane"
        self.metric = ''  # метрика плоскости
        self.openess = openess
        self.round = ROUND_MASK["ZERO"]
        self.objects = []  # список/словарь(?) объектов на этой плоскости (EuclidSet?)

        if ((x_max_lim >= 0 or x_max_lim is None) and
            (x_min_lim <= 0 or x_min_lim is None)):
            self.x_max_lim = x_max_lim
            self.x_min_lim = x_min_lim
        else:
            raise IndexError("Try to setup incorrect plane's limits for x-axis")

        if ((y_max_lim >= 0 or y_max_lim is None) and
            (y_min_lim <= 0 or y_min_lim is None)):
            self.y_max_lim = y_max_lim
            self.y_min_lim = y_min_lim
        else:
            raise IndexError("Try to setup incorrect plane's limits for y-axis")

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

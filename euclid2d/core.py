"""Core module for Euclid basic class"""
from abc import ABC, abstractmethod
from .aksioma import ROUND_MASK


class TransformMask:
    """Класс для хранения информации о маске трансформации (два числа)
        которые предполагается применить к координатам точки/точек/фигур
    """
    trans_x = 0
    trans_y = 0

    def __init__(self, x, y):
        self.trans_x = x
        self.trans_y = y

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
    pass


class Plane:
    '''2-dimensional Euclidean space'''
    ''' Класс хранит информацию о плоскости'''
    ''' the two-dimensional Euclidean plane ExE.
    Хранит размеры плоскости или информацию об их бесконечности'''

    # ==================== Fields of class Plane=============================

    name = "Euclid's plane"
    coord_system = {
        "metric": '',  # метрика плоскости
        "x_lim": None,  # предел плоскости по оси Ox
        "y_lim": None,  # предел плоскости по оси Oy
        "round": ROUND_MASK["ZERO"],
        "openess": True
    }
    objects = []  # список/словарь(?) объектов на этой плоскости (EuclidSet?)

    # ==================== Properties of class Plane=========================

    # ==================== Magic metods of class Plane=======================

    # ==================== Classmetods of class Plane========================
    def round_coords(self, coords):
        if self.coord_system["round"] == ROUND_MASK["ZERO"]:
            return coords

    def is_coords_valid(self, coords):
        pass

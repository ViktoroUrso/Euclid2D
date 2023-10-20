import math, decimal
import aksioma

'''
Модуль EUCLID.core
базовый модуль определяющий класс плоскости, 
и абстрактный базовый класс геометрических объектов Euclid
а также другие вспомогательные классы
'''


class TransformMask:
    """Класс для хранения информации о маске трансформации (два числа)
        которые предполагается применить к координатам точки/точек/фигур
    """


class Euclid:
    '''
    Абстрактный базовый класс для генерации классов пакета
    в качестве методов 5 аффинных преобразований

    '''
    name = ""


class Euclid (*args, **kwargs)

'''
The base class for all geometrical entities.
This class doesn’t represent any particular geometric entity, 
it only provides the implementation of some methods common to all subclasses.
'''
# ==================== Fields of class Point================================================
    _id = None
    _name  # словарь объектов Point - для хранения координат точек
# ==================== Properties of class Point============================================
    @property
    def bounds(self):
        return

    @property
    def bbox(self)
        ''' returns a bounding box containing p.
        :param self:
        :return: 
        Note that bounding boxes are not parameterized with whatsoever.
        '''

    def affine_rank(self, *args):
        ''' The affine rank of a set of points is the dimension of the smallest affine space
        containing all the points. For example, if the points lie on a line
        (and are not all the same - affine rank = 0) their affine rank is 1.
        If the points lie on a plane but not a line, their affine rank is 2.
        By convention, the empty set has affine rank -1.'''
# ==================== Magic metods of class Euclid==========================================
'''
    def name_of_method () 
        Short description of method
        :param parameter1name: short description of parameter 1: name of type/class: mean by default if is set
        :param parameter2name: short description of parameter 2: name of type/class: mean by default if is set
        :param parameterNname: short description of parameter N: name of type/class: mean by default if is set
        :return: rotated Point object

        Raises:
        TypeError : if other is not recognized as a GeometricEntity or is a GeometricEntity for which distance is not defined.

        Notes:
        The return value will either be an empty list if there is no intersection, otherwise it will contain this point.

        #TODO Make a body of method - Rotate angle radians counterclockwise about Point pt.
'''

# ==================== Classmetods of class Euclid===========================================
    def distance_to(self, other):
        ''' The Euclidian distance between self and other object'''
		return sqrt((self.x-p.x)**2+(self.y-p.y)**2) # Определиться с привязкой точности вычисления и разрядности ответа к свойствам класса Plane
        ''' Returns distance to other Euclid object : number.
        Raises TypeError : if other is not recognized as a GeometricEntity or is a
        GeometricEntity for which distance is not defined. '''


    def rotate(self, angle, mes=0, pt=None):
        '''
        :param angle: measure of angle in mes
        :param mes: if 0 - gradus, if 1 - radians
        :param pt: Point object
        :return: rotated Point object

        :raises
        TypeError:
        ValueError:
        '''
        # TODO Make a body of method - Rotate angle radians counterclockwise about Point pt.

    def scale(self, x=1, y=1, pt=None):
        '''
        :param self:
        :param x:
        :param y:
        :param pt:
        :return:

        :raises
        TypeError:
        ValueError:

        '''
        '''Scale the coordinates of the Point by multiplying by x and y after subtracting pt – default is (0, 0) – and then adding pt back again (i.e. pt is the point of reference for the scaling).'''

    def transform(self, matrix):
        ''' 
        :param self: 
        :param matrix: 
        :return: 
        '''  # Is it neccesary?
        ''' Return the point after applying the transformation described by the 3x3 Matrix, matrix.'''


    def translate(self, x=0, y=0):
        '''
        :param self:
        :param x:
        :param y:
        :return:
        '''
        ''' Shift the Point by adding x and y to the coordinates of the Point.'''

"""
class Reflection(Boost.Python.instance)
   	Tag class for affine transformations.
Method resolution order:
Reflection
Boost.Python.instance
__builtin__.object
Methods defined here:
__init__(...)
Data and other attributes defined here:
__instance_size__ = 12
Data and other attributes inherited from Boost.Python.instance:
__dict__ = <dictproxy object>
__new__ = <built-in method __new__ of Boost.Python.class object>
T.__new__(S, ...) -> a new object with type S, a subtype of T
__weakref__ = <member '__weakref__' of 'Boost.Python.instance' objects>
 
class Rotation(Boost.Python.instance)
   	Tag class for affine transformations.
Method resolution order:
Rotation
Boost.Python.instance
__builtin__.object
Methods defined here:
__init__(...)
Data and other attributes defined here:
__instance_size__ = 12
Data and other attributes inherited from Boost.Python.instance:
__dict__ = <dictproxy object>
__new__ = <built-in method __new__ of Boost.Python.class object>
T.__new__(S, ...) -> a new object with type S, a subtype of T
__weakref__ = <member '__weakref__' of 'Boost.Python.instance' objects>
 
class Scaling(Boost.Python.instance)
   	Tag class for affine transformations.
Method resolution order:
Scaling
Boost.Python.instance
__builtin__.object
Methods defined here:
__init__(...)
Data and other attributes defined here:
__instance_size__ = 12
Data and other attributes inherited from Boost.Python.instance:
__dict__ = <dictproxy object>
__new__ = <built-in method __new__ of Boost.Python.class object>
T.__new__(S, ...) -> a new object with type S, a subtype of T
__weakref__ = <member '__weakref__' of 'Boost.Python.instance' objects> 


class Translation(Boost.Python.instance)
   	Tag class for affine transformations.
Method resolution order:
Translation
Boost.Python.instance
__builtin__.object
Methods defined here:
__init__(...)
Data and other attributes defined here:
__instance_size__ = 12
Data and other attributes inherited from Boost.Python.instance:
__dict__ = <dictproxy object>
__new__ = <built-in method __new__ of Boost.Python.class object>
T.__new__(S, ...) -> a new object with type S, a subtype of T
__weakref__ = <member '__weakref__' of 'Boost.Python.instance' objects>
"""


class Plane: 
    '''2-dimensional Euclidean space'''
    ''' Класс хранит информацию о плоскости'''
    ''' the two-dimensional Euclidean plane ExE. Хранит размеры плоскости или информацию об их бесконечности'''

# ==================== Fields of class Plane================================================

    name = "Euclid's plane"
    coord_system = {
        "metric": "",  # метрика плоскости
        "x_lim": 0,  # предел плоскости по оси Ox
        "y_lim": 0,  # предел плоскости по оси Oy
        "round": "",  # режим округления значений координат при вычислениях
        "openess": True,  # замкнутость или открытость плоскости
        }
    objects = []  # список/словарь(?) объектов на этой плоскости

# ==================== Properties of class Plane============================================

# ==================== Magic metods of class Plane==========================================

# ==================== Classmetods of class Plane===========================================

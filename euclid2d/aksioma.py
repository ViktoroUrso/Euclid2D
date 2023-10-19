import math, kernel

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
# ==================== Magic metods of class Point==========================================
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

# ==================== Classmetods of class Point===========================================
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

class Plane # 2-dimensional Euclidean space
''' the two-dimensional Euclidean plane ExE. Хранит размеры плоскости или информацию об их бесконечности'''
# ==================== Fields of class Point================================================
# ==================== Properties of class Point============================================
# ==================== Magic metods of class Point==========================================
# ==================== Classmetods of class Point===========================================

class Point(Euclid):
''' A class of point in a 2D-dimensional Euclidean space.'''
# ==================== Fields of class Point================================================
_x = None # X-coordinate of point (Float)
_y = None # Y-coordinate of point (Float)
# ==================== Properties of class Point============================================

# ==================== Magic metods of class Point==========================================
	def __str__(self):
    ''' Возвращает строковое представление объекта класса '''
		return "%6.1f, %6.1f" % (self.x, self.y)

    def __eq__(self, obj):
    ''' Проверка эквивалентности точек. '''
    #TODO Сделать исключения в случае передачи не объекта класса Point
		return None

    def __init__(self, x=0.0, y=0.0):
        self._x = x # Method sets the X-coordinate of the Point.
        self._y = y # Method sets the Y-coordinate of the Point.
        return

    def __length__(self): # property of Point
        ''' Определиться - нужно ли это свойство. Treating a Point as a Line, this returns 0 for the length of a Point.'''
        return 0

# ============================ Properties of class Point =================================

    @property
    def coords(self):  # property Returns the two coordinates of the Point.
        return (self._x, self._y)

    @property # геттер+сеттер
    def x(self):  # Property returns the X coordinate of the Point.
        return self._x


    @property # геттер+сеттер
    def y(self):  # Property returns the Y coordinate of the Point.
        return self._y

    @property
    def is_nonzero(self):  # property of Point
    ''' True if any coordinate is nonzero, False if every coordinate is zero, and None if it cannot be determined.'''

    @property
    def is_zero(self):  # property of Point
    ''' True if every coordinate is zero, False if any coordinate is not zero, and None if it cannot be determined.'''

# ==================== Classmetods of class Point===========================================
    def unit(self): # property Return the Point that is in the same direction as self and a distance of 1 from the origin
        #TODO Сделать тело свойства

    def is_equal(self, other):
        ''' Returns whether the coordinates of self and other agree.'''

    def x_diff(self, other_point):
        ''' Return difference between x coordinates of self and other_point'''

    def y_diff(self, other_point):
        ''' Return difference between y coordinates of self and other_point'''

    def is_collinear(self,*args):
        '''
        Returns True if there exists a line that contains self and points.
        Returns False otherwise. A trivially True value is returned if no points are given.
        Parameters args : sequence of Points
        Returns is_collinear : boolean
        '''

    def midpoint(self, p):
        '''
        The midpoint between self and point p.
        Parameters p : Point
        Returns midpoint : Point
        '''
    def evalf(prec=None, **options)
        ''' Evaluate the coordinates of the point.
        This method will, where possible, create and return a new Point 
        where the coordinates are evaluated as floating point numbers 
        to the precision indicated (default=15).
        Parameters prec : int
        Returns point : Point
        '''

'''
p[i] -> returns cartesian(i).Precondition: 0 <= i <= 1.

cartesian(...)
cartesian(self,i) -> returns the i'th Cartesian  coordinate of p, starting with 0.
Precondition: 0 <= i <= 1.

dimension(...)
dimension(self) -> returns the dimension (the constant 2).

homogeneous(...)
homogeneous(self,i) -> returns the i'th homogeneous coordinate of p, starting with 0.Precondition: 0 <= i <= 2.

hw(...)
hw(self) -> returns the homogenizing coordinate.

hx(...)
hx(self) -> returns the homogeneous x coordinate.

hy(...)
hy(self) -> returns the homogeneous y coordinate.

transform(...)
transform(self,Aff_transformation_2 t) -> returns the point obtained by applying t on p.

x(...)
x(self) -> returns the Cartesian  x coordinate, that is hx/hw.

y(...)
y(self) -> returns the Cartesian  y coordinate, that is hy/hw.
Data and other attributes defined here:

определить зачем может понадобиться этот метод
    def faces_line(self, line):
    #Tells if point is facing a line (a tupple of two points)	(Point, Point)	True or False
		return point_faces_edge(line, self)

evaluate : if True (default), all floats are turn into exact types.

on_morph : indicates what should happen when the number of coordinates of a point need to be changed by adding or removing zeros. 
Possible values are ′warn′, ′error′, or ignore (default). 
No warning or error is given when ∗args is empty and dim is given. 
An error is always raised when trying to remove nonzero coordinates.
Raises
TypeError : When instantiating with anything but a Point or sequence
ValueError : when instantiating with a sequence with length < 2 or
when trying to reduce dimensions if keyword onmorph=′error′ is set.

Floats are automatically converted to Rational unless the evaluate flag is False:

Attributes
length origin: A Point representing the origin of the appropriately-dimensioned space.

classmethod are_coplanar(*points)[source]
Return True if there exists a plane in which all the points lie. A trivial True value is returned if len(points)<3 or all Points are 2-dimensional.
Parameters A set of points
Returns boolean
Raises ValueError : if less than 3 unique points are given

canberra_distance(p)[source]
The Canberra Distance from self to point p. Returns the weighted sum of horizontal and vertical distances to point p.
Parameters p : Point
Returns canberra_distance : The weighted sum of horizontal and vertical distances to point p. The weight used is the sum of absolute values of the coordinates.
Raises ValueError when both vectors are zero.

dot(p)[source]
Return dot product of self with another Point.

is_concyclic(*args)[source]
Do self and the given sequence of points lie in a circle?
Returns True if the set of points are concyclic and False otherwise. 
A trivial value of True is returned if there are fewer than 2 other points.
Parameters args : sequence of Points
Returns is_concyclic : boolean

property orthogonal_direction
Returns a non-zero point that is orthogonal to the line containing self and the origin.

static project(a, b)[source]
Project the point a onto the line between the origin and point b along the normal direction.
Parameters a : Point b : Point
Returns p : Point

taxicab_distance(p)[source]
The Taxicab Distance from self to point p.
Returns the sum of the horizontal and vertical distances to point p.
Parameters p : Point
Returns taxicab_distance : The sum of the horizontal and vertical distances to point p.

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
'''

class PointSet (Euclid)
    # Класс для хранения информации о группе точек, в том числе для использования в качестве хранилища координат верших сложных объектов
    Points = {} # словарь хранит информацию об объектах типа точка, в качестве ключа используются символы английского алфавита (в порядке алфавитной последовательности)
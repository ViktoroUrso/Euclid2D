import EUCLID.aksioma
import math, kernel, linear


class Shape(Object)
    name
    square  # square of shape
    perimetr  # perimetr of shape
    ''' 
    1. Реализовать методы вычисления длины периметра и площади фигуры
    property ambient_dimension Number of components this point has.'''

    def __init__(self, *args):
        ''' Сделать создание объекта и проверку на неправильные значения переданных координат (если стороны объекта пересекаются - неправильные вершины объекта)'''

    def square(self): # property of Shape object

    def bounds(self): # property Return a tuple? (xmin, ymin, xmax, ymax) representing the bounding rectangle for the geometric figure.

'''
Создайте класс Геометрическая фигура (динамические методы: вывод информации, площадь, периметр).
Создать три производных от Геометрической фигуры класса:
Прямоугольник (поля: стороны),
Круг (поля: радиус, координаты центра),
Треугольник (поля: стороны).
Переопределить для производных классов методы вывод информации, площадь, периметр.
Добавить в класс Круг метод вывода уравнения окружности,
в класс Прямоугольник – метод масштабирования (обе стороны умножаются на одно и то же число).
Продемонстрировать работу всех методов.
'''

class Polygon(Shape)

class RegularPolygon(Polygon)

class Triangle(Polygon)
    ''' 
    Нахождение координат точек и параметров бисектрис, медиан, высот и т.п.  
    '''

'''
class Triangle_2(Boost.Python.instance)
   	An object t of the class Triangle_2 is a triangle in the two-dimensional Euclidean plane.
Triangle t is oriented, i.e., its boundary has clockwise or counterclockwise orientation. 
We call the side to the left of the boundary the positive side and the side to the right of the boundary the negative side.
The boundary of a triangle splits the plane in two open regions, a bounded one and an unbounded one. 
 
For more details see a C++ doc:
http://www.cgal.org/Manual/3.2/doc_html/cgal_manual/Kernel_23_ref/Class_Triangle_2.html
 
 	
Method resolution order:
Triangle_2
Boost.Python.instance
__builtin__.object
Methods defined here:
__eq__(...)
__init__(...)
t.Triangle_2( Point_2 p,Point_2 q,Point_2 r) -> introduces a triangle t with vertices p, q and r.
__ne__(...)
area(...)
t.area() -> double
returns the signed area of t.
bbox(...)
t.bbox( ) -> Bbox_2
returns a bounding box containing t.
bounded_side(...)
t.bounded_side( Point_2 p) -> Bounded_side
returns the constant ON_BOUNDARY, ON_BOUNDED_SIDE, or else ON_UNBOUNDED_SIDE,
depending on where point p is.
Precondition: t is not degenerate.
has_on_boundary(...)
t.has_on_boundary( Point_2 p) -> bool
has_on_bounded_side(...)
t.has_on_bounded_side( Point_2 p) -> bool
has_on_negative_side(...)
t.has_on_negative_side( Point_2 p) -> bool
has_on_positive_side(...)
t.has_on_positive_side( Point_2 p) -> bool
has_on_unbounded_side(...)
t.has_on_unbounded_side( Point_2 p) -> bool
is_degenerate(...)
t.is_degenerate( Point_2 p) -> bool
triangle t is degenerate, if the vertices are collinear.
opposite(...)
t.opposite( ) -> Triangle_2
returns a triangle where the boundary is oriented the other way round
(this flips the positive and the negative side, but not the bounded and unbounded side).
orientation(...)
t.orientation() -> Orientation
returns the orientation of t.
oriented_side(...)
t.oriented_side( Point_2 p) -> Oriented_side
 
returns ON_ORIENTED_BOUNDARY, or POSITIVE_SIDE, or the constant ON_NEGATIVE_SIDE,
determined by the position of point p.
Precondition: t is not degenerate.
transform(...)
t.transform(  Aff_transformation_2 at) -> Triangle_2
returns the triangle obtained by applying at on the three vertices of t.
vertex(...)
t.vertex( int i) ->  Point_2
returns the i'th vertex modulo 3 of t.
Data and other attributes defined here:
__instance_size__ = 56
Data and other attributes inherited from Boost.Python.instance:
__dict__ = <dictproxy object>
__new__ = <built-in method __new__ of Boost.Python.class object>
T.__new__(S, ...) -> a new object with type S, a subtype of T
__weakref__ = <member '__weakref__' of 'Boost.Python.instance' objects>
'''


class Quadrangle(Polygon)

""" 
Задача о принадлежности точки многоугольнику
https://ru.wikipedia.org/wiki/Задача_о_принадлежности_точки_многоугольнику
"""


class Rectangle(Quadrangle)

'''
Python rectangles
Generic rectangles in screen coordinates. Various methods are given to find if rectangles overlap, the distance between them, etc.

A rectangle is made out of four points.
Iterating over a rectangle iterates over its corner points.
Screen coordinates are used (x grows from left to right, y grows from top to bottom). You can still use negative numbers.

Example
rect1=Rect( 0,  0, 10, 10)
rect2=Rect(80, 50, 10, 10)
print(rect1.distance_to_rect(rect2))

Interface
is_point_inside_rect()

 ______
|    . |
|______|
Takes: a Point instance
Gives: True or False

overlaps_with()

 ______
|     _|____
|____|      |
     |______|
Takes: a Rect instance
Gives: True or False

overlaps_on_x_axis_with()

 ______
|      |           
|______|           Sees if the rectangles touch each other
    ______         if they were to be smashed to the top of
   |      |        the sreen.
   |______|
Takes: a Rect instance
Gives: True or False

overlaps_on_y_axis_with()

 ______
|      |   ______  Sees if the rectangles touch each other
|______|  |      | if they were to be smashed to the left
          |______| of the screen.
Takes: a Rect instance
Gives: True or False

distance_to_rect()

 ______
|      |             Finds the shortest distance between
|______|             two rectangles. Both edges and corners
        \            are being taken into concideration.
         \ ______    
          |      |
          |______|
Takes: a Rect instance
Gives: distance in float


Rect
A rectangle is the primary shape of this module. A rectangle is made out of four points (class Point is explained below). Iterating over a rectangle results into an iteration over its corners which essentially are points.

Property	Description	Type
l_top	Left top corner	Point
r_top	Right top corner	Point
l_bot	Left bottom corner	Point
r_bot	Right bottom corner	Point
center	Center of rectangle	Point
width	Width of rectangle	Float
height	Height of rectangle	Float


Method	Description	Takes	Gives
copy()	Gives a new copy of a rectangle	None	Rect
iter_edges()	Iterates over the four edges of the rectangle	None	Point, Point
corners_belong_to_edge()	Tells if two points are the corners on the edge of the rectangle	Point, Point	True or False
is_point_inside_rect()	Tells if a point is inside the rectangle	Point	True or False
overlaps_with()	Tells if the rectangle overlaps with an other rectangle	Rect	True or False
align_with_top_edge_of()	Moves rectangle to the top edge of given rectangle	Rect	self
align_with_left_edge_of()	Moves rectangle to the left edge of given rectangle	Rect	self
overlaps_on_x_axis_with()	Tells if the rectangle overlaps with an other rectangle if they were both moved to the top of the screen	Rect	True or False
overlaps_on_y_axis_with()	Tells if the rectangle overlaps with an other rectangle if they were both moved to the left of the screen	Rect	True or False
distance_to_rect()	Gives the shortest distance between two rectangles	Rect	Float



class Rect():

	# Screen coordinates
	l_top  = None
	r_top  = None
	l_bot  = None
	r_bot  = None
	center = None
	width  = None
	height = None

	def __init__(self, x, y, width, height):
		assert width>0
		assert height>0
		self.l_top  = Point(x, y)
		self.r_top  = Point(x+width, y)
		self.r_bot  = Point(x+width, y+height)
		self.l_bot  = Point(x, y+height)
		self.center = Point(x+width/float(2), y+height/float(2))
		self.width  = width
		self.height = height


	def __str__(self):
		str=("(%4d,%4d)              (%4d,%4d)\n"
		     "      .-----------------------.\n"
		     "      |                       |\n"
		     "      |                %6.1f |\n"
		     "      |       %6.1f          |\n"
		     "      '-----------------------'\n"
		     "(%4d,%4d)              (%4d,%4d)"
		     )
		nums=( self.l_top.x, self.l_top.y,         self.r_top.x, self.r_top.y,
			                                                             self.height,
			                             self.width,
		       self.l_bot.x, self.l_bot.y,         self.r_bot.x, self.l_bot.y  )
		return str % nums


	def __iter__(self):
		yield self.l_top
		yield self.r_top
		yield self.r_bot
		yield self.l_bot

	def iter_edges(self):
		yield self.l_top, self.r_top
		yield self.r_top, self.r_bot
		yield self.r_bot, self.l_bot
		yield self.l_bot, self.l_top


	# Gives back a copy of this rectangle
	def copy(self):
		return Rect(self.l_top.x, self.l_top.y, self.width, self.height)


	# Check to see if two croner points belong to the same edge
	def corners_belong_to_edge(self, c1, c2):
		return True in [
			(c1==self.l_top and c2==self.r_top) or
			(c1==self.r_top and c2==self.l_top) or
			(c1==self.r_top and c2==self.r_bot) or
			(c1==self.r_bot and c2==self.r_top) or
			(c1==self.r_bot and c2==self.l_bot) or
			(c1==self.l_bot and c2==self.r_bot) or
			(c1==self.l_bot and c2==self.l_top) or
			(c1==self.l_top and c2==self.l_bot) ]


    # ______
    #|    . |
    #|______|
	def is_point_inside_rect(self, point):
		return (self.l_top.x <= point.x <= self.r_top.x and
				self.l_top.y <= point.y <= self.l_bot.y)


    #  ______
    # |     _|____
    # |____|      |
    #      |______|
	def overlaps_with(self, rect):
		for corner in rect:
			if self.is_point_inside_rect(corner):
				return True
		for corner in self:
			if rect.is_point_inside_rect(corner):
				return True
		return False


    #  ______                ____ ______
    # |     _|____          |    |      |
    # |____|      |   -->   |____|______|
    #      |______|
	def align_with_top_edge_of(self, rect):
		self.l_top.y = self.r_top.y = rect.r_top.y
		self.l_bot.y = self.r_bot.y = self.l_top.y+self.height
		return self


	#  ______                ______
    # |     _|____          |______|
    # |____|      |   -->   |      |
    #      |______|         |______|
	def align_with_left_edge_of(self, rect):
		self.l_top.x = self.l_bot.x = rect.l_top.x
		self.r_top.x = self.r_bot.x = self.l_top.x+self.width
		return self


    # ______
    #|      |
    #|______|
    #    ______
    #   |      |
    #   |______|
	def overlaps_on_x_axis_with(self, rect):
		return self.copy().align_with_top_edge_of(rect).overlaps_with(rect)


    # ______
    #|      |   ______
    #|______|  |      |
    #          |______|
	def overlaps_on_y_axis_with(self, rect):
		return self.copy().align_with_left_edge_of(rect).overlaps_with(rect)


	# ______
    #|      |             The calculation includes
    #|______|             both edges and corners.
    #        \ d
    #         \ ______
    #          |      |
    #          |______|
	def distance_to_rect(self, rect):

		# 1. see if they overlap
		if self.overlaps_with(rect):
			return 0

		# 2. draw a line between rectangles
		line = (self.center, rect.center)

		# 3. find the two edges that intersect the line
		edge1 = None
		edge2 = None
		for edge in self.iter_edges():
			if lines_intersect(edge, line):
				edge1 = edge
				break
		for edge in rect.iter_edges():
			if lines_intersect(edge, line):
				edge2 = edge
				break
		assert edge1
		assert edge2

		# 4. find shortest distance between these two edges
		distances=[
			distance_between_edge_and_point(edge1, edge2[0]),
			distance_between_edge_and_point(edge1, edge2[1]),
			distance_between_edge_and_point(edge2, edge1[0]),
			distance_between_edge_and_point(edge2, edge1[1]),
		]

		return min(distances)


# ---------------------- Math primitive functions ----------------------

def distance_between_points(point1, point2):
	return point1.distance_to_point(point2)

def distance_between_rects(rect1, rect2):
	return rect1.distance_to_rect(rect2)

def triangle_area_at_points(p1, p2, p3):
	a=p1.distance_to_point(p2)
	b=p2.distance_to_point(p3)
	c=p1.distance_to_point(p3)
	s=(a+b+c)/float(2)
	area=sqrt(s*(s-a)*(s-b)*(s-c))
	return area

# Finds angle using cos law
def angle(a, b, c):
	divid=(a**2+b**2-c**2)
	divis=(2*a*b)
	if (divis)>0:
		result=float(divid)/divis
		if result<=1.0 and result>=-1.0:
			return acos(result)
		return 0
	else:
		return 0

# Checks if point faces edge
def point_faces_edge(edge, point):
	a=edge[0].distance_to_point(edge[1])
	b=edge[0].distance_to_point(point)
	c=edge[1].distance_to_point(point)
	ang1, ang2 = angle(b, a, c), angle(c, a, b)
	if ang1>pi/2 or ang2>pi/2:
		return False
	return True

def lines_intersect(line1, line2):
	return lines_overlap_on_x_axis(line1, line2) and lines_overlap_on_y_axis(line1, line2)

def lines_overlap_on_x_axis(line1, line2):
	x1, x2, = line1[0].x, line1[1].x
	x3, x4, = line2[0].x, line2[1].x
	e1_left, e1_right = min(x1, x2), max(x1, x2)
	e2_left, e2_right = min(x3, x4), max(x3, x4)
	return (e1_left >= e2_left and e1_left <= e2_right) or (e1_right >= e2_left and e1_right <= e2_right) or\
	       (e2_left >= e1_left and e2_left <= e1_right) or (e2_right >= e1_left and e2_right <= e1_right)

def lines_overlap_on_y_axis(line1, line2):
	y1, y2, = line1[0].y, line1[1].y
	y3, y4, = line2[0].y, line2[1].y
	e1_top, e1_bot = min(y1, y2), max(y1, y2)
	e2_top, e2_bot = min(y3, y4), max(y3, y4)
	return (e1_top >= e2_top and e1_top <= e2_bot) or (e1_bot >= e2_top and e1_bot <= e2_bot) or\
	       (e2_top >= e1_top and e2_top <= e1_bot) or (e2_bot >= e1_top and e2_bot <= e1_bot)


# Gives distance if the point is facing edge, else False
def distance_between_edge_and_point(edge, point): # edge is a tupple of points
	if point_faces_edge(edge, point):
		area=triangle_area_at_points(edge[0], edge[1], point)
		base=edge[0].distance_to_point(edge[1])
		height=area/(0.5*base)
		return height
	return min(distance_between_points(edge[0], point),
	           distance_between_points(edge[1], point))

'''


class Square(RegularPolygon)


class Rombus(Rectangle)


class Trapeze(Quadrangle)


class Parallelogram(Rectangle)


Пятиугольник
Шестиугольник


class Circum(Shape)
    Center  # Point object

    def __init__(self):
        return


class Ellipse(Circum)
    Radius
    Radius2
    Center2

    def __init__(self):
        return


class Circle(Circum)
    Radius  # Radise of Circle

    def __init__(self):
        return

    def get_radius(self):
        return

    def get_center(self):
        return

    def set_radius(self):
        return

    def set_center(self):
        return

    def get_length(self):
        return

    def get_square(self):
        return


'''
class Circle_2(Boost.Python.instance)
   	An object of type Circle_2 is a circle in the two-dimensional Euclidean plane. 
The circle is oriented, i.e. its boundary has clockwise or counterclockwise orientation . 
The boundary splits E x E into a positive and a negative side, 
where the positive side is to the left of the boundary. 
The boundary also splits E x E into a bounded and an unbounded side. 
Note that the circle can be degenerated, i.e. the squared radius may be zero.
For more details see a C++ doc:
http://www.cgal.org/Manual/3.2/doc_html/cgal_manual/Kernel_23_ref/Class_Circle_2.html


Method resolution order:
Circle_2
Boost.Python.instance
__builtin__.object
Methods defined here:
__eq__(...)
__init__(...)
c = Circle_2( Point_2 center,squared_radius,Orientation ori = COUNTERCLOCKWISE)introduces a variable c of type Circle_2. 
It is initialized to the circle with center center, squared radius squared_radius and orientation ori.
Precondition: ori COLLINEAR, and further, squared_radius 0.

c = Circle_2( Point_2 p,Point_2 q,Point_2 r);
introduces a variable c of type Circle_2. 
It is initialized to the unique circle which passes through the points p, q and r. 
The orientation of the circle is the orientation of the point triple p, q, r.
Precondition: p, q, and r are not collinear.

c = Circle_2( Point_2 p,Point_2 q,Orientation ori = COUNTERCLOCKWISE)

introduces a variable c of type Circle_2. It is initialized to the circle with diameter pq and orientation ori.
Precondition: ori COLLINEAR.
c = Circle_2( Point_2 center,Orientation ori = COUNTERCLOCKWISE)
introduces a variable c of type Circle_2. 
It is initialized to the circle with center center, squared radius zero and orientation ori.
Precondition: ori COLLINEAR.
Postcondition: c.is_degenerate() = true.
__ne__(...)
bbox(...)
bounded_side(...)
c.bounded_side(self, Point_2 p) -> Bounded_side
returns ON_BOUNDED_SIDE, ON_BOUNDARY, 
or ON_UNBOUNDED_SIDE  iff p lies properly inside, on the boundary, or properly outside of c, resp.
center(...)
c.center(self) ->Point_2
returns the center of c.
has_on_boundary(...)
c.has_on_boundary(self , Point_2 p) -> bool
has_on_bounded_side(...)
c.has_on_bounded_side(self , Point_2 p) -> bool
has_on_negative_side(...)
c.has_on_positive_side(self , Point_2 p) -> bool
has_on_positive_side(...)
c.is_degenerate(self) -> bool
returns true, iff c is degenerate, i.e. if c has squared radius zero.
has_on_unbounded_side(...)
c.has_on_negative_side(self , Point_2 p) -> bool
is_degenerate(...)
c.opposite(self) -> Circle_2
returns the circle with the same center and squared radius as c but with opposite orientation .
opposite(...)
c.bbox(self) -> Bbox_2
returns a bounding box containing c.
orientation(...)
c.orientation(self) -> Orientation
returns the orientation of c.
oriented_side(...)
c.oriented_side(self ,Point_2 p) ->Oriented_side
returns either the constant ON_ORIENTED_BOUNDARY, ON_POSITIVE_SIDE, 
or ON_NEGATIVE_SIDE, iff p lies on the boundary, properly on 
the positive side, or properly on the negative side of c, resp.
squared_radius(...)
c.squared_radius(self) ->double
returns the squared radius of c.
Data and other attributes defined here:
__instance_size__ = 36
Data and other attributes inherited from Boost.Python.instance:
__dict__ = <dictproxy object>
__new__ = <built-in method __new__ of Boost.Python.class object>
T.__new__(S, ...) -> a new object with type S, a subtype of T
__weakref__ = <member '__weakref__' of 'Boost.Python.instance' objects>
'''
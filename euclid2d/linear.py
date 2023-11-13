import euclid2D.core as core


class Linear(core.Euclid):
    """ У всех линейных объектов должен быть метод
    для определения координаты у по имеющейся координате х и наоборот"""
    ''' Класс должен  поддерживать операции отражения, отображения,
    вращения, масштабирования, преобразования, афинные преобразования(?)'''
    length = None  # Full length of linear object

    def __len__(self):
        """ property return full length
        of linear object (redefine for each subclass)"""
        return abs(self.length)


class Line(Linear):
    k = 1
    b = 0

    def __init__(self, k=1, b=0):
        '''Create Line object from line function's attributes "k" and "b"'''
        super().__init__()


''' Нахождение пересечений'''
'''
class Line_2(Boost.Python.instance)
An object l of the data type Line_2 is a directed straight line
in the two-dimensional Euclidean plane ExE.
It is defined by the set of points with Cartesian  coordinates
(x,y) that satisfy the equation l : ax + by + c = 0
The line splits ExE in a positive and a negative side.
A point p with Cartesian coordinates (px, py) is on the positive
side of l, if a px + b py + c > 0,
it is on the negative side of l, if a px + b py + c < 0.
The positive side is to the left of l.
For more details see a C++ documentation:
http://www.cgal.org/Manual/3.2/doc_html/cgal_manual/Kernel_23_ref/Class_Line_2.html


Method resolution order:
Line_2
Boost.Python.instance
__builtin__.object
Methods defined here:
__eq__(...)
__init__(...)
l = Line_2( double a, double b, double c)
introduces a line l with the line equation
in Cartesian coordinates ax +by +c = 0.
l = Line_2( Point_2 p, Point_2 q)
introduces a line l passing through the
points p and q. Line l is directed from p to q.
l = Line_2( Point_2 p, Direction_2 d)
introduces a line l passing through point p with direction d.
l = Line_2( Point_2 p, Vector_2 v)
introduces a line l passing through point p and oriented by v.
l = Line_2( Segment_2 s)
introduces a line l supporting the segment s, oriented from source to target.
l = Line_2( Ray_2 r)
introduces a line l supporting the ray r, with same orientation.
__ne__(...)
a(...)
a(self) -> returns the first coefficient of l.
b(...)
b(self) -> returns the second coefficient of l.
c(...)
c(self) -> returns the third coefficient of l.
direction(...)
direction(self) -> Line_2
returns the direction of l.
has_on(...)
has_on_boundary(...)
has_on_negative_side(...)
has_on_positive_side(...)
is_degenerate(...)
is_degenerate(slef) ->bool
line l is degenerate, if the coefficients a and b of
the line equation are zero.
is_horizontal(...)
is_vertical(...)
opposite(...)
opposite(self) -> Line_2
returns the line with opposite direction.
oriented_side(...)
oriented_side(slef, Point_2 p) -> Oriented_side
returns ON_ORIENTED_BOUNDARY, ON_NEGATIVE_SIDE,
or the constant ON_POSITIVE_SIDE, depending on
the position of p relative to the oriented line l.
perpendicular(...)
perpendicular(self,Point_2 p) -> Line_2
returns the line perpendicular to l and passing through p,
where the direction is the direction of l rotated
counterclockwise by 90 degrees.
point(...)
point(slef,i) -> Point_2
returns an arbitrary point on l.
It holds point(i) == point(j), iff i==j.
Furthermore, l is directed from point(i)  to point(j), for all i < j.
projection(...)
projection(self,Point_2 p) -> Point_2
returns the orthogonal projection of p onto l.
to_vector(...)
to_vector(self) -> Vector_2
returns a vector having the direction of l.
transform(...)
transform(slef,Aff_transformation_2 t) -> Line_2
returns the line obtained by applying t on a point on l and the direction of l.
x_at_y(...)
x_at_y(self,y) -> returns the x-coordinate
of the point at l with given y-coordinate.
Precondition: l is not horizontal.
y_at_x(...)
y_at_x(self,x) -> returns the y-coordinate
of the point at l with given x-coordinate.
Precondition: l is not vertical.
Data and other attributes defined here:
__instance_size__ = 32
Data and other attributes inherited from Boost.Python.instance:
__dict__ = <dictproxy object>
__new__ = <built-in method __new__ of Boost.Python.class object>
T.__new__(S, ...) -> a new object with type S, a subtype of T
__weakref__ = <member '__weakref__' of 'Boost.Python.instance' objects>

'''


class Ray(Linear):
    direction  # направление луча от нулевой точки
    zeropoint  # начало луча на линии

    def __init__(self):
        super().__init__()
        return


'''
class Ray_2(Boost.Python.instance)
An object r of the data type Ray_2
is a directed straight ray in the
two-dimensional Euclidean plane ExE.
It starts in a point called the source
of r and goes to infinity.
for more details see a C++ doc:
http://www.cgal.org/Manual/3.2/doc_html/cgal_manual/Kernel_23_ref/Class_Ray_2.html

Method resolution order:
Ray_2
Boost.Python.instance
__builtin__.object
Methods defined here:
__eq__(...)
__init__(...)
r = Ray_2(self,Point_2 p,Point_2 q)
introduces a ray with source p and passing through point q.
r = Ray_2(self,Point_2 p,Direction_2 d)
introduces a ray starting at source p with direction d.
r = Ray_2(self,Point_2 p,Vector_2 v)
introduces a ray r starting at source p with the direction of v.
r = Ray_2(self,Point_2 p,line_2 l)
introduces a ray r starting at source p with the same direction as l.
__ne__(...)
collinear_has_on(...)
collinear_has_on(self,Point_2 p) -> bool
checks if point p is on r.
This function is faster than function has_on()
if the precondition checking is disabled.
Precondition: p is on the supporting line of r.
direction(...)
direction(self) -> Direction_2
returns the direction of r.
has_on(...)
has_on(self,Point_2 p) -> bool
A point is on r, iff it is equal to the source
of r, or if it is in the interior of r
is_degenerate(...)
is_degenerate(self) -> bool
ray r is degenerate, if the source and the second
defining point fall together (that is if the direction is degenerate).
is_horizontal(...)
is_vertical(...)
opposite(...)
opposite(self) -> Ray_2
returns the ray with the same source and the opposite direction.
point(...)
point(self,i) -> Point_2
returns a point on r. point(0) is the source, point(i), with i>0,
is different from the source.
Precondition: i 0.
second_point(...)
source(...)
source(self) -> Point_2
returns the source of r
start(...)
supporting_line(...)
supporting_line(self) -> line_2
returns the line supporting r which has the same direction.
to_vector(...)
to_vector(self) -> Vector_2
returns a vector giving the direction of r
transform(...)
transform(Aff_transformation_2 t) -> Ray_2
returns the ray obtained by applying t on the source and on the direction of r.
Data and other attributes defined here:
__instance_size__ = 40
Data and other attributes inherited from Boost.Python.instance:
__dict__ = <dictproxy object>
__new__ = <built-in method __new__ of Boost.Python.class object>
T.__new__(S, ...) -> a new object with type S, a subtype of T
__weakref__ = <member '__weakref__' of 'Boost.Python.instance' objects>

'''


class Segment(Linear):
    '''
    Нужно сделать возможность инициации через линию и через две точки
    '''


'''
class Segment_2(Boost.Python.instance)
An object s of the data type Segment_2 is a directed straight line
segment in the two-dimensional Euclidean plane RxR,
i.e. a straight line segment [p,q] connecting two points p,q in RxR.
The segment is topologically closed, i.e. the end points belong to it.
Point p is called the source and q is called the target of s.
The length of s is the Euclidean distance between p and q. Note that
there is only a function to compute the square of the length,
because otherwise we had to perform a square root operation which is
not defined for all number types, which is expensive, and may not be exact..
For more details see a C++ doc:
http://www.cgal.org/Manual/doc_html/cgal_manual/Kernel_23_ref/Class_Segment_2.html

Creation:
 s = Segment_2( Point_2 p, Point_2 q)
introduces a segment s with source p and target q.
 The segment is directed from the source towards the target.

Method resolution order:
Segment_2
Boost.Python.instance
__builtin__.object
Methods defined here:
__eq__(...)
__getitem__(...)
s[i] -> Point_2
returns vertex(i)
__init__(...)
__ne__(...)
bbox(...)
bbox(slef) -> Bbox_2
returns a bounding box containing s.
collinear_has_on(...)
collinear_has_on(slef,Point_2) -> bool
checks if point p is on segment s. This function
is faster than function has_on().
Precondition: p is on the supporting line of s.
direction(...)
direction(slef) -> Direction_2
returns the direction from source to target of s.
end(...)
has_on(...)
has_on(slef,Point_2 p) -> bool
A point p is on s, iff it is equal to the source or target
of s, or if it is in the interior of s.
is_degenerate(...)
is_degenerate(slef) -> bool
segment s is degenerate, if source and target are equal.
is_horizontal(...)
is_vertical(...)
max(...)
max(slef) ->  Point_2
returns the point of Segment with lexicographically largest coordinate.
min(...)
min(slef) ->  Point_2
returns the point of s with lexicographically smallest coordinate.
opposite(...)
opposite(slef) -> Segment_2
returns a segment with source and target point interchanged.
point(...)
point(slef) -> returns vertex(i).
source(...)
source(slef) -> Point_2
returns the source of s.
squared_length(...)
squared_length(slef) -> double
returns the squared length of s.
start(...)
supporting_line(...)
supporting_line(self) -> Line_2
returns the line l passing through s.
Line l has the same orientation as segment s.
target(...)
target(self) -> Point_2
returns the target of s.
to_vector(...)
to_vector(slef) -> Vector_2
returns the vector s.target() - s.source().
transform(...)
transform(slef,Aff_transformation_2 t) -> Segment_2
returns the segment obtained by applying t on the source and the target of s.
vertex(...)
vertex(slef,i) -> Point_2
returns source or target of s: vertex(0) returns the source of s,
vertex(1) returns the target of s.
The parameter i is taken modulo 2, which gives easy access to the other vertex.
Data and other attributes defined here:
__instance_size__ = 40
Data and other attributes inherited from Boost.Python.instance:
__dict__ = <dictproxy object>
__new__ = <built-in method __new__ of Boost.Python.class object>
T.__new__(S, ...) -> a new object with type S, a subtype of T
__weakref__ = <member '__weakref__' of 'Boost.Python.instance' objects>

'''


startpoint  # начальная точка отрезка
endpoint  # конечная точка отрезка


def __init__(self):
    return

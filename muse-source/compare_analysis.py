'''
Цель проекта Библиотека Euclid - сделать настолько же проработанный 
в части интерфейса и возможностей (но только в части 2D) библиотека 
geometry в пакете SimPy. С опорой только на предустановленные библиотеки языка Python.

назначение библиотеки:
Оперирование 2D объектами на плоскости
1. Создание плоскостей и объектов
2. Вычисление расстояний и углов между геометрическими объектами
3. Определение паралелльности линий и отрезков
4. Проведение афинных преобразований
5. Пересечение полигонов с полигонами, линиями, окружностями.

https://server.179.ru/tasks/python/2022b/pgm39__Geometry-1.html
Смотреть здесь понятия и задачи в сфере вычислительной геометрии

Geometry
https://docs.sympy.org/latest/modules/geometry/index.html
The geometry module for SymPy allows one to create two-dimensional geometrical entities, 
such as lines and circles, and query for information about these entities. 
This could include asking the area of an ellipse, checking for collinearity of a set of points, 
or finding the intersection between two lines. 
The primary use case of the module involves entities with numerical values, 
but it is possible to also use symbolic representations.

-
SymPy's geometry module can also be very, very slow. 
Since it is designed for doing symbolic math, 
it prefers to use precise expressions over approximate floating point values. 
Given the amount of square roots that are usually involved in geometric computations, 
you can imagine how those expressions get really large and very slow.

geometry-simple (python library) 
https://github.com/sbliven/geometry-simple
3D geometry in python
A small python library for constructing simple geometrical objects (points, lines, planes) 
and transformations on them. It is also possible to measure distances and angles. 
The library is designed to be usable without knowledge of linear algebra.


Closed. This question does not meet Stack Overflow guidelines. It is not currently accepting answers.
Want to improve this question? Update the question so it's on-topic for Stack Overflow.

Closed 5 years ago.

I am looking for a good and well developed library for geometrical manipulations and evaluations in python, like:

evaluate the intersection between two lines in 2D and 3D (if present)
evaluate the point of intersection between a plane and a line, or the line of intersection between two planes
evaluate the minimum distance between a line and a point
find the orthonormal to a plane passing through a point
rotate, translate, mirror a set of points
find the dihedral angle defined by four points

оценить пересечение двух строк в 2D и 3D (если имеется)
оценить точку пересечения между плоскостью и линией или линию пересечения между двумя плоскостями
оценить минимальное расстояние между линией и точкой
найти ортонормированную плоскость, проходящую через точку
вращать, переводить, зеркально отображать множество точек
найти двугранный угол, определяемый четырьмя точками

I have a compendium book for all these operations, 
and I could implement it but unfortunately I have no time, 
so I would enjoy a library that does it. 
Most operations are useful for gaming purposes, 
so I am sure that some of these functionalities can be found in gaming libraries, 
but I would prefer not to include functionalities (such as graphics) I don't need.
'''


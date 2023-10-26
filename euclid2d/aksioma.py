'''
Модуль хранит информацию об артефактах для работы пакета Euclid2D:
константы, функции и т.п.
'''
# режим округления значений координат при вычислениях на конкретной плоскости
ROUND_MASK = {
    "ZERO": None,  # без округления
    "MATH": 1,  # математический
    "MAX": 2,  # до ближайшего большего целого
    "MIN": 3,  # до ближайшего меньшего целого
    "ROUND": 4  # питонический режим round
    }

AFFINE_RANK = {  
    # the dimension of the smallest affine space containing all the points
    "NONE": -1,  # Not defined. By convention,the empty set has affine rank -1.
    "0D": 0,  # If the points lie on a line and are not all the same - affine rank = 0  
    "1D": 1,  # If the points lie on a line - their affine rank is 1
    "2D": 2  # If the points lie on a plane but not a line, their affine rank is 2
}

EUCLID_OBJECT_TYPE = {
    "NONE": None,  # not defined
    "POINT": 1,  # точка
    "LINE": 2,  # линия
    "ANGLE": 3,  # угол
    "FIGURE": 4  # фигура
    }

plane_list = {}
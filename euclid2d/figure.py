'''
Объект Кривая
'''

class Curve(Linear)
    coef  # список коэффициентов х3, х2, х1, х0 - для построения кривых

    def __init__(self):
        return

    def is_intersect(self):
        return


'''
Объект - Ломанная
нарисовать ломаную линию по точками, заданным как
массив кортежей p(каждый элемент массива – кортеж(x, y)
координат очередной точки)
'''


class Polyline(Linear)
    vertexes  # перечень вершин
    segments  # список объектов Segment составляющих объект Polyline




class Angle(Linear)
    zeropoint
    ray1
    ray2

    def __init__(self):
        return

    def get_bisectrisse(self):
        return

    def get_angle(self):
        return

    def get_bissectrisse_angle(self):
        '''
        Нахождение бисектрисы угла
        '''
        return

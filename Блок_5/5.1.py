"""Подвиг 5"""
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


pt = Point(1, 2)

try:
    pt.z
except AttributeError:
    print('Атрибут с именем z не существует')


"""Подвиг 7"""
# считывание строки и разбиение ее по пробелам
lst_in = input().split()

def f(x):
    try:
        x = int(x)
        return x
    except ValueError:
        return 0
print(sum([f(i) for i in lst_in]))



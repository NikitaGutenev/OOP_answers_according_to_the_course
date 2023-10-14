"""Подвиг 2"""
class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.lst = list(kwargs.keys())
        
    def __getitem__(self, item):
        self.validate(item)
        return self.__dict__[self.lst[item]]
            
    def __setitem__(self, key, value):
        self.validate(key)
        self.__dict__[self.lst[key]] = value
    
    def validate(self, item):
        if item < 0 or item > len(self.lst) or isinstance(item, float):
            raise IndexError('неверный индекс поля')


"""Подвиг 3"""
class Track:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.track = []
    
    def add_point(self, x, y, speed):
        self.track.append([(x, y), speed])
    
    def __getitem__(self, key):
        self.validate(key)
        return self.track[key]

    def __setitem__(self, key, value):
        self.validate(key)
        self.track[key][1] = value

    def validate(self, key):
        if not 0 <= key < len(self.track):
            raise IndexError('некорректный индекс')


"""Подвиг 4"""
class Array:
    def __init__(self, maxx, cell):
        self.maxx = maxx
        self.cell = cell
        self.lst = [cell() for i in range(self.maxx)]
        
    def __getitem__(self, key):
        self.check_key(key)
        return self.lst[key].value
    
    def __setitem__(self, key, value):
        self.check_key(key)
        self.lst[key].value = value
        
    def __str__(self):
        return ' '.join([str(i.value) for i in self.lst])
        
    def check_key(self, key):
        if not 0 <= key < self.maxx or not isinstance(key, int):
            raise IndexError('неверный индекс для доступа к элементам массива')
        
        
class Integer:
    def __init__(self, start=0):
        self.__val = start
        
    @property
    def value(self):
        return self.__val
    
    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise ValueError('должно быть целое число')
        self.__val = val


"""Подвиг 5"""
# мне было лень решать)))


"""Подвиг 6"""
class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.tail = None
        self.count = 0
        
    def __getitem__(self, key):
        return self.find(key)
    
    def __setitem__(self, key, value):
        tmp = self.find(key).next
        tmp2 = self.find(key-1)
        tmp2.next = value
        tmp2.next.next = tmp

    def push(self, obj):
        self.count += 1
        if self.top == None:
            self.top = obj
            self.tail = obj
        else:
            self.tail.next = obj
            self.tail = obj

    def pop(self):
        self.count -= 1
        if self.top.next == None:
            tmp = self.top
            self.top = None
            self.tail = None
            return tmp
        else:
            tmp = self.find(mode=True)
            self.tail = tmp
            tmp = tmp.next
            self.tail.next = None
            return tmp
        
    def find(self, indx = 0, mode=False):
        tmp = self.top
        if not mode:
            if (not isinstance(indx, int)) or not (0 <= indx < self.count):
                raise IndexError('неверный индекс')
            for i in range(indx):
                tmp = tmp.next
        else:
            while tmp.next.next != None:
                tmp = tmp.next
        return tmp


"""Подвиг 7"""
class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)
        self.len = len(self.coords)

    def __getitem__(self, key):
        tmp = tuple(self.coords)
        return tmp[key]

    def __setitem__(self, key, value):
        self.coords[key] = value


"""Подвиг 8"""
class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0
        
    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple([[Cell() for i in range(3)] for j in range(3)])
        
    def clear(self):
        self.pole = tuple([[Cell() for i in range(3)] for j in range(3)])
        
    def validate(self, key):
        tmp = [True if isinstance(i, (int, slice)) else False for i in key]
        if len(key) != 2 or not all(tmp):
            raise IndexError('неверный индекс клетки')
        
    def __getitem__(self, key):
        self.validate(key)
        if (type(key[1])) == slice:
            return tuple([i.value for i in self.pole[key[0]]])
        elif (type(key[0])) == slice:
            return tuple([i[key[1]].value for i in self.pole[key[0]]])
        return self.pole[key[0]][key[1]].value
    
    def __setitem__(self, key, value):
        self.validate(key)
        if bool(self.pole[key[0]][key[1]]):
            self.pole[key[0]][key[1]].value = value


"""Подвиг 9"""
class Bag:
    def __init__(self, w):
        self.max_weight = w
        self.bag = []
        self.total_weight = 0
        
    def add_thing(self, thing, indx = None, mode = False):
        if self.total_weight + thing.weight <= self.max_weight and not mode:
            self.total_weight += thing.weight
            self.bag.append(thing)
        elif mode and self.total_weight + thing.weight - self.bag[indx].weight <= self.max_weight:
            self.total_weight += thing.weight - self.bag[indx].weight
            self.bag[indx] = thing
        else:
            raise ValueError('превышен суммарный вес предметов')
            
    def validate(self, key):
        if not isinstance(key, int) and not 0 <= key < len(self.bag):
            raise IndexError('неверный индекс')
      
    def __getitem__(self, key):
        self.validate(key)
        return self.bag[key]
    
    def __setitem__(self, key, value):
        self.validate(key)
        self.add_thing(value, indx=key, mode=True)
        
    def __delitem__(self, key):
        self.validate(key)
        self.total_weight -= self.bag[key].weight
        return self.bag.pop(key)
        
class Thing:
    def __init__(self, n, w):
        self.name = n
        self.weight = w


"""Подвиг 10"""
class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table = dict()
        
    def get_row_col(self):
        rows = set()
        cols = set()
        for i in self.table.keys():
            rows.add(i[0])
            cols.add(i[1])
        self.rows = max(rows)+1
        self.cols = max(cols)+1
    
    def add_data(self, row, col, data):
        self.table[(row,col)] = data
        self.get_row_col()
    
    def remove_data(self, row, col):
        if (row, col) in self.table:
            tmp = self.table.pop((row, col))
            self.get_row_col()
            return tmp
        else:
            raise IndexError('ячейка с указанными индексами не существует')
    
    def __getitem__(self, key):
        if key in self.table:
            return self.table[key].value
        else:
            raise ValueError('данные по указанным индексам отсутствуют')
            
    def __setitem__(self, key, value):
        self.table[key] = Cell(value)
        self.get_row_col()
    
    
class Cell:
    def __init__(self, value):
        self.value = value
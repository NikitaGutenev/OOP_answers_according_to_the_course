"""Подвиг 4"""
import sys

# считывание списка из входного потока (эту строчку и список lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)
        
    def __bool__(self):
        return self.score > 0
    
players = [Player(*i.split('; ')) for i in lst_in]
players_filtered = list(filter(bool, players))


"""Подвиг 5"""
import sys

# здесь пишите программу
class MailBox:
    def __init__(self):
        self.inbox_list = []
        
    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        for item in lst_in:
            self.inbox_list.append(MailItem(*item.split('; ')))
    
class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from, self.title, self.content = mail_from, title, content
        self.is_read = False
        
    def set_read(self, fl_read):
        self.is_read = fl_read
        
    def __bool__(self):
        return self.is_read

    
mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))


"""Подвиг 6"""
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        
    def __len__(self):
        length = (pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2))**0.5
        return False if length < 1 else int(length)


"""Подвиг 7"""
class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args
            
    def __bool__(self):
        return all([self.__dict__.get('x1'), self.__dict__.get('y1'),
                   self.__dict__.get('x2'), self.__dict__.get('y2')])
    
    def get_coords(self):
        if not bool(self):
            raise AttributeError('нет координат для извлечения')
        else:
            return (self.x1, self.y1, self.x2, self.y2)
        
lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 2, 2), Ellipse(1, 2, 3, 4)]
for i in lst_geom:
    if i:
        i.get_coords()


"""Подвиг 8"""
from random import shuffle,randint,choice

# здесь объявляйте классы
class Cell:
    def __init__(self, around_mines = 0, mine = False):
        self.__number = around_mines
        self.__is_mine = mine
        self.__is_open = False
        
    def __setattr__(self, key, value):
        if key in (f'_{self.__class__}__is_mine', f'_{self.__class__}__is_open', '__is_mine', '__is_open') \
           and type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        elif key in (f'_{self.__class__}__number', '__number') and value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        return object.__setattr__(self, key, value)
    
    def __bool__(self):
        return not self.is_open
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, x):
        self.__number = x
        
    @property
    def is_mine(self):
        return self.__is_mine
    
    @is_mine.setter
    def is_mine(self, x):
        self.__is_mine = x
        
    @property
    def is_open(self):
        return self.__is_open
    
    @is_open.setter
    def is_open(self, x):
        self.__is_open = x
    

class GamePole:
    __instance = None
    
    def __new__(cls, *arg, **kwarg):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, n, m, total_mines):
        self.__pole_cells = tuple([tuple([Cell() for _ in range(m)]) for _ in range(n)])
        self.m = m
        self.n = n
        self.total_mines = total_mines
        
    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        m = 0
        mines = []
        index = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                index.append((i, j))
                if i == j == 0:
                    index.pop(-1)
        while m < self.total_mines:
            i = randint(0,self.n-1)
            j = randint(0,self.m-1)
            if not self.__pole_cells[i][j].is_mine:
                self.__pole_cells[i][j].is_mine = True
                m+=1
                mines.append((i, j))
        for mine in mines:
            for indx in index:
                if 0<=mine[0]+indx[0]<self.n and 0<=mine[1]+indx[1]<self.m:
                    self.__pole_cells[mine[0]+indx[0]][mine[1]+indx[1]].number += 1
     
    def open_cell(self, i, j):
        try:
            self.__pole_cells[i][j].is_open = True
        except:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for i in self.__pole_cells:
            for j in range(len(i)):
                if i[j].is_open:
                    if i[j].is_mine:
                        print('*',end = ' ')
                    else:
                        print(f'{i[j].number}',end=' ')
                else:
                    print(f'#',end=' ')
            print('\n')


"""Подвиг 9"""
class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __len__(self):
        return len(self.coords)
    
    def __eq__(self, other):
        self.validate(other)
        return self.coords == other.coords
    
    def validate(self, other):
        other = self.instance_validate(other)
        if not len(self) == len(other):
            raise ArithmeticError('размерности векторов не совпадают')
            
    def instance_validate(self, obj):
        if type(self) == type(obj):
            return obj.coords
        elif type(obj) in (int, float):
            return [obj for i in range(len(self))]
        else:
            raise TypeError('Неверный тип данных')
    
    def math(self, op, v1, v2):
        v2 = self.instance_validate(v2)
        return [eval(f'{v1[i]}{op}{v2[i]}') for i in range(len(v1))]
    
    def __add__(self, other):
        self.validate(other)
        op = '+'
        return Vector(*self.math(op, self.coords, other))
    
    def __mul__(self, other):
        self.validate(other)
        op = '*'
        return Vector(*self.math(op, self.coords, other))
            
    def __sub__(self, other):
        self.validate(other)
        op = '-'
        return Vector(*self.math(op, self.coords, other))

    def __iadd__(self, other):
        self.validate(other)
        op = '+'
        self.coords = self.math(op, self.coords, other)
        return self

    def __isub__(self, other):
        self.validate(other)
        op = '-'
        self.coords = self.math(op, self.coords, other)
        return self
    
    def __imul__(self, other):
        self.validate(other)
        op = '*'
        self.coords = self.math(op, self.coords, other)
        return self
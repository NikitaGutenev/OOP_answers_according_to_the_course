"""Подвиг 2"""
import sys

# здесь пишите программу
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {self.pages}'

lst_in = list(map(str.strip, sys.stdin.readlines())) # считывание списка из входного потока (эту строчку не менять)
book = Book(lst_in[0], lst_in[1], int(lst_in[2]))
print(book)



"""Подвиг 3"""
class Model:
    def query(self, *args, **kwargs):
        self.query_dict = dict()
        self.query_dict.update(**kwargs)

    def __str__(self):
        res = self.__class__.__name__
        if hasattr(self, 'query_dict'):
            res = f'{self.__class__.__name__}:'
            res += ''.join(f' {k} = {v},' for k,v in self.query_dict.items()).rstrip(', ')
        return res



"""Подвиг 4"""
class WordString:
    def __init__(self, string=''):
        self.__string = string
        self.word = list()
    
    @property
    def string(self):
        return self.__string
    
    @string.setter
    def string(self, st):
        self.__string = st
        
    def __len__(self):
        self.word = self.__string.split()
        return len(self.word)
    
    def __call__(self, indx):
        return self.words(indx)

    def words(self,indx):
        return self.word[indx]



"""Подвиг 5   (Полносвязный список, но с доп дандерами ___len___, __call__)"""
class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        
    def __len__(self):
        return self.find(-1, flag=True)
    
    def __call__(self, indx):
        return self.find(indx).data
        
    def add_obj(self, obj):
        if self.head == None:
            self.head = obj
        elif self.head.next == None:
            self.head.next = obj
            self.head.next.prev = self.head
        else:
            self.tail.next = obj
            self.tail.next.prev = self.tail
        self.tail = obj
            
    def remove_obj(self, indx):
        obj = self.find(indx)
        if obj.next != None and obj.prev != None:
            obj.prev.next, obj.next.prev = obj.next.prev, obj.prev.next
        elif obj.next == None and obj.prev == None:
            self.head = None
            self.tail = None
        elif obj.next == None:
            obj.prev.next = None
            self.tail = obj.prev
        elif obj.prev == None:
            self.head = self.head.next
            self.head.prev = None
        
    def find(self, indx, flag = False):
        obj = self.head
        count = 1
        if indx != -1:
            for i in range(indx):
                obj = obj.next
        else:
            while obj.next != None:
                obj = obj.next
                count += 1
            if flag:
                return count
        return obj


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None
        
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, a):
        self.__prev = a
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, a):
        self.__next = a
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, a):
        self.__data = a



"""Подвиг 6"""
import math

class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img
        
    # def __setattr__(self, key, value):
    #     if isinstance(value, int or float):
    #         object.__setattr__(self,key,value)
    #     else:
    #         raise ValueError("Неверный тип данных.")
            
    def __abs__(self):
        return math.sqrt(self.real * self.real + self.img * self.img)
    
    @property
    def real(self):
        return self.__real
    
    @real.setter
    def real(self, x):
        self.__real = self.check_type(x)
        
    @property
    def img(self):
        return self.__img
    
    @img.setter
    def img(self, x):
        self.__img = self.check_type(x)
        
    @staticmethod
    def check_type(x):
        if isinstance(x, (int, float)):
            return x
        else:
            raise ValueError("Неверный тип данных.")


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)



"""Подвиг 7"""
import math

class RadiusVector:
    def __init__(self, *args):
        self.mera = len(args)
        self.coords = list(args)
        if self.mera == 1:
            self.mera = args[0]
            self.coords = [0] * self.mera
            
    def __len__(self):
        return self.mera
    
    def __abs__(self):
        return math.sqrt(sum([i*i for i in self.coords]))

    def set_coords(self, *args):
        if len(args) >= self.mera:
            self.coords = [args[i] for i in range(self.mera)]
        else:
            for i in range(len(args)):
                self.coords[i] = args[i]
        
    def get_coords(self):
        return tuple(self.coords)



"""Подвиг 8"""
class Clock:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.second = s
        
    def __setattr__(self, key, value):
        if isinstance(value, int) and value >=0:
            object.__setattr__(self, key, value)
    
    def get_time(self):
        return self.hours*3600 + self.minutes*60 + self.second


class DeltaClock:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
        
    def __len__(self):
        return self.get_diff_time(self.c1, self.c2)
    
    def __str__(self):
        res = self.get_diff_time(self.c1, self.c2)
        if res < 0:
            return '00: 00: 00'
        time = list(self.convert_time(res))
        for i in range(len(time)):
            if time[i] < 10:
                time[i] = '0' + str(time[i])
        return '{}: {}: {}'.format(*time)
        
    @staticmethod
    def get_diff_time(c1,c2):
        return c1.get_time() - c2.get_time()
        
    @staticmethod
    def convert_time(time):
        hours = time//3600
        time %=3600
        minutes = time//60
        time %=60
        return (hours,minutes,time)



"""Подвиг 9"""
class Ingredient:
    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return '{}: {}, {}'.format(self.name, self.volume, self.measure)

    
class Recipe:
    def __init__(self, *args):
        self.recipe = list(args)
        
    def __len__(self):
        return len(self.recipe)
        
    def add_ingredient(self, ing):
        self.recipe.append(ing)

    def remove_ingredient(self, ing):
        self.recipe.remove(ing)
        
    def get_ingredients(self):
        return tuple(self.recipe)



"""Подвиг 10"""
class PolyLine:
    def __init__(self, start_coord: tuple, *args: tuple):
        self.start = start_coord
        self.coords = []
        self.coords.append(self.start)
        for i in args:
            self.coords.append(i)

    def add_coord(self, x, y):
        self.coords.append((x,y))

    def remove_coord(self, indx):
        self.coords.pop(indx)
        
    def get_coords(self):
        return self.coords
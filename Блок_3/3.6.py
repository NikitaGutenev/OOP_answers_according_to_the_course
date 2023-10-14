"""Подвиг 4"""
class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def __hash__(self):
        return hash((self.width, self.height))


"""Подвиг 6"""
import sys

# здесь объявляйте классы
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        
    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))
    
    def __eq__(self, other):
        return hash(self) == hash(other)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!
shop_items = {}
for value in lst_in:
    value = value.split()
    item = ShopItem(value[0].rstrip(':'), value[1], value[2])
    total = shop_items.get(item, [-1, 0])[1] + 1
    shop_items[item] = [item, total]


"""Подвиг 7"""
import sys

# здесь объявляйте классы
class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, []).append(record)

    def read(self, id):
        keys = set(self.dict_db.keys())
        for i in keys:
            if i.pk == id:
                return i
            
            
class Record:
    id = 0
    def __new__(cls,*args,**kwargs):
        cls.id += 1
        return object.__new__(cls)
    
    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = int(old)
        self.pk = self.id
        
    def __hash__(self):
        return hash((self.fio.lower(), self.old))
    
    def __eq__(self, other):
        return hash(self) == hash(other)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in не менять!

# здесь продолжайте программу (используйте список строк lst_in)
db = DataBase('./')
for i in lst_in:
    db.write(Record(*i.split('; ')))


"""Подвиг 8"""
import sys

# здесь объявляйте класс
class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        
    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!

# здесь продолжайте программу (используйте список строк lst_in)
lst_bs = [BookStudy(*i.split('; ')) for i in lst_in]
unique_books = len(set(map(lambda x: hash(x), lst_bs)))


"""Подвиг 9"""
s_inp = input()  # эту строку (переменную s_inp) в программе не менять

class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __lt__(self, other):
        return hash(self) < hash(other)
        
    def __hash__(self):
        return hash((self.a, self.b, self.c))
    
    def __setattr__(self, key, value):
        self.validate(value)
        if str(value).find('.') + 1:
            return object.__setattr__(self, key, float(value))
        else:
            return object.__setattr__(self, key, int(value))
    
    @staticmethod
    def validate(x):
        if float(x) <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")

lst = [list(i.split()) for i in s_inp.split('; ')]
lst_dims = []
for i in lst:
    lst_dims.append(Dimensions(*i))
lst_dims.sort()


"""Подвиг 10"""
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.validate(a,b,c)
        
    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)) and value > 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        return object.__setattr__(self, key, value)
            
    def __len__(self):
        return int(self.a + self.b + self.c)
            
    @staticmethod
    def validate(a, b, c):
        if not (a < b+c and b < a+c and c < a+b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
            
    def __call__(self):
        p = self.__len__()/2
        return (p * (p-self.a) * (p-self.b) * (p-self.c))**0.5

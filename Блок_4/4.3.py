"""Подвиг 3"""
class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        

class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = int(size)
        if frm in ('pdf', 'doc', 'fb2', 'txt'):
            self.frm = frm


"""Подвиг 4"""
class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date
        

class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu
        
        
class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims
        
        
class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old
        
        
class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel


"""Подвиг 5"""
class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square
        
        
class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square
            
        
class Agency:
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def add_object(self, obj):
        self.items.append(obj)
        
    def remove_object(self, obj):
        self.items.remove(obj)
        
    def get_objects(self):
        return self.items


"""Подвиг 7"""
# здесь объявляйте функцию-декоратор
def integer_params_decorated(func):
    def wrap(self, *args):
        if all(map(lambda x: isinstance(x, int), args)):
            return func(self, *args)
        else:
            raise TypeError("аргументы должны быть целыми числами")
            
    return wrap
    
    
def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


"""Подвиг 8"""
class SoftList(list):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except IndexError:
            return False



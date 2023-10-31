"""Подвиг 3"""
class ListInteger(list):
    def __init__(self, lst):
        self.lst = list(lst)

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        self.lst[key] = value
        
    def __getitem__(self, key):
        return self.lst[key]
            
    def append(self, val):
        if isinstance(val, int):
            self.lst += [val]

    def __str__(self):
        return '['+ ', '.join(map(str, self.lst)) + ']'


"""Подвиг 4"""
class Thing():
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return str(self)


class DictShop(dict):
    def __init__(self, dicts = {}):
        if not isinstance(dicts, dict):
            raise TypeError('аргумент должен быть словарем')
        if not all([True if isinstance(k, Thing) else False for k in dicts.keys()]):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(dicts)
        
    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)


"""Подвиг 5"""
class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

class Plants(Protists):
    pass

class Mosses(Plants):
    pass

class Flowering(Plants):
    pass


class Animals(Protists):
    pass

class Worms(Animals):
    pass

class Mammals(Animals):
    pass

class Human(Mammals):
    pass

class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass

class Person(Human):
    pass

class Flower(Flowering):
    pass

class Worm(Worms):
    pass


lst_objs = [Monkey("мартышка", 30.4, 7),
            Monkey("шимпанзе", 24.6, 8),
            Person("Балакирев", 88, 34),
            Person("Верховный жрец", 67.5, 45),
            Flower("Тюльпан", 0.2, 1),
            Flower("Роза", 0.1, 2),
            Worm("червь", 0.01, 1),
            Worm("червь 2", 0.02, 1)]

lst_animals = [i for i in lst_objs if isinstance(i, Animals)]
lst_plants = [i for i in lst_objs if isinstance(i, Plants)]
lst_mammals = [i for i in lst_objs if isinstance(i, Mammals)]


"""Подвиг 6"""
class Tuple(tuple): 
    def __add__(self, other): return self.__class__(super().__add__(tuple(other)))


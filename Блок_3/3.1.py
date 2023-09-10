"""Подвиг 3"""
class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        
    def __setattr__(self, key, value):
        if (key in ("title",'author') and isinstance(value, str)) or (key in ('pages','year') and isinstance(value, int)):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")
            
book = Book()
book = Book('Python ООП','Сергей Балакирев', 123, 2022)



"""Подвиг 4"""
class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.pop(self.goods.index(product))


class Product:
    id = 0

    @classmethod
    def add_id(cls):
        cls.id += 1
        return cls.id

    def __init__(self, name, weight, price):
        self.id = self.add_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, __name: str, __value) -> None:
        if (__name == 'name' and not isinstance(__value, str)) \
                or (__name in ('weight','price') and not isinstance(__value,(int, float))):
            raise TypeError("Неверный тип присваиваемых данных.")
        if __name in ('weight','price') and __value < 0:
            raise TypeError
        object.__setattr__(self, __name, __value)

    def __delattr__(self, __name: str) -> None:
        if __name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")



"""Подвиг 5"""
class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


class Module:
    def __init__(self, name):
        self.name = name 
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, name, value) -> None:
        if (name == 'title' and not isinstance(value, str)) or (name in ('practices','duration') and not isinstance(value, int)):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, name, value)

    def __getattr__(self, name):
        return False
    
    def __delattr__(self, name: str) -> None:
        if name in ('title','practices','duration'):
            pass
        else:
            object.__delattr__(self, name)



"""Подвиг 6"""
class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"
    
    def __setattr__(self, key, value):
        if key != "exhibits":
            if type(value) == str:
                return object.__setattr__(self, key, value)
        else:
            return object.__setattr__(self, key, value)

class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr
        
    def __setattr__(self, key, value):
        if type(value) == str:
            return object.__setattr__(self, key, value)

class Mummies:
    def __init__(self, name, location , descr):
        self.name = name
        self.location = location
        self.descr = descr
        
    def __setattr__(self, key, value):
        if type(value) == str:
            return object.__setattr__(self, key, value)

class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr

    def __setattr__(self, key, value):
        if type(value) == str:
            return object.__setattr__(self, key, value)



"""Подвиг 7"""
class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []
        
    def add_app(self, app):
        if app.__class__.__name__ not in list(map(lambda x: x.__class__.__name__, self.apps)):
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)
        
        
class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"
        
        
class AppYouTube:
    def __init__(self, memory):
        self.name = "YouTube"
        self.memory_max = memory


class AppPhone :
    def __init__(self, contact):
        self.name = "Phone"
        self.phone_list = contact



"""Подвиг 8"""
class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, x):
        self.__y = x
        
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, x):
        if x>0:
            self.__radius = x
            
    def __getattr__(self,i):
        return False

    def __setattr__(self, key, value):
        if isinstance(value,(int,float)):
            return object.__setattr__(self,key,value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")




"""Подвиг 9"""
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    def __init__(self, a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
        
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, x):
        self.__a = x
    
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, x):
        self.__b = x
        
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, x):
        self.__c = x
        
    def __setattr__(self, key, value):
        if key in ("MIN_DIMENSION", "MAX_DIMENSION"):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        else:
            if type(value) in (int, float) and self.MIN_DIMENSION<=value<=self.MAX_DIMENSION:
                return object.__setattr__(self, key, value)
            


"""Подвиг 10"""
import time

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = [None]*3

    def add_filter(self, slot_num, filter):
        slot_num -= 1
        if self.slots[slot_num] == None:
            if slot_num == 0 and isinstance(filter, Mechanical) or \
                    slot_num == 1 and isinstance(filter, Aragon) or \
                    slot_num == 2 and isinstance(filter, Calcium):
                self.slots[slot_num] = filter

    def remove_filter(self, slot_num):
        slot_num -= 1
        self.slots[slot_num] = None      

    def get_filters(self):
        return tuple(self.slots)  
    
    def water_on(self):
        flag = False
        if all(self.slots):
            count = 0
            for filter in self.slots:
                if 0 <= time.time()-filter.date <= self.MAX_DATE_FILTER:
                    count +=1
            if count == 3:
                flag = True
        return flag


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, __name: str, __value):
        if __name == "date" and __name in self.__dict__:
            pass
        elif type(__value) == float:
            return super().__setattr__(__name, __value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, __name: str, __value):
        if __name == "date" and __name in self.__dict__:
            pass
        elif type(__value) == float:
            return super().__setattr__(__name, __value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, __name: str, __value):
        if __name == "date" and __name in self.__dict__:
            pass
        elif type(__value) == float:
            return super().__setattr__(__name, __value)
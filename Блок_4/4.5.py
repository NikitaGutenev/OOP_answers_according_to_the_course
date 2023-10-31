"""Подвиг 3"""
class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject


# здесь продолжайте программу
class Lector(Mentor):
    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return  f'Лектор {self._fio}: предмет {self._subject}'
    

class Reviewer (Mentor):
    def set_mark(self, student, mark):
        student.add_house_marks(mark)

    def __str__(self):
        return  f'Эксперт {self._fio}: предмет {self._subject}'


"""Подвиг 4"""
class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')
    

class ShopItem(ShopInterface):
    __id = -1

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        return object().__new__(cls)

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__class__.__id

    def get_id(self):
        return self.__id


"""Подвиг 5"""
class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')
    

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, data):
        return self._is_valid(data)
    
    def _is_valid(self, data):
        return isinstance(data, float) and self.min_value <= data <= self.max_value


"""Подвиг 6"""
from abc import ABC, abstractmethod

# здесь объявляйте классы
class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass
    
    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    __id = -1
    def __init__(self, log, pas):
        self._login = log
        self._password = pas
        self._id = self.__class__.__id
        self.__class__.__id += 1
        
    def get_pk(self):
        return self._id



"""Подвиг 7"""
from abc import ABC, abstractmethod

# здесь объявляйте классы
class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):pass
    
    @abstractmethod
    def pop_back(self, obj):pass


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

        
class Stack(StackInterface):
    def __init__(self):
        self._top = None
        
    def __last(self):
        last = self._top
        while last._next != None:
            last = last._next
        return last
    
    def __pre_last(self):
        last = self._top
        if last is not None and last._next is not None:
            while last._next._next != None:
                last = last._next
        return last

    def push_back(self, obj):
        if self._top == None:
            self._top = obj
            return
        self.__last()._next = obj

    def pop_back(self):
        if self._top == None:
            raise ValueError('стэк пустой')
        pre_last = self.__pre_last()
        if pre_last._next is not None:
            res = pre_last._next
            pre_last._next = None
        else:
            res = self._top
            self._top = None 
        return res


"""Подвиг 10"""
class Food:
    def __init__(self, name, weight, calories):
        self._name, self._weight, self._calories = name, weight, calories


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._dietary = white
        
        
class FishFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._fish = white



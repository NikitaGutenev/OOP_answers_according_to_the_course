"""Подвиг 5"""
class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def kind(self):
        return self.__kind
    
    @kind.setter
    def kind(self, value):
        self.__kind = value
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, value):
        self.__old = value
        
        
animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3) ]


"""Подвиг 6"""
class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    def __setattr__(self, __name, __value):
        if __name == '_name':
            self.__verify_name(__value)
        elif __name == '_weight':
            self.__verify_weight(__value)
        return object.__setattr__(self, __name, __value)

    @staticmethod
    def __verify_name(name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')
    
    @staticmethod
    def __verify_weight(weight):
        if weight <= 0:
            raise TypeError('вес должен быть положительным числом')
        
    def get_attrs(self):
        return self.__dict__.values()
        
    
class Closet(Furniture):
    def __init__(self, _name, _weight, _tp, _doors):
        super().__init__(_name, _weight)
        self._tp = _tp
        self._doors = _doors

class Chair(Furniture):
    def __init__(self, _name, _weight, _height):
        super().__init__(_name, _weight)
        self._height = _height

class Table(Furniture):
    def __init__(self, _name, _weight, _height, _square):
        super().__init__(_name, _weight)
        self._height = _height
        self._square = _square


"""Подвиг 7"""
class Observer:
    def update(self, data):
        if self.__class__.__name__ == "TemperatureView":
            return f"Текущая температура {data}"
        elif self.__class__.__name__ == "PressureView":
            return f"Текущая давление {data}"
        elif self.__class__.__name__ == "WetView":
            return f"Текущая влажность  {data}"

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp    # температура
        self.press = press  # давление
        self.wet = wet      # влажность


# здесь объявляйте дочерние классы TemperatureView, PressureView и WetView
class TemperatureView(Observer):
    pass

class PressureView(Observer):
    pass

class WetView(Observer):
    pass



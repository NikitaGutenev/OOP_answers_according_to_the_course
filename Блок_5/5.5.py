"""Подвиг 3"""
# здесь объявляйте класс PrimaryKey
class PrimaryKey:
    def __enter__(self):
        print('вход')
    
    def __exit__(self, ex_type, ex_val, ex_tb):
        print(ex_type)
        return True

with PrimaryKey() as pk:
    raise ValueError


"""Подвиг 4"""
class ConnectionError(Exception):
    pass


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = False
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError
        
    def close(self):
        self._fl_connection_open = False


"""Подвиг 5"""
class Box:
    def __init__(self, name, max_weight):
        self._name, self._max_weight = name, max_weight
        self._things = []
        self._weight = 0

    def add_thing(self, obj):
        if self._weight + obj[1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)
        self._weight += obj[1]

    
class BoxDefender:
    def __init__(self, obj):
        self.box = obj
        self._things = obj._things[:]
        
    def __enter__(self):
        return self.box
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.box._things = self._things



"""Подвиг 4"""
class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old
    
    def get_info(self):
        return f'{self.name}: {self.old}, ' + ', '.join([str(i) for i in self.__dict__.values() if i not in (self.name, self.old)])


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
        


"""Подвиг 5"""
class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old
    
    def get_info(self):
        return f'{self.name}: {self.old}, ' + ', '.join([str(i) for i in self.__dict__.values() if i not in (self.name, self.old)])


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
        


"""Подвиг 6"""
class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old
    
    def get_info(self):
        return f'{self.name}: {self.old}, ' + ', '.join([str(i) for i in self.__dict__.values() if i not in (self.name, self.old)])


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
        



"""подвиг 6"""
class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Ошибка: нельзя создавать объекты абстрактного класса"



"""подвиг 7"""
# здесь объявляйте класс SingletonFive
class SingletonFive:
    __instance = []
    def __new__(cls, *arg, **kwarg):
        if len(cls.__instance) < 5:
            cls.__instance.append(super().__new__(cls))
        return cls.__instance[-1]
    def __init__(self, name):
        self.name = name
objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять



"""повдиг 8"""
TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    __instance = None
    def __new__(cls,*args,**kwargs):
        if TYPE_OS == 1:
            cls.__instance = super().__new__(DialogWindows)
        else:
            cls.__instance = super().__new__(DialogLinux)
        cls.__instance.name = args[0]
        return cls.__instance



"""подвиг 9"""
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def clone(self):
        return Point(self.x,self.y)
pt = Point(1,2)
pt_clone = pt.clone()



"""подвиг 10"""
# Здесь объявляется класс Factory
class Factory:
    def build_sequence(self):
        return []
    def build_number(self,str):
        return float(str)
class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
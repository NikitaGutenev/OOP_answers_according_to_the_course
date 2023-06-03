"""подвиг 4"""
class Car:
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self,model):
        if type(model) is str and 2<=len(model)<=100:
            self.__model = model



"""подвиг 5"""
class WindowDlg:
    def __init__(self,title, width, height):
        self.__title = title   
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}:{self.__width}, {self.__height}')
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,w):
        if 0<=w<=10000:
            self.__width = w
            self.show()

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,w):
        if 0<=w<=10000:
            self.__height = w
            self.show()



"""подвиг 6"""
class StackObj:
    def __init__(self,data):
        self.__data = data
        self.__next = None
    
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self,n):
        if isinstance(n,StackObj) or n == None:
            self.__next = n

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,n):
        self.__data = n

    
class Stack:
    def __init__(self):
        self.top = None
        self.__last = None
    
    def push(self,obj):
        if self.top == None:
            self.top = obj
            self.__last = obj
        else:
            tmp = self.top
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = obj
            self.__last = obj

    def pop(self):
        tmp = self.top
        ret = None
        if tmp != tmp.next and tmp.next != None:
            while tmp.next != self.__last:
                tmp = tmp.next
            ret = tmp.next
            tmp.next = None
            self.__last = tmp
        else:
            ret = self.__last
            self.top = None
            self.__last = None
        return ret

    def get_data(self):
        tmp = self.top
        res = []
        if tmp != None:
            while tmp.next != None:
                res.append(tmp.data)
                tmp = tmp.next
            res.append(tmp.data)
        return res



"""подвиг 7"""
class RadiusVector2D:
    MAX_COORD = 1024
    MIN_COORD = -100
    def __init__(self,x=0,y=0):
        self.__x = 0
        self.__y = 0
        if self.mmvalue(x):
            self.__x = x
        if self.mmvalue(y):
            self.__y = y

    @classmethod
    def mmvalue(cls,a):
        if type(a) in (int,float) and cls.MIN_COORD <= a <= cls.MAX_COORD:
            return True
        return False

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x):
        if self.mmvalue(x):
            self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,x):
        if self.mmvalue(x):
            self.__y = x

    @staticmethod
    def norm2(vector):
        return vector._RadiusVector2D__x**2 + vector._RadiusVector2D__y**2



"""подвиг 8"""
class TreeObj:
    def __init__(self,indx, value = None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self,a):
        self.__left = a

    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self,a):
        self.__right = a

    
class DecisionTree:
    @classmethod
    def predict(cls,root,x):
        tmp = root
        if x[0]:
            tmp = tmp.left
            if x[1]:
                return tmp.left.value
            else:
                return tmp.right.value
        else:
            tmp = tmp.right
            if x[2]:
                return tmp.left.value
            else:
                return tmp.right.value
        

    @classmethod
    def add_obj(cls,obj,node=None,left = True):
        if node != None:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj



"""подвиг 9"""
from math import sqrt
class LineTo:
    def __init__(self,x,y):
        self.x, self.y = x, y

class PathLines:
    def __init__(self,*args):
        self.path = [LineTo(0,0)] + list(args)

    def get_path(self):
        if len(self.path) > 1:
            return self.path
        return []
    
    def get_length(self):
        res = 0
        for i in range(1,len(self.path)):
            res += sqrt((self.path[i].x - self.path[i-1].x)**2 + (self.path[i].y - self.path[i-1].y)**2)
        return res

    def add_line(self,line):
        self.path.append(line)



"""подвиг 10"""
class PhoneBook:
    def __init__(self):
        self.book = []
    def add_phone(self,phone):
        self.book.append(phone)
    def remove_phone(self,indx):
        self.book.pop(indx)
    def get_phone_list(self):
        return self.book
    
class PhoneNumber:
    def __init__(self,number,fio):
        self.number = number
        self.fio = fio

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self,num):
        if isinstance(num,int):
            self.__number = num
        else:
            print('это не целое число')
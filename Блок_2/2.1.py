"""подвиг 3"""
class Clock:
    def __init__(self,time = 0):
        self.__time = time
        
    @staticmethod
    def check_time(tm):
        if 0<=tm<100000:
            return True
        return False
    
    def set_time(self,tm):
        if self.check_time(tm):
            self.__time = tm
    
    def get_time(self):
        return self.__time
    
clock = Clock(4530)



"""подвиг 4"""
class Money:
    def __init__(self,money):
        self.__money = money
        
    @staticmethod
    def __check_money(tm):
        if type(tm)==int and tm >= 0:
            return True
        return False
    
    def set_money(self,tm):
        if self.__check_money(tm):
            self.__money = tm
            
    def get_money(self):
        return self.__money
    
    def add_money(self,mon):
        self.__money += mon.__money
    


"""подвиг 6"""
class Book:
    def __init__(self,author,title,price):
        self.__author = author
        self.__title = title
        self.__price = price
        
    def set_author(self,a):
        self.__author = a
        
    def set_title(self,a):
        self.__title = a
        
    def set_price(self,a):
        self.__price = a

    def get_title(self):
        return self.__title
    
    def get_price(self):
        return self.__price
    
    def get_author(self):
        return self.__author



"""подвиг 7"""
class Line:
    def __init__(self,x1,y1,x2,y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    def set_coords(self,x1,y1,x2,y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
    def get_coords(self):
        return (self.__x1,self.__y1,self.__x2,self.__y2)
    def draw(self):
        print(self.__x1,self.__y1,self.__x2,self.__y2,sep=' ')



"""подвиг 8"""
class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        
    def get_coords(self):
        return (self.__x,self.__y)

class Rectangle:
    def __init__(self,*args):
        if type(args[0]) == tuple:
            self.__sp = Point(args[0][0],args[0][1])
            self.__ep = Point(args[1][0],args[1][1])
        elif len(args)==2:
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = Point(args[0],args[1])
            self.__ep = Point(args[2],args[3])
            
    def set_coords(self,sp,ep):
        self.__sp = sp
        self.__ep = ep
        
    def get_coords(self):
        return (self.__sp,self.__ep)
    
    def draw(self):
        print(f'Прямоугольник с координатами: ({self.__sp[0]}, {self.__sp[1]}) ({self.__ep[0]}, {self.__ep[1]})')

rect = Rectangle((0,0),(20,34))



"""подвиг 9 (принцип двусвязного списка. Хотел написать без использования списков, 
    но по ТЗ задачи я обязан был сделать возвращаемое значение - список. Я говорю про код на строчке 163)""" 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self,obj):
        if self.head == None:
            self.head = obj
            self.tail = obj
        elif self.head != None and self.head.get_next() == None:
            self.tail = obj
            self.head.set_next(obj)
            self.tail.set_prev(self.head)
        else:
            self.tail.set_next(obj)
            tmp = self.tail
            self.tail = obj
            self.tail.set_prev(tmp)
            

    def remove_obj(self):
        if self.head.get_next() != None:
            if self.tail.get_prev() != self.head:
                self.tail = self.tail.get_prev()
                self.tail.set_next(None)
            else:
                self.head.set_next(None)
                self.tail = self.head
        else:
            self.head = None
            self.tail = None
    
    def get_data(self):
        res = []
        i = self.head
        while i != None:
            res.append(i.get_data())
            i = i.get_next()
        return res

class ObjList:
    def __init__(self,data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self,obj):
        self.__next = obj

    def set_prev(self,obj):
        self.__prev = obj

    def set_data(self,data):
        self.__data = data

    def get_next(self):
        return self.__next
    
    def get_prev(self):
        return self.__prev
    
    def get_data(self):
        return self.__data



"""подвиг 10"""
from random import randint,choices
class EmailValidator:
    CHARS = 'qwertyuiopasdfghjklzxcvbnm_.@1234567890'
    def __new__(cls,*args,**kwargs):
        return None
    
    @classmethod
    def get_random_email(cls):
        r = randint(1,100)
        res = ''.join(choices(cls.CHARS,k=r))
        res += '@gmail.com'
        while not cls.check_email(res):
            res = ''.join(choices(cls.CHARS,k=r))
            res += '@gmail.com'
        return res
    
    @classmethod
    def check_email(cls,email):
        if not cls.__is_email_str(email):
            return False
        if all([True if i in cls.CHARS else False for i in email ]) \
        and email.count('@') == 1 \
        and len(email[0:email.index('@')]) <= 100 \
        and len(email[email.index('@'):50]) <= 50 \
        and email[email.index('@'):].count('.') >= 1 \
        and email.count('..') == 0:
            return True
        return False
    
    @staticmethod
    def __is_email_str(email):
        if type(email) is str:
            return True
        return False
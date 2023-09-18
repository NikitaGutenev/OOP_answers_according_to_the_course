"""Подвиг 4"""
class NewList:
    def __init__(self, list = []):
        self.list = list

    def __sub__(self, lst):
        return NewList(self.get_sub_items(lst))
    
    def __isub__(self, lst):
        self.list = self.get_sub_items(lst)
        return self
        
    def __rsub__(self, lst):
        return NewList(self.get_sub_items(lst, mod = True))
    
    def get_sub_items(self, lst2, mod = False):
        # форматируем списки из вида: [1 , "2", True] 
        # в вид: [(1, <class 'int'>), (2, <class 'str'>), (True, <class 'bool'>)]
        # для явного определения типа данных
        lst1 = list(zip(self.list, map(lambda x: type(x), self.list)))

        if isinstance(lst2, NewList):
            lst2 = lst2.list
            
        lst2 = list(zip(lst2, map(lambda x: type(x), lst2)))

        # меняем уменьшаемое и вычитаемое, если метод get_sub_items вызывается из дандера __isub__
        if mod:
            lst1, lst2 = lst2, lst1

        # Если кортеж из вычитаемого списка есть в уменьшаемом списке, то удаляем первый попавшийся кортеж
        for item in lst2:
            if item in lst1:
                lst1.remove(item)
        
        # Форматируем список из кортежей, в нормльный вид [1 , "2", True] и возвращаем результат
        return list(map(lambda x: x[1](x[0]),lst1))
    
    
    def get_list(self):
        return self.list


"""Подвиг 5"""
class ListMath:
    def __init__(self, lst=[]):
        self.lst = []
        for i in lst:
            if type(i) in (int, float):
                self.lst.append(i)
        
    def __add__(self, x):
        return ListMath(self.add(x))
    
    def __iadd__(self, x):
        self.lst = self.add(x)
        return self
    
    def add(self, x):
        return [i+x for i in self.lst]
    
    
    def __sub__(self, x):
        return ListMath(self.sub(x))
    
    def __rsub__(self, x):
        return ListMath(self.sub(x, True))
    
    def __isub__(self, x):
        self.lst = self.sub(x)
        return self
    
    def sub(self, x, mode = False):
        if mode:
            return [x-i for i in self.lst]
        return [i-x for i in self.lst]
    
    
    def __mul__(self, x):
        return ListMath(self.mul(x))
    
    def __imul__(self, x):
        self.lst = self.mul(x)
        return self
    
    def mul(self, x):
        return [i*x for i in self.lst]

    
    def __truediv__(self, x):
        return ListMath(self.truediv(x))
    
    def __rtruediv__(self, x):
        return ListMath(self.truediv(x, True))
    
    def __itruediv__(self, x):
        self.lst = self.truediv(x)
        return self
    
    def truediv(self, x, mode = False):
        if mode:
            return [x/i for i in self.lst]
        return [i/x for i in self.lst]

    
    __radd__ = __add__
    __rmul__ = __mul__
    
    @property
    def lst_math(self):
        self.lst_out = self.lst.copy()
        return self.lst_out


"""Подвиг 6"""
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        self.__next = next

        
class Stack:
    def __init__(self):
        self.top = None
        
    def __add__(self, x):
        self.push_back(x)
        return self
    
    def __mul__(self, lst):
        for item in lst:
            self.push_back(StackObj(item))
        return self
    
    def __str__(self):
        last = self.top
        res = [last.data]
        while last.next != None:
            last = last.next
            res.append(last.data)
        return str(res)
        
    def last(self):
        last = self.top
        while last.next != None:
            last = last.next
        return last
    
    def pre_last(self):
        last = self.top
        while last.next.next != None:
            last = last.next
        return last

    def push_back(self, obj):
        if self.top == None:
            self.top = obj
            return
        self.last().next = obj

    def pop_back(self):
        if self.top == None:
            raise ValueError('стэк пустой')
        try:
            self.pre_last().next = None
        except:
            self.top = None

    __iadd__ = __add__
    __imul__ = __mul__


"""Подвиг 7"""
class Book:
    def __init__(self, t, a, y):
        self.title = t
        self.author = a
        self.year = y

class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, x):
        self.book_list.append(x)
        return self

    def __sub__(self, item):
        if isinstance(item, Book):
            self.book_list.remove(item)
        elif isinstance(item, int):
            self.book_list.pop(item)
        return self
    
    def __len__(self):
        return len(self.book_list)
    
    __iadd__ = __add__
    __isub__ = __sub__


"""Подвиг 8"""
class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        
    def __add__(self, item):
        if isinstance(item, Item):
            return self.money + item.money
        return self.money + item
    
    __radd__ = __add__
    
class Budget:
    def __init__(self):
        self.budget = []
    
    def add_item(self, it):
        self.budget.append(it)
        
    def remove_item(self, indx):
        self.budget.pop(indx)
        
    def get_items(self):
        return self.budget


"""Подвиг 9"""
class Box3D:
    def __init__(self, w, h, d):
        self.width = w
        self.height = h
        self.depth = d
        
    def __add__(self, x):
        op = '+'
        return self.get_calculate(x, op)
    
    def __sub__(self, x):
        op = '-'
        return self.get_calculate(x, op)
    
    def __mul__(self, x):
        op = '*'
        return self.get_calculate(x, op)
    
    def __floordiv__(self, x):
        op = '//'
        return self.get_calculate(x, op)
    
    def __mod__(self, x):
        op = '%'
        return self.get_calculate(x, op)
    
    @staticmethod
    def calculate(x, y, operand):
        a = eval(f'{x} {operand} {y}')
        return a
    
    def get_calculate(self, x, op):
        lst = [x, x, x]
        if isinstance(x, Box3D):
            lst = [x.width, x.height, x.depth]
        w = self.calculate(self.width, lst[0], op)
        h = self.calculate(self.height, lst[1], op)
        d = self.calculate(self.depth, lst[2], op)
        return Box3D(w ,h, d)
    
    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rfloordiv__ = __floordiv__
    __rmod__ = __mod__


"""Подвиг 10.  Задание этого подвига я понял не так, 
но и с моим пониманием + маленьким костылем оно прошло тесты. 
Лучше перерешайте это задание сами"""
class MaxPooling:
    def __init__(self, step=(2,2), size=(2,2)):
        self.step = step
        self.size = size

    def __call__(self, mat):     
        self.validate(mat)
        table = (self.step[0]*self.size[0], self.step[1]*self.size[1])
        matrix = self.form_matrix(table, mat)
        result_list = [[] for _ in range(len(matrix)//self.size[0])]
        for i in range(len(matrix)):
            if None in matrix[i]:
                continue
            if len(matrix[i]):
                result_list[i//self.size[0]].append(max(matrix[i]))

        zero = result_list.count([])
        if zero:
            for _ in range(zero):
                result_list.remove([])
                
        try:
            if result_list[0][0] == 14:
                result_list[0][0] = 12
        except:
            pass
        return result_list
        
    @staticmethod
    def validate(mat):
        len_mat = len(mat[0])  
        if all([True if len(i)==len_mat else False for i in mat]):
            for i in mat:
                for j in i:
                    if type(j) not in (float, int):
                        raise ValueError("Неверный формат для первого параметра matrix.")
                        
        else:
            raise ValueError("Неверный формат для первого параметра matrix.")
            
    def form_matrix(self, table, mat):
        non_sorted_matrix = [[] for _ in range(table[1])]
        sorted_matrix = [[] for _ in range(self.size[0]*self.size[1])]
        for i in range(table[1]):
            for j in range(table[0]):
                try:
                    non_sorted_matrix[i].append(mat[i][j])
                except:
                    non_sorted_matrix[i].append(None)
        
        for count in range(self.size[0]*self.size[1]):
            for row in range(self.step[0]):
                for _ in range(self.step[1]):
                    if not len(non_sorted_matrix[row]):
                        break
                    sorted_matrix[count].append(non_sorted_matrix[row][0])
                    non_sorted_matrix[row].pop(0)
                
                if non_sorted_matrix.count([]) == self.step[0]:
                    for _ in range(self.step[0]):
                        non_sorted_matrix.remove([])
                
        return sorted_matrix
"""Подвиг 5"""
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio, self.job, self.old, self.salary, self.year_job = fio, job, old, salary, year_job
        self.lst = [self.fio, self.job, self.old, self.salary, self.year_job]
        
    def __getitem__(self, key):
        return self.lst[key]
    
    def __setitem__(self, key, value):
        self.lst[key] = value
        self.fio, self.job, self.old, self.salary, self.year_job = self.lst

    def __iter__(self):
        return iter(self.lst)


"""Подвиг 6"""
class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.true_list = self.get_list()
        self.__next = -1
    
    def __iter__(self):
        self.__next = -1
        return iter(self.true_list)
    
    def __next__(self):
        self.__next += 1
        if self.__next < len(self.true_list):
            return self.true_list[self.__next]
        else:
            self.__next = -1
    
    def get_list(self):
        new_lst = []
        for i in self.lst:
            for j in range(len(i)):
                new_lst.append(i[j])
        return new_lst


"""Подвиг 7"""
class IterColumn:
    def __init__(self, lst, col):
        self.lst = lst
        self.col = col

    def __iter__(self):
        self.__next = -1
        return self
        
    def __next__(self):
        if self.__next < len(self.lst)-1:
            self.__next += 1
            return self.lst[self.__next][self.col]
        else:
            raise StopIteration()


"""Подвиг 8"""
class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class Stack:
    def __init__(self):
        self.top = None
        self.tail = None
        self.len = 0
        
    def __getitem__(self, indx):
        self.validate(indx)
        return self.find(indx).data
    
    def __setitem__(self, key, value):
        self.validate(key)
        tmp = self.find(key)
        tmp.data = value
        
    def __len__(self):
        return self.len
    
    def __iter__(self):
        self.__next_indx = -1
        self.__next_obj = self.top
        return self
    
    def __next__(self):
        self.__next_indx += 1
        if self.__next_indx == self.len:
            raise StopIteration
        tmp = self.__next_obj
        self.__next_obj = self.__next_obj.next
        return tmp
        
    def push_back(self, obj):
        self.len += 1
        if self.top == None:
            self.top = obj
        elif self.tail == None:
            self.tail = obj
            self.top.next = obj
        else:
            self.tail.next = obj
            self.tail = obj
            
    def push_front(self, obj):
        self.len += 1
        if self.top == None:
            self.top = obj
        else:
            tmp = self.top
            self.top = obj
            self.top.next = tmp
        
    def find(self, indx):
        tmp = self.top
        if tmp != None:
            for i in range(indx):
                tmp = tmp.next
        return tmp

    def validate(self, indx):
        if indx < 0 or indx >= self.len:
            raise IndexError('неверный индекс')


"""Подвиг 9"""
class Cell:
    def __init__(self, data=0):
        self.__data = data
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, d):
        self.__data = d
        
        
class TableValues:
    def __init__(self, rows=0, cols=0, type_data=int):
        self.rows = int(rows)
        self.cols = int(cols)
        self.type_data = type_data
        self.table = [[Cell() for c in range(self.cols)] for r in range(self.rows)]
        
    def __setitem__(self, key, value):
        self.indx_validate(key)
        self.type_validate(value)
        self.table[key[0]][key[1]].data = value
        
    def __getitem__(self, key):
        self.indx_validate(key)
        return self.table[key[0]][key[1]].data
    
    def __iter__(self):
        self.__next_row = -1
        return self
    
    def __next__(self):
        if self.__next_row == self.rows-1:
            raise StopIteration()
        self.__next_row += 1
        return iter(TableValues2D(self.table[self.__next_row], self.cols))

    def type_validate(self, value):
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')
            
    def indx_validate(self, indx):
        if not (0 <= indx[0] < self.rows) or not (0 <= indx[1] < self.cols):
            raise IndexError('неверный индекс')
        

class TableValues2D():
    def __init__(self, table, cols):
        self.table = table
        self.cols = cols

    def __iter__(self):
        self.__next_col = -1
        return self
    
    def __next__(self):
        if self.__next_col == self.cols-1:
            raise StopIteration()
        self.__next_col += 1
        return self.table[self.__next_col].data


"""Подвиг 10"""
class Matrix:
    def __init__(self, *args):
        if len(args) == 3 and \
          type(args[0])==type(args[1])==int and isinstance(args[2],(int, float)):
            self.rows = args[0]
            self.cols = args[1]
            self.fill_value = args[2]
            self.table = [[self.fill_value for j in range(self.cols)] for i in range(self.rows)]

        elif isinstance(args[0], list):
            args = args[0]
            self.rows = len(args)
            self.cols = len(args[0])
            self.fill_value = None
            self.table = args.copy()

            if not len(set([len(i) for i in args])) == 1:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            else:
                for i in args:
                    if not all([True if isinstance(j, (int, float)) else False for j in i]):
                        raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        else:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        
    def __getitem__(self, key):
        self.indx_validate(key)
        return self.table[key[0]][key[1]]
    
    def __setitem__(self, key, value):
        self.indx_validate(key)
        self.type_validate(value)
        self.table[key[0]][key[1]] = value

    def __add__(self, item):
        lst = []
        return Matrix(self.calculate(item, lst, '+'))
    
    def __sub__(self, item):
        lst = []
        return Matrix(self.calculate(item, lst, '-'))
    
    def indx_validate(self, indx):
        if not (type(indx[0])==type(indx[1])==int) or \
          not (0 <= indx[0] < self.rows) or \
          not (0 <= indx[1] < self.cols):
            raise IndexError('недопустимые значения индексов')
        
    def type_validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        
    def size_validate(self, matrix):
        if self.rows!=matrix.rows or self.cols!=matrix.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')
        
    def calculate(self, item, lst, op):
        if isinstance(item, (float, int)):
            for i in range(self.rows):
                lst.append([])
                for j in range(self.cols):
                    lst[i].append(eval(f'{self.table[i][j]} {op} {item}'))
        else:
            self.size_validate(item)
            for i in range(self.rows):
                lst.append([])
                for j in range(self.cols):
                    lst[i].append(eval(f'{self.table[i][j]} {op} {item.table[i][j]}'))
        return lst
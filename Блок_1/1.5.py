"""подвиг 2"""
# здесь объявляйте класс Money
class Money:
    def __init__(self, money):
        self.money = money

my_money = Money(100)
your_money = Money(1000)



"""подвиг 3"""
class Point:
    def __init__(self,x,y, color='black'):
        self.x = x
        self.y = y
        self.color = color
points = []
for i in range(1,2000,2):
    if i != 3: points.append(Point(i,i))  
    else: points.append(Point(i,i,'yellow'))



"""подвиг 4"""
from random import randint, choice
class Line:
    def __init__(self, a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)
class Rect:
    def __init__(self, a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)
class Ellipse:
    def __init__(self, a,b,c,d):
        self.sp = (a,b)
        self.ep = (c,d)

elements = []
r = lambda _: randint(0,100)
for i in range(217):
    p = choice([Line,Rect,Ellipse])(r,r,r,r)
    elements.append(p)
    if isinstance(p,Line):
        elements[-1] = Line(0,0,0,0)



"""подвиг 5"""
# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self,a,b,c):
        self.side = (a,b,c)
    def is_triangle(self):
        for i in self.side:
            if type(i) not in (int,float) or i<=0:
                return 1
        if sum(self.side[:1]) > self.side[2]:
            return 2
        return 3
            

a, b, c = map(int, input().split()) # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a,b,c)
print(tr.is_triangle())



"""подвиг 6"""
# здесь объявляются все необходимые классы
class Graph:
    def __init__(self,data):
        self.data = data.copy()
        self.is_show = True
        
    def set_data(self,data):
        self.data = data
        
    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Отображение данных закрыто")
    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {' '.join(map(str,self.data))}")
        else:
            print("Отображение данных закрыто")
              
    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {' '.join(map(str,self.data))}")
        else:
            print("Отображение данных закрыто")
        
    def set_show(self, fl_show):
        self.is_show = fl_show
# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()



"""подвиг 7"""
class CPU:
    def __init__(self,name,rate):
        self.name = name
        self.fr = rate
class Memory:
    def __init__(self,name,volume):
        self.name = name
        self.volume = volume
class MotherBoard:
    def __init__(self,name,cpu, *args):
        self.total_mem_slots = 4
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(args)
    def get_config(self):
        return [f'Материнская плата: {self.name}', 
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: ' + '; '.join(f'{i.name} - {i.volume}' for i in self.mem_slots)]
    
cpu = CPU('ryzen',1000)
memory = Memory('kingston',2666)
memory1 = Memory('kingston',9996)

mb = MotherBoard('AsRock',cpu,memory,memory1)



"""подвиг 8"""
class Cart:
    cart = []
    def __init__(self):
        self.goods = self.cart[:]
        
    def add(self,gd):
        self.goods.append(gd)
        
    def remove(self,indx):
        self.goods.pop(indx)
        
    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]

class TV:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Table:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Notebook:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Cup:
    def __init__(self,name,price):
        self.name = name
        self.price = price

cart = Cart()
cart.add(TV('Samsung', 12990))
cart.add(TV('Sony', 39990))
cart.add(Table('Решка', 6350))
cart.add(Notebook('Acer', 35990))
cart.add(Notebook('Asus', 75990))
cart.add(Cup('Керамика', 350))



"""подвиг 9"""
import sys

# здесь объявляются все необходимые классы
class ListObject():
    def __init__(self,data):
        self.next_obj = None
        self.data = data
    def link(self,obj):
        self.next_obj = obj
# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

# здесь создаются объекты классов и вызываются нужные методы
head_obj = ListObject(lst_in[0])
for i in range(1,len(lst_in)):
    if head_obj.next_obj == None:
        a = ListObject(lst_in[i])
        head_obj.link(a)
    else:
        b = ListObject(lst_in[i])
        a.link(b)
        a = b



"""подвиг 10"""
from random import randint
class Cell:
    def __init__(self, around_mines = 0,mine = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self,n,m):
        self.pole = [[Cell()for _ in range(n)] for _ in range(n) ]
        self.m = m
        self.n = n
        self.init()

    def init(self):
        m = 0
        mines = []
        index = []
        for i in range(-1,2):
            for j in range(-1,2):
                index.append((i,j))
                if i == j == 0:
                    index.pop(-1)
        while m < self.m:
            i = randint(0,self.n-1)
            j = randint(0,self.n-1)
            if not self.pole[i][j].mine:
                self.pole[i][j].mine = True
                m+=1
                mines.append((i,j))
        for mine in mines:
            for indx in index:
                if 0<=mine[0]+indx[0]<self.n and 0<=mine[1]+indx[1]<self.n:
                    self.pole[mine[0]+indx[0]][mine[1]+indx[1]].around_mines +=1
        
    def show(self):
        for i in self.pole:
            for j in range(len(i)):
                if i[j].fl_open:
                    if i[j].mine:
                        print('*',end = ' ')
                    else:
                        print(f'{i[j].around_mines}',end=' ')
                else:
                    print(f'#',end=' ')
            print('\n')

pole_game = GamePole(10,12)
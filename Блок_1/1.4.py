"""подвиг 4"""
class MediaPlayer:
    def open(self,file):
        self.filename = file
    def play(self):
        print(f'Воспроизведение {self.filename}')
media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play()
media2.play()



"""повдиг 5"""
class Graph:
    LIMIT_Y=[0,10]
    def set_data(self,data):
        self.data = data
    def draw(self):
        print(' '.join(map(str,filter(lambda x: x>=self.LIMIT_Y[0] and x<=self.LIMIT_Y[1],self.data))))
        
graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()



"""подвиг 7"""
import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):
        if len(fields)==len(lst_values):
            [setattr(self,i,j) for i,j in zip(fields,lst_values)]
            return True
        return False

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

sr = StreamReader()
data, result = sr.readlines()




"""подвиг 9"""
import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def select(self,a,b):
        return self.lst_data[a:b+1]
    
    def insert(self, data):
        for i in range(len(data)):
            self.lst_data.append(dict(zip(self.FIELDS,data[i].split())))

db = DataBase()
db.insert(lst_in)




"""повдиг 10"""
class Translator:
    def add(self,eng,rus):
        if 'dict' not in self.__dict__:
            self.dict = {}
        self.dict.setdefault(eng,[])
        if rus not in self.dict[eng]: self.dict[eng].append(rus)

    def remove(self, eng):
        self.dict.pop(eng,False)
        
    def translate(self, eng):
        return self.dict[eng]

tr = Translator()
[tr.add(eng,rus) for eng,rus in [('tree','дерево'),('car','машина'),('car','автомобиль'),('leaf','лист'),('river','река'),('go','идти'),('go','ехать'),('go','ходить'),('milk','молоко')]]
tr.remove('car')
print(*tr.translate('go'))
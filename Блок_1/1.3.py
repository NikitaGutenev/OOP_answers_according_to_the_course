"""подвиг 3"""
class DataBase:
    pk = 1
    title = 'Классы и объекты'
    author = 'Сергей Балакирев'
    views = 14356
    comments = 12



"""подвиг 4"""
class Goods:
    title = 'Мороженое'
    weight = 154
    tp = 'Еда'
    price = 1024
Goods.price = 2048
Goods.inflation = 100



"""подвиг 5"""
class Car:
    model = 'Тойота'
    color = "Розовый"
    number = "П111УУ77"

print(Car.__dict__['color'])



"""подвиг 6"""
class Notes:
    ...
dict = {'uid': 1005435,'title': "Шутка",'author': "И.С. Бах",'pages': 2}
[setattr(Notes, *i) for i in dict.items()]
print(getattr(Notes,'author'))



"""подвиг 7"""
class Dictionary:
    rus = 'Питон'
    eng = 'Python'
print(getattr(Dictionary, 'rus_word', False))



"""подвиг 8"""
class TravelBlog:
    total_blogs = 0
tb1 = TravelBlog()
[setattr(tb1, *i) for i in {'name': 'Франция','days': 6}.items()]
TravelBlog.total_blogs += 1
tb2 = TravelBlog()
[setattr(tb2, *i) for i in {'name': 'Италия','days': 5}.items()]
TravelBlog.total_blogs += 1



"""подвиг 9"""
class Figure:
    type_fig = 'ellipse'
    color = 'red'

fig1 = Figure()
[setattr(fig1, *i) for i in {'start_pt': (10, 5),'end_pt': (100, 20),'color': 'blue'}.items()]
delattr(fig1, 'color')
print(*fig1.__dict__)



"""подвиг 10"""
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()
print(hasattr(p1.__dict__, 'job'))
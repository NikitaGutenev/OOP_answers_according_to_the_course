"""Подвиг 3"""
class Track:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.points = []
        
    def add_track(self, tr):
        self.points.append(tr)
        
    def get_tracks(self):
        return tuple(self.points)
    
    def __len__(self):
        x = self.start_x
        y = self.start_y
        length = 0
        for i in self.points:
            length += ( (i.to_x - x)**2 + (i.to_y - y)**2 ) ** 0.5
            x = i.to_x
            y = i.to_y
        return int(length)
    
    def __eq__(self, other):
        return self.__len__() == other.__len__()
    
    def __lt__(self, other):
        return self.__len__() < other.__len__()
    
    def __le__(self, other):
        return self.__len__() <= other.__len__()
        
class TrackLine:
    def __init__(self, x, y, speed):
        self.to_x = x
        self.to_y = y
        self.max_speed = speed


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2


"""Подвиг 4"""
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        
    def __setattr__(self, key, value):
        if key in (f'_{self.__class__.__name__}__a',
                   f'_{self.__class__.__name__}__b',
                   f'_{self.__class__.__name__}__c',
                   'a', 'b', 'c') and self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            return object.__setattr__(self, key, value)

    def __lt__(self, other):
        return self.get_volume() < other.get_volume()
    
    def __le__(self, other):
        return self.get_volume() <= other.get_volume()
    
    def get_volume(self):
        return self.a * self.b * self.c
            
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, x):
        self.__a = x
        
    @property
    def b(self):
        return self.__b
    
    @b.setter
    def b(self, x):
        self.__b = x
        
    @property
    def c(self):
        return self.__c
    
    @c.setter
    def c(self, x):
        self.__c = x


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim
        
        
trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.get_volume())


"""Подвиг 5"""
# эти строчки не менять
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


# здесь продолжайте программу
class StringText:
    def __init__(self, lst):
        self.lst_words = list(lst)
        
    def __len__(self):
        return len(self.lst_words)
    
    def __lt__(self, other):
        return len(self) < len(other)
    
    def __le__(self, other):
        return len(self) <= len(other)
    
    
strip_chars = "–?!,.;"
lst_text = [StringText(x.strip(strip_chars) for x in line.split() if len(x.strip(strip_chars)) > 0) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(x.lst_words) for x in lst_text_sorted]


"""Подвиг 6"""
# здесь объявляйте класс
class Morph:
    def __init__(self, *args):
        self.words = [i.lower() for i in args]
        
    def add_word(self, word):
        self.words.append(word)
        
    def get_words(self):
        return tuple(self.words)
    
    def __eq__(self, other):
        return other.lower() in self.words
    
    def __ne__(self, other):
        return other.lower() not in self.words
    

dict_words = [['связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'], 
              ['формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'], 
              ['вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'], 
              ['эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'], 
              ['день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях']]


text = input()   # эту строчку не менять

# здесь создавайте объекты класса и обрабатывайте строку text
dict_words = [Morph(*i) for i in dict_words]
text = [i.strip('.,:;!?') for i in text.split()]
count = 0
for i in text:
    for j in dict_words:
        if i == j:
            count+=1
print(count)


"""Подвиг 7"""
class FileAcceptor:
    def __init__(self, *args):
        if not isinstance(args[0], str):
            self.files = args[0]
        else:
            self.files = args
        
    def __call__(self, file):
        return file.split('.')[-1] in self.files
    
    def __add__(self, other):
        return FileAcceptor(list(self.files) + list(other.files))


"""Подвиг 8"""
class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return None
    
    @classmethod
    def register(cls, money):
        money.cb = cls


class MoneyR:
    def __init__(self, money = 0):
        self.__volume = money
        self.__cb = None

    def __lt__(self, other):
        v1 = self.volume
        v2 = self.__validate(other)
        return v1 < v2 and not abs(v1-v2) <= 0.1
    
    def __le__(self, other):
        v1 = self.volume
        v2 = self.__validate(other)
        return self.__lt__(other) or self.__eq__(other)
    
    def __eq__(self, other):
        v1 = self.volume
        v2 = self.__validate(other)
        return v1 == v2 or abs(v1-v2) <= 0.1

    def __validate(self, obj):
        if self.cb == None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(obj, MoneyD):
            currency = 'dollar'
        elif isinstance(obj, MoneyE):
            currency = 'euro'
        elif isinstance(obj, MoneyR):
            return obj.volume
        return obj.volume * obj.cb.rates[currency] * obj.cb.rates['rub']

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, x):
        self.__volume = x

    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, x):
        self.__cb = x


class MoneyD:
    def __init__(self, money = 0):
        self.__volume = money
        self.__cb = None

    def __lt__(self, other):
        v1 = self.volume * self.cb.rates['rub']
        v2 = self.__validate(other)
        return v1 < v2 and not abs(v1-v2) <= 0.1
    
    def __le__(self, other):
        v1 = self.volume * self.cb.rates['rub']
        v2 = self.__validate(other)
        return self.__lt__(other) or self.__eq__(other)
    
    def __eq__(self, other):
        v1 = self.volume * self.cb.rates['rub']
        v2 = self.__validate(other)
        return v1 == v2 or abs(v1-v2) <= 0.1

    def __validate(self, obj):
        if self.cb == None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(obj, MoneyD):
            currency = 'dollar'
        elif isinstance(obj, MoneyE):
            currency = 'euro'
        elif isinstance(obj, MoneyR):
            return obj.volume
        return obj.volume * obj.cb.rates[currency] * obj.cb.rates['rub']

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, x):
        self.__volume = x

    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, x):
        self.__cb = x


class MoneyE:
    def __init__(self, money = 0):
        self.__volume = money
        self.__cb = None

    def __lt__(self, other):
        v1 = self.volume * self.cb.rates['rub'] / self.cb.rates['euro']
        v2 = self.__validate(other)
        return v1 < v2 and not abs(v1-v2) <= 0.1
    
    def __le__(self, other):
        v1 = self.volume * self.cb.rates['rub'] / self.cb.rates['euro']
        v2 = self.__validate(other)
        return self.__lt__(other) or self.__eq__(other)
    
    def __eq__(self, other):
        v1 = self.volume * self.cb.rates['rub'] / self.cb.rates['euro']
        v2 = self.__validate(other)
        return v1 == v2 or abs(v1-v2) <= 0.1

    def __validate(self, obj):
        if self.cb == None:
            raise ValueError("Неизвестен курс валют.")
        if isinstance(obj, MoneyD):
            currency = 'dollar'
        elif isinstance(obj, MoneyE):
            currency = 'euro'
        elif isinstance(obj, MoneyR):
            return obj.volume
        return obj.volume * obj.cb.rates[currency] * obj.cb.rates['rub']

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, x):
        self.__volume = x

    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, x):
        self.__cb = x


"""Подвиг 9"""
class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        
    def __lt__(self, other):
        if isinstance(other, Body):
            other = other.get_mass()
        return self.get_mass() < other
    
    def __gt__(self, other):
        if isinstance(other, Body):
            other = other.get_mass()
        return self.get_mass() > other
    
    def __le__(self, other):
        if isinstance(other, Body):
            other = other.get_mass()
        return self.get_mass() <= other
    
    def __ge__(self, other):
        if isinstance(other, Body):
            other = other.get_mass()
        return self.get_mass() >= other
    
    def __eq__(self, other):
        if isinstance(other, Body):
            other = other.get_mass()
        return self.get_mass() == other
        
    def get_mass(self):
        return self.ro * self.volume


"""Подвиг 10"""
class Box:
    def __init__(self):
        self.box = []
        
    def __eq__(self, other):
        return set((i.name.lower(), i.mass) for i in self.box) == set((i.name.lower(), i.mass) for i in other.box)
    
    def add_thing(self, obj):
        self.box.append(obj)

    def get_things(self):
        return self.box


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        
    def __eq__(self, other):
        return len({self.name.lower(), other.name.lower(), self.mass, other.mass}) == 2
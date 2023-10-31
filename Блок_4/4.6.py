"""Подвиг 4"""
class Digit:
    def __init__(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)
        if not isinstance(self.value, int):
            raise TypeError('значение не соответствует типу объекта')

            
class Float(Digit):
    def __init__(self, value):
        super().__init__(value)
        if not isinstance(self.value, float):
            raise TypeError('значение не соответствует типу объекта')
            
            
class Positive(Digit):
    def __init__(self, value):
        super().__init__(value)
        if self.value <= 0:
            raise TypeError('значение не соответствует типу объекта')
            
            
class Negative(Digit):
    def __init__(self, value):
        super().__init__(value)
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')
            
         
class PrimeNumber(Integer, Positive):
    pass

class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(2),
          PrimeNumber(5), 
          PrimeNumber(19), 
          FloatPositive(5.4), 
          FloatPositive(15.3), 
          FloatPositive(11.5), 
          FloatPositive(2.4), 
          FloatPositive(0.5) 
          ]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))


"""Подвиг 5"""
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView
class ShopGenericView:
    
    def __str__(self):
        res = ''
        for k,v in self.__dict__.items():
            res += f'{k}: {v}\n'
        return res
    
    def __repr__(self):
        res = ''
        for k,v in self.__dict__.items():
            res += f'{k}: {v}\n'
        return res

    
class ShopUserView:

    def __str__(self):
        res = ''
        for k,v in self.__dict__.items():
            if k == '_id':
                continue
            res += f'{k}: {v}\n'
        return res
    
    def __repr__(self):
        res = ''
        for k,v in self.__dict__.items():
            if k == '_id':
                continue
            res += f'{k}: {v}\n'
        return res


class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


"""Подвиг 8"""
class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView
class GeneralView():
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    
    def render_request(self, request):
        if request['method'] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
            
        return super().__getattribute__(request.get('method').lower())(request)
    
    
class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', )


"""Подвиг 9"""
class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    # здесь объявляйте еще один метод
    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)

    
# здесь объявляйте класс Money
class Money:
    def __init__(self, money):
        if type(money) not in (int, float):
            raise TypeError('сумма должна быть числом')
        self._money = money

    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, value):
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')
        self._money = value
        

class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"



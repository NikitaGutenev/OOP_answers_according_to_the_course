"""Подвиг 2"""
from random import randint # функция для генерации целых случайных значений в диапазоне [a; b]
from random import choices

# Замыкающиеся ф-ции
# def RandomPassword(psw_chars):
#     def create_psw(min_length, max_length):
#         count = randint(min_length, max_length)
#         return "".join(choices(psw_chars,k=count))
#     return create_psw

# rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*")
# psw = rnd(5,20)
# lst_pass  = [rnd(5,20) for i in range(3)]

# здесь объявляйте класс RandomPassword
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length
        
    def __call__(self, *args, **kwargs):
        count = randint(self.min_length, self.max_length)
        return self.create_psw(count, self.psw_chars)
    
    @staticmethod
    def create_psw(count, chars):
        return "".join(choices(chars,k=count))

rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
psw = rnd()
lst_pass  = [rnd() for i in range(3)]



"""Подвиг 3"""
class ImageFileAcceptor:
    def __init__(self, acc):
        self.extensions = acc
        
    def __call__(self, file, *args, **kwargs):
        if file.split('.')[-1] in self.extensions:
            return True



"""Подвиг 4"""
from string import ascii_lowercase, digits

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator
class LengthValidator:
    def __init__(self, min, max):
        self.min_length = min
        self.max_length = max
    def __call__(self, string):
        return self.min_length <= len(string) <= self.max_length
    
class CharsValidator:
    def __init__(self, chars):
        self.chars = chars
    def __call__(self, string):
        return all([True 
                    if i in self.chars 
                    else False 
                    for i in string])



"""Подвиг 5"""
class DigitRetrieve:
    def __init__(self, chars='1234567890-'):
        self.chars = set(chars)
    def __call__(self, *args, **kwargs):
        if set(args[0]) <= self.chars and args[0][1:].isdigit():
            return int(args[0])
        return None



"""Подвиг 6"""
class RenderList:
    def __init__(self, type):
        if type == 'ol':
            self.type = type
        else:
            self.type = 'ul'
    def __call__(self, *args, **kwargs):
        res = f'<{self.type}>\n'
        for i in args[0]:
            res += f'<li>{i}</li>\n'
        res += f'</{self.type}>'
        return res



"""Подвиг 7"""
class HandlerGET:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        return self.get(self.func, args[0])
        
    def get(self, func, request, *args, **kwargs):
        data = func(request)
        if request.get('method','GET') == 'GET':
            return f'GET: {data}'
        return 



"""Подвиг 8"""
class Handler:
    def __init__(self, methods = ('GET',)):
        self.methods = methods
        
    def __call__(self, *args, **kwargs):
        def wrapper(arg):
            method = arg.get('method','GET')
            if method in self.methods:
                return self.__getattribute__(method.lower())(args[0],arg)
            return 
        return wrapper
        
    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'
    
    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'



"""Подвиг 9"""
class InputDigits:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        digits = self.func()
        return list(map(int, digits.split()))
    
@InputDigits
def input_dg():
    return input()

res = input_dg()



"""Подвиг 10"""
class InputValues:
    def __init__(self, render):
        self.render = render
        
    def __call__(self, func, *args, **kwargs):
        def wrapper():
            return self.render(func())
        return wrapper

class RenderDigit:
    def __call__(self, digits, *args, **kwargs):
        res = []
        chars = set('1234567890-')
        for i in digits.split():
            if set(i)<=chars and (i.isdigit() or i[1:].isdigit()):
                res.append(int(i))
            else:
                res.append(None)
        return res
    
render = RenderDigit()
    
@InputValues(render)
def input_dg():
    return input()
    
res = input_dg()
print(res)
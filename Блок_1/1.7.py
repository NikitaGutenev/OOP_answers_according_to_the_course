"""повдиг 6"""
# Здесь объявляется класс Factory
class Factory:
    @staticmethod
    def build_sequence():
        return []
    @staticmethod
    def build_number(str):
        return int(str)
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)



"""подвиг 7"""
from string import ascii_lowercase, digits

# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    def __init__(self,name,size=10):
        self.check_name(name)
        self.name = name
        self.size = size
        
    def get_html(self):
        return f'<p class="login">{self.name}: <input type="text" size={self.size} />'
    
    @classmethod
    def check_name(cls,name):
        if 3<=len(name)<=50 and all([i in cls.CHARS_CORRECT for i in name]):
            return True
        else:
            raise ValueError("некорректное поле name")
        
class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    def __init__(self,name,size=10):
        self.check_name(name)
        self.name = name
        self.size = size
        
    def get_html(self):
        return f'<p class="password">{self.name}: <input type="text" size={self.size} />'
    
    @classmethod
    def check_name(cls,name):
        if 3<=len(name)<=50 and all([i in cls.CHARS_CORRECT for i in name]):
            return True
        else:
            raise ValueError("некорректное поле name")

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()



"""подвиг 8"""
from string import ascii_lowercase, digits
class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    @staticmethod
    def check_card_number(number):
        number = number.replace('-','')
        if all([i.isdigit() for i in number]) and len(number)==16:
            return True
        return False
    @classmethod
    def check_name(cls,name):
        name = name.replace(' ','',1)
        if all([i in cls.CHARS_FOR_NAME for i in name]):
            return True
        return False



"""подвиг 9"""
class Video:
    def create(self,name):
        self.name = name
        
    def play(self):
        print(f"воспроизведение видео {self.name}")
    
class YouTube:
    videos = []
    @classmethod
    def add_video(cls,video):
        cls.videos.append(video)
    @classmethod
    def play(cls,video_indx):
        cls.videos[video_indx].play()

v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python ООП")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)



"""подвиг 10"""
class AppStore:
    apps = []
    def add_application(self,app):
        self.apps.append(app)
    def remove_application(self,app):
        self.apps.remove(app)
    def block_application(self,app):
        app.blocked = True
    def total_apps(self):
        return len(self.apps)
    
class Application:
    def __init__(self, name, blocked = False):
        self.name = name
        self.blocked = blocked



"""повдиг 11"""
class Viber:
    msg = []
    @classmethod
    def add_message(cls,msg):
        cls.msg.append(msg)
    @classmethod
    def remove_message(cls,msg):
        cls.msg.remove(msg)
    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like
    @classmethod
    def show_last_message(cls,count):
        return cls.msg[-count:]
    @classmethod
    def total_messages(cls):
        return len(cls.msg)
    
class Message:
    def __init__(self, text, fl_like = False):
        self.text = text
        self.fl_like = fl_like
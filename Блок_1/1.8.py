"""Тут 1 большая задача. Контрольная работа по блоку. 
Суть: реализовать простую имитацию локальной сети, состоящую из набора серверов, 
соединенных между собой через роутер."""

class Server:
    __ips = {0:'root'}
    def __new__(cls,*args,**kwargs):
        instance = super().__new__(cls)
        last_ip = list(cls.__ips.keys())[-1]
        cls.__ips[last_ip+1] = instance
        return instance
    
    def __init__(self):
        self.buffer = []
        self.ip = max(self.__ips.keys())
    
    def send_data(self,data):
        Router.buffer.append(data)

    def get_data(self):
        tmp = self.buffer.copy()
        self.buffer = []
        return tmp
    
    def get_ip(self):
        return self.ip
    

class Router:
    __server = []
    buffer = []

    @classmethod
    def link(cls,server):
        if server in cls.__server:
            print('роутер уже подключен к этому серверу')
        else:
            cls.__server.append(server)

    @classmethod
    def unlink(cls,server):
        cls.__server.remove(server)

    @classmethod
    def send_data(cls):
        servers = [(j,j.ip) for j in cls.__server]
        for data in cls.buffer:
            for ip in servers:
                if data.ip == ip[1]:
                    ip[0].buffer.append(data)
        cls.buffer = []

class Data:
    def __init__(self,data,ip):
        self.data = data
        self.ip = ip
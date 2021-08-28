'''
Написать класс router.
Должен иметь методы добавить/удалить/вывести список ip address.
Должен иметь методы добавить/удалить/вывести список ip routes.

Есть маршруты к непосредственно-подключенным сетям:
если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
значит у него должен быть маршрут:
к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.

Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
то надо проверять доступен ли gateway.

Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.

Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
до которого у нас пока еще нет маршрута, то должен вылетать exception.

Например:
Добавляем ip-address 192.168.5.14/24 eth1.
Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.

Итого - 1 интерфейс и 3 маршрута в таблице.
'''

import ipaddress
from prettytable import PrettyTable


class router:
    ip_add = []
    ip_rout = []

    @classmethod
    def set_addr(self, add):
        #ip address 192.168.5.14/24 ex1
        add = add.replace('ip address ', '')
        add = add.split(' ')
        for i in range(0, len(self.ip_add)):
            if add[1] in self.ip_add[i][3]:
                return 0
        temp = []
        net = ipaddress.ip_network(add[0], False)
        temp.append(add[0])
        net = str(net.with_netmask).split('/')
        temp.append(net[0])
        temp.append(net[1])
        temp.append(add[1])
        if add[0] in self.ip_add or add[1] in self.ip_add:
            return 0
        else:
            self.ip_add.append(temp)
            return 1

    @classmethod
    def get_addr(self):
        temp = []
        mytable = PrettyTable(['IP', 'NetMask', 'Int'])
        for i in range(0, len(self.ip_add)):
            tmp = []
            tmp = self.ip_add[i].copy()
            tmp.pop(0)
            mytable.add_row(tmp)
        print(mytable)
        return

    @classmethod
    def del_addr(cls, add):
        # rm address ex1
        add = add.replace('rm address ', '')
        for i in range(0, len(cls.ip_add)):
            if add == cls.ip_add[i][3]:
                cls.ip_add.pop(i)
                return 1
        return 0

    @classmethod
    def set_routes(self, add):
        # ip route 172.16.0.0/16 192.168.5.1
        # ip route 172.24.0.0/16 192.168.8.1
        # ip route 172.24.0.0/16 172.16.8.1
        add = add.replace('ip route ', '')
        add = add.split(' ')
        temp = []
        net = ipaddress.ip_network(add[0], False)
        net = str(net.with_netmask).split('/')
        for i in range(0, len(self.ip_rout)):
            if add[0] in self.ip_rout[i][0]:
                return 0
        for i in range(0, len(self.ip_add)):
            if ipaddress.IPv4Address(add[1]) in ipaddress.ip_network(self.ip_add[i][0], False):
                temp.append(add[0])
                temp.append(net[0])
                temp.append(net[1])
                temp.append(add[1])
                temp.append(self.ip_add[i][3])
                self.ip_rout.append(temp)
                return 1
        for i in range(0, len(self.ip_rout)):
            if ipaddress.IPv4Address(add[1]) in ipaddress.ip_network(self.ip_rout[i][0], False):
                temp.append(add[0])
                temp.append(net[0])
                temp.append(net[1])
                temp.append(add[1])
                temp.append(self.ip_rout[i][4])
                self.ip_rout.append(temp)
                return 1
        return 0


    @classmethod
    def get_routes(self):
        mytable = PrettyTable(['IP', 'NetMask', 'gateway', 'Int'])
        for i in range(0, len(self.ip_rout)):
            tmp = []
            tmp = self.ip_rout[i].copy()
            tmp.pop(0)
            mytable.add_row(tmp)
        print(mytable)
        return

    @classmethod
    def del_routes(cls, add):
        # rm route 172.16.0.0/16
        add = add.replace('rm route ', '')
        for i in range(0, len(cls.ip_rout)):
            if add == cls.ip_rout[i][0]:
                cls.ip_rout.pop(i)
                return 1
        return 0


rout = router
rout.set_addr('ip address 192.168.5.14/24 ex1')
rout.set_routes('ip route 172.16.0.0/16 192.168.5.1')
rout.set_routes('ip route 172.24.0.0/16 172.16.8.1')
rout.get_routes()
rout.del_routes('rm route 172.16.0.0/16')
rout.get_routes()
rout.del_addr('rm address ex1')
rout.get_addr()
# while True:
#     inp = input()
#     if inp.startswith('ip route'):
#         if rout.set_routes(inp) == 0:
#             print("exception")
#         else:
#             print("ok")
#     elif inp.startswith('ip address'):
#         rout.set_addr(inp)
#     elif inp.startswith('show address'):
#         rout.get_addr()
#     elif inp.startswith('show route'):
#         rout.get_routes()
#     elif inp.startswith('rm address'):
#         rout.del_addr(inp)
#     elif inp.startswith('rm route'):
#         rout.del_routes(inp)




# ip address 192.168.5.14/24 ex1
# ip route 172.16.0.0/16 192.168.5.1
# ip route 172.24.0.0/16 172.16.8.1
# show route
# rm route 172.16.0.0/16













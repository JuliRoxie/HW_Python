'''
Написать dns сервер.
Сервер должен принимать соединения по протоколу udp.
Если приходит запрос "domain.name" должен отправлять в ответ ip адрес.
* Доп задание: иметь возможность переопределять записи клиентами:
* ADD my.google.com:228.228.228.228
'''

import socket

host = 'localhost'
port = 7777
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#msg = input('Enter message to send: ')
while True:
    inp = input("DNS request: ")
    if inp == "exit":
        client.close()
        break
    else:
        client.sendto(inp.encode(), (host, port))
        d = client.recvfrom(1024)
        print('Server reply: ' + d[0].decode())



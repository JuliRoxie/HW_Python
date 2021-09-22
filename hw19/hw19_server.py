'''
Написать dns сервер.
Сервер должен принимать соединения по протоколу udp.
Если приходит запрос "domain.name" должен отправлять в ответ ip адрес.
* Доп задание: иметь возможность переопределять записи клиентами:
* ADD my.google.com:228.228.228.228
'''


import socket

DNS = [['yandex.ru', '77.88.55.50']]

timeout = 60
host = 'localhost'
port = 7777
addr = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(addr)

while True:
    server.settimeout(timeout)
    try:
        d = server.recvfrom(1024)
    except socket.timeout:
        break
    st = str(d[0].decode()).split(':')
    myStr = ' '.join(st)
    st = myStr.split(' ')
    if st[0] == 'ADD':
        DNS.append([st[1], st[2]])
        server.sendto('Append.'.encode(), d[1])
    elif st[0] == 'CHANGE':
        for i in DNS:
            if st[1] == i[0]:
                i[1] = st[2]
                server.sendto('Changed.'.encode(), d[1])
    elif len(st) == 1:
        er = 0
        for i in range(0, len(DNS)):
            if st[0] == DNS[i][0]:
                server.sendto(DNS[i][1].encode(), d[1])
                er = 1
        if er == 0:
            server.sendto('No such route'.encode(), d[1])
    else:
        server.sendto('Wrong entry.'.encode(), d[1])
server.close()

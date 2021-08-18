'''
Написать программу, которая будет считывать из файла gps координаты,
и формировать текстовое описание объекта и ссылку на google maps.
Пример:

Input data: 60,01';30,19'
Output data:
Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322
'''


from geopy.geocoders import Nominatim


def geo_coord(st):
    st = st.replace(",", ".")
    st = st.replace(";", " ")
    st = st.replace("'", "")
    geolocator = Nominatim(user_agent="google")
    location = geolocator.reverse(st)
    print('Location:', location.address)
    st = st.replace(" ", ",")
    print('Goggle Maps URL:', f'https://www.google.com/maps/search/?api=1&query={st}')


file = open("coord", "r")
while True:
    line = file.readline()
    if not line:
        break
    geo_coord(line)
file.close()

'''
Написать скрипт, который будет вытаскивать gps данные
из фотографии (jpg файл) и передавать их на вход программе
из hw16.txt
'''

from exif import Image


def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600

    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees

    return decimal_degrees


with open('photo.jpg', 'rb') as image_file:
    image_bytes = image_file.read()
my_image = Image(image_bytes)
print(f"Latitude (DD): {dms_coordinates_to_dd_coordinates(my_image.gps_latitude, my_image.gps_latitude_ref)}")
print(f"Longitude (DD): {dms_coordinates_to_dd_coordinates(my_image.gps_longitude, my_image.gps_longitude_ref)}\n")

my_file = open("coord", "w")
my_file.write(str(dms_coordinates_to_dd_coordinates(my_image.gps_latitude, my_image.gps_latitude_ref)) + ";" + str(dms_coordinates_to_dd_coordinates(my_image.gps_longitude, my_image.gps_longitude_ref)))
my_file.close()

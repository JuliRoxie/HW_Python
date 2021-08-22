'''
Написать скрипт, который будет создавать миниатюры фотографий.
Объем полученого файла должен передаваться как параметр.
'''


from PIL import Image

print("Max height:")
height = input()
print("Max width:")
width = input()
image = Image.open("photo.jpg")
image.thumbnail((int(width), int(height)))
image.save('thumbnail.jpg', 'JPEG')

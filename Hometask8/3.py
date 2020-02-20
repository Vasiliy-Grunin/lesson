import requests
import base64
import os


def cat_transfer(filename):
    response = requests.post("https://postman-echo.com/post",
                             files={filename: open(filename, 'rb')})
    pic = response.json()['files'][filename][len('data:application/octet-stream;base64,'):]
    with open(filename, 'wb') as postkotik_file:
        postkotik_file.write(base64.b64decode(pic))
    return os.path.getsize(filename)


def main():
    name = input('Введите название картинки: ')
    fname = name + '.jpeg'
    size = cat_transfer(fname)
    print(size, 'b')


main()

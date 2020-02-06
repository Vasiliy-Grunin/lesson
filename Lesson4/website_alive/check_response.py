import requests


def foo_site(url):
    # ожидаю на вход ссылку
    s = requests.get(url)
    return s

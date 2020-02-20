import requests


def main():
    # url = input("write url: ")
    # url = "https://google.com."
    # url = "https://yandex.ru"
    url = "https://vk.com"
    answer = requests.get(url).text
    print(len(answer))


main()

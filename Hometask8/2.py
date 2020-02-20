import requests
import datetime

def main():
    your_money = float(input("How money? "))
    your_currency = str(input("What your currency? "))
    trans_currency = str(input("What currency to convert? "))
    url = "https://api.exchangerate-api.com/v4/latest/"
    url += your_currency.upper()
    currency = requests.get(url).json()
    answer = float(your_money*currency['rates'][trans_currency.upper()])
    print('{:.2f}'.format(answer))


main()

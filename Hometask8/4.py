import re


def reg(date):
    date = re.fullmatch(r'\d{4}(-)\d{2}(-)\d{2}(T)\d{2}(:)\d{2}(:)\d{2}(\+|-)\d{2}(:)\d{2}', date)
    print('подходит' if date else 'не подходит')


def main():
    date = input("write date: ")
    reg(date)

main()
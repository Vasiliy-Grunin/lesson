import re


def reg(slovo):
    answer = re.fullmatch(r'[A-Za-z {2,} {4,}] *\?', slovo)
    print('подходит' if answer else 'не подходит')


def main():
    slovo = input("write date: ")
    reg(slovo)

main()
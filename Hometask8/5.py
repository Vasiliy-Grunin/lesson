import re

def password(pas):
    answer = re.fullmatch(r'[A-Za-z] | [0-9] | [\w\d_*%&] {8,12}$', pas)
    print('подходит' if answer else 'не подходит')



def main():
    pas = input("write password: ")
    password(pas)


main()
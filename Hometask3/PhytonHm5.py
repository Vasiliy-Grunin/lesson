def main():
    s=input("write number: ")
    print(foo(s))


def foo(s):
    min=2190200
    a=[float(x) for x in s.split()]
    i=0
    for i in a:
        if abs(min)>abs(i):
             min=i
    return min


main()

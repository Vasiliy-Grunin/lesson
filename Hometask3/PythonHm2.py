def foo(*args):
    sum = 0
    mul=1
    for i in args:
        if type(i) != int and type(i) != float:
            sum += foo1(i)
        else:
            sum += i
    return sum

def foo1 (**kwargs):
    for i in kwargs:
        if type(i) != int or type(i) != float:
            sum += foo(i)
        else:
            sum += i
    return sum


def main():
    a = (10, 11)
    b = (3, 4, [5, 6, [7, 8], []])
    print("Answer: ", foo(a,b))


main()

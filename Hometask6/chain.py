def chain(*args):
    for arg in args:
        yield arg


def main():
    arr=chain(89,5,7,8,(1,2,4))
    it=iter(arr)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

main()
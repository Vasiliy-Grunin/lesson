def circular(*arr):
    while True:
        for connection in arr:
            yield connection


def main():
    arr = circular(6, 5, 7, 2, 8)
    it = iter(arr)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))


main()

class Evenlterator(object):
    def __init__(self, *items):
        self.items = items

    def __getitem__(self, i):
        if i % 2 == 0:
            return self.items[i]
        else:
            i += 1
            return self.items[i]

def main():
    arr = Evenlterator(6, 5, 72, 5)
    it = iter(arr)
    print(next(it))
    print(next(it))


main()

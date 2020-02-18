class example(object):
    arg1 = None
    arg2 = None

    def __init__(self):
        super(example, self).__init__()

    def foo(self):
        pass


def main():
    print(filter(lambda x: not x.startswith("_") or x.startswith("__"), dir(example)))


main()

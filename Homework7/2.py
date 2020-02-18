from time import sleep


def time_methods(foo):
    import time
    def wrapper(*args):
        start_time = time.time()
        foo(*args)
        end_time = time.time()
        return "отработала за {}".format(end_time - start_time)
    return wrapper

class Spam:
    def __init__(self, s):
        self.s = s
    @time_methods
    def inspect(self):
        sleep(self.s)

    def foo(self):
        return self.s


a = Spam(4)
print(a.inspect())
a.foo()

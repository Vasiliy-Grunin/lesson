from time import sleep


def average_time(n):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(n):
                start = time.time()
                value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('Среднее время выполнения: {} секунд.'.format(total / n))
            return value

        return wrapper

    return actual_decorator


@average_time(n=2)
def foo(a):
    import time
    sleep(a)
    return a


a = 3
print(foo(a))
b = 7
print(foo(b))
n = 5
print(foo(n))

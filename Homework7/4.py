def accepts(*types):
    def check_accepts(function):
        if len(types) != function.__code__.co_argcount:
            raise AttributeError

        def new_function(*args, **kwargs):
            for (x, y) in zip(args, types):
                if not isinstance(x, y):
                    print("Type error")
                    raise TypeError
            return function(*args, **kwargs)

        new_function.__name__ = function.__name__
        return new_function

    return check_accepts


@accepts(int, (int))
def func(arg1, arg2):
    return arg1 * arg2


print(func(3, 1))
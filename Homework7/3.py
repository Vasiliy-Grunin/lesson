def curry(func):
    def call(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return (lambda *args2, **kwargs2:
                call(*(args + args2), **dict(kwargs, **kwargs2)))
    return call


@curry
def foo(a, b, c, d, e, f, g, h):
    return a + b + c + d + e+f+g+h


print(foo(1)(2)(3)(4)(5))
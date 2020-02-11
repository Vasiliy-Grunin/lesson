class Observable(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, (', '.join('%s=%s' % (key, val)
                                                               for (key, val) in self.__dict__.items() if
                                                               not key.startswith('_'))))


class X(Observable, dict):
    def __getattr__(self, name):
        try:
            return super(Observable, self).__getitem__(name)
        except KeyError:
            if not name.startswith('get_'):
                return getattr(self, 'get_%s' % name)()
            else:
                raise AttributeError


def main():
    # arr = dict(input("write elem: "))
    x = X(foo=1, bar=5, _bazz=12, name="Amok", props=("One", "two"))
    print(x)
    print(x.name)


main()

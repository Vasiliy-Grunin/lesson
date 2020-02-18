def dict_from_keys(keys, values):
    return dict((len(keys) > len(values)) and map(None, keys, values) or zip(keys, values))

def main():
    a = ('pass', 'vas', 'asd',"qwerty")
    b = (1, 2, 3)
    print(dict_from_keys(b,a))

main()
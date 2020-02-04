max = -2147483647
def foo(a, b, c, d) :
    answer=(a+b+c+d)/4
    if max < a:
        max = a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = c
    s = "answer = " + answer + "max = " + max
    return s

def main() :
    y = input("start program (write y): ")
    while y.lower() == "y":
        a = input("write the first element: ")
        b = input("write the second element: ")
        c = input("write the find element: ")
        d = input("write the fourth element: ")
        print(foo(a, b, c, d))
    print("the end program ")

main ()

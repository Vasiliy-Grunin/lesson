import math

class Complex(object):

    def __init__(self, new_number1, nem_pointer1):
        self.number = float(new_number1)
        self.pointer = float(nem_pointer1)

    def __str__(self):
            try:
                return "{}+{}i".format(round(self.number, 2), round(self.pointer, 2))
            except
                return 

    def __add__(self, other):
        return Complex(float(float(self.number) + float(other.number)),
                       float(float(self.pointer) + float(other.pointer)))

    def __sub__(self, other):
        return Complex(float(float(self.number) - float(other.number)),
                       float(float(self.pointer) - float(other.pointer)))

    def __mul__(self, other):
        return Complex((float(self.number) * float(other.number) - float(self.pointer * other.pointer)),
                       (float(self.number) * float(other.pointer) + float(self.pointer) * float(other.number)))

    def __truediv__(self, other):
        return Complex(float(self.number * other.number + self.pointer * other.pointer)
                       / float(other.number ** 2 + other.pointer ** 2), float(
                                   self.pointer * other.number - self.number * other.pointer) / float(
                               other.number ** 2 + other.pointer ** 2))
    def __abs__(self):
        return Complex(math.sqrt(self.number**2 + self.pointer**2), 0.00)



def main():
    arr1 = list(input().split())
    arr2 = list(input().split())
    number1 = Complex(arr1[0], arr1[1])
    number2 = Complex(arr2[0], arr2[1])
    print(number1 + number2)
    print(number1 - number2)
    print(number1 * number2)
    print(number1 / number2)
    print(abs(number1))
    print(abs(number2))


main()

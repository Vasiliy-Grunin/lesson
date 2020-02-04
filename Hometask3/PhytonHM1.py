def main():
    arr=list(map(int,input("write elements by spaces: ").split()))
    print("x^2 : ", mult(arr))
    print("%2 : ",chet(arr))
    print("third: ",third(arr))
# функция возвращает квадраты элементов
def mult(arr):
    answer=[]
    for i in arr:
        answer.append(i*i)
    return answer
# функция возвращает элементы с четных позицей
def chet(arr):
    answer=[]
    for i in arr:
        if arr.index(i)%2 == 0 and arr.index(i) != 0:
            answer.append(i)
    return answer
#функция возвращает кубы с нечетных позиций у четных элементов
def third(arr):
    answer=[]
    for i in arr:
        if arr.index(i)%2 != 0:
            if i%2 == 0:
                answer.append(i**3)
    return answer

main()

def fuktor(n):
    answer=1
    for i in range(1,n+1):
        answer*=i
    return answer

def main():
    a=int(input("write number: "))
    print(fuktor(a))


main()

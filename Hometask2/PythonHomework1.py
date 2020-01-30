def foo(x):
    x+=1
    for i in range(1,x):
        if i%2 != 0 :
            print(i*i," ")

def main():
    a=int(input("write number: "))
    foo(a)

main()
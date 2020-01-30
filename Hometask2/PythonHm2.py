def foo(a,b,c):
    count=0
    for i in range(a,b):
        if i%c==0:
            count+=1
    return count

def main():
    a=int(input("write left border: "))
    b=int(input("write right border: "))
    c=int(input("write del: "))
    print("answer",foo(a,b,c))

main()

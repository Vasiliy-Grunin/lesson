def Range(i,h,n):
    if h<1:
        h=1
    arr= list() 
    while i < n:
        arr.append(i)
        i+=h
    return arr

def main():
    A = []
    n=int(input("write right border: "))
    s=int(input("write left border: "))
    h=int(input("write step: "))
    A = Range(s,h,n)
    print(A)

main()
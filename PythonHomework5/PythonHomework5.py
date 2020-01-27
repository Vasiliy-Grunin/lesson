def poisk(x,c,y):
    if x in c and y in c:
        return True
    else:
        return False




a=set(input("write 1 set ",))
b=set(input("write 2 set ",))
c=set(input("write 3 set ",))
if c <= a and c <= b:
    print("True")
else :
    print("False")
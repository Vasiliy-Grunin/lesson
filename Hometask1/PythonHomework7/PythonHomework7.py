a={}
b={}
c={}
i=int(input("write size first dict "))
a= dict((x, x**2) for x in range(i))
i=int(input("write size first dict "))
b= dict((x, x) for x in range(i))
c.update(a)
c.update(b)
print("2 ",c)
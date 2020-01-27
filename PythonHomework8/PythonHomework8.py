import random
i=int(input("write size: "))
a=dict((x,random.randint(-11,100)) for x in range(i))
print(a)
arr=list()
for index in range(len(a)):
    arr.append(a[index])
arr.sort()
print("max 1 = ", arr[-1]," max 2 = ", arr[-2]," max 1 = ", arr[-3])

from itertools import groupby

arr=input("write array " )
new_arr = [el for el, _ in groupby(arr)]
print(new_arr)

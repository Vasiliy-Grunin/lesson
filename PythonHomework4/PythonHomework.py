def clone(word):
    count=0
    for i in range(len(word)):
        if len(word[i])>=2 and word[i][0]==word[i][-1]:
            count+=1
    return count

word= [str(i) for i in input("write elements " ).split()]
print(clone(word))
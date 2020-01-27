def first_plus_lust(s):
    if(len(s)==1):
        answer="Empty String"
        return answer
    else:
        answer=s[0]+s[1]+s[-2]+s[-1]
        return answer
s=input("write string ")
print(first_plus_lust(s))

from itertools import groupby
n=int(input())
s=[]
for i in groupby(input(),lambda x:x=="x"):
    s.append(list(i[1]))
#s=list(groupby(input(),lambda x:x=="x"))
ans=0
for i in s:
    if i[0]=="x":
        ans+=max(0,len(i)-2)
print(ans)

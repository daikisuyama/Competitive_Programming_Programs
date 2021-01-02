s=list(map(int,input()))
from itertools import permutations
if len(s)<3:
    for i in permutations(s):
        x=int("".join(map(str,i)))
        if x%8==0:
            print("Yes")
            exit()
    print("No")
    exit()
d=dict()
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in range(100,1000):
    if i%8==0:
        x=list(map(int,str(i)))
        c=dict()
        for j in x:
            if j in c:
                c[j]+=1
            else:
                c[j]=1
        for j in c:
            if j not in d:
                break
            else:
                if d[j]>=c[j]:
                    continue
                else:
                    break
        else:
            print("Yes")
            exit()
print("No")
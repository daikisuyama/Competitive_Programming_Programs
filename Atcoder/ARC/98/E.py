n,k,q=map(int,input().split())
a=list(map(int,input().split()))
c=sorted(a)
#bの小さいものから順にaを分割
b=sorted(list(set(a)))
now=0
ans=[c[q-1]-c[0]]
d=[a]
from itertools import groupby
def calc(x,de):
    ret=[]
    for i in x:
        for ke,val in groupby(i,key=lambda y:y==de):
            if not ke:
                ret.append(list(val))
    return ret
while now<len(b):
    d=calc(d,b[now])
    e=[sorted(i) for i in d]
    cand=[]
    for i in e:
        if len(i)>=k:
            for j in range(len(i)-k+1):
                cand.append(i[j])
    cand.sort()
    if len(cand)>=q:
        ans.append(cand[q-1]-cand[0])
    else:
        break
    now+=1
print(min(ans))
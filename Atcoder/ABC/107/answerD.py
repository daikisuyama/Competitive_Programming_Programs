#は？、問題文誤読した、何やってんの…

n=int(input())
a=list(map(int,input().split()))

cand=[]
if n%2==0:
    for i in range(n//2):
        if i==0:
            cand.append(1)
        else:
            cand.append(cand[-1]+2)
    for i in range(n//2,n):
        cand.append(cand[n-i-1]+1)
else:
    for i in range(n//2+1):
        if i==0:
            cand.append(1)
        else:
            cand.append(cand[-1]+2)
    for i in range(n//2+1,n):
        cand.append(cand[n-i-1]+1)
ans=list(map(list,zip(a,cand)))
#print(ans)
ans.sort()
x,y=[i[0] for i in ans],[i[1] for i in ans]
l=n*(n-1)//2+n
z=l//2+1
from itertools import accumulate
#print(ans)
ac=list(accumulate(y))
#print(ac)
for i in range(n):
    if ac[i]>=z:
        print(x[i])
        break
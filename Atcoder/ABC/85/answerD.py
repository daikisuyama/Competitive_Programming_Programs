import math
n,h=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort(reverse=True)
k=ab[0][0]
ab.sort(reverse=True,key=lambda x:x[1])
ans=0
while h>0:
    if ans==n:
        break
    if k<=ab[ans][1]:
        h-=ab[ans][1]
        ans+=1
    else:
        break
if h<=0:
    print(ans)
else:
    print(ans+math.ceil(h/k))

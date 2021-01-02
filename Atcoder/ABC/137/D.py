#18:10~18:24
#いい感じ
#Aが短いものから貪欲で行けそう
from heapq import *
n,m=map(int,input().split())
#何日かかるのかで(1-indexed)
ab=[[] for i in range(m)]
for i in range(n):
    a,b=map(int,input().split())
    #超えないように
    if a<=m:
        ab[a-1].append(b)
x=[]
l=0
ans=0
for i in range(m-1,-1,-1):
    for j in ab[m-1-i]:
        heappush(x,-j)
        l+=1
    if l:
        l-=1
        ans+=heappop(x)
print(-ans)
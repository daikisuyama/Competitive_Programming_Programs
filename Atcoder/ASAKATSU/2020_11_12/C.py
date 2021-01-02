s=input()
n=len(s)
from itertools import groupby
g=[[key,len(list(gr))] for key,gr in groupby(s)]
m=len(g)
ans=[0]*n
now=0
for i in range(m//2):
    x,y=g[2*i][1],g[2*i+1][1]
    now+=x
    ans[now-1]+=(x-x//2)
    ans[now-1]+=(y//2)
    ans[now]+=(y-y//2)
    ans[now]+=(x//2)
    now+=y
print(" ".join(map(str,ans)))
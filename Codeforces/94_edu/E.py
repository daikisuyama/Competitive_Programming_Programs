from itertools import groupby
from sys import setrecursionlimit
setrecursionlimit(10**6)

n=int(input())
a=list(map(int,input().split()))

def dfs(x):
    l=len(x)
    if l==1:return 1
    ret=min(x)
    for i,j in groupby([i-min(x) for i in x],key=lambda y:y!=0):
        if i:
            ret+=dfs(list(j))
    return min(ret,l)

print(dfs(a))
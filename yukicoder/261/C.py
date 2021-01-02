#ミス
import sys
input=sys.stdin.readline
n,a,b=map(int,input().split())
x=list(map(int,input().split()))
check=[False]*n
from collections import deque
from bisect import bisect_left,bisect_right
ans=deque()
for i in range(n):
    if check[i]==False:
        check[i]=True
        ans_sub=deque({i})
        now=deque({i})
        while len(now):
            for _ in range(len(now)):
                d=x[now.popleft()]
                l1=bisect_left(x,d-b)
                l2=bisect_right(x,d-a)-1
                if l1<=l2:
                    for j in range(l1,l2+1):
                        if check[j]==False:
                            check[j]=True
                            now.append(j)
                            ans_sub.append(j)
                r1=bisect_left(x,d+a)
                r2=bisect_right(x,d+b)-1
                if r1<=r2:
                    for j in range(r1,r2+1):
                        if check[j]==False:
                            check[j]=True
                            now.append(j)
                            ans_sub.append(j)
        ans.append(ans_sub)
g=[0]*n
for i in ans:
    l=len(i)
    for j in i:
        g[j]=l
for i in range(n):
    print(g[i])

from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians
from fractions import Fraction
from decimal import Decimal
import sys
#input=sys.stdin.readline
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=10**20

h,w=map(int,input().split())
r=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=[[-1]*w for i in range(h)]
#print(r)
#print(c)
for i in range(h):
    #print(i,r[i])
    for j in range(r[i]):
        ans[i][j]=1
    if r[i]!=w:
        ans[i][r[i]]=0
#print(ans)
for j in range(w):
    for i in range(c[j]):
        if ans[i][j]!=0:
            ans[i][j]=1
        else:
            #print(1)
            #print(ans)
            print(0)
            exit()
    if c[j]!=h:
        if ans[c[j]][j]!=1:
            ans[c[j]][j]=0
        else:
            print(0)
            exit()
s=0
for i in range(h):
    for j in range(w):
        s+=ans[i][j]==-1
print(pow(2,s,MOD))

            
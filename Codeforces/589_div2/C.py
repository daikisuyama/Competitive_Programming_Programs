from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians
from fractions import Fraction
from decimal import Decimal
import sys
input=sys.stdin.readline().rstrip
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=10**20
prime=[]
def prime_factorize(n):
    if n<=1:return
    l=int(sqrt(n))
    for i in range(2,l+1):
        if n%i==0:
            prime_factorize(i)
            prime_factorize(n//i)
            return
    prime.append(n)
    return
x,m=map(int,input().split())
prime_factorize(x)
prime=list(set(prime))
ans=1
for j in prime:
    ans_sub=0
    now=j
    while now<=m:
        ans_sub+=m//now
        now*=j
    ans*=pow(j,ans_sub,MOD)
    ans%=MOD
print(ans)
#print(prime)
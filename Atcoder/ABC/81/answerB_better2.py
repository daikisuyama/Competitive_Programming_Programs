from functools import reduce
from fractions import gcd
n=int(input())
a=list(map(int,input().split()))
x=reduce(gcd,a)

ans=0
while x%2==0:
    ans+=1
    x//=2
print(ans)

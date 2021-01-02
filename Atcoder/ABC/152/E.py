from fractions import gcd
from functools import reduce
mod=1000000000+7
n=int(input())
a=list(map(int,input().split()))
l=reduce(lambda x,y:x//gcd(x,y)*y,a)
ans=sum(map(lambda x:l//x,a))
print(ans%mod)

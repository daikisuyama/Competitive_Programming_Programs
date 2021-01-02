from math import gcd
def lcm(a,b):
    return a//gcd(a,b)*b
n=int(input())
ans=1
for i in range(2,n+1):
    ans=lcm(i,ans)
print(ans+1)
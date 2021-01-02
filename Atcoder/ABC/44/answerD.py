import math 
import bisect
import sys
def f(b,n):
    m=math.floor(n/b)
    if n>=b:
        return f(b,m) + n%b
    else:
        return n
n=int(input())
s=int(input())
for i in range(2,int(math.sqrt(n))+1):
    x=f(i,n)
    if x==s:
        print(i)
        sys.exit()
if n-int(math.sqrt(n))<2:
    l=2
else:
    l=n-int(math.sqrt(n))
for i in range(n+1,l-1,-1):
    x=f(i,n)
    if x==s:
        print(i)
        sys.exit()
print(-1)

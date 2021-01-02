#いもす法
import sys
#input→sys.stdin.readline半分に
input=sys.stdin.readline
n,q=map(int,input().split())
x=[0]*n
for i in range(q):
    l,r=map(int,input().split())
    x[l-1]+=1
    if r<n:
        x[r]-=1
for i in range(n-1):
    x[i+1]+=x[i]
    x[i]%=2
x[n-1]%=2
print("".join(list(map(str,x))))

from sys import setrecursionlimit
setrecursionlimit(10**8)
def extgcd(a,b,x,y):
    if b==0:
        x[0],y[0]=1,0
        return a
    e=extgcd(b,a%b,y,x)
    y[0]-=(a//b)*x[0]
    return e

n,p,w,d=map(int,input().split())
from math import gcd
if p%gcd(w,d)!=0:
    print(-1)
    exit()
f=gcd(w,d)
h=p//f
x,y=[0],[0]
extgcd(w,d,x,y)
x=x[0]*h
y=y[0]*h
w//=f
d//=f
if y>=0:
    g=y//w
    x+=g*d
    y-=g*w
else:
    g=-(y//w)
    x-=g*d
    y+=g*w
if x<0 or x+y>n:
    print(-1)
else:
    print(x,y,n-x-y)
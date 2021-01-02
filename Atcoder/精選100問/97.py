#11/26 16:28~16:39
#aを全て2でわると
#x=a_k(2p+1)
#2で割り切れた数が違う→0
#同じ時はa_kの最小公倍数の倍数で偶数倍ではないもの
#ちょっとむずいね
n,m=map(int,input().split())
a=[i//2 for i in list(map(int,input().split()))]
now=0
x=a[0]
while x%2==0:
    x//=2
    now+=1
for i in range(1,n):
    x=a[i]
    now_=0
    while x%2==0:
        x//=2
        now_+=1
    if now!=now_:
        print(0)
        exit()
from math import gcd
g=a[0]
for i in range(n-1):
    g=g*a[i+1]//gcd(g,a[i+1])
y=m//g
print(-(-y//2))
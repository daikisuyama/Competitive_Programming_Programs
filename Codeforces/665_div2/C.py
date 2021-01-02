from math import gcd
def gcditer(x):
    ret=x[0]
    for i in range(1,len(x)):
        ret=gcd(ret,x[i])
    return ret
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    #同じやつも使えばいいんじゃね
    #約数なら使っても良い
    m=min(a)
    c=[a[i]%m==0 for i in range(n) if a[i]!=b[i]]
    if len(c)==0:
        print("YES")
    elif all(c):
        print("YES")
    else:
        print("NO")
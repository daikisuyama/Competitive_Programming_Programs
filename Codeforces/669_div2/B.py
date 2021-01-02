from math import gcd
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    check=[False]*n
    b=[0]*n
    b[0]=max(a)
    check[a.index(max(a))]=True
    now=b[0]
    for i in range(1,n):
        #値,インデックス
        max1=[-1,-1]
        for j in range(n):
            if not check[j]:
                if max1[0]<gcd(a[j],now):
                    max1=[gcd(a[j],now),j]
        check[max1[1]]=True
        b[i]=a[max1[1]]
        now=max1[0]
    print(" ".join(map(str,b)))
import math

n,k=map(int,input().split())
a=sorted([int(i) for i in input().split()],reverse=True)
f=sorted([int(i) for i in input().split()])
c=[[a[i],f[i]] for i in range(n)]
c.sort(key=lambda x:x[0]*x[1],reverse=True)

if n==1:
    print(max(0,(c[0][0]-k)*c[0][1]))
else:
    while k!=0 and c[0][0]!=0:
        x=c[0][0]*c[0][1]-c[1][0]*c[1][1]
        if c[0][0]*c[0][1]-c[1][0]*c[1][1]<c[0][1]:
            k-=1
            c[0][0]-=1
        else:
            l=math.ceil(x/c[0][1])
            m=min(l,c[0][0])
            k-=m
            c[0][0]-=m
        for i in range(n-1):
            if c[i][0]*c[i][1]<c[i+1][0]*c[i+1][1]:
                c[i],c[i+1]=c[i+1],c[i]
            else:
                break

    print(c[0][0]*c[0][1])

import cmath
import math
import itertools
n=int(input())
a=[]
b=[]
#偏角ソートの方が楽
for i in range(n):
    x,y=map(int,input().split())
    a.append(complex(x,y))
a.sort(key=cmath.phase)
m=0
#math.piに注意
for i in range(n):
    if a[i]!=complex(0,0):
        za,zb=complex(0,0),complex(0,0)
        for j in range(n):
            p=cmath.phase(a[j]/a[i])
            if -math.pi<=p<=0:
                za+=a[j]
            if 0<=p<=math.pi:
                zb+=a[j]
        m=max([m,abs(za),abs(zb)])
        if i!=n-1 and a[i]+a[i+1]!=0:
            zc,zd=complex(0,0),complex(0,0)
            for j in range(n):
                p=cmath.phase(a[j]/((a[i]+a[i+1])/2))
                if -math.pi<=p<=0:
                    zc+=a[j]
                if 0<=p<=math.pi:
                    zd+=a[j]
            m=max([m,abs(zc),abs(zd)])


print(m)

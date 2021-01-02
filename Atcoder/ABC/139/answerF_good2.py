import cmath
import math
n=int(input())
a=[]
b=[]
#偏角ソートの方が楽
for i in range(n):
    x,y=map(int,input().split())
    a.append(complex(x,y))
    b.append(cmath.phase(a[i]))
#a.sort(key=cmath.phase)
ma=0
#math.piに注意
for i in range(n):
    z=a[i]
    c=b[i]-math.pi/2
    d=b[i]+math.pi/2
    l=max([c,-math.pi])
    r=min([d,math.pi])
    #(0,0)の時は偏角が0になってしまうし、除く
    #あとは-piとpiどっちになるか→piになる
    if a[i]!=complex(0,0):
        for j in range(n):
            if j!=i:
                #境界条件の場合分けがむずい
                if l<=b[j]<=r or (c<=-math.pi and c+2*math.pi<=b[j]<=math.pi) or (d>=math.pi and -math.pi<=b[j]<=d-2*math.pi):
                    z+=a[j]
    ma=max([abs(z),ma])
m=0
for i in range(n):
    za,zb=0,0
    if a[i]!=complex(0,0):
        for j in range(n):
            p=cmath.phase(a[j]/a[i])
            if -math.pi<=p<=0:
                za+=a[j]
            if 0<=p<=math.pi:
                zb+=a[j]
    m=max([abs(za),abs(zb),m])
print(max([m,ma]))

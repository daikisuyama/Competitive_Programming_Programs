import math
t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
#相対速度
c1,c2=a1-b1,a2-b2
#離れる距離
d1,d2=abs(c1*t1),-abs(c2*t2)

if (c1>0 and c2>0) or (c1<0 and c2<0) or d1+d2>0:
    print(0)
elif d1+d2==0:
    print("infinity")
else:
    x=d1//(-(d1+d2))
    y=d1%(-(d1+d2))
    if y==0:
        print(2*x)
    else:
        print(2*x+1)

#10**9+7のあまりを忘れていた
import math 
n=int(input())
d=dict()
for i in range(n):
    a,b=map(int,input().split())
    if a==0 and b==0:
        pass
    elif a==0:
        a,b=0,1
    elif b==0:
        a,b=1,0
    else:
        x=math.gcd(abs(a),abs(b))
        a,b=a//x,b//x
        if a<0:
            a,b=-a,-b
    if (a,b) in d:
        d[(a,b)]+=1
    else:
        d[(a,b)]=1
#こっからは数え上げ
#print(d)
ans1,ans2=1,0
for i in d:
    if d[i]==0:
        continue
    if i==(0,0):
        ans2=d[i]
        d[i]=0
        continue
    #独立…
    a,b=i
    if (-b,a) in d:
        ans1*=(2**(d[i])+2**(d[(-b,a)])-1)
        d[(-b,a)]=0
        d[i]=0
    elif (b,-a) in d:
        ans1*=(2**(d[i])+2**(d[(b,-a)])-1)
        d[(b,-a)]=0
        d[i]=0
    else:
        ans1*=(2**(d[i]))
        d[i]=0
print((ans1+ans2-1)%(10**9+7))
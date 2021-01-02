import bisect
q=int(input())
A1,A2,B=[],[],0
s1,s2=0,0
l1,l2=0,0

for i in range(q):
    x=input()
    if x=="2":
        print(-s1+s2+A1[-1]*(l1-l2)+B)
    else:
        _,a,b=map(int,x.split())
        B+=b
        if i==0:
            A1+=[a]
            l1+=1
            continue
        if l%2==1:
            m=(l-1)//2
            l+=1
            B+=b
            j=bisect.bisect_right(A,a)
            A.insert(j,a)
            if j>m:
                now=(m,now[1]+b+abs(now[0]-a))
            else:
                now=(m,now[1]+b+abs(now[0]-a))
        else:
            l+=1
            B+=b
            j=bisect.bisect_right(A,a)
            A.insert(j,a)
            now=


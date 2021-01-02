n=int(input())
a=list(map(int,input().split()))
q=int(input())
d=dict()
for i in range(n):
    if a[i] in d:
        d[a[i]]+=1
    else:
        d[a[i]]=1
d2,d4,d6,d8=set(),set(),set(),set()
for i in d:
    if d[i]>=8:
        d8.add(i)
    elif d[i]>=6:
        d6.add(i)
    elif d[i]>=4:
        d4.add(i)
    elif d[i]>=2:
        d2.add(i)
for i in range(q):
    s,x=input().split()
    x=int(x)
    if s=="+":
        if x in d:
            d[x]+=1
            if d[x]==2:
                d2.add(x)
            elif d[x]==4:
                d2.remove(x)
                d4.add(x)
            elif d[x]==6:
                d4.remove(x)
                d6.add(x)
            elif d[x]==8:
                d6.remove(x)
                d8.add(x)
        else:
            d[x]=1
    else:
        d[x]-=1
        if d[x]==1:
            d2.remove(x)
        elif d[x]==3:
            d4.remove(x)
            d2.add(x)
        elif d[x]==5:
            d6.remove(x)
            d4.add(x)
        elif d[x]==7:
            d8.remove(x)
            d6.add(x)
    if len(d8)>0:
        print("YES")
    elif len(d6)>=2:
        print("YES")
    elif len(d6)==1 and len(d4)+len(d2)>0:
        print("YES")
    elif len(d4)>=2:
        print("YES")
    elif len(d4)==1 and len(d2)>=2:
        print("YES")
    else:
        print("NO")
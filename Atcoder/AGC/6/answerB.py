#20分くらい(デバッグ①時間以上…)
from itertools import chain
n,x=map(int,input().split())
if x!=2*n-1 and x!=1:
    print("Yes")
    if n==2:
        print(1)
        print(2)
        print(3)
        exit()
    ans=[-1 for i in range(2*n-1)]
    s={i+1 for i in range(2*n-1)}
    if x!=2:
        ans[n-2]=x-1
        ans[n-1]=x
        ans[n]=x+1
        ans[n+1]=x-2
        s.remove(x-1)
        s.remove(x)
        s.remove(x+1)
        s.remove(x-2)
        s=list(s)
        now=0
        for i in chain(range(n-2),range(n+2,2*n-1)):
            ans[i]=s[now]
            now+=1
    else:
        ans[n-3]=x+2
        ans[n-2]=x-1
        ans[n-1]=x
        ans[n]=x+1
        s.remove(x+2)
        s.remove(x-1)
        s.remove(x)
        s.remove(x+1)
        s=list(s)
        now=0
        for i in chain(range(n-3),range(n+1,2*n-1)):
            ans[i]=s[now]
            now+=1
    for i in range(2*n-1):
        print(ans[i])
else:
    print("No")
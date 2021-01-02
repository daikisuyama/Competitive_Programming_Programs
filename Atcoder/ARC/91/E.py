from collections import deque
n,a,b=map(int,input().split())
if a+b>n+1 or a*b<n:
    print(-1)
else:
    ans=[]
    r=list(range(1,n+1))
    for i in range(-(-n//b)):
        ans.append(deque(r[i*b:i*b+b][::-1]))
    l=len(ans)
    x=l
    realans=[]
    now=l-1
    while True:
        if x==a:
            for i in range(l-1,-1,-1):
                while len(ans[i]):
                    p=ans[i].pop()
                    realans.append(p)
            break
        else:
            while True:
                p=ans[now].popleft()
                realans.append(p)
                if len(ans[now])!=0:
                    x+=1
                else:
                    break
                if x==a:
                    break
            now-=1
    print(" ".join(map(str,realans[::-1])))
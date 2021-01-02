from collections import deque
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    a=deque(a)
    w=list(map(int,input().split()))
    w.sort(reverse=True)
    #1を先に処理
    ans=0
    for i in range(w.count(1)):
        ans+=2*a.popleft()
    for i in range(k-w.count(1)):
        p=a.popleft()
        ans+=p
        #print(p)
        for j in range(w[i]-1):
            p=a.pop()
            if j==0:
                ans+=p
                #print(p)
    print(ans)
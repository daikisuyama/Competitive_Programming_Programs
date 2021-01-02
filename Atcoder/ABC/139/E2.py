from collections import deque
n=int(input())
#それぞれ長さはn-1
a=[[j-1+n*i if j-1<i else i+n*(j-1) for j in list(map(int,input().split()))] for i in range(n)]
#試合の候補をいれる
d=dict()
for i in range(n):
    if a[i][0] in d:
        d[a[i][0]]+=1
    else:
        d[a[i][0]]=1
#どこまで見たか
b=[0]*n
#最大n(n-1)/2回
ans=0
nextd=deque()
cleard=deque()
changeable1=deque(set([a[i][0] for i in range(n)]))
while len(d):
    ans+=1
    #一個も同じのなかったらむり
    g=True
    changeable2=deque()
    for i in changeable1:
        if d[i]==2:
            g=False
            e,f=i//n,i%n
            cleard.append(i)
            b[e]+=1
            b[f]+=1
            if b[e]<n-1:
                nextd.append(a[e][b[e]])
                changeable2.append(a[e][b[e]])
            if b[f]<n-1:
                nextd.append(a[f][b[f]])
                changeable2.append(a[f][b[f]])
    if g:
        exit(print(-1))
    ln,lc=len(nextd),len(cleard)  
    for _ in range(ln):
        i=nextd.popleft()
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for _ in range(lc):
        i=cleard.popleft()
        d.pop(i)
    changeable1=set(changeable2)
print(ans)
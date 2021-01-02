n=int(input())
p=[i-1 for i in list(map(int,input().split()))]
#それぞれの数がどのインデックスか
q=[[p[i],i] for i in range(n)]
q.sort()
ind=[q[i][1] for i in range(n)]
now=0
ans=[]
while True:
    for i in range(ind[now]-1,now-1,-1):
        p[i+1],p[i]=p[i],p[i+1]
        ans.append(i+1)
    for i in range(now,ind[now]):
        if i!=p[i]:
            print(-1)
            exit()
    now=ind[now]
    if now==n-1:
        break
    if now==p[now]:
        print(-1)
        exit()
for i in ans:
    print(i)
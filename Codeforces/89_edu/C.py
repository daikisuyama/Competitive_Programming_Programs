from collections import deque
def bfs(dep):
    global a,n,m,ans,d,check,cand
    while len(d):
        cand.append(list(d))
        l=len(d)
        #now0,now1=0,0
        for i in range(l):
            p=d.popleft()
            if p[1]<m-1:
                if not check[p[0]][p[1]+1]:
                    d.append([p[0],p[1]+1])
                    check[p[0]][p[1]+1]=True
                    #now0+=(a[p[0]][p[1]+1]==0)
            if p[0]<n-1:
                if not check[p[0]+1][p[1]]:
                    d.append([p[0]+1,p[1]])
                    check[p[0]+1][p[1]]=True
                    #now1+=(a[p[0]+1][p[1]]==1)
        #if (n+m)%2==1 or (n+m-2)//2!=dep:
            #ans+=min(now0,now1)


for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[list(map(int,input().split())) for i in range(n)]
    ans=0
    d=deque([[0,0]])
    check=[[False]*m for i in range(n)]
    check[0][0]=True
    cand=[]
    bfs(0)
    #print(cand)
    for i in range((n+m-1)//2):
        x=[a[j[0]][j[1]] for j in cand[i]+cand[n+m-1-1-i]]
        ans+=min(x.count(0),x.count(1))
    print(ans)
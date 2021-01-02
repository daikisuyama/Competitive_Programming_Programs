n,m,x,y=map(int,input().split())
x-=1;y-=1
ans=[]
ans.append([x,y])

now=0
for i in list(range(x,-1,-1))+list(range(x+1,n)):
    now=1-now
    if i==x:
        ans+=[[i,j] for j in range(m) if j!=y]
    else:
        if now:
            ans+=[[i,j] for j in range(m)]
        else:
            ans+=[[i,j] for j in range(m)][::-1]
for i in ans:
    print(i[0]+1,i[1]+1)
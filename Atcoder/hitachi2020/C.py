n=int(input())
x=[[] for i in range(n)]
c=[-1]*n
c[0]=1
for i in range(n-1):
    a,b=map(int,input().split())
    x[a-1].append(b-1)
    x[b-1].append(a-1)

def dfs(i,col):
    nex=[]
    for k in x[i]:
        if c[k]==-1:
            c[k]=col
            nex.append(k)
    for k in nex:
        if col==2:
            dfs(k,1)
        else:
            dfs(k,2)

dfs(0,c[0])
d=[]
e=[]
f=[]
for i in range(n):
    if c[i]==1:
        x=n//3+(0 if n%3==0 else 1)
        if len(d)==x:
            f.append(i+1)
        else:
            d.append(i+1)
    else:
        x=n//3+(1 if n%3==2 else 0)
        if len(e)==x:
            f.append(i+1)
        else:
            e.append(i+1)
ans=[-1]*n
g=[d,e,f]
g.sort(key=lambda x:len(x),reverse=True)
d,e,f=g
for i in range(n):
    if i%3==0:
        ans[i]=d[i//3]
    elif i%3==1:
        ans[i]=e[i//3]
    else:
        ans[i]=f[i//3]
print(" ".join(map(str,ans)))

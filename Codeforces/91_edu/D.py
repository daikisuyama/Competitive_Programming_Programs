n,m=map(int,input().split())
x,k,y=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
b=set(c)
d=[]
now=[]
for i in range(n):
    if a[i] not in b:
        now.append(i)
        if i==n-1:
            d.append([now[0]-1,a.index(max(a[now[0]:now[-1]+1])),now[-1]+1])
    else:
        if now!=[]:
            #端とmaxのインデックス(端は-1,nがありうる)
            d.append([now[0]-1,a.index(max(a[now[0]:now[-1]+1])),now[-1]+1])
            now=[]
#位置が順番通りでないやつ
now=0
lc=len(c)
for i in range(n):
    if a[i]==c[now]:
        now+=1
        if now==lc:
            break
else:
    exit(print(-1))
l=len(d)
ans=0
for i in range(l):
    e=d[i]
    f=e[2]-e[0]-1
    if e[0]==-1:
        m=a[e[2]]
    elif e[2]==n:
        m=a[e[0]]
    else:
        m=max(a[e[0]],a[e[2]])
    if m>a[e[1]]:
        ans+=(f%k*y)
        ans+=min((f//k)*x,(f//k)*k*y)
    else:
        if f<k:exit(print(-1))
        ans+=(f%k*y)
        #一回はまとめてkで倒さないと
        ans+=x
        ans+=min((f//k-1)*x,(f//k-1)*k*y)
print(ans)
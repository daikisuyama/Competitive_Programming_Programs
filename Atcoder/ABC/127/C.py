n,m=map(int,input().split())
l,r=[],[]
for i in range(m):
    x,y=map(int,input().split())
    l.append(x)
    r.append(y)
ansl,ansr=max(l),min(r)
print(max(0,ansr-ansl+1))
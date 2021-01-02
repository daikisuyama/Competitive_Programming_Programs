h,w=map(int,input().split())
a=[list(map(int,input().split())) for i in range(h)]
ans=0
x=100000
for i in range(h):
    for j in range(w):
        ans+=a[i][j]
        x=min(x,a[i][j])
print(ans-x*h*w)
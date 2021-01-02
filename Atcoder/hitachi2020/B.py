a_,b_,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=min(a)+min(b)
for i in range(m):
    x,y,c=map(int,input().split())
    t=a[x-1]+b[y-1]-c
    if t<ans:
        ans=t
print(ans)
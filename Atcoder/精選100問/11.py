#11/26 9:55~10:01
n,m=map(int,input().split())
s=[list(map(int,input().split())) for i in range(m)]
p=list(map(int,input().split()))
ans=0
for i in range(2**n):
    f=1
    check=[(i>>j)&1 for j in range(n)]
    for j in range(m):
        x=0
        for k in range(s[j][0]):
            x+=check[s[j][k+1]-1]
        if p[j]!=x%2:
            f=0
            break
    ans+=f
print(ans)
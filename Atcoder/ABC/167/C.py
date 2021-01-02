from itertools import product
n,m,x=map(int,input().split())
ca=[list(map(int,input().split())) for i in range(n)]
ans=100000000000000000
for i in range(2**n):
    check=[0]*m
    ans_=0
    for j in range(n):
        if ((i>>j)&1):
            #(✳︎)
            ans_+=ca[j][0]
            for k in range(m):
                check[k]+=ca[j][k+1]
    if all([l>=x for l in check]):
        ans=min(ans,ans_)
if ans==100000000000000000:
    print(-1)
else:
    print(ans)
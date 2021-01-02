n=int(input())
a=list(map(int,input().split()))
ans=[a]
for i in range(1,n):
    m=min(ans[-1])
    ne=[]
    f=False
    for j in range(n-i,-1,-1):
        if not f:
            if ans[-1][j]!=m:
                ne.append(ans[-1][j])
            else:
                f=True
        else:
            ne.append(ans[-1][j])
    ans.append(ne[::-1])

ans=ans[::-1]
#print(ans)
x=int(input())
for _ in range(x):
    i,j=map(int,input().split())
    print(ans[i-1][j-1])
n,k=map(int,input().split())
ans=[0]*n
for i in range(k):
    d=int(input())
    a=list(map(int,input().split()))
    for j in a:
        ans[j-1]=1
print(n-sum(ans))


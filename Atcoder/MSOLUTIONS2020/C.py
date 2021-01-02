n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=[0]*(n-k)
for i in range(k,n):
    ans[i-k]=(a[i]>a[i-k])
for i in range(0,n-k):
    print("Yes" if ans[i] else "No")
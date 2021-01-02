import bisect
n,m=map(int,input().split())
a=list(map(int,input().split()))
#逆に保存
check=[-i for i in range(n)][::-1]
for i in range(m):
    j=bisect.bisect_left(check,a[i])-1
    if j==-1:
        print(-1)
    else:
        check[j]=a[i]
        print(n-j)
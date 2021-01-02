for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    inf=10**15
    dp1=[-inf]*(n-1)
    dp1[0]=a[0]
    for i in range(1,n-1):
        dp1[i]=max(dp1[i-1]+a[i],a[i])
    dp2=[-inf]*(n-1)
    dp2[0]=a[1]
    for i in range(2,n):
        dp2[i-1]=max(dp2[i-2]+a[i],a[i])
    if max(dp1+dp2)<sum(a):
        print("YES")
    else:
        print("NO")
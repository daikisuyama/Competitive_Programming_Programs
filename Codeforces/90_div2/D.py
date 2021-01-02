for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    dp0=[[0,0,0] for i in range((n-1)//2+1)]
    for i in range((n-1)//2+1):
        if i==0:
            dp0[i][0]=a[2*i]
            continue
        dp0[i][0]=dp0[i-1][0]+a[2*i]
        dp0[i][1]=max(dp0[i-1][0],dp0[i-1][1])+a[2*i-1]
        dp0[i][2]=max(dp0[i-1][1],dp0[i-1][2])+a[2*i]
    dp1=[[0,0,0] for i in range((n-1)//2+1)]
    for i in range((n-1)//2+1):
        if i==0:
            dp1[i][0]=a[2*i]
            if 2*i+1<n:dp1[i][1]=a[2*i+1]
            continue
        dp1[i][0]=dp1[i-1][0]+a[2*i]
        if 2*i+1<n:dp1[i][1]=max(dp1[i-1][0],dp1[i-1][1])+a[2*i+1]
        if 2*i<n:dp1[i][2]=max(dp1[i-1][1],dp1[i-1][2])+a[2*i]
    #print(dp0)
    #print(dp1)
    print(max(dp0[(n-1)//2]+dp1[(n-1)//2]))
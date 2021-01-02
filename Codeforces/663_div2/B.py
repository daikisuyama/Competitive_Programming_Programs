for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[input() for i in range(n)]
    ans=0
    for i in range(m-1):
        ans+=(a[n-1][i]=="D")
    for i in range(n-1):
        ans+=(a[i][m-1]=="R")
    print(ans)
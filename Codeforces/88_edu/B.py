for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    a=[[j for j in input()] for i in range(n)]
    ans=0
    if y>=2*x:
        for i in range(n):
            ans+=a[i].count(".")*x
    else:
        for i in range(n):
            for j in range(m-1):
                if a[i][j]=="." and a[i][j+1]==".":
                    a[i][j]="*"
                    a[i][j+1]="*"
                    ans+=y
        for i in range(n):
            ans+=a[i].count(".")*x
    print(ans)
def dfs(n):
    global b,check,d
    #ttfは235、chaはabc
    #2,3,5の場合それぞれ
    for ttf,cha in zip([2,3,5],b):
        #-1ずつしていく場合
        if check[0]>check[n]+n*d:
            check[0]=check[n]+n*d

        #最寄りまで-してく場合
        x1,x2=n//ttf,n%ttf
        if x1 in check:
            if check[x1]>check[n]+x2*d+cha:
                check[x1]=check[n]+x2*d+cha
                dfs(x1)
        else:
            check[x1]=check[n]+x2*d+cha
            dfs(x1)
        
        #最寄りまで+1してく場合
        x1,x2=n//ttf+1,ttf-n%ttf
        if x1 in check:
            if check[x1]>check[n]+x2*d+cha:
                check[x1]=check[n]+x2*d+cha
                dfs(x1)
        else:
            check[x1]=check[n]+x2*d+cha
            dfs(x1)

t=int(input())
for i in range(t):
    N,*b,d=map(int,input().split())
    check={N:0,0:N*d}
    dfs(N)
    print(check[0])

check=dict()
N,b,d=0,[],0
#ttfは235、chaはabc

def dfs_sub(n,ttf,cha):
    global check,d
    check[0]=min(check[n]+n*d,check[0]) if 0 in check else check[n]+n*d
    if n//ttf==0:
        check[n//ttf]=min(check[n]+(n%ttf)*d,check[n//ttf]) if n//ttf in check else check[n]+(n%ttf)*d
    else:
        if n//ttf in check:
            if check[n//ttf]>check[n]+(n%ttf)*d+cha:
                check[n//ttf]=check[n]+(n%ttf)*d+cha
                dfs(n//ttf)
        else:
            check[n//ttf]=check[n]+(n%ttf)*d+cha
            dfs(n//ttf)
    if 1+n//ttf in check:
        if check[1+n//ttf]>check[n]+(ttf-n%ttf)*d+cha:
            check[1+n//ttf]=check[n]+(ttf-n%ttf)*d+cha
            dfs(1+n//ttf)
    else:
        check[1+n//ttf]=check[n]+(ttf-n%ttf)*d+cha
        dfs(1+n//ttf)

def dfs(n):
    global b
    for i,j in zip([2,3,5],b):
        dfs_sub(n,i,j)

t=int(input())
for i in range(t):
    N,*b,d=map(int,input().split())
    check={N:0}
    dfs(N)
    print(check[0])

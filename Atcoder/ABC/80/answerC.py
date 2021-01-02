n=int(input())
f=[list(map(int,input().split())) for i in range(n)]
p=[list(map(int,input().split())) for i in range(n)]
ma=-10000000000000
for i in range(1,2**10):
    check=[0]*n
    for j in range(10):
        if (i>>j) & 1:
            for k in range(n):
                check[k]+=f[k][j]
    ma_sub=0
    for i in range(n):
        ma_sub+=p[i][check[i]]
    ma=max(ma,ma_sub)
print(ma)
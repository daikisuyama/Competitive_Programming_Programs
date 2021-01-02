n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
inf=100000000
ans=inf

for i in range(1<<n):#for i in range(2**n)と同じ
    x=[[a[j],j,0] if ((i >> j) & 1) == 1 else [b[j],j,1] for j in range(n)]
    y=[[x[j][0],x[j][1],x[j][2]] for j in range(n)]
    x.sort()
    for j in range(n):
        if abs(x[j][1]-j)%2!=x[j][2]:
            break
    else:
        cnt=0
        f=1 #隣接した要素が昇順になっていないものが存在する
        while f:
            f=0
            for k in range(n-1):
                if y[n-k-1]<y[n-k-2]:
                    y[n-k-1],y[n-k-2]=y[n-k-2],y[n-k-1]
                    f=1
                    cnt+=1
                if cnt>=ans:
                    break
            if cnt>=ans:
                    break
        else:
            ans=cnt
    #print(x)
    #print(ans)

if ans==inf:
    print(-1)
else:
    print(ans)

n,x,y=map(int,input().split())
#1→n-1の長さ
ans=[n-i-1 for i in range(n-1)]
k=min(x,n-y+1)#n/2以下になる
for i in range(y-x-1,n-1):
    #iは元の長さ-1
    #jは変更先の長さ-1
    j=i-(y-x-1)
    #変更していくつ短くなるか
    l=min([j+1,n-1-i,k])
    ans[i]-=l
    ans[j]+=l
for i in range(n-1):
    print(ans[i])
#嘘解法
mod=10**9+7
n,m=map(int,input().split())
#iになるのがあるか
#あったら、行[1,行番号]、列[0,列番号]
check=[[] for i in range(n*m)]
a=list(map(int,input().split()))
for i in range(n):
    check[a[i]-1].append([1,i])
b=list(map(int,input().split()))
for i in range(m):
    check[b[i]-1].append([0,i])
for i in range(n*m):
    if len(check[i])>2 or (len(check[i])==2 and check[i][0][0]==check[i][1][0]):
        print(0)
        exit()
#階乗の前計算(n!,m!の最大まで)
fac=[[0]*1001 for i in range(1001)]
for i in range(1001):
    fac[i][0]=1
    for j in range(1,i+1):
        fac[i][j]=fac[i][j-1]*(i+1-j)%mod
ans=1
#r:どれだけ列が埋まってるか(行決まることで)
#c:どれだけ行が埋まってるか(列決まることで)
r,c=0,0
for i in range(n*m):
    if len(check[i])==0:
        pass
    elif len(check[i])==2:
        x=(i+1)-(n*m-(n-r)*(m-c))
        if x>=m-c:
            if x==0:continue
            ans*=(fac[x-1][m-c-1])
            ans%=mod
        else:
            print(0)
            exit()
        r+=1
        x=(i+1)-(n*m-(n-r)*(m-c))
        if x>=n-r:
            if x==0:continue
            ans*=(fac[x-1][n-r-1])
            ans%=mod
        else:
            print(0)
            exit()
        c+=1
    else:
        if check[i][0][0]:
            #残り決めたいのはm-c
            #そのうち1はその数
            #すでにもう決まった数は除く
            x=(i+1)-(n*m-(n-r)*(m-c))
            if x>=m-c:
                if x==0:continue
                ans*=m-c
                ans*=(fac[x-1][m-c-1])
                ans%=mod
            else:
                print(0)
                exit()
            r+=1
        else:
            x=(i+1)-(n*m-(n-r)*(m-c))
            if x>=n-r:
                if x==0:continue
                ans*=n-r
                ans*=(fac[x-1][n-r-1])
                ans%=mod
            else:
                print(0)
                exit()
            c+=1
print(ans)

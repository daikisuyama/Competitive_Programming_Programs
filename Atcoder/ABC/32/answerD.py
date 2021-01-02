n,w=map(int,input().split())
vw=[list(map(int,input().split())) for i in range(n)]
vw.sort(key=lambda x:x[0],reverse=True)
vw.sort(key=lambda x:x[1])

w_max=0
for i in range(n):
    w_max=max(w_max,vw[i][1])
inf=100000000000
if n<=30:
    ma=0
    N=2**n
    for i in range(N):
        mh,mw=0,0
        for j in range(n):
            if (i>>j&1):
                mh+=vw[j][0]
                mw+=vw[j][1]
                if mw>w:
                    break
        else:
            ma=max(ma,mh)
    print(ma)
elif w_max<=1000:
    t1,t2=0,0
    for i in range(n):
        t1+=vw[i][0]
        t2+=vw[i][1]
    if t2<=w:
        print(t1)
    else:
        dp=[0]*(w+1)
        for i in range(n):
            dp_sub=[0]*(w+1)
            for j in range(w+1):
                if j==0 or dp[j]!=0:
                    k=j+vw[i][1]
                    if k<=w:
                        dp_sub[k]=dp[j]+vw[i][0]
            for j in range(w+1):
                dp[j]=max(dp[j],dp_sub[j])
        print(max(dp))
    
else:
    print()
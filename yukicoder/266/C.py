ans=0
n=int(input())
check=[0 for i in range(10)]
a=list(map(int,input().split()))
for i in a:
    check[i%10]+=1
dp=[0 for i in range(10)]
for i in range(10):
    for j in range(check[i]):
        dp_sub=[0]*10
        for k in range(10):
            if k==0:
                dp_sub[(i+k)%10]=dp[k]+1
            elif dp[k]!=0:
                dp_sub[(i+k)%10]=dp[k]+1
        for k in range(10):
            dp[k]=max(dp[k],dp_sub[k])
        #print(dp_sub)
#print(dp)
print(dp[0])
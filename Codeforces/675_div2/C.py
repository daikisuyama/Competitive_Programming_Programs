mod=10**9+7
s=list(map(int,input()))[::-1]
n=len(s)
if n==1:
    print(0)
    exit()
#10^k乗
po=[1]
for i in range(n):
    po.append(po[-1]*10%mod)
#S_iの逆順からの累積
si=[0]*n
si[n-1]=s[n-1]
for i in range(n-2,-1,-1):
    si[i]=si[i+1]+s[i]
ans=0
for k in range(n-1):
    ans+=((k+1)*si[k+1])*po[k]
    #print(ans)
    ans%=mod
for k in range(n-1):
    ans+=s[k]*((n-1-k)*(n-1-k-1)//2+(n-1-k))*po[k]
    #print(ans)
    ans%=mod
#print()
print(ans)
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
a.sort()

def check(d):#そいつが必要か
    global a,n,k
    dp=[0]*(k)#k-1まで
    if a[d]>=k:
        return True
    for i in range(n):
        if i!=d:
            dp_sub=[0]*(k)
            for j in range(k-1):
                if j==0 or dp[j]!=0:
                    if j+a[i]<k:
                        dp_sub[j+a[i]]=1
                    else:
                        break
            for j in range(k):
                if dp_sub[j]==1:
                    dp[j]=1
                    if j+a[d]>=k:
                        return True
    return False
l,r=0,n-1
while l+1<r:
    d=(l+r)//2
    if check(d):#必要か
        r=d
    else:
        l=d
if check(l):
    print(l)
else:
    if check(r):
        print(r)
    else:
        print(r+1)

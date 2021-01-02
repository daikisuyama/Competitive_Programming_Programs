def make_divisors(n):
    divisors=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

n,k=map(int,input().split())
mod=10**9+7
memo=[pow(k//i,n,mod) for i in range(1,k+1)] #gcdが1~kになる場合をメモする
for i in range(k-1,-1,-1):
    x=make_divisors(i+1)
    for j in x:
        if j!=i+1:
            memo[j-1]-=memo[i]
ans=0
for i in range(k):
    ans+=(memo[i]*(i+1))
    ans%=mod
print(ans)
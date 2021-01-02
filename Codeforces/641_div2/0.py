def check_divisors(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return i
    return n

t=int(input())
nk=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    n,k=nk[i]
    ans=n
    for j in range(k):
        c=check_divisors(ans)
        if c==2:
            ans+=(k-j)*2
            break
        else:
            ans+=c
    print(ans)
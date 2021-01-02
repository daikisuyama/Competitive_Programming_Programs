ans=0
n,k=map(int,input().split())
while True:
    n=n//k
    ans+=1
    if n==0:
        break
print(ans)

n=int(input())
a=list(map(int,input().split()))
ans=0

while all(i%2==0 for i in a):
    ans+=1
    for j in range(n):
        a[j]//=2
print(ans)

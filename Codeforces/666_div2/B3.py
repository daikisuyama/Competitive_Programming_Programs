n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=10**18
for c in range(2,int((2*sum(a)-n)**(1/(n-1)))+1):
    x=1
    ans_sub=abs(a[0]-x)
    for i in range(n-1):
        x*=c
        ans_sub+=abs(a[i+1]-x)
    ans=min(ans,ans_sub)
print(min(ans,sum(a)-n))
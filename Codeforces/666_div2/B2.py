n=int(input())
a=list(map(int,input().split()))
a.sort()
cand=int(a[-1]**(1/(n-1)))-1
def f(k):
    ans=abs(1-a[0])
    b=1
    for i in range(n-1):
        b=b*k
        ans+=abs(b-a[i])
    return ans
ans=1000000000000000000000
for i in range(max(0,cand-5),cand+5):
    ans=min(ans,f(i))
print(ans)
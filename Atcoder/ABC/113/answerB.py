n=int(input())
t,a=map(int,input().split())
h=[t-int(i)*0.006 for i in input().split()]
ans=[-1,1000000000]
for i in range(n):
    if abs(h[i]-a)<abs(ans[1]-a):
        ans=[i,h[i]]
print(ans[0]+1)
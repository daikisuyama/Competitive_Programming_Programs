n=int(input())
a=list(map(int,input().split()))
ans=[2,sum(i%2==0 for i in a)]
for j in range(1000,2,-1):
    x=[j,sum(i%j==0 for i in a)]
    if x[1]>ans[1]:
        ans=[x[0],x[1]]
print(ans[0])
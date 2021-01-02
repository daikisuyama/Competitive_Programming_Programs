n=int(input())
a=list(map(int,input().split()))
b=[0]
b.extend(a)
b.append(0)
a=b
base=0
for i in range(n+1):
    base+=abs(a[i+1]-a[i])
ans=[]
for i in range(1,n+1):
    ans.append(base+abs(a[i+1]-a[i-1])-abs(a[i+1]-a[i])-abs(a[i]-a[i-1]))
for i in range(n):
    print(ans[i])
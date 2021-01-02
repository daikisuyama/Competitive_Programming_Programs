n=int(input())
a=list(map(int,input().split()))
base=0
for i in range(n+1):
    if i==0:
        base+=abs(a[0])
    elif i==n:
        base+=abs(a[n-1])
    else:
        base+=abs(a[i]-a[i-1])
ans=[]
for i in range(n):
    if i==0:
        ans.append(base+abs(a[1])-abs(a[0])-abs(a[1]-a[0]))
    elif i==n-1:
        ans.append(base+abs(a[n-2])-abs(a[n-1])-abs(a[n-2]-a[n-1]))
    else:
        ans.append(base+abs(a[i+1]-a[i-1])-abs(a[i+1]-a[i])-abs(a[i]-a[i-1]))
for i in range(n):
    print(ans[i])
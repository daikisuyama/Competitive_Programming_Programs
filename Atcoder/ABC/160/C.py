k,n=map(int,input().split())
a=list(map(int,input().split()))
ma=0
for i in range(n-1):
    ma=max(ma,a[i+1]-a[i])
print(k-max(ma,a[0]+k-a[n-1]))
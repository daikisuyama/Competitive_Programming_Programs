n,k=map(int,input().split())
x=list(map(int,input().split()))
mi=10**10
for i in range(n-k+1):
    mi=min(mi,x[k-1+i]-x[i]+min(abs(x[i]),abs(x[k-1+i])))
print(mi)

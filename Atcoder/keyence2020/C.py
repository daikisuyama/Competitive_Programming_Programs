n,k,s=map(int,input().split())
if s<10**9:
    x=[s]*k
    y=[s+1]*(n-k)
else:
    x=[s]*k
    y=[1]*(n-k)
z=" ".join(map(str,x))+" "+" ".join(map(str,y))
print(z)
